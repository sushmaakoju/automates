from gromet import *  # never do this :)


# -----------------------------------------------------------------------------
# GroMEt instance
# -----------------------------------------------------------------------------

def generate_gromet() -> Gromet:
    # ----- Metadata -----

    chime_model_description = \
        ModelDescription(uid=UidMetadatum('chime_model_description'),
                         provenance=Provenance(method=MetadatumMethod('Manual_claytonm@az'),
                                               timestamp=get_current_datetime()),
                         name='CHIME SVIIvR',
                         description='Version of the CHIME model that extedns the core SIR dynamics '
                                     'to add vaccination (V) and vaccinated but infected (Iv) '
                                     'compartments.'
                                     'Maintains pre-computation of simple policy affecting relative contact '
                                     'rate and its impact on infection rate (beta).')

    # TODO: Regenerate ModelInterface
    chime_model_interface = \
        ModelInterface(
            uid=UidMetadatum("chime_model_interface"),
            provenance=Provenance(method=MetadatumMethod('Manual_claytonm@az'),
                                  timestamp=get_current_datetime()),
            variables=[
                # parameters
                # i_day                 : UidJunction("J:main.i_day")
                UidVariable("V:i_day"),
                # n_days                : UidJunction("J:main.n_days")
                UidVariable("V:n_days"),
                # N_p                   : UidJunction("J:main.N_p")
                UidVariable("V:N_p"),

                # Removed from CHIME_SIR_Base
                # # infections_days       : UidJunction("J:main.infections_days")
                # UidVariable("V:infections_days"),

                # TODO
                # CHIME_SVIIvR
                # infections_days_unvaccinated  :
                UidVariable("V:infections_days_unvaccinated"),

                # TODO
                # CHIME_SVIIvR
                # infections_days_vaccinated    :
                UidVariable("V:infections_days_vaccinated"),

                # TODO
                # CHIME_SVIIvR
                # vaccination_rate              :
                UidVariable("V:vaccination_rate"),

                # TODO
                # CHIME_SVIIvR
                # vaccine_efficacy              :
                UidVariable("V:vaccine_efficacy"),

                # relative_contact_rate : UidJunction("J:main.relative_contact_rate")
                UidVariable("V:relative_contact_rate"),

                # initial conditions
                # s_n                   : UidJunction("J:main.s_n")
                UidVariable("V:s_n"),

                # TODO
                # CHIME_SVIIvR
                # v_n                   :
                UidVariable("V:v_n"),

                # i_n                   : UidJunction("J:main.i_n")
                UidVariable("V:i_n"),

                # TODO
                # CHIME_SVIIvR
                # i_v_n                 :
                UidVariable("V:i_v_n"),

                # r_n                   : UidJunction("J:main.r_n")
                UidVariable("V:r_n"),

                # typical measurements
                # out S                 : UidPort("P:main.out.S")
                UidVariable("V:S"),

                # TODO
                # CHIME_SVIIvR
                # out V                 :
                UidVariable("V:V"),

                # out I                 : UidPort("P:main.out.I")
                UidVariable("V:I"),

                # TODO
                # CHIME_SVIIvR
                # out Iv                :
                UidVariable("V:Iv"),

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

                # REMOVE_CHIME_SIR_Base
                # infections_days       : UidJunction("J:main.infections_days")
                # UidVariable("V:infections_days"),

                # TODO
                # CHIME_SVIIvR
                # infections_days_unvaccinated  :
                UidVariable("V:infections_days_unvaccinated"),

                # TODO
                # CHIME_SVIIvR
                # infections_days_vaccinated    :
                UidVariable("V:infections_days_vaccinated"),

                # TODO
                # CHIME_SVIIvR
                # vaccination_rate              :
                UidVariable("V:vaccination_rate"),

                # TODO
                # CHIME_SVIIvR
                # vaccine_efficacy              :
                UidVariable("V:vaccine_efficacy"),

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

                # TODO
                # CHIME_SVIIvR
                # v_n                   :
                UidVariable("V:v_n"),

                # TODO
                # CHIME_SVIIvR
                # i_v_n                 :
                UidVariable("V:i_v_n"),
            ]
        )

    # -- code collection reference metadata
    file_chime_base_py_uid = UidCodeFileReference("chime_base_code")
    file_chime_base_py_code_file_reference = \
        CodeFileReference(uid=file_chime_base_py_uid,
                          name="CHIME_SIR_Base",
                          path="CHIME_SIR.py")
    askeid_chime_base_code = \
        GlobalReferenceId(type='aske_id',
                          id='2c75d1ef-906b-4a60-bad6-416eff5cbfc4')
    # https://drive.google.com/file/d/18uMBhEIqIWuO0XKz3eYUtaNg4hasmCLW/view?usp=sharing
    metadatum_code_collection_ref = \
        CodeCollectionReference(uid=UidMetadatum("chime_base_code_collection_ref"),
                                provenance=Provenance(method=MetadatumMethod('Manual_claytonm@az'),
                                                      timestamp=get_current_datetime()),
                                global_reference_id=askeid_chime_base_code,
                                file_ids=[file_chime_base_py_code_file_reference])

    # -- textual document reference set
    askeid_chime_webdoc_as_pdf = \
        GlobalReferenceId(type='aske_id',
                          id='4b429087-7e7c-4623-80fd-64fb934a8be6')
    chime_webdocs_as_pdf = \
        TextualDocumentReference(uid=UidDocumentReference("chime_webdocs_as_pdf"),
                                 global_reference_id=askeid_chime_webdoc_as_pdf,
                                 cosmos_id="COSMOS",
                                 cosmos_version_number="3.0",
                                 automates_id="AutoMATES-TR",
                                 automates_version_number="2.0",
                                 bibjson=Bibjson(title="CHIME: COVID-19 Hospital Impact for Epidemics - Online Documentation",
                                                 author=[BibjsonAuthor(name="Jason Lubken"),
                                                         BibjsonAuthor(name="Marieke Jackson"),
                                                         BibjsonAuthor(name="Michael Chow")],
                                                 type="web_documentation",
                                                 website=BibjsonLinkObject(type="url",
                                                                           location="https://code-for-philly.gitbook.io/chime/"),
                                                 timestamp="2021-01-19T21:08",
                                                 link=[BibjsonLinkObject(type="gdrive",
                                                                         location="https://drive.google.com/file/d/122LEBSEMF9x-3r3tWbF6YQ9xeV4I_9Eh/view?usp=sharing")],
                                                 identifier=[BibjsonIdentifier(type="aske_id",
                                                                               id="8467496e-3dfb-4efd-9061-433fef1b92de")]))
    metadatum_textual_document_reference_set = \
        TextualDocumentReferenceSet(uid=UidMetadatum("chime_textual_document_ref_set"),
                                    provenance=Provenance(method=MetadatumMethod('Manual_claytonm@az'),
                                                          timestamp=get_current_datetime()),
                                    documents=[chime_webdocs_as_pdf])

    # ----- Model component definitions -----

    variables_sir = [

        # CTM 2021-08-19: Hardcoding this as this was not included;
        # only used in bookkeeping (which is not included here)
        Variable(uid=UidVariable("V:i_day"),
                 name="i_day", type=UidType("Float"),
                 proxy_state=UidJunction("J:main.i_day"),
                 states=[UidJunction("J:main.i_day")],
                 metadata=None),

        # TODO: Remaining Variables will be defined in post-processing
    ]

    wires_main = [

        ### -- CHIME_SVIIvR -- START

        Wire(uid=UidWire("W:main_call_simsir.out.v>main.out.V"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.v"),
             tgt=UidPort("P:main.out.V")),
        Wire(uid=UidWire("W:main_call_simsir.out.i_v>main.out.Iv"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.i_v"),
             tgt=UidPort("P:main.out.Iv")),

        Wire(uid=UidWire("W:main_call_simsir.out.i_v>main_ever_infected_exp.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.i_v"),
             tgt=UidPort("P:main_ever_infected_exp.in.i_v")),

        Wire(uid=UidWire("W:main.v_n>main_call_simsir.in.v_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.v_n"),
             tgt=UidPort("PC:main_call_simsir.in.v_n")),
        Wire(uid=UidWire("W:main.i_v_n>main_call_simsir.in.i_v_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.i_v_n"),
             tgt=UidPort("PC:main_call_simsir.in.i_v_n")),
        Wire(uid=UidWire("W:main.vaccination_rate>main_call_simsir.in.vaccination_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.vaccination_rate"),
             tgt=UidPort("PC:main_call_simsir.in.vaccination_rate")),
        Wire(uid=UidWire("W:main.vaccine_efficacy>main_call_simsir.in.vaccine_efficacy"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.vaccine_efficacy"),
             tgt=UidPort("PC:main_call_simsir.in.vaccine_efficacy")),
        Wire(uid=UidWire("W:main_gamma_unvaccinated_exp.out.gamma_unvaccinated>main_call_simsir.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_gamma_unvaccinated_exp.out.gamma_unvaccinated"),
             tgt=UidPort("PC:main_call_simsir.in.gamma_unvaccinated")),
        Wire(uid=UidWire("W:main_gamma_vaccinated_exp.out.gamma_vaccinated>main_call_simsir.in.gamma_vaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_gamma_vaccinated_exp.out.gamma_vaccinated"),
             tgt=UidPort("PC:main_call_simsir.in.gamma_vaccinated")),

        Wire(uid=UidWire("W:main.infections_days_unvaccinated>main_gamma_unvaccinated_exp.in.infections_days_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.infections_days_unvaccinated"),
             tgt=UidPort("P:main_gamma_unvaccinated_exp.in.infections_days_unvaccinated")),
        Wire(uid=UidWire("W:main_gamma_unvaccinated_exp.out.gamma_unvaccinated>main_loop_1.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_gamma_unvaccinated_exp.out.gamma_unvaccinated"),
             tgt=UidPort("P:main_loop_1.in.gamma_unvaccinated")),
        Wire(uid=UidWire("W:main.infections_days_vaccinated>main_gamma_vaccinated_exp.in.infections_days_vaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.infections_days_vaccinated"),
             tgt=UidPort("P:main_gamma_vaccinated_exp.in.infections_days_vaccinated")),

        ### -- CHIME_SVIIvR -- END

        # main <body>

        Wire(uid=UidWire("W:main_call_simsir.out.s_n>main.out.S"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.s_n"),
             tgt=UidPort("P:main.out.S")),
        Wire(uid=UidWire("W:main_call_simsir.out.i_n>main.out.I"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.i_n"),
             tgt=UidPort("P:main.out.I")),
        Wire(uid=UidWire("W:main_call_simsir.out.r_n>main.out.R"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.r_n"),
             tgt=UidPort("P:main.out.R")),

        Wire(uid=UidWire("W:main_call_simsir.out.i_n>main_ever_infected_exp.in.i"),  # UidWire("W:simsir.out.i>main_ever_infected_exp.in.i"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.i_n"),  # UidPort("P:simsir.out.i"),
             tgt=UidPort("P:main_ever_infected_exp.in.i")),
        Wire(uid=UidWire("W:main_call_simsir.out.r_n>main_ever_infected_exp.in.r"),  # UidWire("W:simsir.out.r>main_ever_infected_exp.in.r"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_call_simsir.out.r_n"),  # UidPort("P:simsir.out.r"),
             tgt=UidPort("P:main_ever_infected_exp.in.r")),

        Wire(uid=UidWire("W:main_ever_infected_exp.out.E>main.out.E"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_ever_infected_exp.out.E"),
             tgt=UidPort("P:main.out.E")),

        Wire(uid=UidWire("W:main.s_n>main_call_simsir.in.s_n"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.s_n"),
             tgt=UidPort("PC:main_call_simsir.in.s_n")),
        Wire(uid=UidWire("W:main.s_n>main_loop_1.in.s_n"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.s_n"),
             tgt=UidPort("P:main_loop_1.in.s_n")),
        Wire(uid=UidWire("W:main.i_n>main_call_simsir.in.i_n"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.i_n"),
             tgt=UidPort("PC:main_call_simsir.in.i_n")),
        Wire(uid=UidWire("W:main.r_n>main_call_simsir.in.r_n"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.r_n"),
             tgt=UidPort("PC:main_call_simsir.in.r_n")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:main.infections_days>main_gamma_exp.in.infections_days"),
        #      type=None,
        #      value_type=UidType("Integer"),
        #      name=None, value=None, metadata=None,
        #      src=UidJunction("J:main.infections_days"),
        #      tgt=UidPort("P:main_gamma_exp.in.infections_days")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:main_gamma_exp.out.gamma>main_call_simsir.in.gamma"),
        #      type=None,
        #      value_type=UidType("Integer"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:main_gamma_exp.out.gamma"),
        #      tgt=UidPort("PC:main_call_simsir.in.gamma")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:main_gamma_exp.out.gamma>main_loop_1.in.gamma"),
        #      type=None,
        #      value_type=UidType("Integer"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:main_gamma_exp.out.gamma"),
        #      tgt=UidPort("P:main_loop_1.in.gamma")),

        Wire(uid=UidWire("W:main.relative_contact_rate>main_loop_1.in.relative_contact_rate"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.relative_contact_rate"),
             tgt=UidPort("P:main_loop_1.in.relative_contact_rate")),
        Wire(uid=UidWire("W:main_pbetas_seq.out.policys_betas>main_loop_1.in.policys_betas"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_pbetas_seq.out.policys_betas"),
             tgt=UidPort("P:main_loop_1.in.policys_betas")),
        Wire(uid=UidWire("W:main_loop_1.out.policys_betas>main_call_simsir.in.betas"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_loop_1.out.policys_betas"),
             tgt=UidPort("PC:main_call_simsir.in.betas")),
        Wire(uid=UidWire("W:main_pdays_seq.out.policy_days>main_loop_1.in.policy_days"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_pdays_seq.out.policy_days"),
             tgt=UidPort("P:main_loop_1.in.policy_days")),
        Wire(uid=UidWire("W:main.n_days>main_loop_1.in.n_days"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.n_days"),
             tgt=UidPort("P:main_loop_1.in.n_days"),),

        Wire(uid=UidWire("W:main.N_p>main_call_simsir.in.N_p"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("J:main.N_p"),
             tgt=UidPort("PC:main_call_simsir.in.N_p")),
        Wire(uid=UidWire("W:main.N_p>main_pbetas_seq.in.size"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("J:main.N_p"),
             tgt=UidPort("P:main_pbetas_seq.in.size")),
        Wire(uid=UidWire("W:main.N_p>main_pdays_seq.in.size"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("J:main.N_p"),
             tgt=UidPort("P:main_pdays_seq.in.size")),
        Wire(uid=UidWire("W:main.p_idx>main_loop_1.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:main.p_idx"),
             tgt=UidPort("P:main_loop_1.in.p_idx")),
        Wire(uid=UidWire("W:main.N_p>main_loop_1.in.N_p"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("J:main.N_p"),
             tgt=UidPort("P:main_loop_1.in.N_p")),

        Wire(uid=UidWire("W:main_pdays_seq.out.policy_days>main_call_simsir.in.days"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_pdays_seq.out.policy_days"),
             tgt=UidPort("PC:main_call_simsir.in.days")),

    ]

    wires_main_loop_1 = [

        ### -- CHIME_SVIIvR -- START

        Wire(uid=UidWire("W:main_loop_1.in.gamma_unvaccinated>main_loop_1_call_get_beta_exp.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.gamma_unvaccinated"),
             tgt=UidPort("PC:main_loop_1_call_get_beta_exp.in.gamma_unvaccinated")),

        ### -- CHIME_SVIIvR -- END

        Wire(uid=UidWire("W:main_loop_1.in.p_idx>main_loop_1_cond.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.p_idx"),
             tgt=UidPort("P:main_loop_1_cond.in.p_idx")),
        Wire(uid=UidWire("W:main_loop_1.in.N_p>main_loop_1_cond.in.N_p"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.N_p"),
             tgt=UidPort("P:main_loop_1_cond.in.N_p")),
        Wire(uid=UidWire("W:main_loop_1.in.p_idx>main_loop_1_p_idx_exp.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.p_idx"),
             tgt=UidPort("P:main_loop_1_p_idx_exp.in.p_idx")),
        Wire(uid=UidWire("W:main_loop_1_p_idx_exp.out.p_idx>main_loop_1.out.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1_p_idx_exp.out.p_idx"),
             tgt=UidPort("PC:main_loop_1.out.p_idx")),

        Wire(uid=UidWire("W:main_loop_1.in.p_idx>main_loop_1_dtime_exp.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.p_idx"),
             tgt=UidPort("P:main_loop_1_dtime_exp.in.p_idx")),
        Wire(uid=UidWire("W:main_loop_1_dtime_exp.out.doubling_time>main_loop_1_call_growth_rate_exp.in.doubling_time"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1_dtime_exp.out.doubling_time"),
             tgt=UidPort("PC:main_loop_1_call_growth_rate_exp.in.doubling_time")),
        Wire(uid=UidWire("W:main_loop_1_call_growth_rate_exp.out.growth_rate>main_loop_1_call_get_beta_exp.in.growth_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_loop_1_call_growth_rate_exp.out.growth_rate"),
             tgt=UidPort("PC:main_loop_1_call_get_beta_exp.in.growth_rate")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:main_loop_1.in.gamma>main_loop_1_call_get_beta_exp.in.gamma"),
        #      type=None,
        #      value_type=UidType("Float"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:main_loop_1.in.gamma"),
        #      tgt=UidPort("PC:main_loop_1_call_get_beta_exp.in.gamma")),

        Wire(uid=UidWire("W:main_loop_1.in.s_n>main_loop_1_call_get_beta_exp.in.s_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.s_n"),
             tgt=UidPort("PC:main_loop_1_call_get_beta_exp.in.s_n")),
        Wire(uid=UidWire("W:main_loop_1.in.relative_contact_rate>main_loop_1_call_get_beta_exp.in.relative_contact_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.relative_contact_rate"),
             tgt=UidPort("PC:main_loop_1_call_get_beta_exp.in.relative_contact_rate")),

        Wire(uid=UidWire("W:main_loop_1.in.policys_betas>main_loop_1_pbetas_exp.in.policys_betas"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.policys_betas"),
             tgt=UidPort("P:main_loop_1_pbetas_exp.in.policys_betas")),
        Wire(uid=UidWire("W:main_loop_1.in.p_idx>main_loop_1_pbetas_exp.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.p_idx"),
             tgt=UidPort("P:main_loop_1_pbetas_exp.in.p_idx")),
        Wire(uid=UidWire("W:main_loop_1_call_get_beta_exp.out.beta>main_loop_1_pbetas_exp.in.beta"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:main_loop_1_call_get_beta_exp.out.beta"),
             tgt=UidPort("P:main_loop_1_pbetas_exp.in.beta")),
        Wire(uid=UidWire("W:main_loop_1_pbetas_exp.out.policys_betas>main_loop_1.out.policys_betas"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1_pbetas_exp.out.policys_betas"),
             tgt=UidPort("PC:main_loop_1.out.policys_betas")),

        Wire(uid=UidWire("W:main_loop_1.in.policy_days>main_loop_1_pdays_exp.in.policy_days"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.policy_days"),
             tgt=UidPort("P:main_loop_1_pdays_exp.in.policy_days")),
        Wire(uid=UidWire("W:main_loop_1.in.p_idx>main_loop_1_pdays_exp.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.p_idx"),
             tgt=UidPort("P:main_loop_1_pdays_exp.in.p_idx")),
        Wire(uid=UidWire("W:main_loop_1.in.n_days>main_loop_1_pdays_exp.in.n_days"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1.in.n_days"),
             tgt=UidPort("P:main_loop_1_pdays_exp.in.n_days")),
        Wire(uid=UidWire("W:main_loop_1_pdays_exp.out.policy_days>main_loop_1.out.policy_days"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:main_loop_1_pdays_exp.out.policy_days"),
             tgt=UidPort("PC:main_loop_1.out.policy_days")),

        # -- called functions

        # TODO: replace with Conditional
        Wire(uid=UidWire("W:get_growth_rate.in.doubling_time>get_growth_rate.out.growth_rate"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_growth_rate.in.doubling_time"),
             tgt=UidPort("P:get_growth_rate.out.growth_rate")),

        Wire(uid=UidWire("W:get_beta.in.intrinsic_growth_rate>get_beta_updated_growth_rate_expr.in.intrinsic_growth_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta.in.intrinsic_growth_rate"),
             tgt=UidPort("P:get_beta_updated_growth_rate_expr.in.intrinsic_growth_rate")),
        Wire(uid=UidWire("W:get_beta.in.gamma>get_beta_updated_growth_rate_expr.in.gamma"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta.in.gamma"),
             tgt=UidPort("P:get_beta_updated_growth_rate_expr.in.gamma")),
        Wire(uid=UidWire("W:get_beta_updated_growth_rate_expr.out.updated_growth_rate>get_beta_betas_exp.in.updated_growth_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta_updated_growth_rate_expr.out.updated_growth_rate"),
             tgt=UidPort("P:get_beta_betas_exp.in.updated_growth_rate")),
        Wire(uid=UidWire("W:get_beta.in.susceptible>get_beta_betas_exp.in.susceptible"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta.in.susceptible"),
             tgt=UidPort("P:get_beta_betas_exp.in.susceptible")),
        Wire(uid=UidWire("W:get_beta.in.relative_contact_rate>get_beta_inv_contact_rate_exp.in.relative_contact_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta.in.relative_contact_rate"),
             tgt=UidPort("P:get_beta_inv_contact_rate_exp.in.relative_contact_rate")),
        Wire(uid=UidWire("W:get_beta_inv_contact_rate_exp.out.inv_contact_rate>get_beta_betas_exp.in.inv_contact_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta_inv_contact_rate_exp.out.inv_contact_rate"),
             tgt=UidPort("P:get_beta_betas_exp.in.inv_contact_rate")),
        Wire(uid=UidWire("W:get_beta_betas_exp.out.beta>get_beta.out.beta"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:get_beta_betas_exp.out.beta"),
             tgt=UidPort("P:get_beta.out.beta")),
    ]

    wires_simsir = [

        # -- sim_sir() Wires --

        ### -- CHIME_SVIIvR -- START

        Wire(uid=UidWire("W:simsir.in.v>simsir_n_exp.in.v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.v"),
             tgt=UidPort("P:simsir_n_exp.in.v")),
        Wire(uid=UidWire("W:simsir.in.v>simsir_loop_1.in.v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.v"),
             tgt=UidPort("P:simsir_loop_1.in.v")),
        Wire(uid=UidWire("W:simsir.in.i_v>simsir_n_exp.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.i_v"),
             tgt=UidPort("P:simsir_n_exp.in.i_v")),
        Wire(uid=UidWire("W:simsir.in.i_v>simsir_loop_1.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.i_v"),
             tgt=UidPort("P:simsir_loop_1.in.i_v")),
        Wire(uid=UidWire("W:simsir.in.vaccination_rate>simsir_loop_1.in.vaccination_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.vaccination_rate"),
             tgt=UidPort("P:simsir_loop_1.in.vaccination_rate")),
        Wire(uid=UidWire("W:simsir.in.vaccine_efficacy>simsir_loop_1.in.vaccine_efficacy"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.vaccine_efficacy"),
             tgt=UidPort("P:simsir_loop_1.in.vaccine_efficacy")),
        Wire(uid=UidWire("W:simsir.in.gamma_unvaccinated>simsir_loop_1.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.gamma_unvaccinated"),
             tgt=UidPort("P:simsir_loop_1.in.gamma_unvaccinated")),
        Wire(uid=UidWire("W:simsir.in.gamma_vaccinated>simsir_loop_1.in.gamma_vaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.gamma_vaccinated"),
             tgt=UidPort("P:simsir_loop_1.in.gamma_vaccinated")),
        Wire(uid=UidWire("W:simsir_loop_1.out.v>simsir.out.v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1.out.v"),
             tgt=UidPort("P:simsir.out.v")),
        Wire(uid=UidWire("W:simsir_loop_1.out.i_v>simsir.out.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1.out.i_v"),
             tgt=UidPort("P:simsir.out.i_v")),

        ### -- CHIME_SVIIvR -- END

        Wire(uid=UidWire("W:simsir.in.N_p>simsir_loop_1_range_init_exp.in.N_p"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.N_p"),
             tgt=UidPort("P:simsir_loop_1_range_init_exp.in.N_p")),
        Wire(uid=UidWire("W:simsir_loop_1_range_init_exp.out.loop_1_seq>simsir_loop_1_get_p_idx_init_exp.in.loop_1_seq"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_range_init_exp.out.loop_1_seq"),
             tgt=UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_range_init_exp.out.loop_1_seq>simsir_loop_1.in.loop_1_seq"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_range_init_exp.out.loop_1_seq"),
             tgt=UidPort("P:simsir_loop_1.in.loop_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_get_p_idx_init_exp.out.p_idx>simsir_loop_1.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_get_p_idx_init_exp.out.p_idx"),
             tgt=UidPort("P:simsir_loop_1.in.p_idx")),
        Wire(uid=UidWire("W:simsir.loop_1_i>simsir_loop_1_get_p_idx_init_exp.in.loop_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:simsir.loop_1_i"),
             tgt=UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_i")),
        Wire(uid=UidWire("W:simsir.loop_1_i>simsir_loop_1.in.loop_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction("J:simsir.loop_1_i"),
             tgt=UidPort("P:simsir_loop_1.in.loop_1_i")),
        Wire(uid=UidWire("W:simsir.in.days>simsir_loop_1.in.days"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.days"),
             tgt=UidPort("P:simsir_loop_1.in.days")),
        Wire(uid=UidWire("W:simsir.in.betas>simsir_loop_1.in.betas"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.betas"),
             tgt=UidPort("P:simsir_loop_1.in.betas")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:simsir.in.gamma>simsir_loop_1.in.gamma"),
        #      type=None,
        #      value_type=UidType("Float"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:simsir.in.gamma"),
        #      tgt=UidPort("P:simsir_loop_1.in.gamma")),

        Wire(uid=UidWire("W:simsir.in.s>simsir_loop_1.in.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.s"),
             tgt=UidPort("P:simsir_loop_1.in.s")),
        Wire(uid=UidWire("W:simsir.in.s>simsir_n_exp.in.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.s"),
             tgt=UidPort("P:simsir_n_exp.in.s")),
        Wire(uid=UidWire("W:simsir.in.i>simsir_loop_1.in.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.i"),
             tgt=UidPort("P:simsir_loop_1.in.i")),
        Wire(uid=UidWire("W:simsir.in.i>simsir_n_exp.in.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.i"),
             tgt=UidPort("P:simsir_n_exp.in.i")),
        Wire(uid=UidWire("W:simsir.in.r>simsir_loop_1.in.r"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.r"),
             tgt=UidPort("P:simsir_loop_1.in.r")),
        Wire(uid=UidWire("W:simsir.in.r>simsir_n_exp.in.r"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir.in.r"),
             tgt=UidPort("P:simsir_n_exp.in.r")),
        Wire(uid=UidWire("W:simsir_n_exp.out.n>simsir_loop_1.in.n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_n_exp.out.n"),
             tgt=UidPort("P:simsir_loop_1.in.n")),
        Wire(uid=UidWire("W:simsir_loop_1.out.s>simsir.out.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1.out.s"),
             tgt=UidPort("P:simsir.out.s")),
        Wire(uid=UidWire("W:simsir_loop_1.out.i>simsir.out.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1.out.i"),
             tgt=UidPort("P:simsir.out.i")),
        Wire(uid=UidWire("W:simsir_loop_1.out.r>simsir.out.r"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1.out.r"),
             tgt=UidPort("P:simsir.out.r")),
    ]

    wires_simsir_loop_1 = [

        ### -- CHIME_SVIIvR -- START

        Wire(uid=UidWire("W:simsir_loop_1.in.v>simsir_loop_1_1.in.v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.v"),
             tgt=UidPort("P:simsir_loop_1_1.in.v")),
        Wire(uid=UidWire("W:simsir_loop_1.in.i_v>simsir_loop_1_1.in.i_v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.i_v"),
             tgt=UidPort("P:simsir_loop_1_1.in.i_v")),
        Wire(uid=UidWire("W:simsir_loop_1.in.vaccination_rate>simsir_loop_1_1.in.vaccination_rate"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.vaccination_rate"),
             tgt=UidPort("P:simsir_loop_1_1.in.vaccination_rate")),
        Wire(uid=UidWire("W:simsir_loop_1.in.vaccine_efficacy>simsir_loop_1_1.in.vaccine_efficacy"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.vaccine_efficacy"),
             tgt=UidPort("P:simsir_loop_1_1.in.vaccine_efficacy")),
        Wire(uid=UidWire("W:simsir_loop_1.in.gamma_unvaccinated>simsir_loop_1_1.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.gamma_unvaccinated"),
             tgt=UidPort("P:simsir_loop_1_1.in.gamma_unvaccinated")),
        Wire(uid=UidWire("W:simsir_loop_1.in.gamma_vaccinated>simsir_loop_1_1.in.gamma_vaccinated"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.gamma_vaccinated"),
             tgt=UidPort("P:simsir_loop_1_1.in.gamma_vaccinated")),
        Wire(uid=UidWire("W:simsir_loop_1_1.out.v>simsir_loop_1.out.v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1.out.v"),
             tgt=UidPort("PC:simsir_loop_1.out.v")),
        Wire(uid=UidWire("W:simsir_loop_1_1.out.i_v>simsir_loop_1.out.i_v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1.out.i_v"),
             tgt=UidPort("PC:simsir_loop_1.out.i_v")),

        ### -- CHIME_SVIIvR -- END

        # simsir_loop_1 Wires <loop control>
        Wire(uid=UidWire("W:simsir_loop_1.in.loop_1_i>simsir_loop_1_i_exp.in.loop_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.loop_1_i"),
             tgt=UidPort("P:simsir_loop_1_i_exp.in.loop_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1.in.loop_1_seq>simsir_loop_1_get_p_idx_exp.in.loop_1_seq"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.loop_1_seq"),
             tgt=UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_i_exp.out.loop_1_i>simsir_loop_1_get_p_idx_exp.in.loop_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_i_exp.out.loop_1_i"),
             tgt=UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1_i_exp.out.loop_1_i>simsir_loop_1.out.loop_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_i_exp.out.loop_1_i"),
             tgt=UidPort("PC:simsir_loop_1.out.loop_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1_get_p_idx_exp.out.p_idx>simsir_loop_1.out.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_get_p_idx_exp.out.p_idx"),
             tgt=UidPort("PC:simsir_loop_1.out.p_idx")),

        # Wire simsir_loop_1 <body>

        Wire(uid=UidWire("W:simsir_loop_1.in.days>simsir_loop_1_n_days_exp.in.days"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.days"),
             tgt=UidPort("P:simsir_loop_1_n_days_exp.in.days")),
        Wire(uid=UidWire("W:simsir_loop_1_get_p_idx_exp.out.p_idx>simsir_loop_1_n_days_exp.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_get_p_idx_exp.out.p_idx"),
             tgt=UidPort("P:simsir_loop_1_n_days_exp.in.p_idx")),
        Wire(uid=UidWire("W:simsir_loop_1_n_days_exp.out.n_days>simsir_loop_1_1_range_init_exp.in.n_days"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_n_days_exp.out.n_days"),
             tgt=UidPort("P:simsir_loop_1_1_range_init_exp.in.n_days")),
        Wire(uid=UidWire("W:simsir_loop_1.in.betas>simsir_loop_1_get_beta_exp.in.betas"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.betas"),
             tgt=UidPort("P:simsir_loop_1_get_beta_exp.in.betas")),
        Wire(uid=UidWire("W:simsir_loop_1_get_p_idx_exp.out.p_idx>simsir_loop_1_get_beta_exp.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_get_p_idx_exp.out.p_idx"),
             tgt=UidPort("P:simsir_loop_1_get_beta_exp.in.p_idx")),
        Wire(uid=UidWire("W:simsir_loop_1_get_beta_exp.out.beta>simsir_loop_1_1.in.beta"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_get_beta_exp.out.beta"),
             tgt=UidPort("P:simsir_loop_1_1.in.beta")),

        # Wire simsir_loop_1 <body> passthrough

        Wire(uid=UidWire("W:simsir_loop_1.in.n>simsir_loop_1_1.in.n"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.n"),
             tgt=UidPort("P:simsir_loop_1_1.in.n")),
        Wire(uid=UidWire("W:simsir_loop_1.in.s>simsir_loop_1_1.in.s"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.s"),
             tgt=UidPort("P:simsir_loop_1_1.in.s")),
        Wire(uid=UidWire("W:simsir_loop_1.in.i>simsir_loop_1_1.in.i"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.i"),
             tgt=UidPort("P:simsir_loop_1_1.in.i")),
        Wire(uid=UidWire("W:simsir_loop_1.in.r>simsir_loop_1_1.in.r"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.r"),
             tgt=UidPort("P:simsir_loop_1_1.in.r")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:simsir_loop_1.in.gamma>simsir_loop_1_1.in.gamma"),
        #      type=None,
        #      value_type=UidType("Real"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:simsir_loop_1.in.gamma"),
        #      tgt=UidPort("P:simsir_loop_1_1.in.gamma")),

        Wire(uid=UidWire("W:simsir_loop_1_1.out.s>simsir_loop_1.out.s"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1.out.s"),
             tgt=UidPort("PC:simsir_loop_1.out.s")),
        Wire(uid=UidWire("W:simsir_loop_1_1.out.i>simsir_loop_1.out.i"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1.out.i"),
             tgt=UidPort("PC:simsir_loop_1.out.i")),
        Wire(uid=UidWire("W:simsir_loop_1_1.out.r>simsir_loop_1.out.r"),
             type=None,
             value_type=UidType("Real"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1.out.r"),
             tgt=UidPort("PC:simsir_loop_1.out.r")),

        # loop_1_1 init Wires <loop control>
        Wire(uid=UidWire("W:simsir_loop_1.in.p_idx>simsir_loop_1_cond.in.p_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.p_idx"),
             tgt=UidPort("P:simsir_loop_1_cond.in.p_idx")),
        Wire(uid=UidWire("W:simsir_loop_1.in.loop_1_seq>simsir_loop_1_cond.in.loop_1_seq"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1.in.loop_1_seq"),
             tgt=UidPort("P:simsir_loop_1_cond.in.loop_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_1_get_d_idx_init_exp.out.d_idx>simsir_loop_1_1.in.d_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.out.d_idx"),
             tgt=UidPort("P:simsir_loop_1_1.in.d_idx")),
        Wire(uid=UidWire("W:simsir_loop_1.loop_1_1_i>simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction('J:simsir_loop_1.loop_1_1_i'),
             tgt=UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1.loop_1_1_i>simsir_loop_1_1.in.loop_1_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidJunction('J:simsir_loop_1.loop_1_1_i'),
             tgt=UidPort("P:simsir_loop_1_1.in.loop_1_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq>simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_seq"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq"),
             tgt=UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq>simsir_loop_1_1.in.loop_1_1_seq"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq"),
             tgt=UidPort("P:simsir_loop_1_1.in.loop_1_1_seq")),
    ]

    wires_simsir_loop_1_1 = [

        ### -- CHIME_SVIIvR -- START

        Wire(uid=UidWire("W:P:simsir_loop_1_1.in.v>simsir_loop_1_1_call_sir_exp.in.v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.v"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.v")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.i_v>simsir_loop_1_1_call_sir_exp.in.i_v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.i_v"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.i_v")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.vaccination_rate>simsir_loop_1_1_call_sir_exp.in.vaccination_rate"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.vaccination_rate"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.vaccination_rate")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.vaccine_efficacy>simsir_loop_1_1_call_sir_exp.in.vaccine_efficacy"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.vaccine_efficacy"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.vaccine_efficacy")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.gamma_unvaccinated>simsir_loop_1_1_call_sir_exp.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.gamma_unvaccinated"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma_unvaccinated")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.gamma_vaccinated>simsir_loop_1_1_call_sir_exp.in.gamma_vaccinated"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.gamma_vaccinated"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma_vaccinated")),
        Wire(uid=UidWire("W:simsir_loop_1_1_call_sir_exp.out.v>simsir_loop_1_1.out.v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.v"),
             tgt=UidPort("PC:simsir_loop_1_1.out.v")),
        Wire(uid=UidWire("W:simsir_loop_1_1_call_sir_exp.out.i_v>simsir_loop_1_1.out.i_v"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.i_v"),
             tgt=UidPort("PC:simsir_loop_1_1.out.i_v")),

        ### -- CHIME_SVIIvR -- END

        # loop_1_1 Wires <loop control>
        Wire(uid=UidWire("W:simsir_loop_1_1.in.d_idx>simsir_loop_1_1_cond.in.d_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.d_idx"),
             tgt=UidPort("P:simsir_loop_1_1_cond.in.d_idx")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.loop_1_1_seq>simsir_loop_1_1_cond.in.loop_1_1_seq"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.loop_1_1_seq"),
             tgt=UidPort("P:simsir_loop_1_1_cond.in.loop_1_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.loop_1_1_i>simsir_loop_1_1_i_exp.in.loop_1_1_i"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.loop_1_1_i"),
             tgt=UidPort("P:simsir_loop_1_1_i_exp.in.loop_1_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.loop_1_1_seq>simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_seq"),
             type=None,
             value_type=UidType("Sequence"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.loop_1_1_seq"),
             tgt=UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_seq")),
        Wire(uid=UidWire("W:simsir_loop_1_1_i_exp.out.loop_1_1_i>simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1_i_exp.out.loop_1_1_i"),
             tgt=UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1_1_i_exp.out.loop_1_1_i>simsir_loop_1_1.out.loop_1_1_i"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1_i_exp.out.loop_1_1_i"),
             tgt=UidPort("PC:simsir_loop_1_1.out.loop_1_1_i")),
        Wire(uid=UidWire("W:simsir_loop_1_1_get_d_idx_exp.out.d_idx>simsir_loop_1_1.out.d_idx"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1_get_d_idx_exp.out.d_idx"),
             tgt=UidPort("PC:simsir_loop_1_1.out.d_idx")),

        # loop_1_1 Wires <body>
        Wire(uid=UidWire("W:simsir_loop_1_1.in.s>simsir_loop_1_1_call_sir_exp.in.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.s"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.s")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.i>simsir_loop_1_1_call_sir_exp.in.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.i"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.i")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.r>simsir_loop_1_1_call_sir_exp.in.r"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.r"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.r")),

        # REMOVE_CHIME_SIR_Base
        # Wire(uid=UidWire("W:simsir_loop_1_1.in.gamma>simsir_loop_1_1_call_sir_exp.in.gamma"),
        #      type=None,
        #      value_type=UidType("Float"),
        #      name=None, value=None, metadata=None,
        #      src=UidPort("P:simsir_loop_1_1.in.gamma"),
        #      tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma")),

        Wire(uid=UidWire("W:simsir_loop_1_1.in.beta>simsir_loop_1_1_call_sir_exp.in.beta"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.beta"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.beta")),
        Wire(uid=UidWire("W:simsir_loop_1_1.in.n>simsir_loop_1_1_call_sir_exp.in.n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:simsir_loop_1_1.in.n"),
             tgt=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.n")),

        Wire(uid=UidWire("W:simsir_loop_1_1_call_sir_exp.out.s>simsir_loop_1_1.out.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.s"),
             tgt=UidPort("PC:simsir_loop_1_1.out.s")),
        Wire(uid=UidWire("W:simsir_loop_1_1_call_sir_exp.out.i>simsir_loop_1_1.out.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.i"),
             tgt=UidPort("PC:simsir_loop_1_1.out.i")),
        Wire(uid=UidWire("W:simsir_loop_1_1_call_sir_exp.out.r>simsir_loop_1_1.out.r"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.r"),
             tgt=UidPort("PC:simsir_loop_1_1.out.r")),
    ]

    wires_sir = [

        # -- sir() Wires --

        ### -- CHIME_SVIIvR -- START

        Wire(uid=UidWire("W:sir.in.i_v>sir_s_n_exp.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.i_v"),
             tgt=UidPort("P:sir_s_n_exp.in.i_v")),
        Wire(uid=UidWire("W:sir.in.vaccination_rate>sir_s_n_exp.in.vaccination_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.vaccination_rate"),
             tgt=UidPort("P:sir_s_n_exp.in.vaccination_rate")),
        Wire(uid=UidWire("W:sir.in.vaccination_rate>sir_v_n_exp.in.vaccination_rate"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.vaccination_rate"),
             tgt=UidPort("P:sir_v_n_exp.in.vaccination_rate")),
        Wire(uid=UidWire("W:sir.s_in>sir_v_n_exp.in.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.s_in"),
             tgt=UidPort("P:sir_v_n_exp.in.s")),
        Wire(uid=UidWire("W:sir.in.vaccination_efficacy>sir_v_n_exp.in.vaccination_efficacy"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.vaccination_efficacy"),
             tgt=UidPort("P:sir_v_n_exp.in.vaccination_efficacy")),
        Wire(uid=UidWire("W:sir.beta>sir_v_n_exp.in.beta"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.beta"),
             tgt=UidPort("P:sir_v_n_exp.in.beta")),
        Wire(uid=UidWire("W:sir.in.v>sir_v_n_exp.in.v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.v"),
             tgt=UidPort("P:sir_v_n_exp.in.v")),
        Wire(uid=UidWire("W:sir.i_in>sir_v_n_exp.in.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.i_in"),
             tgt=UidPort("P:sir_v_n_exp.in.i")),
        Wire(uid=UidWire("W:sir.in.i_v>sir_v_n_exp.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.i_v"),
             tgt=UidPort("P:sir_v_n_exp.in.i_v")),
        Wire(uid=UidWire("W:sir_v_n_exp.out.v_n>sir_scale_exp.v_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_v_n_exp.out.v_n"),
             tgt=UidPort("P:sir_scale_exp.v_n")),
        Wire(uid=UidWire("W:sir_v_n_exp.out.v_n>sir_v_exp.in.v_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_v_n_exp.out.v_n"),
             tgt=UidPort("P:sir_v_exp.in.v_n")),

        Wire(uid=UidWire("W:sir.in.i_v>sir_i_n_exp.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.i_v"),
             tgt=UidPort("P:sir_i_n_exp.i_v")),
        Wire(uid=UidWire("W:sir.in.gamma_unvaccinated>sir_i_n_exp.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.gamma_unvaccinated"),
             tgt=UidPort("P:sir_i_n_exp.gamma_unvaccinated")),

        Wire(uid=UidWire("W:sir.in.vaccination_efficacy>sir_i_v_n_exp.in.vaccine_efficacy"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.vaccination_efficacy"),
             tgt=UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy")),
        Wire(uid=UidWire("W:sir.beta>sir_i_v_n_exp.in.beta"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.beta"),
             tgt=UidPort("P:sir_i_v_n_exp.in.beta")),
        Wire(uid=UidWire("W:sir.in.v>sir_i_v_n_exp.in.v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.v"),
             tgt=UidPort("P:sir_i_v_n_exp.in.v")),
        Wire(uid=UidWire("W:sir.i_in>sir_i_v_n_exp.in.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.i_in"),
             tgt=UidPort("P:sir_i_v_n_exp.in.i")),
        Wire(uid=UidWire("W:sir.in.i_v>sir_i_v_n_exp.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.i_v"),
             tgt=UidPort("P:sir_i_v_n_exp.in.i_v")),
        Wire(uid=UidWire("W:sir.in.gamma_vaccinated>sir_i_v_n_exp.in.gamma_vaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.gamma_vaccinated"),
             tgt=UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated")),
        Wire(uid=UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_scale_exp.i_v_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_i_v_n_exp.out.i_v_n"),
             tgt=UidPort("P:sir_scale_exp.i_v_n")),
        Wire(uid=UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_i_v_exp.in.i_v_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_i_v_n_exp.out.i_v_n"),
             tgt=UidPort("P:sir_i_v_exp.in.i_v_n")),

        Wire(uid=UidWire("W:sir_scale_exp.scale>sir_v_exp.in.scale"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_scale_exp.scale"),
             tgt=UidPort("P:sir_v_exp.in.scale")),
        Wire(uid=UidWire("W:sir_v_exp.out.v>sir.out.v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_v_exp.out.v"),
             tgt=UidPort("P:sir.out.v")),

        Wire(uid=UidWire("W:sir.in.gamma_vaccinated>sir_r_n_exp.in.gamma_vaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.gamma_vaccinated"),
             tgt=UidPort("P:sir_r_n_exp.in.gamma_vaccinated")),
        Wire(uid=UidWire("W:sir.in.i_v>sir_r_n_exp.in.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.i_v"),
             tgt=UidPort("P:sir_r_n_exp.in.i_v")),
        Wire(uid=UidWire("W:sir.in.gamma_unvaccinated>sir_r_n_exp.in.gamma_unvaccinated"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.in.gamma_unvaccinated"),
             tgt=UidPort("P:sir_r_n_exp.in.gamma_unvaccinated")),

        Wire(uid=UidWire("W:sir_scale_exp.scale>sir_i_v_exp.in.scale"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_scale_exp.scale"),
             tgt=UidPort("P:sir_i_v_exp.in.scale")),
        Wire(uid=UidWire("W:sir_i_v_exp.out.i_v>sir.out.i_v"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_i_v_exp.out.i_v"),
             tgt=UidPort("P:sir.out.i_v")),

        ### -- CHIME_SVIIvR -- END

        # sir
        Wire(uid=UidWire("W:sir.n>sir_scale_exp.n"),
             type=None,
             value_type=UidType("Integer"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.n"),
             tgt=UidPort("P:sir_scale_exp.n")),
        Wire(uid=UidWire("W:sir.beta>sir_s_n_exp.beta"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.beta"),
             tgt=UidPort("P:sir_s_n_exp.beta")),
        Wire(uid=UidWire("W:sir.beta>sir_i_n_exp.beta"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.beta"),
             tgt=UidPort("P:sir_i_n_exp.beta")),

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

        Wire(uid=UidWire("W:sir.s_in>sir_s_n_exp.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.s_in"),
             tgt=UidPort("P:sir_s_n_exp.s")),
        Wire(uid=UidWire("W:sir.s_in>sir_i_n_exp.s"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.s_in"),
             tgt=UidPort("P:sir_i_n_exp.s")),
        Wire(uid=UidWire("W:sir.i_in>sir_s_n_exp.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.i_in"),
             tgt=UidPort("P:sir_s_n_exp.i")),
        Wire(uid=UidWire("W:sir.i_in>sir_i_n_exp.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.i_in"),
             tgt=UidPort("P:sir_i_n_exp.i")),
        Wire(uid=UidWire("W:sir.i_in>sir_r_n_exp.i"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.i_in"),
             tgt=UidPort("P:sir_r_n_exp.i")),
        Wire(uid=UidWire("W:sir.r_in>sir_r_n_exp.r"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir.r_in"),
             tgt=UidPort("P:sir_r_n_exp.r")),
        Wire(uid=UidWire("W:sir_s_n_exp.s_n>sir_scale_exp.s_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_s_n_exp.s_n"),
             tgt=UidPort("P:sir_scale_exp.s_n")),
        Wire(uid=UidWire("W:sir_s_n_exp.s_n>sir_s_exp.s_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_s_n_exp.s_n"),
             tgt=UidPort("P:sir_s_exp.s_n")),
        Wire(uid=UidWire("W:sir_i_n_exp.i_n>sir_scale_exp.i_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_i_n_exp.i_n"),
             tgt=UidPort("P:sir_scale_exp.i_n")),
        Wire(uid=UidWire("W:sir_i_n_exp.i_n>sir_i_exp.i_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_i_n_exp.i_n"),
             tgt=UidPort("P:sir_i_exp.i_n")),
        Wire(uid=UidWire("W:sir_r_n_exp.r_n>sir_scale_exp.r_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_r_n_exp.r_n"),
             tgt=UidPort("P:sir_scale_exp.r_n")),
        Wire(uid=UidWire("W:sir_r_n_exp.r_n>sir_r_exp.r_n"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_r_n_exp.r_n"),
             tgt=UidPort("P:sir_r_exp.r_n")),

        Wire(uid=UidWire("W:sir_scale_exp.scale>sir_s_exp.scale"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_scale_exp.scale"),
             tgt=UidPort("P:sir_s_exp.scale")),
        Wire(uid=UidWire("W:sir_scale_exp.scale>sir_i_exp.scale"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_scale_exp.scale"),
             tgt=UidPort("P:sir_i_exp.scale")),
        Wire(uid=UidWire("W:sir_scale_exp.scale>sir_r_exp.scale"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_scale_exp.scale"),
             tgt=UidPort("P:sir_r_exp.scale")),

        Wire(uid=UidWire("W:sir_s_exp.s>sir.s_out"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_s_exp.s"),
             tgt=UidPort("P:sir.s_out")),

        Wire(uid=UidWire("W:sir_i_exp.i>sir.i_out"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_i_exp.i"),
             tgt=UidPort("P:sir.i_out")),

        Wire(uid=UidWire("W:sir_r_exp.r>sir.r_out"),
             type=None,
             value_type=UidType("Float"),
             name=None, value=None, metadata=None,
             src=UidPort("P:sir_r_exp.r"),
             tgt=UidPort("P:sir.r_out"))
    ]

    ports_main = [

        ### -- CHIME_SVIIvR -- START

        # main out
        Port(uid=UidPort("P:main.out.V"),
             box=UidBox("B:main"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="V",
             value=None, metadata=None),
        Port(uid=UidPort("P:main.out.Iv"),
             box=UidBox("B:main"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="Iv",
             value=None, metadata=None),

        # main_gamma_unvaccinated_exp in
        Port(uid=UidPort("P:main_gamma_unvaccinated_exp.in.infections_days_unvaccinated"),
             box=UidBox("B:main_gamma_unvaccinated_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="infections_days_unvaccinated",
             value=None, metadata=None),
        # main_gamma_unvaccinated_exp out
        Port(uid=UidPort("P:main_gamma_unvaccinated_exp.out.gamma_unvaccinated"),
             box=UidBox("B:main_gamma_unvaccinated_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),

        # main_gamma_vaccinated_exp in
        Port(uid=UidPort("P:main_gamma_vaccinated_exp.in.infections_days_vaccinated"),
             box=UidBox("B:main_gamma_vaccinated_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="infections_days_vaccinated",
             value=None, metadata=None),
        # main_gamma_vaccinated_exp out
        Port(uid=UidPort("P:main_gamma_vaccinated_exp.out.gamma_vaccinated"),
             box=UidBox("B:main_gamma_vaccinated_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),

        # main_call_simsir in
        PortCall(uid=UidPort("PC:main_call_simsir.in.v_n"),
                 call=UidPort("P:simsir.in.v"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="v_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.i_v_n"),
                 call=UidPort("P:simsir.in.i_v"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="i_v_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.vaccination_rate"),
                 call=UidPort("P:simsir.in.vaccination_rate"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="vaccination_rate",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.vaccine_efficacy"),
                 call=UidPort("P:simsir.in.vaccine_efficacy"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="vaccine_efficacy",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.gamma_unvaccinated"),
                 call=UidPort("P:simsir.in.gamma_unvaccinated"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="gamma_unvaccinated",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.gamma_vaccinated"),
                 call=UidPort("P:simsir.in.gamma_vaccinated"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="gamma_vaccinated",
                 value=None,
                 metadata=None),
        # main_call_simsir out
        PortCall(uid=UidPort("PC:main_call_simsir.out.v"),
                 call=UidPort("P:simsir.out.v"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="v",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.out.i_v"),
                 call=UidPort("P:simsir.out.i_v"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i_v",
                 value=None,
                 metadata=None),

        # main_ever_infected_exp in
        Port(uid=UidPort("P:main_ever_infected_exp.in.i_v"),
             box=UidBox("B:main_ever_infected_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),

        ### -- CHIME_SVIIvR -- END

        # main out
        Port(uid=UidPort("P:main.out.S"),
             box=UidBox("B:main"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="S",
             value=None, metadata=None),
        Port(uid=UidPort("P:main.out.I"),
             box=UidBox("B:main"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="I",
             value=None, metadata=None),
        Port(uid=UidPort("P:main.out.R"),
             box=UidBox("B:main"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="R",
             value=None, metadata=None),
        Port(uid=UidPort("P:main.out.E"),
             box=UidBox("B:main"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="E",
             value=None, metadata=None),

        # main_ever_infected_exp in
        Port(uid=UidPort("P:main_ever_infected_exp.in.i"),
             box=UidBox("B:main_ever_infected_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_ever_infected_exp.in.r"),
             box=UidBox("B:main_ever_infected_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
        # main_ever_infected_exp out
        Port(uid=UidPort("P:main_ever_infected_exp.out.E"),
             box=UidBox("B:main_ever_infected_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="E",
             value=None, metadata=None),

        # main_gamma_exp in
        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:main_gamma_exp.in.infections_days"),
        #      box=UidBox("B:main_gamma_exp"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="infections_days",
        #      value=None, metadata=None),
        # main_gamma_exp out
        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:main_gamma_exp.out.gamma"),
        #      box=UidBox("B:main_gamma_exp"),
        #      type=UidType("PortOutput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        # main_pbetas_seq in
        Port(uid=UidPort("P:main_pbetas_seq.in.fill"),
             box=UidBox("B:main_pbetas_seq"),
             type=UidType("PortInput"),
             value_type=UidType("Any"),
             name="fill",
             value=Literal(uid=None,
                           type=UidType('Float'),
                           value=Val('0.0'),
                           name=None, metadata=None),
             metadata=None),
        Port(uid=UidPort("P:main_pbetas_seq.in.size"),
             box=UidBox("B:main_pbetas_seq"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="size",
             value=None, metadata=None),
        # main_pbetas_seq out
        Port(uid=UidPort("P:main_pbetas_seq.out.policys_betas"),
             box=UidBox("B:main_pbetas_seq"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="policys_betas",
             value=None, metadata=None),

        # main_pdays_seq in
        Port(uid=UidPort("P:main_pdays_seq.in.fill"),
             box=UidBox("B:main_pdays_seq"),
             type=UidType("PortInput"),
             value_type=UidType("Any"),
             name="fill",
             value=Literal(uid=None,
                           type=UidType('Integer'),
                           value=Val('0'),
                           name=None, metadata=None),
             metadata=None),
        Port(uid=UidPort("P:main_pdays_seq.in.size"),
             box=UidBox("B:main_pdays_seq"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="size",
             value=None, metadata=None),
        # main_pdays_seq out
        Port(uid=UidPort("P:main_pdays_seq.out.policy_days"),
             box=UidBox("B:main_pdays_seq"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="policy_days",
             value=None, metadata=None),

        # main_call_simsir in
        PortCall(uid=UidPort("PC:main_call_simsir.in.s_n"),
                 call=UidPort("P:simsir.in.s"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="s_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.i_n"),
                 call=UidPort("P:simsir.in.i"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="i_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.r_n"),
                 call=UidPort("P:simsir.in.r"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="r_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.betas"),
                 call=UidPort("P:simsir.in.betas"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Sequence"),
                 name="betas",
                 value=None,
                 metadata=None),

        # REMOVE_CHIME_SIR_Base
        # PortCall(uid=UidPort("PC:main_call_simsir.in.gamma"),
        #          call=UidPort("P:simsir.in.gamma"),
        #          box=UidBox("B:main_call_simsir"),
        #          type=UidType("PortInput"),
        #          value_type=UidType("Float"),
        #          name="gamma",
        #          value=None,
        #          metadata=None),

        PortCall(uid=UidPort("PC:main_call_simsir.in.days"),
                 call=UidPort("P:simsir.in.days"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Sequence"),
                 name="days",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.in.N_p"),
                 call=UidPort("P:simsir.in.N_p"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortInput"),
                 value_type=UidType("Integer"),
                 name="N_p",
                 value=None,
                 metadata=None),
        # main_call_simsir out
        PortCall(uid=UidPort("PC:main_call_simsir.out.s_n"),
                 call=UidPort("P:simsir.out.s"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="s_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.out.i_n"),
                 call=UidPort("P:simsir.out.i"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_call_simsir.out.r_n"),
                 call=UidPort("P:simsir.out.r"),
                 box=UidBox("B:main_call_simsir"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="r_n",
                 value=None,
                 metadata=None),
    ]

    ports_main_loop_1 = [

        ### -- CHIME_SVIIvR -- START
        # main_loop_1 in
        Port(uid=UidPort("P:main_loop_1.in.gamma_unvaccinated"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),
        # main_loop_1 out
        PortCall(uid=UidPort("PC:main_loop_1.out.gamma_unvaccinated"),
                 call=UidPort("P:main_loop_1.in.gamma_unvaccinated"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="gamma_unvaccinated",
                 value=None,
                 metadata=None),

        # main_loop_1_call_get_beta_exp in
        PortCall(uid=UidPort("PC:main_loop_1_call_get_beta_exp.in.gamma_unvaccinated"),
                 call=UidPort("P:get_beta.in.gamma"),
                 box=UidBox("B:main_loop_1_call_get_beta_exp"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="gamma_unvaccinated",
                 value=None,
                 metadata=None),
        ### -- CHIME_SVIIvR -- END

        # main_loop_1 in
        Port(uid=UidPort("P:main_loop_1.in.s_n"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s_n",
             value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:main_loop_1.in.gamma"),
        #      box=UidBox("B:main_loop_1"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        Port(uid=UidPort("P:main_loop_1.in.relative_contact_rate"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="relative_contact_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1.in.policys_betas"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="policys_betas",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1.in.policy_days"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="policy_days",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1.in.n_days"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="n_days",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1.in.p_idx"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1.in.N_p"),
             box=UidBox("B:main_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="N_p",
             value=None, metadata=None),
        # main_loop_1 out
        PortCall(uid=UidPort("PC:main_loop_1.out.s_n"),
                 call=UidPort("P:main_loop_1.in.s_n"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="s_n",
                 value=None,
                 metadata=None),

        # REMOVE_CHIME_SIR_Base
        # PortCall(uid=UidPort("PC:main_loop_1.out.gamma"),
        #          call=UidPort("P:main_loop_1.in.gamma"),
        #          box=UidBox("B:main_loop_1"),
        #          type=UidType("PortOutput"),
        #          value_type=UidType("Integer"),
        #          name="gamma",
        #          value=None,
        #          metadata=None),

        PortCall(uid=UidPort("PC:main_loop_1.out.relative_contact_rate"),
                 call=UidPort("P:main_loop_1.in.relative_contact_rate"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="relative_contact_rate",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_loop_1.out.policys_betas"),
                 call=UidPort("P:main_loop_1.in.policys_betas"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Sequence"),
                 name="policys_betas",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_loop_1.out.policy_days"),
                 call=UidPort("P:main_loop_1.in.policy_days"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Sequence"),
                 name="policy_days",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_loop_1.out.n_days"),
                 call=UidPort("P:main_loop_1.in.n_days"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="n_days",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_loop_1.out.p_idx"),
                 call=UidPort("P:main_loop_1.in.p_idx"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="p_idx",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_loop_1.out.N_p"),
                 call=UidPort("P:main_loop_1.in.N_p"),
                 box=UidBox("B:main_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="N_p",
                 value=None,
                 metadata=None),

        # main_loop_1_cond in
        Port(uid=UidPort("P:main_loop_1_cond.in.p_idx"),
             box=UidBox("B:main_loop_1_cond"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1_cond.in.N_p"),
             box=UidBox("B:main_loop_1_cond"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="N_p",
             value=None, metadata=None),
        # main_loop_1_cond out
        Port(uid=UidPort("P:main_loop_1_cond.out.exit"),
             box=UidBox("B:main_loop_1_cond"),
             type=UidType("PortOutput"),
             value_type=UidType("Boolean"),
             name="Exit",
             value=None, metadata=None),

        # main_loop_1_p_idx_exp in
        Port(uid=UidPort("P:main_loop_1_p_idx_exp.in.p_idx"),
             box=UidBox("B:main_loop_1_p_idx_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="N_p",
             value=None, metadata=None),
        # main_loop_1_p_idx_exp out
        Port(uid=UidPort("P:main_loop_1_p_idx_exp.out.p_idx"),
             box=UidBox("B:main_loop_1_p_idx_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),

        # main_loop_1_dtime_exp in
        Port(uid=UidPort("P:main_loop_1_dtime_exp.in.p_idx"),
             box=UidBox("B:main_loop_1_dtime_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        # main_loop_1_dtime_exp out
        Port(uid=UidPort("P:main_loop_1_dtime_exp.out.doubling_time"),
             box=UidBox("B:main_loop_1_dtime_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="doubling_time",
             value=None, metadata=None),

        # main_loop_1_call_growth_rate_exp in
        PortCall(uid=UidPort("PC:main_loop_1_call_growth_rate_exp.in.doubling_time"),
                 call=UidPort("P:get_growth_rate.in.doubling_time"),
                 box=UidBox("B:main_loop_1_call_growth_rate_exp"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="doubling_time",
                 value=None,
                 metadata=None),
        # main_loop_1_call_growth_rate_exp out
        PortCall(uid=UidPort("PC:main_loop_1_call_growth_rate_exp.out.growth_rate"),
                 call=UidPort("P:get_growth_rate.out.growth_rate"),
                 box=UidBox("B:main_loop_1_call_growth_rate_exp"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="growth_rate",
                 value=None,
                 metadata=None),

        # main_loop_1_call_get_beta_exp in
        PortCall(uid=UidPort("PC:main_loop_1_call_get_beta_exp.in.growth_rate"),
                 call=UidPort("P:get_beta.in.intrinsic_growth_rate"),
                 box=UidBox("B:main_loop_1_call_get_beta_exp"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="growth_rate",
                 value=None,
                 metadata=None),

        # REMOVE_CHIME_SIR_Base
        # PortCall(uid=UidPort("PC:main_loop_1_call_get_beta_exp.in.gamma"),
        #          call=UidPort("P:get_beta.in.gamma"),
        #          box=UidBox("B:main_loop_1_call_get_beta_exp"),
        #          type=UidType("PortInput"),
        #          value_type=UidType("Float"),
        #          name="gamma",
        #          value=None,
        #          metadata=None),

        PortCall(uid=UidPort("PC:main_loop_1_call_get_beta_exp.in.s_n"),
                 call=UidPort("P:get_beta.in.susceptible"),
                 box=UidBox("B:main_loop_1_call_get_beta_exp"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="s_n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:main_loop_1_call_get_beta_exp.in.relative_contact_rate"),
                 call=UidPort("P:get_beta.in.relative_contact_rate"),
                 box=UidBox("B:main_loop_1_call_get_beta_exp"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="relative_contact_rate",
                 value=None,
                 metadata=None),
        # main_loop_1_call_get_beta_exp out
        PortCall(uid=UidPort("PC:main_loop_1_call_get_beta_exp.out.beta"),
                 call=UidPort("P:get_beta.out.beta"),
                 box=UidBox("B:main_loop_1_call_get_beta_exp"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="beta",
                 value=None,
                 metadata=None),

        # main_loop_1_pbetas_exp in
        Port(uid=UidPort("P:main_loop_1_pbetas_exp.in.policys_betas"),
             box=UidBox("B:main_loop_1_pbetas_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="policys_betas",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1_pbetas_exp.in.p_idx"),
             box=UidBox("B:main_loop_1_pbetas_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="p_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1_pbetas_exp.in.beta"),
             box=UidBox("B:main_loop_1_pbetas_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),
        # main_loop_1_pbetas_exp out
        Port(uid=UidPort("P:main_loop_1_pbetas_exp.out.policys_betas"),
             box=UidBox("B:main_loop_1_pbetas_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="policys_betas",
             value=None, metadata=None),

        # main_loop_1_pdays_exp in
        Port(uid=UidPort("P:main_loop_1_pdays_exp.in.policy_days"),
             box=UidBox("B:main_loop_1_pdays_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="policy_days",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1_pdays_exp.in.p_idx"),
             box=UidBox("B:main_loop_1_pdays_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:main_loop_1_pdays_exp.in.n_days"),
             box=UidBox("B:main_loop_1_pdays_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="n_days",
             value=None, metadata=None),
        # main_loop_1_pdays_exp out
        Port(uid=UidPort("P:main_loop_1_pdays_exp.out.policy_days"),
             box=UidBox("B:main_loop_1_pdays_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="policy_days",
             value=None, metadata=None),

        # -- called functions

        # get_growth_rate in
        Port(uid=UidPort("P:get_growth_rate.in.doubling_time"),
             box=UidBox("B:get_growth_rate"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="doubling_time",
             value=None, metadata=None),
        # get_growth_rate out
        Port(uid=UidPort("P:get_growth_rate.out.growth_rate"),
             box=UidBox("B:get_growth_rate"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="growth_rate",
             value=None, metadata=None),

        # get_beta in
        Port(uid=UidPort("P:get_beta.in.intrinsic_growth_rate"),
             box=UidBox("B:get_beta"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="intrinsic_growth_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:get_beta.in.gamma"),
             box=UidBox("B:get_beta"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma",
             value=None, metadata=None),
        Port(uid=UidPort("P:get_beta.in.susceptible"),
             box=UidBox("B:get_beta"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="susceptible",
             value=None, metadata=None),
        Port(uid=UidPort("P:get_beta.in.relative_contact_rate"),
             box=UidBox("B:get_beta"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="relative_contact_rate",
             value=None, metadata=None),
        # get_beta out
        Port(uid=UidPort("P:get_beta.out.beta"),
             box=UidBox("B:get_beta"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),

        # get_beta_updated_growth_rate_expr in
        Port(uid=UidPort("P:get_beta_updated_growth_rate_expr.in.intrinsic_growth_rate"),
             box=UidBox("B:get_beta_updated_growth_rate_expr"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="intrinsic_growth_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:get_beta_updated_growth_rate_expr.in.gamma"),
             box=UidBox("B:get_beta_updated_growth_rate_expr"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma",
             value=None, metadata=None),
        # get_beta_updated_growth_rate_expr out
        Port(uid=UidPort("P:get_beta_updated_growth_rate_expr.out.updated_growth_rate"),
             box=UidBox("B:get_beta_updated_growth_rate_expr"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="updated_growth_rate",
             value=None, metadata=None),

        # get_beta_inv_contact_rate_exp in
        Port(uid=UidPort("P:get_beta_inv_contact_rate_exp.in.relative_contact_rate"),
             box=UidBox("B:get_beta_inv_contact_rate_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="relative_contact_rate",
             value=None, metadata=None),
        # get_beta_inv_contact_rate_exp out
        Port(uid=UidPort("P:get_beta_inv_contact_rate_exp.out.inv_contact_rate"),
             box=UidBox("B:get_beta_inv_contact_rate_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="inv_contact_rate",
             value=None, metadata=None),

        # get_beta_betas_exp in
        Port(uid=UidPort("P:get_beta_betas_exp.in.updated_growth_rate"),
             box=UidBox("B:get_beta_betas_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="updated_growth_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:get_beta_betas_exp.in.susceptible"),
             box=UidBox("B:get_beta_betas_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="susceptible",
             value=None, metadata=None),
        Port(uid=UidPort("P:get_beta_betas_exp.in.inv_contact_rate"),
             box=UidBox("B:get_beta_betas_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="inv_contact_rate",
             value=None, metadata=None),
        # get_beta_betas_exp out
        Port(uid=UidPort("P:get_beta_betas_exp.out.beta"),
             box=UidBox("B:get_beta_betas_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),
    ]

    ports_simsir = [

        # -- sim_sir() Ports --

        ### -- CHIME_SVIIvR -- START

        # simsir in CHIME_SVIIvR
        Port(uid=UidPort("P:simsir.in.v"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.i_v"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.vaccination_rate"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.vaccine_efficacy"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccine_efficacy",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.gamma_unvaccinated"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.gamma_vaccinated"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),
        # simsir out CHIME_SVIIvR
        Port(uid=UidPort("P:simsir.out.v"),
             box=UidBox("B:simsir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.out.i_v"),
             box=UidBox("B:simsir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        # simsir_n_exp in
        Port(uid=UidPort("P:simsir_n_exp.in.v"),
             box=UidBox("B:simsir_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_n_exp.in.i_v"),
             box=UidBox("B:simsir_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),

        ### -- CHIME_SVIIvR -- END

        # simsir in
        Port(uid=UidPort("P:simsir.in.s"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.i"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.r"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:simsir.in.gamma"),
        #      box=UidBox("B:simsir"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        Port(uid=UidPort("P:simsir.in.betas"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="betas",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.days"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="days",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.in.N_p"),
             box=UidBox("B:simsir"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="N_p",
             value=None, metadata=None),
        # simsir out
        Port(uid=UidPort("P:simsir.out.s"),
             box=UidBox("B:simsir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.out.i"),
             box=UidBox("B:simsir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir.out.r"),
             box=UidBox("B:simsir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),

        # simsir_loop_1_range_init_exp in
        Port(uid=UidPort("P:simsir_loop_1_range_init_exp.in.N_p"),
             box=UidBox("B:simsir_loop_1_range_init_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="N_p",
             value=None, metadata=None),
        # simsir_loop_1_range_init_exp out
        Port(uid=UidPort("P:simsir_loop_1_range_init_exp.out.loop_1_seq"),
             box=UidBox("B:simsir_loop_1_range_init_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="loop_1_seq",
             value=None, metadata=None),

        # simsir_loop_1_get_p_idx_init_exp in
        Port(uid=UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_seq"),
             box=UidBox("B:simsir_loop_1_get_p_idx_init_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_seq",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_i"),
             box=UidBox("B:simsir_loop_1_get_p_idx_init_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_i",
             value=None, metadata=None),
        # simsir_loop_1_get_p_idx_init_exp out
        Port(uid=UidPort("P:simsir_loop_1_get_p_idx_init_exp.out.p_idx"),
             box=UidBox("B:simsir_loop_1_get_p_idx_init_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),

        # simsir_n_exp in
        Port(uid=UidPort("P:simsir_n_exp.in.s"),
             box=UidBox("B:simsir_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_n_exp.in.i"),
             box=UidBox("B:simsir_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_n_exp.in.r"),
             box=UidBox("B:simsir_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
        # simsir_n_exp out
        Port(uid=UidPort("P:simsir_n_exp.out.n"),
             box=UidBox("B:simsir_n_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
    ]

    ports_simsir_loop_1 = [

        ### -- CHIME_SVIIvR -- START
        # simsir_loop_1 in CHIME_SVIIvR
        Port(uid=UidPort("P:simsir_loop_1.in.v"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.i_v"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.vaccination_rate"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.vaccine_efficacy"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccine_efficacy",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.gamma_unvaccinated"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.gamma_vaccinated"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),
        # simsir_loop_1 out CHIME_SVIIvR
        PortCall(uid=UidPort("PC:simsir_loop_1.out.v"),
                 call=UidPort("P:simsir_loop_1.in.v"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="v",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.i_v"),
                 call=UidPort("P:simsir_loop_1.in.i_v"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i_v",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.vaccination_rate"),
                 call=UidPort("P:simsir_loop_1.in.vaccination_rate"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="vaccination_rate",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.vaccine_efficacy"),
                 call=UidPort("P:simsir_loop_1.in.vaccine_efficacy"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="vaccine_efficacy",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.gamma_unvaccinated"),
                 call=UidPort("P:simsir_loop_1.in.gamma_unvaccinated"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="gamma_unvaccinated",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.gamma_vaccinated"),
                 call=UidPort("P:simsir_loop_1.in.gamma_vaccinated"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="gamma_vaccinated",
                 value=None,
                 metadata=None),
        ### -- CHIME_SVIIvR -- END

        # simsir_loop_1 in <loop control>
        Port(uid=UidPort("P:simsir_loop_1.in.p_idx"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.loop_1_seq"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_seq",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.loop_1_i"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_i",
             value=None, metadata=None),
        # simsir_loop_1 out <loop control>
        PortCall(uid=UidPort("PC:simsir_loop_1.out.p_idx"),
                 call=UidPort("P:simsir_loop_1.in.p_idx"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="p_idx",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.loop_1_seq"),
                 call=UidPort("P:simsir_loop_1.in.loop_1_seq"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Sequence"),
                 name="loop_1_seq",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.loop_1_i"),
                 call=UidPort("P:simsir_loop_1.in.loop_1_i"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="loop_1_i",
                 value=None,
                 metadata=None),

        # simsir_loop_1 in <body>
        Port(uid=UidPort("P:simsir_loop_1.in.days"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="days",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.betas"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="betas",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.n"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="n",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.s"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.i"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1.in.r"),
             box=UidBox("B:simsir_loop_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:simsir_loop_1.in.gamma"),
        #      box=UidBox("B:simsir_loop_1"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        # simsir_loop_1 out <body>
        PortCall(uid=UidPort("PC:simsir_loop_1.out.days"),
                 call=UidPort("P:simsir_loop_1.in.days"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Sequence"),
                 name="days",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.betas"),
                 call=UidPort("P:simsir_loop_1.in.betas"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Sequence"),
                 name="betas",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.n"),
                 call=UidPort("P:simsir_loop_1.in.n"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="n",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.s"),
                 call=UidPort("P:simsir_loop_1.in.s"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="s",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.i"),
                 call=UidPort("P:simsir_loop_1.in.i"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1.out.r"),
                 call=UidPort("P:simsir_loop_1.in.r"),
                 box=UidBox("B:simsir_loop_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="r",
                 value=None,
                 metadata=None),

        # REMOVE_CHIME_SIR_Base
        # PortCall(uid=UidPort("PC:simsir_loop_1.out.gamma"),
        #          call=UidPort("P:simsir_loop_1.in.gamma"),
        #          box=UidBox("B:simsir_loop_1"),
        #          type=UidType("PortOutput"),
        #          value_type=UidType("Float"),
        #          name="gamma",
        #          value=None,
        #          metadata=None),

        # simsir_loop_1_i_exp in
        Port(uid=UidPort("P:simsir_loop_1_i_exp.in.loop_1_i"),
             box=UidBox("B:simsir_loop_1_i_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_i",
             value=None, metadata=None),
        # simsir_loop_1_i_exp out
        Port(uid=UidPort("P:simsir_loop_1_i_exp.out.loop_1_i"),
             box=UidBox("B:simsir_loop_1_i_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="loop_1_i",
             value=None, metadata=None),

        # simsir_loop_1_i_exp in
        Port(uid=UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_seq"),
             box=UidBox("B:simsir_loop_1_get_p_idx_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_seq",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_i"),
             box=UidBox("B:simsir_loop_1_get_p_idx_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_i",
             value=None, metadata=None),
        # simsir_loop_1_i_exp out
        Port(uid=UidPort("P:simsir_loop_1_get_p_idx_exp.out.p_idx"),
             box=UidBox("B:simsir_loop_1_get_p_idx_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),

        # simsir_loop_1_cond in
        Port(uid=UidPort("P:simsir_loop_1_cond.in.p_idx"),
             box=UidBox("B:simsir_loop_1_cond"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_cond.in.loop_1_seq"),
             box=UidBox("B:simsir_loop_1_cond"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_seq",
             value=None, metadata=None),
        # simsir_loop_1_cond out
        Port(uid=UidPort("P:simsir_loop_1_cond.out.exit"),
             box=UidBox("B:simsir_loop_1_cond"),
             type=UidType("PortOutput"),
             value_type=UidType("Boolean"),
             name="exit",
             value=None, metadata=None),

        # -- loop_1 body components

        # simsir_loop_1_n_days_exp in
        Port(uid=UidPort("P:simsir_loop_1_n_days_exp.in.days"),
             box=UidBox("B:simsir_loop_1_n_days_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="days",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_n_days_exp.in.p_idx"),
             box=UidBox("B:simsir_loop_1_n_days_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        # simsir_loop_1_n_days_exp out
        Port(uid=UidPort("P:simsir_loop_1_n_days_exp.out.n_days"),
             box=UidBox("B:simsir_loop_1_n_days_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="n_days",
             value=None, metadata=None),

        # simsir_loop_1_get_beta_exp in
        Port(uid=UidPort("P:simsir_loop_1_get_beta_exp.in.betas"),
             box=UidBox("B:simsir_loop_1_get_beta_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="betas",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_get_beta_exp.in.p_idx"),
             box=UidBox("B:simsir_loop_1_get_beta_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="p_idx",
             value=None, metadata=None),
        # simsir_loop_1_get_beta_exp out
        Port(uid=UidPort("P:simsir_loop_1_get_beta_exp.out.beta"),
             box=UidBox("B:simsir_loop_1_get_beta_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),

        # -- in loop_1: loop_1_1 for-loop sequence iteration initialization

        # simsir_loop_1_1_range_init_exp in
        Port(uid=UidPort("P:simsir_loop_1_1_range_init_exp.in.n_days"),
             box=UidBox("B:simsir_loop_1_1_range_init_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="n_days",
             value=None, metadata=None),
        # simsir_loop_1_1_range_init_exp out
        Port(uid=UidPort("P:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq"),
             box=UidBox("B:simsir_loop_1_1_range_init_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Sequence"),
             name="loop_1_1_seq",
             value=None, metadata=None),

        # simsir_loop_1_1_get_d_idx_init_exp in
        Port(uid=UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_seq"),
             box=UidBox("B:simsir_loop_1_1_get_d_idx_init_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_1_seq",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_i"),
             box=UidBox("B:simsir_loop_1_1_get_d_idx_init_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_1_i",
             value=None, metadata=None),
        # simsir_loop_1_1_get_d_idx_init_exp out
        Port(uid=UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.out.d_idx"),
             box=UidBox("B:simsir_loop_1_1_get_d_idx_init_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="d_idx",
             value=None, metadata=None),
    ]

    ports_simsir_loop_1_1 = [

        ### -- CHIME_SVIIvR -- START

        # simsir_loop_1_1 in CHIME_SVIIvR
        Port(uid=UidPort("P:simsir_loop_1_1.in.v"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.i_v"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.vaccination_rate"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.vaccine_efficacy"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccine_efficacy",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.gamma_unvaccinated"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.gamma_vaccinated"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),
        # simsir_loop_1_1 out CHIME_SVIIvR
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.v"),
                 box=UidBox("B:simsir_loop_1_1"),
                 call=UidPort("P:simsir_loop_1_1.in.v"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="v",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.i_v"),
                 box=UidBox("B:simsir_loop_1_1"),
                 call=UidPort("P:simsir_loop_1_1.in.i_v"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i_v",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.vaccination_rate"),
                 box=UidBox("B:simsir_loop_1_1"),
                 call=UidPort("P:simsir_loop_1_1.in.vaccination_rate"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="vaccination_rate",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.vaccine_efficacy"),
                 box=UidBox("B:simsir_loop_1_1"),
                 call=UidPort("P:simsir_loop_1_1.in.vaccine_efficacy"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="vaccine_efficacy",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.gamma_unvaccinated"),
                 box=UidBox("B:simsir_loop_1_1"),
                 call=UidPort("P:simsir_loop_1_1.in.gamma_unvaccinated"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="gamma_unvaccinated",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.gamma_vaccinated"),
                 box=UidBox("B:simsir_loop_1_1"),
                 call=UidPort("P:simsir_loop_1_1.in.gamma_vaccinated"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="gamma_vaccinated",
                 value=None, metadata=None),

        # simsir_loop_1_1_call_sir_exp in CHIME_SVIIvR
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.v"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.in.v"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="v",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.i_v"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.in.i_v"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="i_v",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.vaccination_rate"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.in.vaccination_rate"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="vaccination_rate",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.vaccine_efficacy"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.in.vaccination_efficacy"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="vaccine_efficacy",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma_unvaccinated"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.in.gamma_unvaccinated"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="gamma_unvaccinated",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma_vaccinated"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.in.gamma_vaccinated"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="gamma_vaccinated",
                 value=None, metadata=None),
        # simsir_loop_1_1_call_sir_exp out CHIME_SVIIvR
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.v"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.out.v"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="v",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.i_v"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.out.i_v"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i_v",
                 value=None, metadata=None),

        ### -- CHIME_SVIIvR -- END

        # simsir_loop_1_1 in <loop control>
        Port(uid=UidPort("P:simsir_loop_1_1.in.d_idx"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="d_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.loop_1_1_seq"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_1_seq",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.loop_1_1_i"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_1_i",
             value=None, metadata=None),
        # simsir_loop_1_1 out <loop control>
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.d_idx"),
                 call=UidPort("P:simsir_loop_1_1.in.d_idx"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="d_idx",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.loop_1_1_seq"),
                 call=UidPort("P:simsir_loop_1_1.in.loop_1_1_seq"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Sequence"),
                 name="loop_1_1_seq",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.loop_1_1_i"),
                 call=UidPort("P:simsir_loop_1_1.in.loop_1_1_i"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="loop_1_1_i",
                 value=None,
                 metadata=None),

        # simsir_loop_1_1 in <body>
        Port(uid=UidPort("P:simsir_loop_1_1.in.s"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.i"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.r"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.n"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="n",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1.in.beta"),
             box=UidBox("B:simsir_loop_1_1"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:simsir_loop_1_1.in.gamma"),
        #      box=UidBox("B:simsir_loop_1_1"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        # simsir_loop_1_1 out <body>
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.s"),
                 call=UidPort("P:simsir_loop_1_1.in.s"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="s",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.i"),
                 call=UidPort("P:simsir_loop_1_1.in.i"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="i",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.r"),
                 call=UidPort("P:simsir_loop_1_1.in.r"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="r",
                 value=None,
                 metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.n"),
                 call=UidPort("P:simsir_loop_1_1.in.n"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="n",
                 value=None,
                 metadata=None),

        # REMOVE_CHIME_SIR_Base
        # PortCall(uid=UidPort("PC:simsir_loop_1_1.out.gamma"),
        #          call=UidPort("P:simsir_loop_1_1.in.gamma"),
        #          box=UidBox("B:simsir_loop_1_1"),
        #          type=UidType("PortOutput"),
        #          value_type=UidType("Integer"),
        #          name="gamma",
        #          value=None,
        #          metadata=None),

        PortCall(uid=UidPort("PC:simsir_loop_1_1.out.beta"),
                 call=UidPort("P:simsir_loop_1_1.in.beta"),
                 box=UidBox("B:simsir_loop_1_1"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Integer"),
                 name="beta",
                 value=None,
                 metadata=None),

        # simsir_loop_1_1_cond in
        Port(uid=UidPort("P:simsir_loop_1_1_cond.in.d_idx"),
             box=UidBox("B:simsir_loop_1_1_cond"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="d_idx",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1_cond.in.loop_1_1_seq"),
             box=UidBox("B:simsir_loop_1_1_cond"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_1_seq",
             value=None, metadata=None),
        # simsir_loop_1_1_cond out
        Port(uid=UidPort("P:simsir_loop_1_1_cond.out.exit"),
             box=UidBox("B:simsir_loop_1_1_cond"),
             type=UidType("PortOutput"),
             value_type=UidType("Boolean"),
             name="exit",
             value=None, metadata=None),

        # simsir_loop_1_1_i_exp in
        Port(uid=UidPort("P:simsir_loop_1_1_i_exp.in.loop_1_1_i"),
             box=UidBox("B:simsir_loop_1_1_i_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_1_i",
             value=None, metadata=None),
        # simsir_loop_1_1_i_exp out
        Port(uid=UidPort("P:simsir_loop_1_1_i_exp.out.loop_1_1_i"),
             box=UidBox("B:simsir_loop_1_1_i_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="loop_1_1_i",
             value=None, metadata=None),

        # simsir_loop_1_1_get_d_idx_exp in
        Port(uid=UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_seq"),
             box=UidBox("B:simsir_loop_1_1_get_d_idx_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Sequence"),
             name="loop_1_1_seq",
             value=None, metadata=None),
        Port(uid=UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_i"),
             box=UidBox("B:simsir_loop_1_1_get_d_idx_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="loop_1_1_i",
             value=None, metadata=None),
        # simsir_loop_1_1_get_d_idx_exp out
        Port(uid=UidPort("P:simsir_loop_1_1_get_d_idx_exp.out.d_idx"),
             box=UidBox("B:simsir_loop_1_1_get_d_idx_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Integer"),
             name="d_idx",
             value=None, metadata=None),

        # simsir_loop_1_1_call_sir_exp in
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.s"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.s_in"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="s",
                 value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.i"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.i_in"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="i", value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.r"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.r_in"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="r", value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.beta"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.beta"),
                 type=UidType("PortInput"),
                 value_type=UidType("Float"),
                 name="beta", value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma"),
        #          box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
        #          call=UidPort("P:sir.gamma"),
        #          type=UidType("PortInput"),
        #          value_type=UidType("Float"),
        #          name=None, value=None, metadata=None),

        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.in.n"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.n"),
                 type=UidType("PortInput"),
                 value_type=UidType("Integer"),
                 name="n", value=None, metadata=None),
        # simsir_loop_1_1_call_sir_exp out
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.s"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.s_out"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="s", value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.i"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.i_out"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="i", value=None, metadata=None),
        PortCall(uid=UidPort("PC:simsir_loop_1_1_call_sir_exp.out.r"),
                 box=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                 call=UidPort("P:sir.r_out"),
                 type=UidType("PortOutput"),
                 value_type=UidType("Float"),
                 name="r", value=None, metadata=None),
    ]

    ports_sir = [

        # -- sir() Ports --

        ### -- CHIME_SVIIvR -- START

        # sir in CHIME_SVIIvR
        Port(uid=UidPort("P:sir.in.vaccination_rate"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.in.vaccination_efficacy"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_efficacy",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.in.v"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.in.i_v"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.in.gamma_unvaccinated"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.in.gamma_vaccinated"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),
        # sir out CHIME_SVIIvR
        Port(uid=UidPort("P:sir.out.v"),
             box=UidBox("B:sir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.out.i_v"),
             box=UidBox("B:sir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),

        # sir_v_n_exp in
        Port(uid=UidPort("P:sir_v_n_exp.in.vaccination_rate"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_rate",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_n_exp.in.s"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_n_exp.in.vaccination_efficacy"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_efficacy",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_n_exp.in.beta"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_n_exp.in.v"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_n_exp.in.i"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_n_exp.in.i_v"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        # sir_v_n_exp out
        Port(uid=UidPort("P:sir_v_n_exp.out.v_n"),
             box=UidBox("B:sir_v_n_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="v_n",
             value=None, metadata=None),

        # sir_i_v_n_exp in
        Port(uid=UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccine_efficacy",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_v_n_exp.in.beta"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_v_n_exp.in.v"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_v_n_exp.in.i"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_v_n_exp.in.i_v"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),
        # sir_i_v_n_exp out
        Port(uid=UidPort("P:sir_i_v_n_exp.out.i_v_n"),
             box=UidBox("B:sir_i_v_n_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i_v_n",
             value=None, metadata=None),

        # sir_i_v_n_exp in
        Port(uid=UidPort("P:sir_r_n_exp.in.gamma_vaccinated"),
             box=UidBox("B:sir_r_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_vaccinated",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_r_n_exp.in.i_v"),
             box=UidBox("B:sir_r_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_r_n_exp.in.gamma_unvaccinated"),
             box=UidBox("B:sir_r_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),

        # sir_i_n_exp in
        Port(uid=UidPort("P:sir_i_n_exp.i_v"),
             box=UidBox("B:sir_i_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
             box=UidBox("B:sir_i_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="gamma_unvaccinated",
             value=None, metadata=None),

        # sir_s_n_exp in
        Port(uid=UidPort("P:sir_s_n_exp.in.i_v"),
             box=UidBox("B:sir_s_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_s_n_exp.in.vaccination_rate"),
             box=UidBox("B:sir_s_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="vaccination_rate",
             value=None, metadata=None),

        # sir_v_exp in
        Port(uid=UidPort("P:sir_v_exp.in.v_n"),
             box=UidBox("B:sir_v_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_v_exp.in.scale"),
             box=UidBox("B:sir_v_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="scale",
             value=None, metadata=None),
        # sir_v_exp out
        Port(uid=UidPort("P:sir_v_exp.out.v"),
             box=UidBox("B:sir_v_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="v",
             value=None, metadata=None),

        # sir_i_v_exp in
        Port(uid=UidPort("P:sir_i_v_exp.in.i_v_n"),
             box=UidBox("B:sir_i_v_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_v_exp.in.scale"),
             box=UidBox("B:sir_i_v_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="scale",
             value=None, metadata=None),
        # sir_i_v_exp out
        Port(uid=UidPort("P:sir_i_v_exp.out.i_v"),
             box=UidBox("B:sir_i_v_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i_v",
             value=None, metadata=None),

        # sir_scale_exp in CHIME_SVIIvR
        Port(uid=UidPort("P:sir_scale_exp.v_n"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="v_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_scale_exp.i_v_n"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_v_n",
             value=None, metadata=None),

        ### -- CHIME_SVIIvR -- END

        # sir in
        Port(uid=UidPort("P:sir.n"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Integer"),
             name="n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.beta"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:sir.gamma"),
        #      box=UidBox("B:sir"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        Port(uid=UidPort("P:sir.s_in"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.i_in"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.r_in"),
             box=UidBox("B:sir"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
        # sir out
        Port(uid=UidPort("P:sir.s_out"),
             box=UidBox("B:sir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.i_out"),
             box=UidBox("B:sir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir.r_out"),
             box=UidBox("B:sir"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),

        # sir_s_n_exp in
        Port(uid=UidPort("P:sir_s_n_exp.beta"),
             box=UidBox("B:sir_s_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_s_n_exp.s"),
             box=UidBox("B:sir_s_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_s_n_exp.i"),
             box=UidBox("B:sir_s_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        # sir_s_n_exp out
        Port(uid=UidPort("P:sir_s_n_exp.s_n"),
             box=UidBox("B:sir_s_n_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="s_n",
             value=None, metadata=None),

        # sir_s_n_exp in
        Port(uid=UidPort("P:sir_i_n_exp.beta"),
             box=UidBox("B:sir_i_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="beta",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_n_exp.s"),
             box=UidBox("B:sir_i_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_n_exp.i"),
             box=UidBox("B:sir_i_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:sir_i_n_exp.gamma"),
        #      box=UidBox("B:sir_i_n_exp"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        # sir_i_n_exp out
        Port(uid=UidPort("P:sir_i_n_exp.i_n"),
             box=UidBox("B:sir_i_n_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i_n",
             value=None, metadata=None),

        # sir_r_n_exp in
        # REMOVE_CHIME_SIR_Base
        # Port(uid=UidPort("P:sir_r_n_exp.gamma"),
        #      box=UidBox("B:sir_r_n_exp"),
        #      type=UidType("PortInput"),
        #      value_type=UidType("Float"),
        #      name="gamma",
        #      value=None, metadata=None),

        Port(uid=UidPort("P:sir_r_n_exp.i"),
             box=UidBox("B:sir_r_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_r_n_exp.r"),
             box=UidBox("B:sir_r_n_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
        # sir_r_n_exp out
        Port(uid=UidPort("P:sir_r_n_exp.r_n"),
             box=UidBox("B:sir_r_n_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="r_n",
             value=None, metadata=None),

        # sir_scale_exp in
        Port(uid=UidPort("P:sir_scale_exp.n"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_scale_exp.s_n"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_scale_exp.i_n"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_scale_exp.r_n"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r_n",
             value=None, metadata=None),
        # sir_scale_exp out
        Port(uid=UidPort("P:sir_scale_exp.scale"),
             box=UidBox("B:sir_scale_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="scale",
             value=None, metadata=None),

        # sir_s_exp in
        Port(uid=UidPort("P:sir_s_exp.s_n"),
             box=UidBox("B:sir_s_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="s_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_s_exp.scale"),
             box=UidBox("B:sir_s_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="scale",
             value=None, metadata=None),
        # sir_s_exp out
        Port(uid=UidPort("P:sir_s_exp.s"),
             box=UidBox("B:sir_s_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="s",
             value=None, metadata=None),

        # sir_i_exp in
        Port(uid=UidPort("P:sir_i_exp.i_n"),
             box=UidBox("B:sir_i_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="i_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_i_exp.scale"),
             box=UidBox("B:sir_i_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="scale",
             value=None, metadata=None),
        # sir_i_exp out
        Port(uid=UidPort("P:sir_i_exp.i"),
             box=UidBox("B:sir_i_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="i",
             value=None, metadata=None),

        # sir_r_exp in
        Port(uid=UidPort("P:sir_r_exp.r_n"),
             box=UidBox("B:sir_r_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="r_n",
             value=None, metadata=None),
        Port(uid=UidPort("P:sir_r_exp.scale"),
             box=UidBox("B:sir_r_exp"),
             type=UidType("PortInput"),
             value_type=UidType("Float"),
             name="scale",
             value=None, metadata=None),
        # sir_r_exp out
        Port(uid=UidPort("P:sir_r_exp.r"),
             box=UidBox("B:sir_r_exp"),
             type=UidType("PortOutput"),
             value_type=UidType("Float"),
             name="r",
             value=None, metadata=None),
    ]

    junctions_main = [
        Junction(uid=UidJunction("J:main.s_n"),
                 name='s_n',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('1000'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.i_n"),
                 name='i_n',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('1'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.r_n"),
                 name='r_n',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('1'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.N_p"),
                 name='N_p',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('3'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),

        # REMOVE_CHIME_SIR_Base
        # Junction(uid=UidJunction("J:main.infections_days"),
        #          name='infections_days',
        #          type=None,
        #          value=Literal(uid=None,
        #                        type=UidType('Float'),
        #                        value=Val('14.0'),
        #                        name=None, metadata=None),
        #          value_type=UidType('Float'),
        #          metadata=None),

        ### -- CHIME_SVIIvR -- START

        Junction(uid=UidJunction("J:main.infections_days_unvaccinated"),
                 name='infections_days_unvaccinated',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('14'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.infections_days_vaccinated"),
                 name='infections_days_vaccinated',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('10'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),

        Junction(uid=UidJunction("J:main.v_n"),
                 name='v_n',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('0'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.i_v_n"),
                 name='i_v_n',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('0'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.vaccination_rate"),
                 name='vaccination_rate',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Float'),
                               value=Val('0.02'),
                               name=None, metadata=None),
                 value_type=UidType('Float'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.vaccine_efficacy"),
                 name='vaccine_efficacy',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Float'),
                               value=Val('0.85'),
                               name=None, metadata=None),
                 value_type=UidType('Float'),
                 metadata=None),

        ### -- CHIME_SVIIvR -- END

        Junction(uid=UidJunction("J:main.relative_contact_rate"),
                 name='relative_contact_rate',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Float'),
                               value=Val('0.05'),
                               name=None, metadata=None),
                 value_type=UidType('Float'),
                 metadata=None),
        Junction(uid=UidJunction("J:main.n_days"),
                 name='n_days',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('20'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),

        Junction(uid=UidJunction("J:main.i_day"),
                 name='i_day',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Float'),
                               value=Val('17.0'),
                               name=None, metadata=None),
                 value_type=UidType('Float'),
                 metadata=None),

        Junction(uid=UidJunction("J:main.p_idx"),
                 name='p_idx',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('1000'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
    ]

    junctions_simsir = [
        Junction(uid=UidJunction("J:simsir.loop_1_i"),
                 name='loop_1_i',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('0'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
    ]

    junctions_simsir_loop_1 = [
        Junction(uid=UidJunction('J:simsir_loop_1.loop_1_1_i'),
                 name='loop_1_1_i',
                 type=None,
                 value=Literal(uid=None,
                               type=UidType('Integer'),
                               value=Val('0'),
                               name=None, metadata=None),
                 value_type=UidType('Integer'),
                 metadata=None),
    ]

    # -- sim_sir() Expressions and Function --

    # simsir_loop_1_1_call_sir_exp
    simsir_loop_1_1_call_sir_exp = \
        BoxCall(uid=UidBox("B:simsir_loop_1_1_call_sir_exp"),
                type=None,
                name=None,
                call=UidBox("B:sir"),
                ports=[UidPort("PC:simsir_loop_1_1_call_sir_exp.in.s"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.i"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.r"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.beta"),

                       # REMOVE_CHIME_SIR_Base
                       # UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma"),

                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.n"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.out.s"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.out.i"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.out.r"),

                       ### -- CHIME_SVIIvR -- START
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.v"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.i_v"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.vaccination_rate"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.vaccine_efficacy"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma_unvaccinated"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.in.gamma_vaccinated"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.out.v"),
                       UidPort("PC:simsir_loop_1_1_call_sir_exp.out.i_v"),
                       ### -- CHIME_SVIIvR -- END
                       ],
                metadata=None)

    # simsir_loop_1_1_cond
    simsir_loop_1_1_cond_e0 = \
        Expr(call=RefOp(UidOp('len')),
             args=[UidPort("P:simsir_loop_1_1_cond.in.loop_1_1_seq")])
    simsir_loop_1_1_cond_e1 = \
        Expr(call=RefOp(UidOp('lt')),
             args=[UidPort("P:simsir_loop_1_1_cond.in.d_idx"),
                   simsir_loop_1_1_cond_e0])
    simsir_loop_1_1_cond = \
        Predicate(uid=UidBox("B:simsir_loop_1_1_cond"),
                  type=None,
                  name=None,
                  ports=[UidPort("P:simsir_loop_1_1_cond.in.d_idx"),
                         UidPort("P:simsir_loop_1_1_cond.in.loop_1_1_seq"),
                         UidPort("P:simsir_loop_1_1_cond.out.exit")],
                  tree=simsir_loop_1_1_cond_e1,
                  metadata=None)

    # simsir_loop_1_1_i_exp
    simsir_loop_1_1_i_exp_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:simsir_loop_1_1_i_exp.in.loop_1_1_i"),
                   Literal(uid=None, type=UidType("Integer"), value=Val("1"),
                           name=None, metadata=None)])
    simsir_loop_1_1_i_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_1_i_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_1_i_exp.in.loop_1_1_i"),
                          UidPort("P:simsir_loop_1_1_i_exp.out.loop_1_1_i")],
                   tree=simsir_loop_1_1_i_exp_e0,
                   metadata=None)

    # simsir_loop_1_1_get_d_idx_exp
    simsir_loop_1_1_get_d_idx_exp_e0 = \
        Expr(call=RefOp(UidOp('get')),
             args=[UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_seq"),
                   UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_i")])
    simsir_loop_1_1_get_d_idx_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_1_get_d_idx_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_seq"),
                          UidPort("P:simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_i"),
                          UidPort("P:simsir_loop_1_1_get_d_idx_exp.out.d_idx")],
                   tree=simsir_loop_1_1_get_d_idx_exp_e0,
                   metadata=None)

    # simsir_loop_1_1
    simsir_loop_1_1 = \
        Loop(uid=UidBox("B:simsir_loop_1_1"),
             type=None,
             name=None,
             ports=[
                 # -- "control" loop ports
                 UidPort("P:simsir_loop_1_1.in.d_idx"),
                 UidPort("P:simsir_loop_1_1.in.loop_1_1_seq"),
                 UidPort("P:simsir_loop_1_1.in.loop_1_1_i"),
                 UidPort("PC:simsir_loop_1_1.out.d_idx"),
                 UidPort("PC:simsir_loop_1_1.out.loop_1_1_seq"),
                 UidPort("PC:simsir_loop_1_1.out.loop_1_1_i"),

                 # -- "body" loop inputs
                 UidPort("P:simsir_loop_1_1.in.s"),
                 UidPort("P:simsir_loop_1_1.in.i"),
                 UidPort("P:simsir_loop_1_1.in.r"),
                 UidPort("P:simsir_loop_1_1.in.n"),

                 # REMOVE_CHIME_SIR_Base
                 # UidPort("P:simsir_loop_1_1.in.gamma"),
                 UidPort("P:simsir_loop_1_1.in.beta"),

                 # -- "body" loop outputs
                 UidPort("PC:simsir_loop_1_1.out.s"),
                 UidPort("PC:simsir_loop_1_1.out.i"),
                 UidPort("PC:simsir_loop_1_1.out.r"),
                 UidPort("PC:simsir_loop_1_1.out.n"),

                 # REMOVE_CHIME_SIR_Base
                 # UidPort("PC:simsir_loop_1_1.out.gamma"),

                 UidPort("PC:simsir_loop_1_1.out.beta"),

                 ### -- CHIME_SVIIvR -- START
                 UidPort("P:simsir_loop_1_1.in.v"),
                 UidPort("P:simsir_loop_1_1.in.i_v"),
                 UidPort("P:simsir_loop_1_1.in.vaccination_rate"),
                 UidPort("P:simsir_loop_1_1.in.vaccine_efficacy"),
                 UidPort("P:simsir_loop_1_1.in.gamma_unvaccinated"),
                 UidPort("P:simsir_loop_1_1.in.gamma_vaccinated"),
                 ### -- CHIME_SVIIvR -- END
                 UidPort("PC:simsir_loop_1_1.out.v"),
                 UidPort("PC:simsir_loop_1_1.out.i_v"),
                 UidPort("PC:simsir_loop_1_1.out.vaccination_rate"),
                 UidPort("PC:simsir_loop_1_1.out.vaccine_efficacy"),
                 UidPort("PC:simsir_loop_1_1.out.gamma_unvaccinated"),
                 UidPort("PC:simsir_loop_1_1.out.gamma_vaccinated"),

             ],

             exit_condition=UidBox("B:simsir_loop_1_1_cond"),

             # contents
             wires=[
                 UidWire("W:simsir_loop_1_1.in.d_idx>simsir_loop_1_1_cond.in.d_idx"),
                 UidWire("W:simsir_loop_1_1.in.loop_1_1_seq>simsir_loop_1_1_cond.in.loop_1_1_seq"),
                 UidWire("W:simsir_loop_1_1.in.loop_1_1_i>simsir_loop_1_1_i_exp.in.loop_1_1_i"),
                 UidWire("W:simsir_loop_1_1.in.loop_1_1_seq>simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_seq"),
                 UidWire("W:simsir_loop_1_1_i_exp.out.loop_1_1_i>simsir_loop_1_1_get_d_idx_exp.in.loop_1_1_i"),
                 UidWire("W:simsir_loop_1_1_i_exp.out.loop_1_1_i>simsir_loop_1_1.out.loop_1_1_i"),
                 UidWire("W:simsir_loop_1_1_get_d_idx_exp.out.d_idx>simsir_loop_1_1.out.d_idx"),
                 UidWire("W:simsir_loop_1_1.in.n>simsir_loop_1_1_call_sir_exp.in.n"),
                 UidWire("W:simsir_loop_1_1.in.s>simsir_loop_1_1_call_sir_exp.in.s"),
                 UidWire("W:simsir_loop_1_1.in.i>simsir_loop_1_1_call_sir_exp.in.i"),
                 UidWire("W:simsir_loop_1_1.in.r>simsir_loop_1_1_call_sir_exp.in.r"),

                 # REMOVE_CHIME_SIR_Base
                 # UidWire("W:simsir_loop_1_1.in.gamma>simsir_loop_1_1_call_sir_exp.in.gamma"),

                 UidWire("W:simsir_loop_1_1.in.beta>simsir_loop_1_1_call_sir_exp.in.beta"),
                 UidWire("W:simsir_loop_1_1_call_sir_exp.out.s>simsir_loop_1_1.out.s"),
                 UidWire("W:simsir_loop_1_1_call_sir_exp.out.i>simsir_loop_1_1.out.i"),
                 UidWire("W:simsir_loop_1_1_call_sir_exp.out.r>simsir_loop_1_1.out.r"),

                 ### -- CHIME_SVIIvR -- START
                 UidWire("W:P:simsir_loop_1_1.in.v>simsir_loop_1_1_call_sir_exp.in.v"),
                 UidWire("W:simsir_loop_1_1.in.i_v>simsir_loop_1_1_call_sir_exp.in.i_v"),
                 UidWire("W:simsir_loop_1_1.in.vaccination_rate>simsir_loop_1_1_call_sir_exp.in.vaccination_rate"),
                 UidWire("W:simsir_loop_1_1.in.vaccine_efficacy>simsir_loop_1_1_call_sir_exp.in.vaccine_efficacy"),
                 UidWire("W:simsir_loop_1_1.in.gamma_unvaccinated>simsir_loop_1_1_call_sir_exp.in.gamma_unvaccinated"),
                 UidWire("W:simsir_loop_1_1.in.gamma_vaccinated>simsir_loop_1_1_call_sir_exp.in.gamma_vaccinated"),
                 UidWire("W:simsir_loop_1_1_call_sir_exp.out.v>simsir_loop_1_1.out.v"),
                 UidWire("W:simsir_loop_1_1_call_sir_exp.out.i_v>simsir_loop_1_1.out.i_v"),
                 ### -- CHIME_SVIIvR -- END
             ],
             junctions=None,
             boxes=[
                 UidBox("B:simsir_loop_1_1_i_exp"),
                 UidBox("B:simsir_loop_1_1_get_d_idx_exp"),
                 UidBox("B:simsir_loop_1_1_call_sir_exp")
             ],

             metadata=None)

    # simsir_loop_1

    # -- loop_1 control components

    # simsir_loop_1_cond
    simsir_loop_1_cond_e0 = \
        Expr(call=RefOp(UidOp('len')),
             args=[UidPort("P:simsir_loop_1_cond.in.loop_1_seq")])
    simsir_loop_1_cond_e1 = \
        Expr(call=RefOp(UidOp('lt')),
             args=[UidPort("P:simsir_loop_1_cond.in.p_idx"),
                   simsir_loop_1_cond_e0])
    simsir_loop_1_cond = \
        Predicate(uid=UidBox("B:simsir_loop_1_cond"),
                  type=None,
                  name=None,
                  ports=[UidPort("P:simsir_loop_1_cond.in.p_idx"),
                         UidPort("P:simsir_loop_1_cond.in.loop_1_seq"),
                         UidPort("P:simsir_loop_1_cond.out.exit")],
                  tree=simsir_loop_1_cond_e1,
                  metadata=None)

    # simsir_loop_1_i_exp
    simsir_loop_1_i_exp_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:simsir_loop_1_i_exp.in.loop_1_i"),
                   Literal(uid=None, type=UidType("Integer"), value=Val("1"),
                           name=None, metadata=None)])
    simsir_loop_1_i_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_i_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_i_exp.in.loop_1_i"),
                          UidPort("P:simsir_loop_1_i_exp.out.loop_1_i")],
                   tree=simsir_loop_1_i_exp_e0,
                   metadata=None)

    # simsir_loop_1_get_p_idx_exp
    simsir_loop_1_get_p_idx_exp_e0 = \
        Expr(call=RefOp(UidOp('get')),
             args=[UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_seq"),
                   UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_i")])
    simsir_loop_1_get_p_idx_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_get_p_idx_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_seq"),
                          UidPort("P:simsir_loop_1_get_p_idx_exp.in.loop_1_i"),
                          UidPort("P:simsir_loop_1_get_p_idx_exp.out.p_idx")],
                   tree=simsir_loop_1_get_p_idx_exp_e0,
                   metadata=None)

    # -- loop_1 body components

    # simsir_loop_1_n_days_exp
    simsir_loop_1_n_days_exp_e0 = \
        Expr(call=RefOp(UidOp('get')),
             args=[UidPort("P:simsir_loop_1_n_days_exp.in.days"),
                   UidPort("P:simsir_loop_1_n_days_exp.in.p_idx")])
    simsir_loop_1_n_days_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_n_days_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_n_days_exp.in.days"),
                          UidPort("P:simsir_loop_1_n_days_exp.in.p_idx"),
                          UidPort("P:simsir_loop_1_n_days_exp.out.n_days")],
                   tree=simsir_loop_1_n_days_exp_e0,
                   metadata=None)

    # simsir_loop_1_get_beta_exp
    simsir_loop_1_get_beta_exp_e0 = \
        Expr(call=RefOp(UidOp('get')),
             args=[UidPort("P:simsir_loop_1_get_beta_exp.in.betas"),
                   UidPort("P:simsir_loop_1_get_beta_exp.in.p_idx")])
    simsir_loop_1_get_beta_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_get_beta_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_get_beta_exp.in.betas"),
                          UidPort("P:simsir_loop_1_get_beta_exp.in.p_idx"),
                          UidPort("P:simsir_loop_1_get_beta_exp.out.beta")],
                   tree=simsir_loop_1_get_beta_exp_e0,
                   metadata=None)

    # -- in loop_1: loop_1_1 for-loop sequence iteration initialization

    # simsir_loop_1_1_range_init_exp
    simsir_loop_1_1_range_init_exp_e0 = \
        Expr(call=RefOp(UidOp('range')),
             args=[UidPort("P:simsir_loop_1_1_range_init_exp.in.n_days")])
    simsir_loop_1_1_range_init_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_1_range_init_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_1_range_init_exp.in.n_days"),
                          UidPort("P:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq")],
                   tree=simsir_loop_1_1_range_init_exp_e0,
                   metadata=None)

    # simsir_loop_1_1_get_d_idx_init_exp
    simsir_loop_1_1_get_d_idx_init_exp_0 = \
        Expr(call=RefOp(UidOp('get')),
             args=[UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_seq"),
                   UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_i")])
    simsir_loop_1_1_get_d_idx_init_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_1_get_d_idx_init_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_seq"),
                          UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_i"),
                          UidPort("P:simsir_loop_1_1_get_d_idx_init_exp.out.d_idx")],
                   tree=simsir_loop_1_1_get_d_idx_init_exp_0,
                   metadata=None)

    simsir_loop_1 = \
        Loop(uid=UidBox("B:simsir_loop_1"),
             type=None,
             name=None,
             ports=[
                 # -- "control" loop ports
                 UidPort("P:simsir_loop_1.in.p_idx"),
                 UidPort("P:simsir_loop_1.in.loop_1_seq"),
                 UidPort("P:simsir_loop_1.in.loop_1_i"),

                 UidPort("PC:simsir_loop_1.out.p_idx"),
                 UidPort("PC:simsir_loop_1.out.loop_1_seq"),
                 UidPort("PC:simsir_loop_1.out.loop_1_i"),

                 # -- "body" loop inputs
                 UidPort("P:simsir_loop_1.in.days"),
                 UidPort("P:simsir_loop_1.in.betas"),
                 UidPort("P:simsir_loop_1.in.n"),
                 UidPort("P:simsir_loop_1.in.s"),
                 UidPort("P:simsir_loop_1.in.i"),
                 UidPort("P:simsir_loop_1.in.r"),

                 # REMOVE_CHIME_SIR_Base
                 # UidPort("P:simsir_loop_1.in.gamma"),

                 # -- "body" loop outputs
                 UidPort("PC:simsir_loop_1.out.days"),
                 UidPort("PC:simsir_loop_1.out.betas"),
                 UidPort("PC:simsir_loop_1.out.n"),
                 UidPort("PC:simsir_loop_1.out.s"),
                 UidPort("PC:simsir_loop_1.out.i"),
                 UidPort("PC:simsir_loop_1.out.r"),

                 # REMOVE_CHIME_SIR_Base
                 # UidPort("PC:simsir_loop_1.out.gamma"),

                 ### -- CHIME_SVIIvR -- START
                 UidPort("P:simsir_loop_1.in.v"),
                 UidPort("P:simsir_loop_1.in.i_v"),
                 UidPort("P:simsir_loop_1.in.vaccination_rate"),
                 UidPort("P:simsir_loop_1.in.vaccine_efficacy"),
                 UidPort("P:simsir_loop_1.in.gamma_unvaccinated"),
                 UidPort("P:simsir_loop_1.in.gamma_vaccinated"),

                 UidPort("PC:simsir_loop_1.out.v"),
                 UidPort("PC:simsir_loop_1.out.i_v"),
                 UidPort("PC:simsir_loop_1.out.vaccination_rate"),
                 UidPort("PC:simsir_loop_1.out.vaccine_efficacy"),
                 UidPort("PC:simsir_loop_1.out.gamma_unvaccinated"),
                 UidPort("PC:simsir_loop_1.out.gamma_vaccinated"),
                 ### -- CHIME_SVIIvR -- END

            ],

             exit_condition=UidBox("B:simsir_loop_1_cond"),

             # contents
             junctions=[UidJunction('J:simsir_loop_1.loop_1_1_i')],
             wires=[
                 # loop_1 control
                 UidWire("W:simsir_loop_1.in.p_idx>simsir_loop_1_cond.in.p_idx"),
                 UidWire("W:simsir_loop_1.in.loop_1_seq>simsir_loop_1_cond.in.loop_1_seq"),
                 UidWire("W:simsir_loop_1.in.loop_1_i>simsir_loop_1_i_exp.in.loop_1_i"),
                 UidWire("W:simsir_loop_1.in.loop_1_seq>simsir_loop_1_get_p_idx_exp.in.loop_1_seq"),
                 UidWire("W:simsir_loop_1_i_exp.out.loop_1_i>simsir_loop_1_get_p_idx_exp.in.loop_1_i"),
                 UidWire("W:simsir_loop_1_i_exp.out.loop_1_i>simsir_loop_1.out.loop_1_i"),
                 UidWire("W:simsir_loop_1_get_p_idx_exp.out.p_idx>simsir_loop_1.out.p_idx"),

                 # loop_1 body
                 UidWire("W:simsir_loop_1.in.days>simsir_loop_1_n_days_exp.in.days"),
                 UidWire("W:simsir_loop_1_get_p_idx_exp.out.p_idx>simsir_loop_1_n_days_exp.in.p_idx"),
                 UidWire("W:simsir_loop_1_n_days_exp.out.n_days>simsir_loop_1_1_range_init_exp.in.n_days"),
                 UidWire("W:simsir_loop_1.in.betas>simsir_loop_1_get_beta_exp.in.betas"),
                 UidWire("W:simsir_loop_1_get_p_idx_exp.out.p_idx>simsir_loop_1_get_beta_exp.in.p_idx"),
                 UidWire("W:simsir_loop_1_get_beta_exp.out.beta>simsir_loop_1_1.in.beta"),

                 # loop_1 body passthrough
                 UidWire("W:simsir_loop_1.in.n>simsir_loop_1_1.in.n"),
                 UidWire("W:simsir_loop_1.in.s>simsir_loop_1_1.in.s"),
                 UidWire("W:simsir_loop_1.in.i>simsir_loop_1_1.in.i"),
                 UidWire("W:simsir_loop_1.in.r>simsir_loop_1_1.in.r"),

                 # REMOVE_CHIME_SIR_Base
                 # UidWire("W:simsir_loop_1.in.gamma>simsir_loop_1_1.in.gamma"),

                 UidWire("W:simsir_loop_1_1.out.s>simsir_loop_1.out.s"),
                 UidWire("W:simsir_loop_1_1.out.i>simsir_loop_1.out.i"),
                 UidWire("W:simsir_loop_1_1.out.r>simsir_loop_1.out.r"),

                 # loop_1_1 for-iteration init
                 UidWire("W:simsir_loop_1_1_get_d_idx_init_exp.out.d_idx>simsir_loop_1_1.in.d_idx"),
                 UidWire("W:simsir_loop_1.loop_1_1_i>simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_i"),
                 UidWire("W:simsir_loop_1.loop_1_1_i>simsir_loop_1_1.in.loop_1_1_i"),
                 UidWire("W:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq>simsir_loop_1_1_get_d_idx_init_exp.in.loop_1_1_seq"),
                 UidWire("W:simsir_loop_1_1_range_init_exp.out.loop_1_1_seq>simsir_loop_1_1.in.loop_1_1_seq"),

                 ### -- CHIME_SVIIvR -- START
                 UidWire("W:simsir_loop_1.in.v>simsir_loop_1_1.in.v"),
                 UidWire("W:simsir_loop_1.in.i_v>simsir_loop_1_1.in.i_v"),
                 UidWire("W:simsir_loop_1.in.vaccination_rate>simsir_loop_1_1.in.vaccination_rate"),
                 UidWire("W:simsir_loop_1.in.vaccine_efficacy>simsir_loop_1_1.in.vaccine_efficacy"),
                 UidWire("W:simsir_loop_1.in.gamma_unvaccinated>simsir_loop_1_1.in.gamma_unvaccinated"),
                 UidWire("W:simsir_loop_1.in.gamma_vaccinated>simsir_loop_1_1.in.gamma_vaccinated"),
                 UidWire("W:simsir_loop_1_1.out.v>simsir_loop_1.out.v"),
                 UidWire("W:simsir_loop_1_1.out.i_v>simsir_loop_1.out.i_v"),
                 ### -- CHIME_SVIIvR -- END
             ],
             boxes=[
                 # control
                 UidBox("B:simsir_loop_1_i_exp"),
                 UidBox("B:simsir_loop_1_get_p_idx_exp"),

                 # body
                 UidBox("B:simsir_loop_1_n_days_exp"),
                 UidBox("B:simsir_loop_1_get_beta_exp"),

                 # loop_1_1 for-iteration init
                 UidBox("B:simsir_loop_1_1_range_init_exp"),
                 UidBox("B:simsir_loop_1_1_get_d_idx_init_exp"),
                 UidBox("B:simsir_loop_1_1"),
             ],

             metadata=None
             )

    # -- in simsir: loop_1 for-loop sequence iteration initialization

    # simsir_loop_1_range_init_exp
    simsir_loop_1_range_init_exp_e0 = \
        Expr(call=RefOp(UidOp('range')),
             args=[UidPort("P:simsir_loop_1_range_init_exp.in.N_p")])
    simsir_loop_1_range_init_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_range_init_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_range_init_exp.in.N_p"),
                          UidPort("P:simsir_loop_1_range_init_exp.out.loop_1_seq")],
                   tree=simsir_loop_1_range_init_exp_e0,
                   metadata=None)

    # simsir_loop_1_get_p_idx_init_exp
    simsir_loop_1_get_p_idx_init_exp_e0 = \
        Expr(call=RefOp(UidOp('get')),
             args=[UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_seq"),
                   UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_i")])
    simsir_loop_1_get_p_idx_init_exp = \
        Expression(uid=UidBox("B:simsir_loop_1_get_p_idx_init_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_seq"),
                          UidPort("P:simsir_loop_1_get_p_idx_init_exp.in.loop_1_i"),
                          UidPort("P:simsir_loop_1_get_p_idx_init_exp.out.p_idx")],
                   tree=simsir_loop_1_get_p_idx_init_exp_e0,
                   metadata=None)

    # simsir_n_exp
    simsir_n_exp_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:simsir_n_exp.in.s"),
                   UidPort("P:simsir_n_exp.in.i"),
                   UidPort("P:simsir_n_exp.in.r"),
                   ### -- CHIME_SVIIvR -- START
                   UidPort("P:simsir_n_exp.in.v"),
                   UidPort("P:simsir_n_exp.in.i_v"),
                   ### -- CHIME_SVIIvR -- END
                   ])
    simsir_n_exp = \
        Expression(uid=UidBox("B:simsir_n_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:simsir_n_exp.in.s"),
                          UidPort("P:simsir_n_exp.in.i"),
                          UidPort("P:simsir_n_exp.in.r"),
                          UidPort("P:simsir_n_exp.out.n"),

                          ### -- CHIME_SVIIvR -- START
                          UidPort("P:simsir_n_exp.in.v"),
                          UidPort("P:simsir_n_exp.in.i_v"),
                          ### -- CHIME_SVIIvR -- END
                          ],
                   tree=simsir_n_exp_e0,
                   metadata=None)

    simsir = \
        Function(uid=UidBox("B:simsir"),
                 type=None,
                 name=UidOp("sim_sir"),
                 ports=[
                     UidPort("P:simsir.in.s"),
                     UidPort("P:simsir.in.i"),
                     UidPort("P:simsir.in.r"),

                     # REMOVE_CHIME_SIR_Base
                     # UidPort("P:simsir.in.gamma"),

                     UidPort("P:simsir.in.betas"),
                     UidPort("P:simsir.in.days"),
                     UidPort("P:simsir.in.N_p"),

                     UidPort("P:simsir.out.s"),
                     UidPort("P:simsir.out.i"),
                     UidPort("P:simsir.out.r"),

                     ### -- CHIME_SVIIvR -- START
                     UidPort("P:simsir.in.v"),
                     UidPort("P:simsir.in.i_v"),
                     UidPort("P:simsir.in.vaccination_rate"),
                     UidPort("P:simsir.in.vaccine_efficacy"),
                     UidPort("P:simsir.in.gamma_unvaccinated"),
                     UidPort("P:simsir.in.gamma_vaccinated"),

                     UidPort("P:simsir.out.v"),
                     UidPort("P:simsir.out.i_v"),
                     ### -- CHIME_SVIIvR -- END
                 ],

                 # contents
                 junctions=[UidJunction("J:simsir.loop_1_i")],
                 wires=[
                     UidWire("W:simsir.in.N_p>simsir_loop_1_range_init_exp.in.N_p"),
                     UidWire("W:simsir_loop_1_range_init_exp.out.loop_1_seq>simsir_loop_1_get_p_idx_init_exp.in.loop_1_seq"),
                     UidWire("W:simsir_loop_1_range_init_exp.out.loop_1_seq>simsir_loop_1.in.loop_1_seq"),
                     UidWire("W:simsir_loop_1_get_p_idx_init_exp.out.p_idx>simsir_loop_1.in.p_idx"),
                     UidWire("W:simsir.loop_1_i>simsir_loop_1_get_p_idx_init_exp.in.loop_1_i"),
                     UidWire("W:simsir.loop_1_i>simsir_loop_1.in.loop_1_i"),
                     UidWire("W:simsir.in.days>simsir_loop_1.in.days"),
                     UidWire("W:simsir.in.betas>simsir_loop_1.in.betas"),

                     # REMOVE_CHIME_SIR_Base
                     # UidWire("W:simsir.in.gamma>simsir_loop_1.in.gamma"),

                     UidWire("W:simsir.in.s>simsir_loop_1.in.s"),
                     UidWire("W:simsir.in.s>simsir_n_exp.in.s"),
                     UidWire("W:simsir.in.i>simsir_loop_1.in.i"),
                     UidWire("W:simsir.in.i>simsir_n_exp.in.i"),
                     UidWire("W:simsir.in.r>simsir_loop_1.in.r"),
                     UidWire("W:simsir.in.r>simsir_n_exp.in.r"),
                     UidWire("W:simsir_n_exp.out.n>simsir_loop_1.in.n"),
                     UidWire("W:simsir_loop_1.out.s>simsir.out.s"),
                     UidWire("W:simsir_loop_1.out.i>simsir.out.i"),
                     UidWire("W:simsir_loop_1.out.r>simsir.out.r"),

                     ### -- CHIME_SVIIvR -- START
                     UidWire("W:simsir.in.v>simsir_n_exp.in.v"),
                     UidWire("W:simsir.in.v>simsir_loop_1.in.v"),
                     UidWire("W:simsir.in.i_v>simsir_n_exp.in.i_v"),
                     UidWire("W:simsir.in.i_v>simsir_loop_1.in.i_v"),
                     UidWire("W:simsir.in.vaccination_rate>simsir_loop_1.in.vaccination_rate"),
                     UidWire("W:simsir.in.vaccine_efficacy>simsir_loop_1.in.vaccine_efficacy"),
                     UidWire("W:simsir.in.gamma_unvaccinated>simsir_loop_1.in.gamma_unvaccinated"),
                     UidWire("W:simsir.in.gamma_vaccinated>simsir_loop_1.in.gamma_vaccinated"),
                     UidWire("W:simsir_loop_1.out.v>simsir.out.v"),
                     UidWire("W:simsir_loop_1.out.i_v>simsir.out.i_v"),
                     ### -- CHIME_SVIIvR -- END
                 ],
                 boxes=[UidBox("B:simsir_loop_1_range_init_exp"),
                        UidBox("B:simsir_loop_1_get_p_idx_init_exp"),
                        UidBox("B:simsir_n_exp"),
                        UidBox("B:simsir_loop_1")],

                 metadata=None)

    # -- sir() --

    # Expression sir_s_n_exp
    # sir_s_n_exp_e0 = (* -1 beta s i)
    sir_s_n_exp_e0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Int"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_s_n_exp.beta"),
                   UidPort("P:sir_s_n_exp.s"),
                   UidPort("P:sir_s_n_exp.i")])
    ### -- CHIME_SVIIvR -- START
    # sir_s_n_exp_e1 = (* -1 beta s i_v)
    sir_s_n_exp_e1 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Int"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_s_n_exp.beta"),
                   UidPort("P:sir_s_n_exp.s"),
                   UidPort("P:sir_s_n_exp.in.i_v")])
    # sir_s_n_exp_e2 = (* -1 vaccination_rate s)
    sir_s_n_exp_e2 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Int"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_s_n_exp.in.vaccination_rate"),
                   UidPort("P:sir_s_n_exp.s")])
    ### -- CHIME_SVIIvR -- END
    # e2 = (+ e1 s) -> e2
    sir_s_n_exp_e3 = \
        Expr(call=RefOp(UidOp('+')),
             args=[sir_s_n_exp_e0,
                   ### -- CHIME_SVIIvR -- START
                   sir_s_n_exp_e1,
                   sir_s_n_exp_e2,
                   ### -- CHIME_SVIIvR -- END
                   UidPort("P:sir_s_n_exp.s")])
    sir_s_n_exp = Expression(uid=UidBox("B:sir_s_n_exp"),
                             type=None,
                             name=None,
                             ports=[UidPort("P:sir_s_n_exp.beta"),
                                    UidPort("P:sir_s_n_exp.s"),
                                    UidPort("P:sir_s_n_exp.i"),

                                    ### -- CHIME_SVIIvR -- START
                                    UidPort("P:sir_s_n_exp.in.i_v"),
                                    UidPort("P:sir_s_n_exp.in.vaccination_rate"),
                                    ### -- CHIME_SVIIvR -- END

                                    UidPort("P:sir_s_n_exp.s_n")],
                             tree=sir_s_n_exp_e3,
                             metadata=None)

    ### -- CHIME_SVIIvR -- START

    # -- sir_v_n_exp
    # sir_v_n_exp_0 = (* vaccination_rate s)
    sir_v_n_exp_0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_v_n_exp.in.vaccination_rate"),
                   UidPort("P:sir_v_n_exp.in.s")])
    # sir_v_n_exp_1 = (- 1 vaccine_efficacy)
    sir_v_n_exp_1 = \
        Expr(call=RefOp(UidOp('-')),
             args=[Literal(uid=None, type=UidType("Integer"), value=Val("1"),
                           name=None, metadata=None),
                   UidPort("P:sir_v_n_exp.in.vaccination_efficacy")])
    # sir_v_n_exp_1 = (* -1 beta sir_v_n_exp_1 v i)
    sir_v_n_exp_2 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Integer"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_v_n_exp.in.beta"),
                   sir_v_n_exp_1,
                   UidPort("P:sir_v_n_exp.in.v"),
                   UidPort("P:sir_v_n_exp.in.i")])
    # sir_v_n_exp_3 = (* -1 beta sir_v_n_exp_1 v i_v)
    sir_v_n_exp_3 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Integer"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_v_n_exp.in.beta"),
                   sir_v_n_exp_1,
                   UidPort("P:sir_v_n_exp.in.v"),
                   UidPort("P:sir_v_n_exp.in.i_v")])
    # sir_v_n_exp_4 = (+ sir_v_n_exp_0 sir_v_n_exp_2 sir_v_n_exp_3)
    sir_v_n_exp_4 = \
        Expr(call=RefOp(UidOp('+')),
             args=[sir_v_n_exp_0,
                   sir_v_n_exp_2,
                   sir_v_n_exp_3])
    # sir_v_n_exp_4 = (+ sir_v_n_exp_0 sir_v_n_exp_1 sir_v_n_exp_3 v)
    sir_v_n_exp = \
        Expression(uid=UidBox("B:sir_v_n_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:sir_v_n_exp.in.vaccination_rate"),
                          UidPort("P:sir_v_n_exp.in.s"),
                          UidPort("P:sir_v_n_exp.in.vaccination_efficacy"),
                          UidPort("P:sir_v_n_exp.in.beta"),
                          UidPort("P:sir_v_n_exp.in.v"),
                          UidPort("P:sir_v_n_exp.in.i"),
                          UidPort("P:sir_v_n_exp.in.i_v"),
                          UidPort("P:sir_v_n_exp.out.v_n")],
                   tree=sir_v_n_exp_4,
                   metadata=None)

    # -- sir_i_v_n_exp
    # sir_i_v_n_exp_0 = (- 1 vaccine_efficacy)
    sir_i_v_n_exp_0 = \
        Expr(call=RefOp(UidOp('-')),
             args=[Literal(uid=None, type=UidType("Integer"), value=Val("1"),
                           name=None, metadata=None),
                   UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy")])
    # sir_i_v_n_exp_1 = (* beta sir_i_v_n_exp_0 v i)
    sir_i_v_n_exp_1 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_i_v_n_exp.in.beta"),
                   sir_i_v_n_exp_0,
                   UidPort("P:sir_i_v_n_exp.in.v"),
                   UidPort("P:sir_i_v_n_exp.in.i")])
    # sir_i_v_n_exp_2 = (* beta sir_i_v_n_exp_0 v i_v)
    sir_i_v_n_exp_2 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_i_v_n_exp.in.beta"),
                   sir_i_v_n_exp_0,
                   UidPort("P:sir_i_v_n_exp.in.v"),
                   UidPort("P:sir_i_v_n_exp.in.i_v")])
    # sir_i_v_n_exp_3 = (* -1 gamma_vaccinated i_v)
    sir_i_v_n_exp_3 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Integer"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
                   UidPort("P:sir_i_v_n_exp.in.i_v")])
    # sir_i_v_n_exp_4 = (+ sir_i_v_n_exp_1 sir_i_v_n_exp_2 sir_i_v_n_exp_3 i_v)
    sir_i_v_n_exp_4 = \
        Expr(call=RefOp(UidOp('*')),
             args=[sir_i_v_n_exp_1, sir_i_v_n_exp_2, sir_i_v_n_exp_3,
                   UidPort("P:sir_i_v_n_exp.in.i_v")])
    sir_i_v_n_exp = \
        Expression(uid=UidBox("B:sir_i_v_n_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:sir_i_v_n_exp.in.vaccine_efficacy"),
                          UidPort("P:sir_i_v_n_exp.in.beta"),
                          UidPort("P:sir_i_v_n_exp.in.v"),
                          UidPort("P:sir_i_v_n_exp.in.i"),
                          UidPort("P:sir_i_v_n_exp.in.i_v"),
                          UidPort("P:sir_i_v_n_exp.in.gamma_vaccinated"),
                          UidPort("P:sir_i_v_n_exp.out.i_v_n")],
                   tree=sir_i_v_n_exp_4,
                   metadata=None)

    ### -- CHIME_SVIIvR -- END

    # Expression sir_i_n_exp
    # e3 = (* beta s i)
    sir_i_n_exp_e0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_i_n_exp.beta"),
                   UidPort("P:sir_i_n_exp.s"),
                   UidPort("P:sir_i_n_exp.i")])
    # sir_i_n_exp_e1 = (* beta s i_v)
    sir_i_n_exp_e1 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_i_n_exp.beta"),
                   UidPort("P:sir_i_n_exp.s"),
                   UidPort("P:sir_i_n_exp.i_v")])
    # sir_i_n_exp_e2 = (* -1 gamma_unvaccinated i)
    sir_i_n_exp_e2 = \
        Expr(call=RefOp(UidOp('*')),
             args=[Literal(uid=None, type=UidType("Integer"), value=Val("-1"),
                           name=None, metadata=None),
                   UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
                   UidPort("P:sir_i_n_exp.i")])

    # sir_i_n_exp_e3 = (+ sir_i_n_exp_e0 sir_i_n_exp_e1 sir_i_n_exp_e2 i)
    sir_i_n_exp_e3 = \
        Expr(call=RefOp('+'),
             args=[sir_i_n_exp_e0, sir_i_n_exp_e1, sir_i_n_exp_e2,
                   UidPort("P:sir_i_n_exp.i")])
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
    sir_i_n_exp = Expression(uid=UidBox("B:sir_i_n_exp"),
                             type=None,
                             name=None,
                             ports=[UidPort("P:sir_i_n_exp.beta"),
                                    UidPort("P:sir_i_n_exp.s"),
                                    UidPort("P:sir_i_n_exp.i"),

                                    # REMOVE_CHIME_SIR_Base
                                    # UidPort("P:sir_i_n_exp.gamma"),

                                    ### -- CHIME_SVIIvR -- START
                                    UidPort("P:sir_i_n_exp.i_v"),
                                    UidPort("P:sir_i_n_exp.gamma_unvaccinated"),
                                    ### -- CHIME_SVIIvR -- END

                                    UidPort("P:sir_i_n_exp.i_n")],
                             tree=sir_i_n_exp_e3,
                             metadata=None)

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
    sir_r_n_exp_e0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_r_n_exp.in.gamma_vaccinated"),
                   UidPort("P:sir_r_n_exp.in.i_v"),])
    # sir_r_n_exp_e1 = (* gamma_unvaccinated i)
    sir_r_n_exp_e1 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_r_n_exp.in.gamma_unvaccinated"),
                   UidPort("P:sir_r_n_exp.i"),])
    # sir_r_n_exp_e2 = (+ sir_r_n_exp_e0 sir_r_n_exp_e1 r)
    sir_r_n_exp_e2 = \
        Expr(call=RefOp(UidOp('+')),
             args=[sir_r_n_exp_e0, sir_r_n_exp_e1, UidPort("P:sir_r_n_exp.r")])
    sir_r_n_exp = Expression(uid=UidBox("B:sir_r_n_exp"),
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
                             metadata=None)

    # Expression sir_scale_exp
    # e8 = (+ s_n i_n r_n) -> e8
    e8 = Expr(call=RefOp(UidOp('+')),
              args=[UidPort("P:sir_scale_exp.s_n"),
                    UidPort("P:sir_scale_exp.i_n"),
                    UidPort("P:sir_scale_exp.r_n"),
                    ### -- CHIME_SVIIvR -- START
                    UidPort("P:sir_scale_exp.v_n"),
                    UidPort("P:sir_scale_exp.i_v_n")
                    ### -- CHIME_SVIIvR -- END
                    ])
    # e9 = (/ n e8)
    e9 = Expr(call=RefOp(UidOp('/')),
              args=[UidPort("P:sir_scale_exp.n"),
                    e8])
    sir_scale_exp = Expression(uid=UidBox("B:sir_scale_exp"),
                               type=None,
                               name=None,
                               ports=[UidPort("P:sir_scale_exp.n"),
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
                               metadata=None)

    # Expression sir_s_exp
    # e10 = (* s_n scale) -> e10
    e10 = Expr(call=RefOp(UidOp('*')),
               args=[UidPort("P:sir_s_exp.s_n"),
                     UidPort("P:sir_s_exp.scale")])
    sir_s_exp = Expression(uid=UidBox("B:sir_s_exp"),
                           type=None,
                           name=None,
                           ports=[UidPort("P:sir_s_exp.s_n"),
                                  UidPort("P:sir_s_exp.scale"),
                                  UidPort("P:sir_s_exp.s")],
                           tree=e10,
                           metadata=None)

    # Expression sir_i_exp
    # e11 = (* i_n scale) -> e11
    e11 = Expr(call=RefOp(UidOp('*')),
               args=[UidPort("P:sir_i_exp.i_n"),
                     UidPort("P:sir_i_exp.scale")])
    sir_i_exp = Expression(uid=UidBox("B:sir_i_exp"),
                           type=None,
                           name=None,
                           ports=[UidPort("P:sir_i_exp.i_n"),
                                  UidPort("P:sir_i_exp.scale"),
                                  UidPort("P:sir_i_exp.i")],
                           tree=e11,
                           metadata=None)

    # Expression sir_r_exp
    # e12 = (* r_n scale) -> e12
    e12 = Expr(call=RefOp(UidOp('*')),
               args=[UidPort("P:sir_r_exp.r_n"),
                     UidPort("P:sir_r_exp.scale")])
    sir_r_exp = Expression(uid=UidBox("B:sir_r_exp"),
                           type=None,
                           name=None,
                           ports=[UidPort("P:sir_r_exp.r_n"),
                                  UidPort("P:sir_r_exp.scale"),
                                  UidPort("P:sir_r_exp.r")],
                           tree=e12,
                           metadata=None)

    ### -- CHIME_SVIIvR -- START

    # sir_v_exp
    sir_v_exp_e0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_v_exp.in.v_n"),
                   UidPort("P:sir_v_exp.in.scale")])
    sir_v_exp = \
        Expression(uid=UidBox("B:sir_v_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:sir_v_exp.in.v_n"),
                          UidPort("P:sir_v_exp.in.scale"),
                          UidPort("P:sir_v_exp.out.v")],
                   tree=sir_v_exp_e0,
                   metadata=None)

    # sir_i_v_exp
    sir_i_v_exp_0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:sir_i_v_exp.in.i_v_n"),
                   UidPort("P:sir_i_v_exp.in.scale")])
    sir_i_v_exp = \
        Expression(uid=UidBox("B:sir_i_v_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:sir_i_v_exp.in.i_v_n"),
                          UidPort("P:sir_i_v_exp.in.scale"),
                          UidPort("P:sir_i_v_exp.out.i_v")],
                   tree=sir_i_v_exp_0,
                   metadata=None)

    ### -- CHIME_SVIIvR -- END

    # Function sir
    sir = \
        Function(uid=UidBox("B:sir"),
                 type=None,
                 name=UidOp("sir"),
                 ports=[UidPort("P:sir.n"),
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
                 wires=[UidWire("W:sir.n>sir_scale_exp.n"),
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
                        UidWire("W:sir.in.vaccination_rate>sir_s_n_exp.in.vaccination_rate"),

                        UidWire("W:sir.in.vaccination_rate>sir_v_n_exp.in.vaccination_rate"),
                        UidWire("W:sir.s_in>sir_v_n_exp.in.s"),
                        UidWire("W:sir.in.vaccination_efficacy>sir_v_n_exp.in.vaccination_efficacy"),
                        UidWire("W:sir.beta>sir_v_n_exp.in.beta"),
                        UidWire("W:sir.in.v>sir_v_n_exp.in.v"),
                        UidWire("W:sir.i_in>sir_v_n_exp.in.i"),
                        UidWire("W:sir.in.i_v>sir_v_n_exp.in.i_v"),
                        UidWire("W:sir_v_n_exp.out.v_n>sir_scale_exp.v_n"),
                        UidWire("W:sir_v_n_exp.out.v_n>sir_v_exp.in.v_n"),

                        UidWire("W:sir.in.i_v>sir_i_n_exp.i_v"),
                        UidWire("W:sir.in.gamma_unvaccinated>sir_i_n_exp.gamma_unvaccinated"),

                        UidWire("W:sir.in.vaccination_efficacy>sir_i_v_n_exp.in.vaccine_efficacy"),
                        UidWire("W:sir.beta>sir_i_v_n_exp.in.beta"),
                        UidWire("W:sir.in.v>sir_i_v_n_exp.in.v"),
                        UidWire("W:sir.i_in>sir_i_v_n_exp.in.i"),
                        UidWire("W:sir.in.i_v>sir_i_v_n_exp.in.i_v"),
                        UidWire("W:sir.in.gamma_vaccinated>sir_i_v_n_exp.in.gamma_vaccinated"),
                        UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_scale_exp.i_v_n"),
                        UidWire("W:sir_i_v_n_exp.out.i_v_n>sir_i_v_exp.in.i_v_n"),

                        UidWire("W:sir.in.gamma_vaccinated>sir_r_n_exp.in.gamma_vaccinated"),
                        UidWire("W:sir.in.i_v>sir_r_n_exp.in.i_v"),
                        UidWire("W:sir.in.gamma_unvaccinated>sir_r_n_exp.in.gamma_unvaccinated"),

                        UidWire("W:sir_scale_exp.scale>sir_v_exp.in.scale"),
                        UidWire("W:sir_v_exp.out.v>sir.out.v"),
                        UidWire("W:sir_scale_exp.scale>sir_i_v_exp.in.scale"),
                        UidWire("W:sir_i_v_exp.out.i_v>sir.out.i_v"),
                        ### -- CHIME_SVIIvR -- END
                        ],
                 boxes=[UidBox("B:sir_s_n_exp"),
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

                 metadata=None)

    # -- main() --

    # main_call_simsir
    main_call_simsir = \
        BoxCall(uid=UidBox("B:main_call_simsir"),
                type=None,
                name=None,
                call=UidBox("B:simsir"),
                ports=[
                    UidPort("PC:main_call_simsir.in.s_n"),
                    UidPort("PC:main_call_simsir.in.i_n"),
                    UidPort("PC:main_call_simsir.in.r_n"),
                    UidPort("PC:main_call_simsir.in.betas"),

                    # REMOVE_CHIME_SIR_Base
                    # UidPort("PC:main_call_simsir.in.gamma"),

                    UidPort("PC:main_call_simsir.in.days"),
                    UidPort("PC:main_call_simsir.in.N_p"),
                    UidPort("PC:main_call_simsir.out.s_n"),
                    UidPort("PC:main_call_simsir.out.i_n"),
                    UidPort("PC:main_call_simsir.out.r_n"),

                    ### -- CHIME_SVIIvR -- START
                    UidPort("PC:main_call_simsir.in.v_n"),
                    UidPort("PC:main_call_simsir.in.i_v_n"),
                    UidPort("PC:main_call_simsir.in.vaccination_rate"),
                    UidPort("PC:main_call_simsir.in.vaccine_efficacy"),
                    UidPort("PC:main_call_simsir.in.gamma_unvaccinated"),
                    UidPort("PC:main_call_simsir.in.gamma_vaccinated"),
                    UidPort("PC:main_call_simsir.out.v"),
                    UidPort("PC:main_call_simsir.out.i_v"),
                    ### -- CHIME_SVIIvR -- END
                ],
                metadata=None)

    # main_gamma_exp
    # REMOVE_CHIME_SIR_Base
    # main_gamma_exp_e0 = \
    #     Expr(call=RefOp(UidOp('/')),
    #          args=[Literal(uid=None,
    #                        type=UidType('Float'),
    #                        value=Val('1.0'),
    #                        name=None, metadata=None),
    #                UidPort("P:main_gamma_exp.in.infections_days")])
    # main_gamma_exp = \
    #     Expression(uid=UidBox("B:main_gamma_exp"),
    #                type=None,
    #                name=None,
    #                ports=[UidPort("P:main_gamma_exp.in.infections_days"),
    #                       UidPort("P:main_gamma_exp.out.gamma")],
    #                tree=main_gamma_exp_e0,
    #                metadata=None)

    # TODO HERE
    ### -- CHIME_SVIIvR -- START

    # main_gamma_unvaccinated_exp CHIME_SVIIvR
    main_gamma_unvaccinated_exp_e0 = \
        Expr(call=RefOp(UidOp('/')),
             args=[Literal(uid=None,
                           type=UidType('Float'),
                           value=Val('1.0'),
                           name=None, metadata=None),
                   UidPort("P:main_gamma_unvaccinated_exp.in.infections_days_unvaccinated")])
    main_gamma_unvaccinated_exp = \
        Expression(uid=UidBox("B:main_gamma_unvaccinated_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_gamma_unvaccinated_exp.in.infections_days_unvaccinated"),
                          UidPort("P:main_gamma_unvaccinated_exp.out.gamma_unvaccinated")],
                   tree=main_gamma_unvaccinated_exp_e0,
                   metadata=None)

    # main_gamma_vaccinated_exp CHIME_SVIIvR
    main_gamma_vaccinated_exp_0 = \
        Expr(call=RefOp(UidOp('/')),
             args=[Literal(uid=None,
                           type=UidType('Float'),
                           value=Val('1.0'),
                           name=None, metadata=None),
                   UidPort("P:main_gamma_vaccinated_exp.in.infections_days_vaccinated")])
    main_gamma_vaccinated_exp = \
        Expression(uid=UidBox("B:main_gamma_vaccinated_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_gamma_vaccinated_exp.in.infections_days_vaccinated"),
                          UidPort("P:main_gamma_vaccinated_exp.out.gamma_vaccinated")],
                   tree=main_gamma_vaccinated_exp_0,
                   metadata=None)

    ### -- CHIME_SVIIvR -- END

    # main_pbetas_seq
    main_pbetas_seq_e0 = \
        Expr(call=RefOp(UidOp('init_seq')),
             args=[UidPort("P:main_pbetas_seq.in.fill"),
                   UidPort("P:main_pbetas_seq.in.size")])
    main_pbetas_seq = \
        Expression(uid=UidBox("B:main_pbetas_seq"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_pbetas_seq.in.fill"),
                          UidPort("P:main_pbetas_seq.in.size"),
                          UidPort("P:main_pbetas_seq.out.policys_betas")],
                   tree=main_pbetas_seq_e0,
                   metadata=None)

    # main_pdays_seq
    main_pdays_seq_e0 = \
        Expr(call=RefOp(UidOp('init_seq')),
             args=[UidPort("P:main_pdays_seq.in.fill"),
                   UidPort("P:main_pdays_seq.in.size")])
    main_pdays_seq = \
        Expression(uid=UidBox("B:main_pdays_seq"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_pdays_seq.in.fill"),
                          UidPort("P:main_pdays_seq.in.size"),
                          UidPort("P:main_pdays_seq.out.policy_days")],
                   tree=main_pdays_seq_e0,
                   metadata=None)

    # -- main_loop_1

    # main_loop_1_cond
    main_loop_1_cond_e0 = \
        Expr(call=RefOp(UidOp('geq')),
             args=[UidPort("P:main_loop_1_cond.in.p_idx"),
                   UidPort("P:main_loop_1_cond.in.N_p")])
    main_loop_1_cond = \
        Predicate(uid=UidBox("B:main_loop_1_cond"),
                  type=None,
                  name=None,
                  ports=[UidPort("P:main_loop_1_cond.in.p_idx"),
                         UidPort("P:main_loop_1_cond.in.N_p"),
                         UidPort("P:main_loop_1_cond.out.exit")],
                  tree=main_loop_1_cond_e0,
                  metadata=None)

    # main_loop_1_p_idx_exp
    main_loop_1_p_idx_exp_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:main_loop_1_p_idx_exp.in.p_idx"),
                   Literal(uid=None,
                           type=UidType('Integer'),
                           value=Val('1'),
                           name=None, metadata=None)])
    main_loop_1_p_idx_exp = \
        Expression(uid=UidBox("B:main_loop_1_p_idx_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_loop_1_p_idx_exp.in.p_idx"),
                          UidPort("P:main_loop_1_p_idx_exp.out.p_idx")],
                   tree=main_loop_1_p_idx_exp_e0,
                   metadata=None)

    # -- main_loop_1 body

    # get_growth_rate
    get_growth_rate = \
        Function(uid=UidBox("B:get_growth_rate"),
                 type=None,
                 name=UidOp("get_growth_rate"),
                 ports=[
                     UidPort("P:get_growth_rate.in.doubling_time"),
                     UidPort("P:get_growth_rate.out.growth_rate"),
                 ],

                 # contents
                 junctions=None,
                 wires=[
                     UidWire("W:get_growth_rate.in.doubling_time>get_growth_rate.out.growth_rate")
                 ],
                 boxes=None,

                 metadata=None)

    # main_loop_1_call_growth_rate_exp
    main_loop_1_call_growth_rate_exp = \
        BoxCall(uid=UidBox("B:main_loop_1_call_growth_rate_exp"),
                type=None,
                name=None,
                call=UidBox("B:get_growth_rate"),
                ports=[
                    UidPort("PC:main_loop_1_call_growth_rate_exp.in.doubling_time"),
                    UidPort("PC:main_loop_1_call_growth_rate_exp.out.growth_rate")
                ],
                metadata=None)

    # main_loop_1_dtime_exp
    main_loop_1_dtime_exp_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:main_loop_1_dtime_exp.in.p_idx"),
                   Literal(uid=None,
                           type=UidType('Float'),
                           value=Val('1.0'),
                           name=None, metadata=None)])
    main_loop_1_dtime_exp_e1 = \
        Expr(call=RefOp(UidOp('*')),
             args=[main_loop_1_dtime_exp_e0,
                   Literal(uid=None,
                           type=UidType('Float'),
                           value=Val('5.0'),
                           name=None, metadata=None)])
    main_loop_1_dtime_exp = \
        Expression(uid=UidBox("B:main_loop_1_dtime_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_loop_1_dtime_exp.in.p_idx"),
                          UidPort("P:main_loop_1_dtime_exp.out.doubling_time")],
                   tree=main_loop_1_dtime_exp_e1,
                   metadata=None)

    # -- get_beta

    # get_beta_updated_growth_rate_expr
    get_beta_updated_growth_rate_expr_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:get_beta_updated_growth_rate_expr.in.intrinsic_growth_rate"),
                   UidPort("P:get_beta_updated_growth_rate_expr.in.gamma"),])
    get_beta_updated_growth_rate_expr = \
        Expression(uid=UidBox("B:get_beta_updated_growth_rate_expr"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:get_beta_updated_growth_rate_expr.in.intrinsic_growth_rate"),
                          UidPort("P:get_beta_updated_growth_rate_expr.in.gamma"),
                          UidPort("P:get_beta_updated_growth_rate_expr.out.updated_growth_rate"),],
                   tree=get_beta_updated_growth_rate_expr_e0,
                   metadata=None)

    # get_beta_inv_contact_rate_exp
    get_beta_inv_contact_rate_exp_e0 = \
        Expr(call=RefOp(UidOp('-')),
             args=[Literal(uid=None,
                           type=UidType('Float'),
                           value=Val('1.0'),
                           name=None, metadata=None),
                   UidPort("P:get_beta_inv_contact_rate_exp.in.relative_contact_rate")])
    get_beta_inv_contact_rate_exp = \
        Expression(uid=UidBox("B:get_beta_inv_contact_rate_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:get_beta_inv_contact_rate_exp.in.relative_contact_rate"),
                          UidPort("P:get_beta_inv_contact_rate_exp.out.inv_contact_rate")],
                   tree=get_beta_inv_contact_rate_exp_e0,
                   metadata=None)

    # get_beta_betas_exp
    get_beta_betas_exp_e0 = \
        Expr(call=RefOp(UidOp('/')),
             args=[UidPort("P:get_beta_betas_exp.in.updated_growth_rate"),
                   UidPort("P:get_beta_betas_exp.in.susceptible")])
    get_beta_betas_exp_e1 = \
        Expr(call=RefOp(UidOp('*')),
             args=[get_beta_betas_exp_e0,
                   UidPort("P:get_beta_betas_exp.in.inv_contact_rate")])
    get_beta_betas_exp = \
        Expression(uid=UidBox("B:get_beta_betas_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:get_beta_betas_exp.in.updated_growth_rate"),
                          UidPort("P:get_beta_betas_exp.in.susceptible"),
                          UidPort("P:get_beta_betas_exp.in.inv_contact_rate"),
                          UidPort("P:get_beta_betas_exp.out.beta")],
                   tree=get_beta_betas_exp_e1,
                   metadata=None)

    get_beta = \
        Function(uid=UidBox("B:get_beta"),
                 type=None,
                 name=UidOp("get_beta"),
                 ports=[
                     UidPort("P:get_beta.in.intrinsic_growth_rate"),
                     UidPort("P:get_beta.in.gamma"),
                     UidPort("P:get_beta.in.susceptible"),
                     UidPort("P:get_beta.in.relative_contact_rate"),
                     UidPort("P:get_beta.out.beta")
                 ],

                 # contents
                 junctions=None,
                 wires=[
                     UidWire("W:get_beta.in.intrinsic_growth_rate>get_beta_updated_growth_rate_expr.in.intrinsic_growth_rate"),
                     UidWire("W:get_beta.in.gamma>get_beta_updated_growth_rate_expr.in.gamma"),
                     UidWire("W:get_beta_updated_growth_rate_expr.out.updated_growth_rate>get_beta_betas_exp.in.updated_growth_rate"),
                     UidWire("W:get_beta.in.susceptible>get_beta_betas_exp.in.susceptible"),
                     UidWire("W:get_beta.in.relative_contact_rate>get_beta_inv_contact_rate_exp.in.relative_contact_rate"),
                     UidWire("W:get_beta_inv_contact_rate_exp.out.inv_contact_rate>get_beta_betas_exp.in.inv_contact_rate"),
                     UidWire("W:get_beta_betas_exp.out.beta>get_beta.out.beta")
                 ],
                 boxes=[
                     UidBox("B:get_beta_updated_growth_rate_expr"),
                     UidBox("B:get_beta_inv_contact_rate_exp"),
                     UidBox("B:get_beta_betas_exp")
                 ],

                 metadata=None)

    # main_loop_1_call_get_beta_exp
    main_loop_1_call_get_beta_exp = \
        BoxCall(uid=UidBox("B:main_loop_1_call_get_beta_exp"),
                type=None,
                name=None,
                call=UidBox("B:get_beta"),
                ports=[
                    UidPort("PC:main_loop_1_call_get_beta_exp.in.growth_rate"),

                    # REMOVE_CHIME_SIR_Base
                    # UidPort("PC:main_loop_1_call_get_beta_exp.in.gamma"),

                    ### -- CHIME_SVIIvR -- START
                    UidPort("PC:main_loop_1_call_get_beta_exp.in.gamma_unvaccinated"),
                    ### -- CHIME_SVIIvR -- END

                    UidPort("PC:main_loop_1_call_get_beta_exp.in.s_n"),
                    UidPort("PC:main_loop_1_call_get_beta_exp.in.relative_contact_rate"),
                    UidPort("PC:main_loop_1_call_get_beta_exp.out.beta")
                ],
                metadata=None)

    # main_loop_1_pbetas_exp
    main_loop_1_pbetas_exp_e0 = \
        Expr(call=RefOp(UidOp('set')),
             args=[UidPort("P:main_loop_1_pbetas_exp.in.policys_betas"),
                   UidPort("P:main_loop_1_pbetas_exp.in.p_idx"),
                   UidPort("P:main_loop_1_pbetas_exp.in.beta")])
    main_loop_1_pbetas_exp = \
        Expression(uid=UidBox("B:main_loop_1_pbetas_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_loop_1_pbetas_exp.in.policys_betas"),
                          UidPort("P:main_loop_1_pbetas_exp.in.p_idx"),
                          UidPort("P:main_loop_1_pbetas_exp.in.beta"),
                          UidPort("P:main_loop_1_pbetas_exp.out.policys_betas")],
                   tree=main_loop_1_pbetas_exp_e0,
                   metadata=None)

    # main_loop_1_pdays_exp
    main_loop_1_pdays_exp_e0 = \
        Expr(call=RefOp(UidOp('*')),
             args=[UidPort("P:main_loop_1_pdays_exp.in.p_idx"),
                   UidPort("P:main_loop_1_pdays_exp.in.n_days")])
    main_loop_1_pdays_exp_e1 = \
        Expr(call=RefOp(UidOp('set')),
             args=[UidPort("P:main_loop_1_pdays_exp.in.policy_days"),
                   UidPort("P:main_loop_1_pdays_exp.in.p_idx"),
                   main_loop_1_pdays_exp_e0])
    main_loop_1_pdays_exp = \
        Expression(uid=UidBox("B:main_loop_1_pdays_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_loop_1_pdays_exp.in.policy_days"),
                          UidPort("P:main_loop_1_pdays_exp.in.p_idx"),
                          UidPort("P:main_loop_1_pdays_exp.in.n_days"),
                          UidPort("P:main_loop_1_pdays_exp.out.policy_days")],
                   tree=main_loop_1_pdays_exp_e1,
                   metadata=None)

    main_loop_1 = \
        Loop(uid=UidBox("B:main_loop_1"),
             type=None,
             name=None,
             ports=[
                 # -- "control" loop ports
                 UidPort("P:main_loop_1.in.p_idx"),
                 UidPort("P:main_loop_1.in.N_p"),
                 UidPort("PC:main_loop_1.out.p_idx"),
                 UidPort("PC:main_loop_1.out.N_p"),
                 # -- "body" loop inputs
                 UidPort("P:main_loop_1.in.s_n"),

                 # REMOVE_CHIME_SIR_Base
                 # UidPort("P:main_loop_1.in.gamma"),

                 UidPort("P:main_loop_1.in.relative_contact_rate"),
                 UidPort("P:main_loop_1.in.policys_betas"),
                 UidPort("P:main_loop_1.in.policy_days"),
                 UidPort("P:main_loop_1.in.n_days"),
                 # -- "body" loop outputs
                 UidPort("PC:main_loop_1.out.s_n"),

                 # REMOVE_CHIME_SIR_Base
                 # UidPort("PC:main_loop_1.out.gamma"),

                 UidPort("PC:main_loop_1.out.relative_contact_rate"),
                 UidPort("PC:main_loop_1.out.policys_betas"),
                 UidPort("PC:main_loop_1.out.policy_days"),
                 UidPort("PC:main_loop_1.out.n_days"),

                 ### -- CHIME_SVIIvR -- START
                 UidPort("P:main_loop_1.in.gamma_unvaccinated"),
                 UidPort("PC:main_loop_1.out.gamma_unvaccinated"),
                 ### -- CHIME_SVIIvR -- END
             ],

             exit_condition=UidBox("B:main_loop_1_cond"),

             # contents
             junctions=None,
             wires=[
                 # main_loop_1 control
                 UidWire("W:main_loop_1.in.p_idx>main_loop_1_cond.in.p_idx"),
                 UidWire("W:main_loop_1.in.N_p>main_loop_1_cond.in.N_p"),
                 UidWire("W:main_loop_1.in.p_idx>main_loop_1_p_idx_exp.in.p_idx"),
                 UidWire("W:main_loop_1_p_idx_exp.out.p_idx>main_loop_1.out.p_idx"),
                 # main_loop_1 body
                 UidWire("W:main_loop_1.in.p_idx>main_loop_1_dtime_exp.in.p_idx"),
                 UidWire("W:main_loop_1_dtime_exp.out.doubling_time>main_loop_1_call_growth_rate_exp.in.doubling_time"),
                 UidWire("W:main_loop_1_call_growth_rate_exp.out.growth_rate>main_loop_1_call_get_beta_exp.in.growth_rate"),

                 # REMOVE_CHIME_SIR_Base
                 # UidWire("W:main_loop_1.in.gamma>main_loop_1_call_get_beta_exp.in.gamma"),

                 UidWire("W:main_loop_1.in.s_n>main_loop_1_call_get_beta_exp.in.s_n"),
                 UidWire("W:main_loop_1.in.relative_contact_rate>main_loop_1_call_get_beta_exp.in.relative_contact_rate"),
                 UidWire("W:main_loop_1.in.policys_betas>main_loop_1_pbetas_exp.in.policys_betas"),
                 UidWire("W:main_loop_1.in.p_idx>main_loop_1_pbetas_exp.in.p_idx"),
                 UidWire("W:main_loop_1_call_get_beta_exp.out.beta>main_loop_1_pbetas_exp.in.beta"),
                 UidWire("W:main_loop_1_pbetas_exp.out.policys_betas>main_loop_1.out.policys_betas"),

                 UidWire("W:main_loop_1.in.policy_days>main_loop_1_pdays_exp.in.policy_days"),
                 UidWire("W:main_loop_1.in.p_idx>main_loop_1_pdays_exp.in.p_idx"),
                 UidWire("W:main_loop_1.in.n_days>main_loop_1_pdays_exp.in.n_days"),
                 UidWire("W:main_loop_1_pdays_exp.out.policy_days>main_loop_1.out.policy_days"),

                 ### -- CHIME_SVIIvR -- START
                 UidWire("W:main_loop_1.in.gamma_unvaccinated>main_loop_1_call_get_beta_exp.in.gamma_unvaccinated"),
                 ### -- CHIME_SVIIvR -- END
             ],
             boxes=[
                 # control
                 UidBox("B:main_loop_1_p_idx_exp"),
                 # body
                 UidBox("B:main_loop_1_dtime_exp"),
                 UidBox("B:main_loop_1_call_growth_rate_exp"),
                 UidBox("B:main_loop_1_call_get_beta_exp"),
                 UidBox("B:main_loop_1_pbetas_exp"),
                 UidBox("B:main_loop_1_pdays_exp")
             ],

             metadata=None)

    # main_ever_infected_exp
    main_ever_infected_exp_e0 = \
        Expr(call=RefOp(UidOp('+')),
             args=[UidPort("P:main_ever_infected_exp.in.i"),
                   ### -- CHIME_SVIIvR -- START
                   UidPort("P:main_ever_infected_exp.in.i_v"),
                   ### -- CHIME_SVIIvR -- END
                   UidPort("P:main_ever_infected_exp.in.r")])
    main_ever_infected_exp = \
        Expression(uid=UidBox("B:main_ever_infected_exp"),
                   type=None,
                   name=None,
                   ports=[UidPort("P:main_ever_infected_exp.in.i"),
                          UidPort("P:main_ever_infected_exp.in.r"),
                          UidPort("P:main_ever_infected_exp.out.E"),

                          ### -- CHIME_SVIIvR -- START
                          UidPort("P:main_ever_infected_exp.in.i_v"),
                          ### -- CHIME_SVIIvR -- END
                          ],
                   tree=main_ever_infected_exp_e0,
                   metadata=None)

    main = \
        Function(uid=UidBox("B:main"),
                 type=None,
                 name=UidOp("main"),
                 ports=[
                     UidPort("P:main.out.S"),
                     UidPort("P:main.out.I"),
                     UidPort("P:main.out.R"),
                     UidPort("P:main.out.E"),

                     ### -- CHIME_SVIIvR -- START
                     UidPort("P:main.out.V"),
                     UidPort("P:main.out.Iv"),
                     ### -- CHIME_SVIIvR -- END
                 ],

                 # contents
                 junctions=[
                     UidJunction("J:main.s_n"),
                     UidJunction("J:main.i_n"),
                     UidJunction("J:main.r_n"),
                     UidJunction("J:main.N_p"),

                     # REMOVE_CHIME_SIR_Base
                     # UidJunction("J:main.infections_days"),

                     ### -- CHIME_SVIIvR -- START
                     UidJunction("J:main.infections_days_unvaccinated"),
                     UidJunction("J:main.infections_days_vaccinated"),

                     UidJunction("J:main.v_n"),
                     UidJunction("J:main.i_v_n"),
                     UidJunction("J:main.vaccination_rate"),
                     UidJunction("J:main.vaccine_efficacy"),
                     ### -- CHIME_SVIIvR -- END

                     UidJunction("J:main.relative_contact_rate"),
                     UidJunction("J:main.n_days"),
                     UidJunction("J:main.i_day"),
                     UidJunction("J:main.p_idx")
                 ],
                 wires=[
                     UidWire("W:main.s_n>main_call_simsir.in.s_n"),
                     UidWire("W:main.s_n>main_loop_1.in.s_n"),
                     UidWire("W:main.i_n>main_call_simsir.in.i_n"),
                     UidWire("W:main.r_n>main_call_simsir.in.r_n"),
                     # REMOVE_CHIME_SIR_Base
                     # UidWire("W:main_gamma_exp.out.gamma>main_call_simsir.in.gamma"),
                     # REMOVE_CHIME_SIR_Base
                     # UidWire("W:main_gamma_exp.out.gamma>main_loop_1.in.gamma"),
                     UidWire("W:main.relative_contact_rate>main_loop_1.in.relative_contact_rate"),
                     UidWire("W:main_pbetas_seq.out.policys_betas>main_loop_1.in.policys_betas"),
                     UidWire("W:main_loop_1.out.policys_betas>main_call_simsir.in.betas"),
                     UidWire("W:main_pdays_seq.out.policy_days>main_loop_1.in.policy_days"),
                     UidWire("W:main.n_days>main_loop_1.in.n_days"),
                     UidWire("W:main_pdays_seq.out.policy_days>main_call_simsir.in.days"),
                     UidWire("W:main.N_p>main_call_simsir.in.N_p"),
                     UidWire("W:main.N_p>main_pbetas_seq.in.size"),
                     UidWire("W:main.N_p>main_pdays_seq.in.size"),
                     UidWire("W:main.N_p>main_loop_1.in.N_p"),
                     UidWire("W:main.p_idx>main_loop_1.in.p_idx"),
                     # REMOVE_CHIME_SIR_Base
                     # UidWire("W:main.infections_days>main_gamma_exp.in.infections_days"),

                     UidWire("W:main_call_simsir.out.i_n>main_ever_infected_exp.in.i"),
                     UidWire("W:main_call_simsir.out.r_n>main_ever_infected_exp.in.r"),
                     UidWire("W:main_ever_infected_exp.out.E>main.out.E"),

                     UidWire("W:main_call_simsir.out.s_n>main.out.S"),
                     UidWire("W:main_call_simsir.out.i_n>main.out.I"),
                     UidWire("W:main_call_simsir.out.r_n>main.out.R"),

                     ### -- CHIME_SVIIvR -- START
                     # TODO HERE main wires
                     UidWire("W:main.infections_days_unvaccinated>main_gamma_unvaccinated_exp.in.infections_days_unvaccinated"),
                     UidWire("W:main_gamma_unvaccinated_exp.out.gamma_unvaccinated>main_loop_1.in.gamma_unvaccinated"),
                     UidWire("W:main.infections_days_vaccinated>main_gamma_vaccinated_exp.in.infections_days_vaccinated"),

                     UidWire("W:main.v_n>main_call_simsir.in.v_n"),
                     UidWire("W:main.i_v_n>main_call_simsir.in.i_v_n"),
                     UidWire("W:main.vaccination_rate>main_call_simsir.in.vaccination_rate"),
                     UidWire("W:main.vaccine_efficacy>main_call_simsir.in.vaccine_efficacy"),
                     UidWire("W:main_gamma_unvaccinated_exp.out.gamma_unvaccinated>main_call_simsir.in.gamma_unvaccinated"),
                     UidWire("W:main_gamma_vaccinated_exp.out.gamma_vaccinated>main_call_simsir.in.gamma_vaccinated"),

                     UidWire("W:main_call_simsir.out.i_v>main_ever_infected_exp.in.i_v"),
                     UidWire("W:main_call_simsir.out.i_v>main.out.Iv"),
                     UidWire("W:main_call_simsir.out.v>main.out.V"),
                     ### -- CHIME_SVIIvR -- END
                 ],
                 boxes=[
                     # UidBox("B:main_gamma_exp"),

                     ### -- CHIME_SVIIvR -- START
                     UidBox("B:main_gamma_vaccinated_exp"),
                     UidBox("B:main_gamma_unvaccinated_exp"),
                     ### -- CHIME_SVIIvR -- END

                     UidBox("B:main_pbetas_seq"),
                     UidBox("B:main_pdays_seq"),
                     UidBox("B:main_loop_1"),
                     UidBox("B:main_call_simsir"),
                     UidBox("B:main_ever_infected_exp")
                 ],

                 metadata=None)

    wires = wires_main + wires_main_loop_1 + wires_simsir + wires_simsir_loop_1 + wires_simsir_loop_1_1 + wires_sir

    ports = ports_main + ports_main_loop_1 + ports_simsir + ports_simsir_loop_1 + ports_simsir_loop_1_1 + ports_sir

    junctions = junctions_main + junctions_simsir + junctions_simsir_loop_1

    boxes = [
        main,
        # REMOVE_CHIME_SIR_Base: main_gamma_exp,

        ### -- CHIME_SVIIvR -- START
        main_gamma_vaccinated_exp, main_gamma_unvaccinated_exp,
        ### -- CHIME_SVIIvR -- END

        main_pbetas_seq, main_pdays_seq,
        main_loop_1, main_loop_1_cond, main_loop_1_p_idx_exp,
        main_loop_1_dtime_exp, main_loop_1_call_growth_rate_exp,
        main_loop_1_call_get_beta_exp, main_loop_1_pbetas_exp, main_loop_1_pdays_exp,
        main_call_simsir,
        main_ever_infected_exp,

        get_growth_rate,
        get_beta, get_beta_updated_growth_rate_expr, get_beta_inv_contact_rate_exp, get_beta_betas_exp,

        simsir,
        simsir_n_exp,
        simsir_loop_1_range_init_exp, simsir_loop_1_get_p_idx_init_exp,

        simsir_loop_1,
        simsir_loop_1_cond, simsir_loop_1_i_exp, simsir_loop_1_get_p_idx_exp,
        simsir_loop_1_n_days_exp, simsir_loop_1_get_beta_exp,
        simsir_loop_1_1_range_init_exp, simsir_loop_1_1_get_d_idx_init_exp,

        simsir_loop_1_1,
        simsir_loop_1_1_cond, simsir_loop_1_1_i_exp, simsir_loop_1_1_get_d_idx_exp,
        simsir_loop_1_1_call_sir_exp,

        sir,
        sir_s_n_exp, sir_i_n_exp, sir_r_n_exp,
        sir_scale_exp,
        sir_s_exp, sir_i_exp, sir_r_exp,

        ### -- CHIME_SVIIvR -- START
        sir_v_n_exp, sir_i_v_n_exp,
        sir_v_exp, sir_i_v_exp,
        ### -- CHIME_SVIIvR -- END

    ]

    variables = variables_sir

    _g = Gromet(
        uid=UidGromet("CHIME_SVIIvR"),
        name="CHIME_SVIIvR",
        type=UidType("FunctionNetwork"),
        root=UidBox("B:main"),
        types=None,
        literals=None,
        junctions=junctions,
        ports=ports,
        wires=wires,
        boxes=boxes,
        variables=variables,
        metadata=[chime_model_description,
                  chime_model_interface,
                  metadatum_code_collection_ref,
                  metadatum_textual_document_reference_set]
    )

    return _g


# -----------------------------------------------------------------------------
# Script
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    gromet_to_json(generate_gromet())
