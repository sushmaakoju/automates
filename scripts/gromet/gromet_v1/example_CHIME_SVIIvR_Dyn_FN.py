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
        name="CHIME SVIIvR Dynamics",
        description="Version of the CHIME model dynamics that extends the core SIR dynamics to add vaccination (V) and vaccinated but infected (Iv) compartmemts.",
    )

    # TODO: Regenerate ModelInterface
    chime_model_interface = ModelInterface(
        uid=UidMetadatum("chime_model_interface"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        variables=[
            UidVariable("V:n"),
            UidVariable("V:beta"),
            UidVariable("V:vaccination_rate"),
            UidVariable("V:vaccination_efficacy"),
            UidVariable("V:gamma_vaccinated"),
            UidVariable("V:gamma_unvaccinated"),
            UidVariable("V:s"),
            UidVariable("V:v"),
            UidVariable("V:i"),
            UidVariable("V:i_v"),
            UidVariable("V:r"),
            UidVariable("V:s_n"),
            UidVariable("V:v_n"),
            UidVariable("V:i_n"),
            UidVariable("V:i_v_n"),
            UidVariable("V:r_n"),
            UidVariable("V:scale"),
            UidVariable("V:s_1"),
            UidVariable("V:v_1"),
            UidVariable("V:i_1"),
            UidVariable("V:i_v_1"),
            UidVariable("V:r_1"),
        ],
        parameters=[
            UidVariable("V:beta"),
            UidVariable("V:vaccination_rate"),
            UidVariable("V:vaccination_efficacy"),
            UidVariable("V:gamma_vaccinated"),
            UidVariable("V:gamma_unvaccinated"),
        ],
        initial_conditions=[
            UidVariable("V:n"),
            UidVariable("V:s"),
            UidVariable("V:v"),
            UidVariable("V:i"),
            UidVariable("V:i_v"),
            UidVariable("V:r"),
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

    # -- Equation definition metadata

    # ---------------
    # sir_s_n_exp
    eqn_extraction_sir_s_n_exp = EquationExtraction(
        document_reference_uid=UidDocumentReference("chime_webdocs_as_pdf"),
        equation_number=0,
        equation_source_latex="S \\leftarrow S - \\beta S I - \\beta S I_v - v_r S",
        equation_source_mml='<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" title="S \leftarrow S - \beta S I - \beta S I_v - v_r S "><mrow><mi>S</mi><mo>←</mo><mi>S</mi><mo>-</mo><mi>β</mi><mi>S</mi><mi>I</mi><mo>-</mo><mi>β</mi><mi>S</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>-</mo><msub><mrow><mi>v</mi></mrow><mrow><mi>r</mi></mrow></msub><mi>S</mi></mrow></math>',
    )
    # referenced on line 4647
    eqn_def_sir_s_n_exp = EquationDefinition(
        uid=UidMetadatum("eqn_def_sir_s_n_exp"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        equation_extraction=eqn_extraction_sir_s_n_exp,
    )

    # ---------------
    # sir_v_n_exp
    eqn_extraction_sir_v_n_exp = EquationExtraction(
        document_reference_uid=UidDocumentReference("chime_webdocs_as_pdf"),
        equation_number=1,
        equation_source_latex="V \\leftarrow V + v_r S - \\beta(1 - v_e) V I - \\beta(1 - v_e) V I_v",
        equation_source_mml='<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" title="V \leftarrow V + v_r S - \beta(1 - v_e) V I - \beta(1 - v_e) V I_v "><mrow><mi>V</mi><mo>←</mo><mi>V</mi><mo>+</mo><msub><mrow><mi>v</mi></mrow><mrow><mi>r</mi></mrow></msub><mi>S</mi><mo>-</mo><mi>β</mi><mo maxsize="1">(</mo><mn>1</mn><mo>-</mo><msub><mrow><mi>v</mi></mrow><mrow><mi>e</mi></mrow></msub><mo maxsize="1">)</mo><mi>V</mi><mi>I</mi><mo>-</mo><mi>β</mi><mo maxsize="1">(</mo><mn>1</mn><mo>-</mo><msub><mrow><mi>v</mi></mrow><mrow><mi>e</mi></mrow></msub><mo maxsize="1">)</mo><mi>V</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub></mrow></math>',
    )
    # referenced on line 4701
    eqn_def_sir_v_n_exp = EquationDefinition(
        uid=UidMetadatum("eqn_def_sir_v_n_exp"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        equation_extraction=eqn_extraction_sir_v_n_exp,
    )

    # ---------------
    # sir_i_n_exp
    eqn_extraction_sir_i_n_exp = EquationExtraction(
        document_reference_uid=UidDocumentReference("chime_webdocs_as_pdf"),
        equation_number=2,
        equation_source_latex="I \\leftarrow I + \\beta S I + \\beta S I_v - \\gamma I",
        equation_source_mml='<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" title="I \leftarrow I + \beta S I + \beta S I_v - \gamma I "><mrow><mi>I</mi><mo>←</mo><mi>I</mi><mo>+</mo><mi>β</mi><mi>S</mi><mi>I</mi><mo>+</mo><mi>β</mi><mi>S</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>-</mo><mi>γ</mi><mi>I</mi></mrow></math>',
    )
    # referenced on line 4809
    eqn_def_sir_i_n_exp = EquationDefinition(
        uid=UidMetadatum("eqn_def_sir_i_n_exp"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        equation_extraction=eqn_extraction_sir_i_n_exp,
    )

    # ---------------
    # sir_i_v_n_exp
    eqn_extraction_sir_i_v_n_exp = EquationExtraction(
        document_reference_uid=UidDocumentReference("chime_webdocs_as_pdf"),
        equation_number=3,
        equation_source_latex="I_v \\leftarrow I_v + \\beta (1 - v_e) V I + \\beta (1 - v_e) V I_v - \\gamma I_v",
        equation_source_mml='<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" title="I_v \leftarrow I_v + \beta (1 - v_e) V I + \beta (1 - v_e) V I_v - \gamma I_v "><mrow><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>←</mo><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>+</mo><mi>β</mi><mo maxsize="1">(</mo><mn>1</mn><mo>-</mo><msub><mrow><mi>v</mi></mrow><mrow><mi>e</mi></mrow></msub><mo maxsize="1">)</mo><mi>V</mi><mi>I</mi><mo>+</mo><mi>β</mi><mo maxsize="1">(</mo><mn>1</mn><mo>-</mo><msub><mrow><mi>v</mi></mrow><mrow><mi>e</mi></mrow></msub><mo maxsize="1">)</mo><mi>V</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>-</mo><mi>γ</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub></mrow></math>',
    )
    # referenced on line 4748
    eqn_def_sir_i_v_n_exp = EquationDefinition(
        uid=UidMetadatum("eqn_def_sir_i_v_n_exp"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        equation_extraction=eqn_extraction_sir_i_v_n_exp,
    )

    # ---------------
    # sir_r_n_exp
    eqn_extraction_sir_r_n_exp = EquationExtraction(
        document_reference_uid=UidDocumentReference("chime_webdocs_as_pdf"),
        equation_number=4,
        equation_source_latex="R \\leftarrow R + \\gamma I_v + \\gamma I",
        equation_source_mml='<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" title="R \leftarrow R + \gamma I_v + \gamma I "><mrow><mi>R</mi><mo>←</mo><mi>R</mi><mo>+</mo><mi>γ</mi><msub><mrow><mi>I</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>+</mo><mi>γ</mi><mi>I</mi></mrow></math>',
    )
    # referenced on line 4857
    eqn_def_sir_r_n_exp = EquationDefinition(
        uid=UidMetadatum("eqn_def_sir_r_n_exp"),
        provenance=Provenance(
            method=MetadatumMethod("Manual_claytonm@az"),
            timestamp=get_current_datetime(),
        ),
        equation_extraction=eqn_extraction_sir_r_n_exp,
    )

    # ----- Model component definitions -----

    variables_sir = [
        # TODO: Remaining Variables will be defined in post-processing
    ]

    wires_sir = [
        # -- sir() Wires --
        ### -- CHIME_SVIIvR -- START
        Wire(
            uid=UidWire("W:sir.in.i_v>sir_s_n_exp.in.i_v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.i_v"),
            tgt=UidPort("P:sir_s_n_exp.in.i_v"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.vaccination_rate>sir_s_n_exp.in.vaccination_rate"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.vaccination_rate"),
            tgt=UidPort("P:sir_s_n_exp.in.vaccination_rate"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.vaccination_rate>sir_v_n_exp.in.vaccination_rate"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.vaccination_rate"),
            tgt=UidPort("P:sir_v_n_exp.in.vaccination_rate"),
        ),
        Wire(
            uid=UidWire("W:sir.s_in>sir_v_n_exp.in.s"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.s_in"),
            tgt=UidPort("P:sir_v_n_exp.in.s"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.vaccination_efficacy>sir_v_n_exp.in.vaccination_efficacy"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.vaccination_efficacy"),
            tgt=UidPort("P:sir_v_n_exp.in.vaccination_efficacy"),
        ),
        Wire(
            uid=UidWire("W:sir.beta>sir_v_n_exp.in.beta"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.beta"),
            tgt=UidPort("P:sir_v_n_exp.in.beta"),
        ),
        Wire(
            uid=UidWire("W:sir.in.v>sir_v_n_exp.in.v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.v"),
            tgt=UidPort("P:sir_v_n_exp.in.v"),
        ),
        Wire(
            uid=UidWire("W:sir.i_in>sir_v_n_exp.in.i"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.i_in"),
            tgt=UidPort("P:sir_v_n_exp.in.i"),
        ),
        Wire(
            uid=UidWire("W:sir.in.i_v>sir_v_n_exp.in.i_v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.i_v"),
            tgt=UidPort("P:sir_v_n_exp.in.i_v"),
        ),
        Wire(
            uid=UidWire("W:sir_v_n_exp.out.v_n>sir_scale_exp.v_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_v_n_exp.out.v_n"),
            tgt=UidPort("P:sir_scale_exp.v_n"),
        ),
        Wire(
            uid=UidWire("W:sir_v_n_exp.out.v_n>sir_v_exp.in.v_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_v_n_exp.out.v_n"),
            tgt=UidPort("P:sir_v_exp.in.v_n"),
        ),
        Wire(
            uid=UidWire("W:sir.in.i_v>sir_i_n_exp.i_v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.i_v"),
            tgt=UidPort("P:sir_i_n_exp.i_v"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.gamma_unvaccinated>sir_i_n_exp.gamma_unvaccinated"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.gamma_unvaccinated"),
            tgt=UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.vaccination_efficacy>sir_i_v_n_exp.in.vaccine_efficacy"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.vaccination_efficacy"),
            tgt=UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy"),
        ),
        Wire(
            uid=UidWire("W:sir.beta>sir_i_v_n_exp.in.beta"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.beta"),
            tgt=UidPort("P:sir_i_v_n_exp.in.beta"),
        ),
        Wire(
            uid=UidWire("W:sir.in.v>sir_i_v_n_exp.in.v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.v"),
            tgt=UidPort("P:sir_i_v_n_exp.in.v"),
        ),
        Wire(
            uid=UidWire("W:sir.i_in>sir_i_v_n_exp.in.i"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.i_in"),
            tgt=UidPort("P:sir_i_v_n_exp.in.i"),
        ),
        Wire(
            uid=UidWire("W:sir.in.i_v>sir_i_v_n_exp.in.i_v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.i_v"),
            tgt=UidPort("P:sir_i_v_n_exp.in.i_v"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.gamma_vaccinated>sir_i_v_n_exp.in.gamma_vaccinated"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.gamma_vaccinated"),
            tgt=UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
        ),
        Wire(
            uid=UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_scale_exp.i_v_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_i_v_n_exp.out.i_v_n"),
            tgt=UidPort("P:sir_scale_exp.i_v_n"),
        ),
        Wire(
            uid=UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_i_v_exp.in.i_v_n"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_i_v_n_exp.out.i_v_n"),
            tgt=UidPort("P:sir_i_v_exp.in.i_v_n"),
        ),
        Wire(
            uid=UidWire("W:sir_scale_exp.scale>sir_v_exp.in.scale"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_scale_exp.scale"),
            tgt=UidPort("P:sir_v_exp.in.scale"),
        ),
        Wire(
            uid=UidWire("W:sir_v_exp.out.v>sir.out.v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_v_exp.out.v"),
            tgt=UidPort("P:sir.out.v"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.gamma_vaccinated>sir_r_n_exp.in.gamma_vaccinated"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.gamma_vaccinated"),
            tgt=UidPort("P:sir_r_n_exp.in.gamma_vaccinated"),
        ),
        Wire(
            uid=UidWire("W:sir.in.i_v>sir_r_n_exp.in.i_v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.i_v"),
            tgt=UidPort("P:sir_r_n_exp.in.i_v"),
        ),
        Wire(
            uid=UidWire(
                "W:sir.in.gamma_unvaccinated>sir_r_n_exp.in.gamma_unvaccinated"
            ),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir.in.gamma_unvaccinated"),
            tgt=UidPort("P:sir_r_n_exp.in.gamma_unvaccinated"),
        ),
        Wire(
            uid=UidWire("W:sir_scale_exp.scale>sir_i_v_exp.in.scale"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_scale_exp.scale"),
            tgt=UidPort("P:sir_i_v_exp.in.scale"),
        ),
        Wire(
            uid=UidWire("W:sir_i_v_exp.out.i_v>sir.out.i_v"),
            type=None,
            value_type=UidType("Float"),
            name=None,
            value=None,
            metadata=None,
            src=UidPort("P:sir_i_v_exp.out.i_v"),
            tgt=UidPort("P:sir.out.i_v"),
        ),
        ### -- CHIME_SVIIvR -- END
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
        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:sir.gamma>sir_i_n_exp.gamma"),
        #      type=None,
        #      value_type=UidType("Float"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:sir.gamma"),
        #      tgt=UidPort("P:sir_i_n_exp.gamma")),
        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:sir.gamma>sir_r_n_exp.gamma"),
        #      type=None,
        #      value_type=UidType("Float"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:sir.gamma"),
        #      tgt=UidPort("P:sir_r_n_exp.gamma")),
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
        ### -- CHIME_SVIIvR -- START
        # sir in CHIME_SVIIvR
        Port(
            uid=UidPort("P:sir.in.vaccination_rate"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="vaccination_rate",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.in.vaccination_efficacy"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="vaccination_efficacy",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.in.v"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.in.i_v"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.in.gamma_unvaccinated"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma_unvaccinated",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.in.gamma_vaccinated"),
            box=UidBox("B:sir"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma_vaccinated",
            value=None,
            metadata=None,
        ),
        # sir out CHIME_SVIIvR
        Port(
            uid=UidPort("P:sir.out.v"),
            box=UidBox("B:sir"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir.out.i_v"),
            box=UidBox("B:sir"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        # sir_v_n_exp in
        Port(
            uid=UidPort("P:sir_v_n_exp.in.vaccination_rate"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="vaccination_rate",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_n_exp.in.s"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="s",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_n_exp.in.vaccination_efficacy"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="vaccination_efficacy",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_n_exp.in.beta"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="beta",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_n_exp.in.v"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_n_exp.in.i"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_n_exp.in.i_v"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        # sir_v_n_exp out
        Port(
            uid=UidPort("P:sir_v_n_exp.out.v_n"),
            box=UidBox("B:sir_v_n_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="v_n",
            value=None,
            metadata=None,
        ),
        # sir_i_v_n_exp in
        Port(
            uid=UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="vaccine_efficacy",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_v_n_exp.in.beta"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="beta",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_v_n_exp.in.v"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_v_n_exp.in.i"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_v_n_exp.in.i_v"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma_vaccinated",
            value=None,
            metadata=None,
        ),
        # sir_i_v_n_exp out
        Port(
            uid=UidPort("P:sir_i_v_n_exp.out.i_v_n"),
            box=UidBox("B:sir_i_v_n_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="i_v_n",
            value=None,
            metadata=None,
        ),
        # sir_i_v_n_exp in
        Port(
            uid=UidPort("P:sir_r_n_exp.in.gamma_vaccinated"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma_vaccinated",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_r_n_exp.in.i_v"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_r_n_exp.in.gamma_unvaccinated"),
            box=UidBox("B:sir_r_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma_unvaccinated",
            value=None,
            metadata=None,
        ),
        # sir_i_n_exp in
        Port(
            uid=UidPort("P:sir_i_n_exp.i_v"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
            box=UidBox("B:sir_i_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="gamma_unvaccinated",
            value=None,
            metadata=None,
        ),
        # sir_s_n_exp in
        Port(
            uid=UidPort("P:sir_s_n_exp.in.i_v"),
            box=UidBox("B:sir_s_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_s_n_exp.in.vaccination_rate"),
            box=UidBox("B:sir_s_n_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="vaccination_rate",
            value=None,
            metadata=None,
        ),
        # sir_v_exp in
        Port(
            uid=UidPort("P:sir_v_exp.in.v_n"),
            box=UidBox("B:sir_v_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="v_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_v_exp.in.scale"),
            box=UidBox("B:sir_v_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="scale",
            value=None,
            metadata=None,
        ),
        # sir_v_exp out
        Port(
            uid=UidPort("P:sir_v_exp.out.v"),
            box=UidBox("B:sir_v_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="v",
            value=None,
            metadata=None,
        ),
        # sir_i_v_exp in
        Port(
            uid=UidPort("P:sir_i_v_exp.in.i_v_n"),
            box=UidBox("B:sir_i_v_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_i_v_exp.in.scale"),
            box=UidBox("B:sir_i_v_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="scale",
            value=None,
            metadata=None,
        ),
        # sir_i_v_exp out
        Port(
            uid=UidPort("P:sir_i_v_exp.out.i_v"),
            box=UidBox("B:sir_i_v_exp"),
            type=UidType("PortOutput"),
            value_type=UidType("Float"),
            name="i_v",
            value=None,
            metadata=None,
        ),
        # sir_scale_exp in CHIME_SVIIvR
        Port(
            uid=UidPort("P:sir_scale_exp.v_n"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="v_n",
            value=None,
            metadata=None,
        ),
        Port(
            uid=UidPort("P:sir_scale_exp.i_v_n"),
            box=UidBox("B:sir_scale_exp"),
            type=UidType("PortInput"),
            value_type=UidType("Float"),
            name="i_v_n",
            value=None,
            metadata=None,
        ),
        ### -- CHIME_SVIIvR -- END
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
        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:sir.gamma"),
        #      box=UidBox("B:sir"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),
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
        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:sir_i_n_exp.gamma"),
        #      box=UidBox("B:sir_i_n_exp"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),
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
        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:sir_r_n_exp.gamma"),
        #      box=UidBox("B:sir_r_n_exp"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),
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
    # sir_s_n_exp_e0 = (* -1 beta s i)
    sir_s_n_exp_e0 = Expr(
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
    ### -- CHIME_SVIIvR -- START
    # sir_s_n_exp_e1 = (* -1 beta s i_v)
    sir_s_n_exp_e1 = Expr(
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
            UidPort("P:sir_s_n_exp.in.i_v"),
        ],
    )
    # sir_s_n_exp_e2 = (* -1 vaccination_rate s)
    sir_s_n_exp_e2 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Int"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_s_n_exp.in.vaccination_rate"),
            UidPort("P:sir_s_n_exp.s"),
        ],
    )
    ### -- CHIME_SVIIvR -- END
    # e2 = (+ e1 s) -> e2
    sir_s_n_exp_e3 = Expr(
        call=RefOp(UidOp("+")),
        args=[
            sir_s_n_exp_e0,
            ### -- CHIME_SVIIvR -- START
            sir_s_n_exp_e1,
            sir_s_n_exp_e2,
            ### -- CHIME_SVIIvR -- END
            UidPort("P:sir_s_n_exp.s"),
        ],
    )
    sir_s_n_exp = Expression(
        uid=UidBox("B:sir_s_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_s_n_exp.beta"),
            UidPort("P:sir_s_n_exp.s"),
            UidPort("P:sir_s_n_exp.i"),
            ### -- CHIME_SVIIvR -- START
            UidPort("P:sir_s_n_exp.in.i_v"),
            UidPort("P:sir_s_n_exp.in.vaccination_rate"),
            ### -- CHIME_SVIIvR -- END
            UidPort("P:sir_s_n_exp.s_n"),
        ],
        tree=sir_s_n_exp_e3,
        metadata=[eqn_def_sir_s_n_exp],
    )

    ### -- CHIME_SVIIvR -- START

    # -- sir_v_n_exp
    # sir_v_n_exp_0 = (* vaccination_rate s)
    sir_v_n_exp_0 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_v_n_exp.in.vaccination_rate"),
            UidPort("P:sir_v_n_exp.in.s"),
        ],
    )
    # sir_v_n_exp_1 = (- 1 vaccine_efficacy)
    sir_v_n_exp_1 = Expr(
        call=RefOp(UidOp("-")),
        args=[
            Literal(
                uid=None,
                type=UidType("Integer"),
                value=Val("1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_v_n_exp.in.vaccination_efficacy"),
        ],
    )
    # sir_v_n_exp_1 = (* -1 beta sir_v_n_exp_1 v i)
    sir_v_n_exp_2 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Integer"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_v_n_exp.in.beta"),
            sir_v_n_exp_1,
            UidPort("P:sir_v_n_exp.in.v"),
            UidPort("P:sir_v_n_exp.in.i"),
        ],
    )
    # sir_v_n_exp_3 = (* -1 beta sir_v_n_exp_1 v i_v)
    sir_v_n_exp_3 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Integer"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_v_n_exp.in.beta"),
            sir_v_n_exp_1,
            UidPort("P:sir_v_n_exp.in.v"),
            UidPort("P:sir_v_n_exp.in.i_v"),
        ],
    )
    # sir_v_n_exp_4 = (+ sir_v_n_exp_0 sir_v_n_exp_2 sir_v_n_exp_3)
    sir_v_n_exp_4 = Expr(
        call=RefOp(UidOp("+")),
        args=[sir_v_n_exp_0, sir_v_n_exp_2, sir_v_n_exp_3],
    )
    # sir_v_n_exp_4 = (+ sir_v_n_exp_0 sir_v_n_exp_1 sir_v_n_exp_3 v)
    sir_v_n_exp = Expression(
        uid=UidBox("B:sir_v_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_v_n_exp.in.vaccination_rate"),
            UidPort("P:sir_v_n_exp.in.s"),
            UidPort("P:sir_v_n_exp.in.vaccination_efficacy"),
            UidPort("P:sir_v_n_exp.in.beta"),
            UidPort("P:sir_v_n_exp.in.v"),
            UidPort("P:sir_v_n_exp.in.i"),
            UidPort("P:sir_v_n_exp.in.i_v"),
            UidPort("P:sir_v_n_exp.out.v_n"),
        ],
        tree=sir_v_n_exp_4,
        metadata=[eqn_def_sir_v_n_exp],
    )

    # -- sir_i_v_n_exp
    # sir_i_v_n_exp_0 = (- 1 vaccine_efficacy)
    sir_i_v_n_exp_0 = Expr(
        call=RefOp(UidOp("-")),
        args=[
            Literal(
                uid=None,
                type=UidType("Integer"),
                value=Val("1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy"),
        ],
    )
    # sir_i_v_n_exp_1 = (* beta sir_i_v_n_exp_0 v i)
    sir_i_v_n_exp_1 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_i_v_n_exp.in.beta"),
            sir_i_v_n_exp_0,
            UidPort("P:sir_i_v_n_exp.in.v"),
            UidPort("P:sir_i_v_n_exp.in.i"),
        ],
    )
    # sir_i_v_n_exp_2 = (* beta sir_i_v_n_exp_0 v i_v)
    sir_i_v_n_exp_2 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_i_v_n_exp.in.beta"),
            sir_i_v_n_exp_0,
            UidPort("P:sir_i_v_n_exp.in.v"),
            UidPort("P:sir_i_v_n_exp.in.i_v"),
        ],
    )
    # sir_i_v_n_exp_3 = (* -1 gamma_vaccinated i_v)
    sir_i_v_n_exp_3 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Integer"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
            UidPort("P:sir_i_v_n_exp.in.i_v"),
        ],
    )
    # sir_i_v_n_exp_4 = (+ sir_i_v_n_exp_1 sir_i_v_n_exp_2 sir_i_v_n_exp_3 i_v)
    sir_i_v_n_exp_4 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            sir_i_v_n_exp_1,
            sir_i_v_n_exp_2,
            sir_i_v_n_exp_3,
            UidPort("P:sir_i_v_n_exp.in.i_v"),
        ],
    )
    sir_i_v_n_exp = Expression(
        uid=UidBox("B:sir_i_v_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy"),
            UidPort("P:sir_i_v_n_exp.in.beta"),
            UidPort("P:sir_i_v_n_exp.in.v"),
            UidPort("P:sir_i_v_n_exp.in.i"),
            UidPort("P:sir_i_v_n_exp.in.i_v"),
            UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
            UidPort("P:sir_i_v_n_exp.out.i_v_n"),
        ],
        tree=sir_i_v_n_exp_4,
        metadata=[eqn_def_sir_i_v_n_exp],
    )

    ### -- CHIME_SVIIvR -- END

    # Expression sir_i_n_exp
    # e3 = (* beta s i)
    sir_i_n_exp_e0 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_i_n_exp.beta"),
            UidPort("P:sir_i_n_exp.s"),
            UidPort("P:sir_i_n_exp.i"),
        ],
    )
    # sir_i_n_exp_e1 = (* beta s i_v)
    sir_i_n_exp_e1 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_i_n_exp.beta"),
            UidPort("P:sir_i_n_exp.s"),
            UidPort("P:sir_i_n_exp.i_v"),
        ],
    )
    # sir_i_n_exp_e2 = (* -1 gamma_unvaccinated i)
    sir_i_n_exp_e2 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            Literal(
                uid=None,
                type=UidType("Integer"),
                value=Val("-1"),
                name=None,
                metadata=None,
            ),
            UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
            UidPort("P:sir_i_n_exp.i"),
        ],
    )

    # sir_i_n_exp_e3 = (+ sir_i_n_exp_e0 sir_i_n_exp_e1 sir_i_n_exp_e2 i)
    sir_i_n_exp_e3 = Expr(
        call=RefOp("+"),
        args=[
            sir_i_n_exp_e0,
            sir_i_n_exp_e1,
            sir_i_n_exp_e2,
            UidPort("P:sir_i_n_exp.i"),
        ],
    )
    # # e4 = (* -1 i gamma) -> e4
    # e4 = Expr(call=RefOp(UidOp('*')),
    #           args=[Literal(uid=None, type=UidType("Int"), value=Val("-1"),
    #                         name=None, metadata=None),
    #                 UidPort("P:sir_i_n_exp.i"),
    #
    #                 # TODO
    #                 # REMOVE_CHIME_SIR_Base
    #                 # UidPort("P:sir_i_n_exp.gamma")
    #
    #                 ])
    # # e5 = (+ e3 e4 i)
    # e5 = Expr(call=RefOp(UidOp('+')),
    #           args=[sir_i_n_exp_e0, e4, UidPort("P:sir_i_n_exp.i")])
    sir_i_n_exp = Expression(
        uid=UidBox("B:sir_i_n_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_i_n_exp.beta"),
            UidPort("P:sir_i_n_exp.s"),
            UidPort("P:sir_i_n_exp.i"),
            # REMOVE_CHIME_SIR_Base
            # UidPort("P:sir_i_n_exp.gamma"),
            ### -- CHIME_SVIIvR -- START
            UidPort("P:sir_i_n_exp.i_v"),
            UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
            ### -- CHIME_SVIIvR -- END
            UidPort("P:sir_i_n_exp.i_n"),
        ],
        tree=sir_i_n_exp_e3,
        metadata=[eqn_def_sir_i_n_exp],
    )

    # Expression sir_r_n_exp
    # # e6 = (* gamma i r) -> e6
    # e6 = Expr(call=RefOp(UidOp('*')),
    #           args=[
    #                 # TODO
    #                 # REMOVE_CHIME_SIR_Base
    #                 # UidPort("P:sir_r_n_exp.gamma"),
    #
    #                 UidPort("P:sir_r_n_exp.i"),
    #                 UidPort("P:sir_r_n_exp.r")])
    # # e7 = (+ e6 r) -> e7
    # e7 = Expr(call=RefOp(UidOp('+')),
    #           args=[e6, UidPort("P:sir_r_n_exp.r")])

    # sir_r_n_exp_e0 = (* gamma_vaccinated i_v)
    sir_r_n_exp_e0 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_r_n_exp.in.gamma_vaccinated"),
            UidPort("P:sir_r_n_exp.in.i_v"),
        ],
    )
    # sir_r_n_exp_e1 = (* gamma_unvaccinated i)
    sir_r_n_exp_e1 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_r_n_exp.in.gamma_unvaccinated"),
            UidPort("P:sir_r_n_exp.i"),
        ],
    )
    # sir_r_n_exp_e2 = (+ sir_r_n_exp_e0 sir_r_n_exp_e1 r)
    sir_r_n_exp_e2 = Expr(
        call=RefOp(UidOp("+")),
        args=[sir_r_n_exp_e0, sir_r_n_exp_e1, UidPort("P:sir_r_n_exp.r")],
    )
    sir_r_n_exp = Expression(
        uid=UidBox("B:sir_r_n_exp"),
        type=None,
        name=None,
        ports=[
            # REMOVE_CHIME_SIR_Base
            # UidPort("P:sir_r_n_exp.gamma"),
            UidPort("P:sir_r_n_exp.i"),
            UidPort("P:sir_r_n_exp.r"),
            UidPort("P:sir_r_n_exp.r_n"),
            ### -- CHIME_SVIIvR -- START
            UidPort("P:sir_r_n_exp.in.gamma_vaccinated"),
            UidPort("P:sir_r_n_exp.in.i_v"),
            UidPort("P:sir_r_n_exp.in.gamma_unvaccinated"),
            ### -- CHIME_SVIIvR -- END
        ],
        tree=sir_r_n_exp_e2,
        metadata=[eqn_def_sir_r_n_exp],
    )

    # Expression sir_scale_exp
    # e8 = (+ s_n i_n r_n) -> e8
    e8 = Expr(
        call=RefOp(UidOp("+")),
        args=[
            UidPort("P:sir_scale_exp.s_n"),
            UidPort("P:sir_scale_exp.i_n"),
            UidPort("P:sir_scale_exp.r_n"),
            ### -- CHIME_SVIIvR -- START
            UidPort("P:sir_scale_exp.v_n"),
            UidPort("P:sir_scale_exp.i_v_n")
            ### -- CHIME_SVIIvR -- END
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
            ### -- CHIME_SVIIvR -- START
            UidPort("P:sir_scale_exp.v_n"),
            UidPort("P:sir_scale_exp.i_v_n"),
            ### -- CHIME_SVIIvR -- END
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

    ### -- CHIME_SVIIvR -- START

    # sir_v_exp
    sir_v_exp_e0 = Expr(
        call=RefOp(UidOp("*")),
        args=[UidPort("P:sir_v_exp.in.v_n"), UidPort("P:sir_v_exp.in.scale")],
    )
    sir_v_exp = Expression(
        uid=UidBox("B:sir_v_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_v_exp.in.v_n"),
            UidPort("P:sir_v_exp.in.scale"),
            UidPort("P:sir_v_exp.out.v"),
        ],
        tree=sir_v_exp_e0,
        metadata=None,
    )

    # sir_i_v_exp
    sir_i_v_exp_0 = Expr(
        call=RefOp(UidOp("*")),
        args=[
            UidPort("P:sir_i_v_exp.in.i_v_n"),
            UidPort("P:sir_i_v_exp.in.scale"),
        ],
    )
    sir_i_v_exp = Expression(
        uid=UidBox("B:sir_i_v_exp"),
        type=None,
        name=None,
        ports=[
            UidPort("P:sir_i_v_exp.in.i_v_n"),
            UidPort("P:sir_i_v_exp.in.scale"),
            UidPort("P:sir_i_v_exp.out.i_v"),
        ],
        tree=sir_i_v_exp_0,
        metadata=None,
    )

    ### -- CHIME_SVIIvR -- END

    # Function sir
    sir = Function(
        uid=UidBox("B:sir"),
        type=None,
        name=UidOp("sir"),
        ports=[
            UidPort("P:sir.n"),
            UidPort("P:sir.beta"),
            # REMOVE_CHIME_SIR_Base
            # UidPort("P:sir.gamma"),
            UidPort("P:sir.s_in"),
            UidPort("P:sir.i_in"),
            UidPort("P:sir.r_in"),
            UidPort("P:sir.s_out"),
            UidPort("P:sir.i_out"),
            UidPort("P:sir.r_out"),
            ### -- CHIME_SVIIvR -- START
            UidPort("P:sir.in.vaccination_rate"),
            UidPort("P:sir.in.vaccination_efficacy"),
            UidPort("P:sir.in.gamma_unvaccinated"),
            UidPort("P:sir.in.gamma_vaccinated"),
            UidPort("P:sir.in.v"),
            UidPort("P:sir.in.i_v"),
            UidPort("P:sir.out.v"),
            UidPort("P:sir.out.i_v"),
            ### -- CHIME_SVIIvR -- END
        ],
        # contents
        wires=[
            UidWire("W:sir.n>sir_scale_exp.n"),
            UidWire("W:sir.beta>sir_s_n_exp.beta"),
            UidWire("W:sir.beta>sir_i_n_exp.beta"),
            # REMOVE_CHIME_SIR_Base
            # UidWire("W:sir.gamma>sir_i_n_exp.gamma"),
            # REMOVE_CHIME_SIR_Base
            # UidWire("W:sir.gamma>sir_r_n_exp.gamma"),
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
            ### -- CHIME_SVIIvR -- START
            UidWire("W:sir.in.i_v>sir_s_n_exp.in.i_v"),
            UidWire(
                "W:sir.in.vaccination_rate>sir_s_n_exp.in.vaccination_rate"
            ),
            UidWire(
                "W:sir.in.vaccination_rate>sir_v_n_exp.in.vaccination_rate"
            ),
            UidWire("W:sir.s_in>sir_v_n_exp.in.s"),
            UidWire(
                "W:sir.in.vaccination_efficacy>sir_v_n_exp.in.vaccination_efficacy"
            ),
            UidWire("W:sir.beta>sir_v_n_exp.in.beta"),
            UidWire("W:sir.in.v>sir_v_n_exp.in.v"),
            UidWire("W:sir.i_in>sir_v_n_exp.in.i"),
            UidWire("W:sir.in.i_v>sir_v_n_exp.in.i_v"),
            UidWire("W:sir_v_n_exp.out.v_n>sir_scale_exp.v_n"),
            UidWire("W:sir_v_n_exp.out.v_n>sir_v_exp.in.v_n"),
            UidWire("W:sir.in.i_v>sir_i_n_exp.i_v"),
            UidWire(
                "W:sir.in.gamma_unvaccinated>sir_i_n_exp.gamma_unvaccinated"
            ),
            UidWire(
                "W:sir.in.vaccination_efficacy>sir_i_v_n_exp.in.vaccine_efficacy"
            ),
            UidWire("W:sir.beta>sir_i_v_n_exp.in.beta"),
            UidWire("W:sir.in.v>sir_i_v_n_exp.in.v"),
            UidWire("W:sir.i_in>sir_i_v_n_exp.in.i"),
            UidWire("W:sir.in.i_v>sir_i_v_n_exp.in.i_v"),
            UidWire(
                "W:sir.in.gamma_vaccinated>sir_i_v_n_exp.in.gamma_vaccinated"
            ),
            UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_scale_exp.i_v_n"),
            UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_i_v_exp.in.i_v_n"),
            UidWire(
                "W:sir.in.gamma_vaccinated>sir_r_n_exp.in.gamma_vaccinated"
            ),
            UidWire("W:sir.in.i_v>sir_r_n_exp.in.i_v"),
            UidWire(
                "W:sir.in.gamma_unvaccinated>sir_r_n_exp.in.gamma_unvaccinated"
            ),
            UidWire("W:sir_scale_exp.scale>sir_v_exp.in.scale"),
            UidWire("W:sir_v_exp.out.v>sir.out.v"),
            UidWire("W:sir_scale_exp.scale>sir_i_v_exp.in.scale"),
            UidWire("W:sir_i_v_exp.out.i_v>sir.out.i_v"),
            ### -- CHIME_SVIIvR -- END
        ],
        boxes=[
            UidBox("B:sir_s_n_exp"),
            UidBox("B:sir_i_n_exp"),
            UidBox("B:sir_r_n_exp"),
            UidBox("B:sir_scale_exp"),
            UidBox("B:sir_s_exp"),
            UidBox("B:sir_i_exp"),
            UidBox("B:sir_r_exp"),
            ### -- CHIME_SVIIvR -- START
            UidBox("B:sir_v_n_exp"),
            UidBox("B:sir_i_v_n_exp"),
            UidBox("B:sir_v_exp"),
            UidBox("B:sir_i_v_exp"),
            ### -- CHIME_SVIIvR -- END
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
        ### -- CHIME_SVIIvR -- START
        sir_v_n_exp,
        sir_i_v_n_exp,
        sir_v_exp,
        sir_i_v_exp,
        ### -- CHIME_SVIIvR -- END
    ]

    variables = variables_sir

    _g = Gromet(
        uid=UidGromet("CHIME_SVIIvR_Dyn"),
        name="CHIME_SVIIvR_Dyn",
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
