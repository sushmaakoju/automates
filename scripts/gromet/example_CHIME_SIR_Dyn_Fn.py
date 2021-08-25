from gromet import *  # never do this :)


# -----------------------------------------------------------------------------
# GroMEt instance
# -----------------------------------------------------------------------------


def generate_gromet() -> Gromet:
    # ----- Metadata -----

    chime_model_description = ModelDescription(
        uid=UidMetadatum("chime_model_description"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        name="CHIME SIR Dynamics",
        description="The core SIR dynamics of the CHIME model",
    )

    # TODO: Regenerate ModelInterface
    chime_model_interface = ModelInterface(
        uid=UidMetadatum("chime_model_interface"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        variables=[
            # parameters
            # i_day                 : UidJunction("J:main.i_day")
            UidVariable("V:i_day"),
            # n_days                : UidJunction("J:main.n_days")
            UidVariable("V:n_days"),
            # N_p                   : UidJunction("J:main.N_p")
            UidVariable("V:N_p"),
            # infections_days       : UidJunction("J:main.infections_days")
            UidVariable("V:infections_days"),
            # relative_contact_rate : UidJunction("J:main.relative_contact_rate")
            UidVariable("V:relative_contact_rate"),
            # initial conditions
            # s_n                   : UidJunction("J:main.s_n")
            UidVariable("V:s_n"),
            # i_n                   : UidJunction("J:main.i_n")
            UidVariable("V:i_n"),
            # r_n                   : UidJunction("J:main.r_n")
            UidVariable("V:r_n"),
            # typical measurements
            # out S                 : UidPort("P:main.out.S")
            UidVariable("V:S"),
            # out I                 : UidPort("P:main.out.I")
            UidVariable("V:I"),
            # out R                 : UidPort("P:main.out.R")
            UidVariable("V:R"),
            # out E                 : UidPort("P:main.out.E")
            UidVariable("V:E"),
        ],
        parameters=[
            # i_day                 : UidJunction("J:main.i_day")
            UidVariable("V:i_day"),
            # n_days                : UidJunction("J:main.n_days")
            UidVariable("V:n_days"),
            # N_p                   : UidJunction("J:main.N_p")
            UidVariable("V:N_p"),
            # infections_days       : UidJunction("J:main.infections_days")
            UidVariable("V:infections_days"),
            # relative_contact_rate : UidJunction("J:main.relative_contact_rate")
            UidVariable("V:relative_contact_rate"),
        ],
        initial_conditions=[
            # s_n                   : UidJunction("J:main.s_n")
            UidVariable("V:s_n"),
            # i_n                   : UidJunction("J:main.i_n")
            UidVariable("V:i_n"),
            # r_n                   : UidJunction("J:main.r_n")
            UidVariable("V:r_n"),
        ],
    )

    # -- code collection reference metadata
    file_chime_base_py_uid = UidCodeFileReference("chime_base_code")
    file_chime_base_py_code_file_reference = CodeFileReference(
        uid=file_chime_base_py_uid, name="CHIME_SIR_Base", path="CHIME_SIR.py"
    )
    askeid_chime_base_code = GlobalReferenceId(
        type="aske_id", id="2c75d1ef-906b-4a60-bad6-416eff5cbfc4"
    )
    # https://drive.google.com/file/d/18uMBhEIqIWuO0XKz3eYUtaNg4hasmCLW/view?usp=sharing
    metadatum_code_collection_ref = CodeCollectionReference(
        uid=UidMetadatum("chime_base_code_collection_ref"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        global_reference_id=askeid_chime_base_code,
        file_ids=[file_chime_base_py_code_file_reference],
    )

    # -- textual document reference set
    askeid_chime_webdoc_as_pdf = GlobalReferenceId(
        type="aske_id", id="4b429087-7e7c-4623-80fd-64fb934a8be6"
    )
    chime_webdocs_as_pdf = TextualDocumentReference(
        uid=UidDocumentReference("chime_webdocs_as_pdf"),
        global_reference_id=askeid_chime_webdoc_as_pdf,
        cosmos_id="COSMOS",
        cosmos_version_number="3.0",
        automates_id="AutoMATES-TR",
        automates_version_number="2.0",
        bibjson=Bibjson(
            title="CHIME: COVID-19 Hospital Impact for Epidemics - Online Documentation",
            author=[
                BibjsonAuthor(name="Jason Lubken"),
                BibjsonAuthor(name="Marieke Jackson"),
                BibjsonAuthor(name="Michael Chow"),
            ],
            type="web_documentation",
            website=BibjsonLinkObject(
                type="url",
                location="https://code-for-philly.gitbook.io/chime/",
            ),
            timestamp="2021-01-19T21:08",
            link=[
                BibjsonLinkObject(
                    type="gdrive",
                    location="https://drive.google.com/file/d/122LEBSEMF9x-3r3tWbF6YQ9xeV4I_9Eh/view?usp=sharing",
                )
            ],
            identifier=[
                BibjsonIdentifier(
                    type="aske_id", id="8467496e-3dfb-4efd-9061-433fef1b92de"
                )
            ],
        ),
    )
    metadatum_textual_document_reference_set = TextualDocumentReferenceSet(
        uid=UidMetadatum("chime_textual_document_ref_set"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        documents=[chime_webdocs_as_pdf],
    )

    # ----- Model component definitions -----

    variables_sir = [
        # CTM 2021-08-19: Hardcoding this as this was not included;
        # only used in bookkeeping (which is not included here)
        Variable(
            uid=UidVariable("V:i_day"),
            name="i_day",
            type=UidType("Float"),
            proxy_state=UidJunction("J:main.i_day"),
            states=[UidJunction("J:main.i_day")],
            metadata=None,
        ),
        # TODO: Remaining Variables will be defined in post-processing
    ]

    wires_sir = [
        # -- sir() Wires --
        # sir
        Wire(
            uid=UidWire("W:sir.n>sir_scale_exp.n"),
            type=None,
            value_type=UidType("Integer"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.n"),
            tgt=UidPort("P:sir_scale_exp.n"),
        ),
        Wire(
            uid=UidWire("W:sir.beta>sir_s_n_exp.beta"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.beta"),
            tgt=UidPort("P:sir_s_n_exp.beta"),
        ),
        Wire(
            uid=UidWire("W:sir.beta>sir_i_n_exp.beta"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.beta"),
            tgt=UidPort("P:sir_i_n_exp.beta"),
        ),
        Wire(
            uid=UidWire("W:sir.gamma>sir_i_n_exp.gamma"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.gamma"),
            tgt=UidPort("P:sir_i_n_exp.gamma"),
        ),
        Wire(
            uid=UidWire("W:sir.gamma>sir_r_n_exp.gamma"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.gamma"),
            tgt=UidPort("P:sir_r_n_exp.gamma"),
        ),
        Wire(
            uid=UidWire("W:sir.s_in>sir_s_n_exp.s"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.s_in"),
            tgt=UidPort("P:sir_s_n_exp.s"),
        ),
        Wire(
            uid=UidWire("W:sir.s_in>sir_i_n_exp.s"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.s_in"),
            tgt=UidPort("P:sir_i_n_exp.s"),
        ),
        Wire(
            uid=UidWire("W:sir.i_in>sir_s_n_exp.i"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.i_in"),
            tgt=UidPort("P:sir_s_n_exp.i"),
        ),
        Wire(
            uid=UidWire("W:sir.i_in>sir_i_n_exp.i"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.i_in"),
            tgt=UidPort("P:sir_i_n_exp.i"),
        ),
        Wire(
            uid=UidWire("W:sir.i_in>sir_r_n_exp.i"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.i_in"),
            tgt=UidPort("P:sir_r_n_exp.i"),
        ),
        Wire(
            uid=UidWire("W:sir.r_in>sir_r_n_exp.r"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.r_in"),
            tgt=UidPort("P:sir_r_n_exp.r"),
        ),
        Wire(
            uid=UidWire("W:sir_s_n_exp.s_n>sir_scale_exp.s_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_s_n_exp.s_n"),
            tgt=UidPort("P:sir_scale_exp.s_n"),
        ),
        Wire(
            uid=UidWire("W:sir_s_n_exp.s_n>sir_s_exp.s_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_s_n_exp.s_n"),
            tgt=UidPort("P:sir_s_exp.s_n"),
        ),
        Wire(
            uid=UidWire("W:sir_i_n_exp.i_n>sir_scale_exp.i_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_i_n_exp.i_n"),
            tgt=UidPort("P:sir_scale_exp.i_n"),
        ),
        Wire(
            uid=UidWire("W:sir_i_n_exp.i_n>sir_i_exp.i_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_i_n_exp.i_n"),
            tgt=UidPort("P:sir_i_exp.i_n"),
        ),
        Wire(
            uid=UidWire("W:sir_r_n_exp.r_n>sir_scale_exp.r_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_r_n_exp.r_n"),
            tgt=UidPort("P:sir_scale_exp.r_n"),
        ),
        Wire(
            uid=UidWire("W:sir_r_n_exp.r_n>sir_r_exp.r_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_r_n_exp.r_n"),
            tgt=UidPort("P:sir_r_exp.r_n"),
        ),
        Wire(
            uid=UidWire("W:sir_scale_exp.scale>sir_s_exp.scale"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_scale_exp.scale"),
            tgt=UidPort("P:sir_s_exp.scale"),
        ),
        Wire(
            uid=UidWire("W:sir_scale_exp.scale>sir_i_exp.scale"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_scale_exp.scale"),
            tgt=UidPort("P:sir_i_exp.scale"),
        ),
        Wire(
            uid=UidWire("W:sir_scale_exp.scale>sir_r_exp.scale"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_scale_exp.scale"),
            tgt=UidPort("P:sir_r_exp.scale"),
        ),
        Wire(
            uid=UidWire("W:sir_s_exp.s>sir.s_out"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_s_exp.s"),
            tgt=UidPort("P:sir.s_out"),
        ),
        Wire(
            uid=UidWire("W:sir_i_exp.i>sir.i_out"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_i_exp.i"),
            tgt=UidPort("P:sir.i_out"),
        ),
        Wire(
            uid=UidWire("W:sir_r_exp.r>sir.r_out"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_r_exp.r"),
            tgt=UidPort("P:sir.r_out"),
        ),
    ]

    ports_sir = [
        # -- sir() Ports --
        # sir in
        Port(
            uid=UidPort("P:sir.n"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Integer"),
            name="n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.beta"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="beta",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.gamma"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.s_in"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="s",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.i_in"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.r_in"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="r",
            value=None,
            metadata=None,
        ),
        # sir out
        Port(
            uid=UidPort("P:sir.s_out"),
            box=UidBox("B:sir"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="s",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.i_out"),
            box=UidBox("B:sir"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.r_out"),
            box=UidBox("B:sir"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="r",
            value=None,
            metadata=None,
        ),
        # sir_s_n_exp in
        Port(
            uid=UidPort("P:sir_s_n_exp.beta"),
            box=UidBox("B:sir_s_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="beta",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_s_n_exp.s"),
            box=UidBox("B:sir_s_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="s",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_s_n_exp.i"),
            box=UidBox("B:sir_s_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        # sir_s_n_exp out
        Port(
            uid=UidPort("P:sir_s_n_exp.s_n"),
            box=UidBox("B:sir_s_n_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="s_n",
            value=None,
            metadata=None,
        ),
        # sir_s_n_exp in
        Port(
            uid=UidPort("P:sir_i_n_exp.beta"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="beta",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_n_exp.s"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="s",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_n_exp.i"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_n_exp.gamma"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma",
            value=None,
            metadata=None,
        ),
        # sir_i_n_exp out
        Port(
            uid=UidPort("P:sir_i_n_exp.i_n"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="i_n",
            value=None,
            metadata=None,
        ),
        # sir_r_n_exp in
        Port(
            uid=UidPort("P:sir_r_n_exp.gamma"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_r_n_exp.i"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_r_n_exp.r"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="r",
            value=None,
            metadata=None,
        ),
        # sir_r_n_exp out
        Port(
            uid=UidPort("P:sir_r_n_exp.r_n"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="r_n",
            value=None,
            metadata=None,
        ),
        # sir_scale_exp in
        Port(
            uid=UidPort("P:sir_scale_exp.n"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_scale_exp.s_n"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="s_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_scale_exp.i_n"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_scale_exp.r_n"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="r_n",
            value=None,
            metadata=None,
        ),
        # sir_scale_exp out
        Port(
            uid=UidPort("P:sir_scale_exp.scale"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="scale",
            value=None,
            metadata=None,
        ),
        # sir_s_exp in
        Port(
            uid=UidPort("P:sir_s_exp.s_n"),
            box=UidBox("B:sir_s_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="s_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_s_exp.scale"),
            box=UidBox("B:sir_s_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="scale",
            value=None,
            metadata=None,
        ),
        # sir_s_exp out
        Port(
            uid=UidPort("P:sir_s_exp.s"),
            box=UidBox("B:sir_s_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="s",
            value=None,
            metadata=None,
        ),
        # sir_i_exp in
        Port(
            uid=UidPort("P:sir_i_exp.i_n"),
            box=UidBox("B:sir_i_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_exp.scale"),
            box=UidBox("B:sir_i_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="scale",
            value=None,
            metadata=None,
        ),
        # sir_i_exp out
        Port(
            uid=UidPort("P:sir_i_exp.i"),
            box=UidBox("B:sir_i_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        # sir_r_exp in
        Port(
            uid=UidPort("P:sir_r_exp.r_n"),
            box=UidBox("B:sir_r_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="r_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_r_exp.scale"),
            box=UidBox("B:sir_r_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="scale",
            value=None,
            metadata=None,
        ),
        # sir_r_exp out
        Port(
            uid=UidPort("P:sir_r_exp.r"),
            box=UidBox("B:sir_r_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="r",
            value=None,
            metadata=None,
        ),
    ]

    # -- sir() --

    # Expression sir_s_n_exp
    # e1 = (* -1 beta i s) -> e1
    e1 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Int"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_s_n_exp.beta"),
            UidPort("P:sir_s_n_exp.s"),
            UidPort("P:sir_s_n_exp.i"),
        ],
    )
    # e2 = (+ e1 s) -> e2
    e2 = Expr(call=RefOp(UidOp("+")), args=[e1, UidPort("P:sir_s_n_exp.s")])
    sir_s_n_exp = Expression(
        uid=UidBox("B:sir_s_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_s_n_exp.beta"),
            UidPort("P:sir_s_n_exp.s"),
            UidPort("P:sir_s_n_exp.i"),
            UidPort("P:sir_s_n_exp.s_n"),
        ],
        tree=e2,
        metadata=None,
    )

    # Expression sir_i_n_exp
    # e3 = (* beta s i) -> e3
    e3 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_i_n_exp.beta"),
            UidPort("P:sir_i_n_exp.s"),
            UidPort("P:sir_i_n_exp.i"),
        ],
    )
    # e4 = (* -1 i gamma) -> e4
    e4 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Int"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_i_n_exp.i"),
            UidPort("P:sir_i_n_exp.gamma"),
        ],
    )
    # e5 = (+ e3 e4 i)
    e5 = Expr(
        call=RefOp(UidOp("+")), args=[e3, e4, UidPort("P:sir_i_n_exp.i")]
    )
    sir_i_n_exp = Expression(
        uid=UidBox("B:sir_i_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_i_n_exp.beta"),
            UidPort("P:sir_i_n_exp.s"),
            UidPort("P:sir_i_n_exp.i"),
            UidPort("P:sir_i_n_exp.gamma"),
            UidPort("P:sir_i_n_exp.i_n"),
        ],
        tree=e5,
        metadata=None,
    )

    # Expression sir_r_n_exp
    # e6 = (* gamma i r) -> e6
    e6 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_r_n_exp.gamma"),
            UidPort("P:sir_r_n_exp.i"),
            UidPort("P:sir_r_n_exp.r"),
        ],
    )
    # e7 = (+ e6 r) -> e7
    e7 = Expr(call=RefOp(UidOp("+")), args=[e6, UidPort("P:sir_r_n_exp.r")])
    sir_r_n_exp = Expression(
        uid=UidBox("B:sir_r_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_r_n_exp.gamma"),
            UidPort("P:sir_r_n_exp.i"),
            UidPort("P:sir_r_n_exp.r"),
            UidPort("P:sir_r_n_exp.r_n"),
        ],
        tree=e7,
        metadata=None,
    )

    # Expression sir_scale_exp
    # e8 = (+ s_n i_n r_n) -> e8
    e8 = Expr(
        call=RefOp(UidOp("+")),
        args=[
            UidPort("P:sir_scale_exp.s_n"),
            UidPort("P:sir_scale_exp.i_n"),
            UidPort("P:sir_scale_exp.r_n"),
        ],
    )
    # e9 = (/ n e8)
    e9 = Expr(call=RefOp(UidOp("/")), args=[UidPort("P:sir_scale_exp.n"), e8])
    sir_scale_exp = Expression(
        uid=UidBox("B:sir_scale_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_scale_exp.n"),
            UidPort("P:sir_scale_exp.s_n"),
            UidPort("P:sir_scale_exp.i_n"),
            UidPort("P:sir_scale_exp.r_n"),
            UidPort("P:sir_scale_exp.scale"),
        ],
        tree=e9,
        metadata=None,
    )

    # Expression sir_s_exp
    # e10 = (* s_n scale) -> e10
    e10 = Expr(
        call=RefOp(UidOp("*")),
        args=[UidPort("P:sir_s_exp.s_n"), UidPort("P:sir_s_exp.scale")],
    )
    sir_s_exp = Expression(
        uid=UidBox("B:sir_s_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_s_exp.s_n"),
            UidPort("P:sir_s_exp.scale"),
            UidPort("P:sir_s_exp.s"),
        ],
        tree=e10,
        metadata=None,
    )

    # Expression sir_i_exp
    # e11 = (* i_n scale) -> e11
    e11 = Expr(
        call=RefOp(UidOp("*")),
        args=[UidPort("P:sir_i_exp.i_n"), UidPort("P:sir_i_exp.scale")],
    )
    sir_i_exp = Expression(
        uid=UidBox("B:sir_i_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_i_exp.i_n"),
            UidPort("P:sir_i_exp.scale"),
            UidPort("P:sir_i_exp.i"),
        ],
        tree=e11,
        metadata=None,
    )

    # Expression sir_r_exp
    # e12 = (* r_n scale) -> e12
    e12 = Expr(
        call=RefOp(UidOp("*")),
        args=[UidPort("P:sir_r_exp.r_n"), UidPort("P:sir_r_exp.scale")],
    )
    sir_r_exp = Expression(
        uid=UidBox("B:sir_r_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_r_exp.r_n"),
            UidPort("P:sir_r_exp.scale"),
            UidPort("P:sir_r_exp.r"),
        ],
        tree=e12,
        metadata=None,
    )

    # Function sir
    sir = Function(
        uid=UidBox("B:sir"),
        type=None,
        name=UidOp("sir"),
        ports=[
            UidPort("P:sir.n"),
            UidPort("P:sir.beta"),
            UidPort("P:sir.gamma"),
            UidPort("P:sir.s_in"),
            UidPort("P:sir.i_in"),
            UidPort("P:sir.r_in"),
            UidPort("P:sir.s_out"),
            UidPort("P:sir.i_out"),
            UidPort("P:sir.r_out"),
        ],
        # contents
        wires=[
            UidWire("W:sir.n>sir_scale_exp.n"),
            UidWire("W:sir.beta>sir_s_n_exp.beta"),
            UidWire("W:sir.beta>sir_i_n_exp.beta"),
            UidWire("W:sir.gamma>sir_i_n_exp.gamma"),
            UidWire("W:sir.gamma>sir_r_n_exp.gamma"),
            UidWire("W:sir.s_in>sir_s_n_exp.s"),
            UidWire("W:sir.s_in>sir_i_n_exp.s"),
            UidWire("W:sir.i_in>sir_s_n_exp.i"),
            UidWire("W:sir.i_in>sir_i_n_exp.i"),
            UidWire("W:sir.i_in>sir_r_n_exp.i"),
            UidWire("W:sir.r_in>sir_r_n_exp.r"),
            UidWire("W:sir_s_n_exp.s_n>sir_scale_exp.s_n"),
            UidWire("W:sir_s_n_exp.s_n>sir_s_exp.s_n"),
            UidWire("W:sir_i_n_exp.i_n>sir_scale_exp.i_n"),
            UidWire("W:sir_i_n_exp.i_n>sir_i_exp.i_n"),
            UidWire("W:sir_r_n_exp.r_n>sir_scale_exp.r_n"),
            UidWire("W:sir_r_n_exp.r_n>sir_r_exp.r_n"),
            UidWire("W:sir_scale_exp.scale>sir_s_exp.scale"),
            UidWire("W:sir_scale_exp.scale>sir_i_exp.scale"),
            UidWire("W:sir_scale_exp.scale>sir_r_exp.scale"),
            UidWire("W:sir_s_exp.s>sir.s_out"),
            UidWire("W:sir_i_exp.i>sir.i_out"),
            UidWire("W:sir_r_exp.r>sir.r_out"),
        ],
        boxes=[
            UidBox("B:sir_s_n_exp"),
            UidBox("B:sir_i_n_exp"),
            UidBox("B:sir_r_n_exp"),
            UidBox("B:sir_scale_exp"),
            UidBox("B:sir_s_exp"),
            UidBox("B:sir_i_exp"),
            UidBox("B:sir_r_exp"),
        ],
        junctions=None,
        metadata=None,
    )

    wires = wires_sir
    ports = ports_sir

    boxes = [
        sir,
        sir_s_n_exp,
        sir_i_n_exp,
        sir_r_n_exp,
        sir_scale_exp,
        sir_s_exp,
        sir_i_exp,
        sir_r_exp,
    ]

    variables = variables_sir

    _g = Gromet(
        uid=UidGromet("CHIME_SIR_Dyn"),
        name="CHIME_SIR_Dyn",
        type=UidType("FunctionNetwork"),
        root=UidBox("B:sir"),
        types=None,
        literals=None,
        junctions=None,
        ports=ports,
        wires=wires,
        boxes=boxes,
        variables=variables,
        metadata=[
            chime_model_description,
            chime_model_interface,
            metadatum_code_collection_ref,
            metadatum_textual_document_reference_set,
        ],
    )

    return _g


# -----------------------------------------------------------------------------
# Script
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    gromet_to_json(generate_gromet())
