import sys

from automates.program_analysis.CAST2GrFN.visitors.cast_to_annotated_cast import (
    CastToAnnotatedCastVisitor
)
from automates.program_analysis.CAST2GrFN.cast import CAST
from automates.program_analysis.CAST2GrFN.visitors.annotations_pass import AnnotationsPass
from automates.program_analysis.CAST2GrFN.visitors.cast_to_agraph_visitor import CASTToAGraphVisitor
from automates.program_analysis.CAST2GrFN.visitors.id_collapse_pass import IdCollapsePass
from automates.program_analysis.CAST2GrFN.visitors.container_scope_pass import ContainerScopePass
from automates.program_analysis.CAST2GrFN.visitors.variable_version_pass import VariableVersionPass
from automates.program_analysis.CAST2GrFN.visitors.incoming_outgoing_pass import IncomingOutgoingPass
from automates.program_analysis.CAST2GrFN.visitors.grfn_var_creation_pass import GrfnVarCreationPass


def main():
    """cast_to_annotated.py

    This program reads a JSON file that contains the CAST representation
    of a program, and transforms it to annotated CAST. It then calls a
    series of passes that each augment the information in the annotatd CAST nodes
    in preparation for the GrFN generation.
   
    One command-line argument is expected, namely the name of the JSON file that
    contains the CAST data.
    """
    f_name = sys.argv[1]
    file_contents = open(f_name).read()
    C = CAST([], "python")
    C2 = C.from_json_str(file_contents)

    visitor = CastToAnnotatedCastVisitor(C2)
    annotated_cast = visitor.generate_annotated_cast()

    print("Calling IdCollapsePass------------------------")
    collapsed_ids = IdCollapsePass(annotated_cast)
    V = CASTToAGraphVisitor(collapsed_ids)

    print("\nCalling ContainerScopePass-------------------")
    con_scope  = ContainerScopePass(annotated_cast)

    print("\nCalling VariableVersionPass-------------------")
    VariableVersionPass(annotated_cast)

    print("\nCalling GrfnVarCreationPass-------------------")
    GrfnVarCreationPass(annotated_cast)

    # print("\nCalling IncomingOutgoingPass-------------------")
    # IncomingOutgoingPass(annotated_cast)

    V2 = CASTToAGraphVisitor(annotated_cast)

    f_name = "con_scop-AnnCAST"
    pdf_file_name = f"{f_name}.pdf"
    V2.to_pdf(pdf_file_name)


if __name__ == "__main__":
    main()
