from functools import singledispatchmethod
from dataclasses import dataclass
from collections import defaultdict
import copy
import typing


from automates.utils.misc import uuid
from .cast_visitor import CASTVisitor
from automates.program_analysis.CAST2GrFN.visitors.annotated_cast import *


class ContainerData:
    modified_vars: typing.Dict[id, str]
    accessed_vars: typing.Dict[id, str]

    def __init__(self):
        self.modified_vars = {}
        self.accessed_vars = {}


class ContainerScopePass:
    def __init__(self, ann_cast: AnnCast):
        self.ann_cast = ann_cast
        # dicts mapping container scope strs to the if/loop count inside
        # the container
        self.if_count = defaultdict(int)
        self.loop_count = defaultdict(int)
        # dict mapping containter scope str to AnnCastNode
        self.con_str_to_node = {}
        # dict mapping container scope str to cached Container Data
        self.con_str_to_con_data = {}

        for node in self.ann_cast.nodes:
            # assign_lhs is False at the start of our visitor
            self.visit(node, [], False)
        self.nodes = self.ann_cast.nodes

        # add cached container data to container nodes
        self.add_container_data_to_nodes()

    def next_if_scope(self, enclosing_con_scope):
        scopestr = con_scope_to_str(enclosing_con_scope)
        count = self.if_count[scopestr]
        self.if_count[scopestr] += 1
        return enclosing_con_scope + [f"if{count}"]

    def next_loop_scope(self, enclosing_con_scope):
        scopestr = con_scope_to_str(enclosing_con_scope)
        count = self.loop_count[scopestr]
        self.loop_count[scopestr] += 1
        return enclosing_con_scope + [f"loop{count}"]


    def add_container_data_to_nodes(self):
        for scopestr, data in self.con_str_to_con_data.items():
            print(f"For scopestr: {scopestr} found data with")
            modified_vars = var_dict_to_str("  Modified: ", data.modified_vars)
            print(modified_vars)
            accessed_vars = var_dict_to_str("  Accessed: ", data.accessed_vars)
            print(accessed_vars)
            container = self.con_str_to_node[scopestr]
            container.accessed_vars = data.accessed_vars
            container.modified_vars = data.modified_vars

    def initialize_con_scope_data(self, con_scope: typing.List, node):
        """
        Create an empty `ContainterData` in `self.con_str_to_con_data`
        and cache the container `node` in `self.con_str_to_node`
        """
        con_scopestr = con_scope_to_str(con_scope)
        self.con_str_to_node[con_scopestr] = node
        self.con_str_to_con_data[con_scopestr] = ContainerData()
        
    def visit(
        self, node: AnnCastNode, enclosing_con_scope: typing.List, assign_lhs: bool
    ):
        # type(node) is a string which looks like
        # "class '<path.to.class.ClassName>'"
        class_name = str(type(node))
        last_dot = class_name.rfind(".")
        class_name = class_name[last_dot + 1 : -2]
        print(f"\nProcessing node type {class_name}")
        return self._visit(node, enclosing_con_scope, assign_lhs)

    @singledispatchmethod
    def _visit(
        self, node: AnnCastNode, enclosing_con_scope: typing.List, assign_lhs: bool
    ) -> typing.Dict:
        """
        Visit each AnnCastNode
        Parameters:
          - `assign_lhs`: this denotes whether we are visiting the LHS or RHS of an AnnCastAssignment
                      This is used to determine whether a variable (AnnCastName node) is
                      accessed or modified in that context
        """
        raise Exception(f"Unimplemented AST node of type: {type(node)}")

    def visit_node_list(
        self, node_list: typing.List[AnnCastNode], enclosing_con_scope, assign_lhs
    ):
        return [self.visit(node, enclosing_con_scope, assign_lhs) for node in node_list]

    @_visit.register
    def visit_assignment(
        self, node: AnnCastAssignment, enclosing_con_scope, assign_lhs
    ):
        # TODO: what if the rhs has side-effects
        self.visit(node.right, enclosing_con_scope, assign_lhs)
        assert isinstance(node.left, AnnCastVar)
        self.visit(node.left, enclosing_con_scope, True)

    @_visit.register
    def visit_attribute(self, node: AnnCastAttribute, assign_lhs):
        pass

    @_visit.register
    def visit_binary_op(self, node: AnnCastBinaryOp, enclosing_con_scope, assign_lhs):
        # visit LHS first
        self.visit(node.left, enclosing_con_scope, assign_lhs)

        # visit RHS second
        self.visit(node.right, enclosing_con_scope, assign_lhs)

    @_visit.register
    def visit_boolean(self, node: AnnCastBoolean, assign_lhs):
        pass

    @_visit.register
    def visit_call(self, node: AnnCastCall, enclosing_con_scope, assign_lhs):
        assert isinstance(node.func, AnnCastName)
        node.func.con_scope = enclosing_con_scope
        self.visit_node_list(node.arguments, enclosing_con_scope, assign_lhs)

    # TODO: What to do for classes about modified/accessed vars?
    @_visit.register
    def visit_class_def(self, node: AnnCastClassDef, enclosing_con_scope, assign_lhs):
        # We do not visit the name because it is a string
        assert isinstance(node.name, str)
        classscope = enclosing_con_scope + [node.name]
        # node.bases is a list of strings
        # node.funcs is a list of Vars
        self.visit_node_list(node.funcs, classscope, assign_lhs)
        # node.fields is a list of Vars
        self.visit_node_list(node.fields, classscope, assign_lhs)

    @_visit.register
    def visit_dict(self, node: AnnCastDict, assign_lhs):
        pass

    @_visit.register
    def visit_expr(self, node: AnnCastExpr, enclosing_con_scope, assign_lhs):
        self.visit(node.expr, enclosing_con_scope, assign_lhs)

    @_visit.register
    def visit_function_def(
        self, node: AnnCastFunctionDef, enclosing_con_scope, assign_lhs
    ):
        # Add this AnnCastFunctionDef node to the AnnotatedCast `func_names_to_def` dict
        self.ann_cast.func_names_to_defs[node.name] = node

        # Modify scope to include the function name
        funcscope = enclosing_con_scope + [node.name]

        self.initialize_con_scope_data(funcscope, node)
        node.con_scope = funcscope

        # Each argument is a AnnCastVar node
        # Initialize each Name and visit to modify its scope
        self.visit_node_list(node.func_args, funcscope, assign_lhs)

        self.visit_node_list(node.body, funcscope, assign_lhs)

    @_visit.register
    def visit_list(self, node: AnnCastList, enclosing_con_scope, assign_lhs):
        self.visit_node_list(node.values, enclosing_con_scope, assign_lhs)

    @_visit.register
    def visit_loop(self, node: AnnCastLoop, enclosing_con_scope, assign_lhs):
        loopscope = self.next_loop_scope(enclosing_con_scope)
        self.initialize_con_scope_data(loopscope, node)
        node.con_scope = loopscope
        # TODO: What if expr has side-effects?
        loopexprscope = loopscope + [LOOPEXPR]
        self.visit(node.expr, loopexprscope, assign_lhs)

        loopbodyscope = loopscope + [LOOPBODY]
        self.visit_node_list(node.body, loopbodyscope, assign_lhs)

    @_visit.register
    def visit_model_break(self, node: AnnCastModelBreak, assign_lhs):
        pass

    @_visit.register
    def visit_model_continue(self, node: AnnCastModelContinue, assign_lhs):
        pass

    @_visit.register
    def visit_model_if(self, node: AnnCastModelIf, enclosing_con_scope, assign_lhs):
        # want orig enclosing
        ifscope = self.next_if_scope(enclosing_con_scope)
        self.initialize_con_scope_data(ifscope, node)
        node.con_scope = ifscope

        # TODO-what if the condition has a side-effect?
        ifexprscope = ifscope + [IFEXPR]
        self.visit(node.expr, ifexprscope, assign_lhs)

        ifbodyscope = ifscope + [IFBODY]
        self.visit_node_list(node.body, ifbodyscope, assign_lhs)

        orelsebodyscope = ifscope + [ELSEBODY]
        self.visit_node_list(node.orelse, orelsebodyscope, assign_lhs)

    @_visit.register
    def visit_return(self, node: AnnCastModelReturn, enclosing_con_scope, assign_lhs):
        self.visit(node.value, enclosing_con_scope, assign_lhs)

    @_visit.register
    def visit_module(self, node: AnnCastModule, enclosing_con_scope, assign_lhs):
        # Container scope for the module will be called "module" for now
        enclosing_con_scope = ["module"]
        self.visit_node_list(node.body, enclosing_con_scope, assign_lhs)

    @_visit.register
    def visit_name(self, node: AnnCastName, enclosing_con_scope, assign_lhs):
        node.con_scope = enclosing_con_scope

        # check every prefix of enclosing_con_scope, and build
        # its associated scopestr
        # add to container data if this is an already cached container string
        scopestr = ""
        for index, name in enumerate(enclosing_con_scope):
            # add separator between container scope component names
            if index != 0:
                scopestr += f"{CON_STR_SEP}"
            scopestr += f"{name}"
            # fill in container data if this is a cached container str
            if scopestr in self.con_str_to_con_data:
                con_data = self.con_str_to_con_data[scopestr]
                # if we are on LHS of assignment, this Name should be
                # added to modified vars
                if assign_lhs:
                    con_data.modified_vars[node.id] = node.name
                # otherwise it should be added to accessed_vars
                else:
                    con_data.accessed_vars[node.id] = node.name

    @_visit.register
    def visit_number(self, node: AnnCastNumber, enclosing_con_scope, assign_lhs):
        pass

    @_visit.register
    def visit_set(self, node: AnnCastSet, assign_lhs):
        pass

    @_visit.register
    def visit_string(self, node: AnnCastString, enclosing_con_scope, assign_lhs):
        pass

    @_visit.register
    def visit_subscript(self, node: AnnCastSubscript, assign_lhs):
        pass

    @_visit.register
    def visit_tuple(self, node: AnnCastTuple, assign_lhs):
        pass

    @_visit.register
    def visit_unary_op(self, node: AnnCastUnaryOp, enclosing_con_scope, assign_lhs):
        self.visit(node.value, enclosing_con_scope, assign_lhs)

    @_visit.register
    def visit_var(self, node: AnnCastVar, enclosing_con_scope, assign_lhs):
        self.visit(node.val, enclosing_con_scope, assign_lhs)
