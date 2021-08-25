import gromet_intersection_graph as ig


# -----------------------------------------------------------------------------
# GroMEt instance
# -----------------------------------------------------------------------------


def generate_gig() -> ig.GrometIntersectionGraph:
    chime_sir_name = "CHIME_SIR_Base"
    chime_sviivr_name = "CHIME_SVIIvR"
    ver_chime_sir_name = f"{chime_sir_name}_v01"
    ver_chime_sviivr_name = f"{chime_sviivr_name}_v01"
    gig_uid_str = f"{ver_chime_sir_name}<->{ver_chime_sviivr_name}"

    # TODO: implement correct nodes based off of this guide
    common_nodes = [
        ig.CommonNode(
            uid=ig.UidCommonNode("S_in"),
            # type='input',
            g1_variable=[ig.UidVariable("V:s_6")],
            g2_variable=[ig.UidVariable("V:s_6")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("I_in"),
            # type='input',
            g1_variable=[ig.UidVariable("V:i_6")],
            g2_variable=[ig.UidVariable("V:i_6")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("R_in"),
            # type='input',
            g1_variable=[ig.UidVariable("V:r_7")],
            g2_variable=[ig.UidVariable("V:r_7")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("beta"),
            # type='input',
            g1_variable=[ig.UidVariable("V:beta_4")],
            g2_variable=[ig.UidVariable("V:beta_4")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("n"),
            # type='input',
            g1_variable=[ig.UidVariable("V:n_2")],
            g2_variable=[ig.UidVariable("V:n_2")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("scale"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:scale")],
            g2_variable=[ig.UidVariable("V:scale")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("S_n"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:s_n_2")],
            g2_variable=[ig.UidVariable("V:s_n_2")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("I_n"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:i_n_1")],
            g2_variable=[ig.UidVariable("V:i_n_1")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("R_n"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:r_n_1")],
            g2_variable=[ig.UidVariable("V:r_n_1")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("S_out"),
            # type='output',
            g1_variable=[ig.UidVariable("V:s_7")],
            g2_variable=[ig.UidVariable("V:s_7")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("I_out"),
            # type='output',
            g1_variable=[ig.UidVariable("V:i_7")],
            g2_variable=[ig.UidVariable("V:i_7")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("R_out"),
            # type='output',
            g1_variable=[ig.UidVariable("V:r_8")],
            g2_variable=[ig.UidVariable("V:r_8")],
        ),
    ]

    oap_nodes = []

    noap_nodes = [
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_1"),
            gromet_name=ver_chime_sir_name,
            variables=[
                ig.UidVariable("V:gamma_6"),
            ],
        ),
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_2"),
            gromet_name=ver_chime_sviivr_name,
            variables=[
                ig.UidVariable("V:vaccination_rate_4"),
                ig.UidVariable("V:vaccination_efficacy"),
                ig.UidVariable("V:v_6"),
                ig.UidVariable("V:i_v_6"),
                ig.UidVariable("V:gamma_vaccinated_4"),
                ig.UidVariable("V:gamma_unvaccinated_5"),
            ],
        ),
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_3"),
            gromet_name=ver_chime_sviivr_name,
            variables=[
                ig.UidVariable("V:v_n_1"),
                ig.UidVariable("V:i_v_n_1"),
            ],
        ),
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_4"),
            gromet_name=ver_chime_sviivr_name,
            variables=[
                ig.UidVariable("V:v_7"),
                ig.UidVariable("V:i_v_7"),
            ],
        ),
    ]

    edges = [
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("n"),
            dst=ig.UidCommonNode("scale"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("beta"),
            dst=ig.UidCommonNode("S_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("beta"),
            dst=ig.UidCommonNode("I_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("S_in"),
            dst=ig.UidCommonNode("S_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("S_in"),
            dst=ig.UidCommonNode("I_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("S_in"),
            dst=ig.UidCommonNode("NOAP_3"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("I_in"),
            dst=ig.UidCommonNode("S_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("I_in"),
            dst=ig.UidCommonNode("I_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("I_in"),
            dst=ig.UidCommonNode("R_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("I_in"),
            dst=ig.UidCommonNode("NOAP_3"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("R_in"),
            dst=ig.UidCommonNode("R_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_1"),
            dst=ig.UidCommonNode("I_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_1"),
            dst=ig.UidCommonNode("R_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_2"),
            dst=ig.UidCommonNode("NOAP_3"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_2"),
            dst=ig.UidCommonNode("S_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_2"),
            dst=ig.UidCommonNode("I_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_2"),
            dst=ig.UidCommonNode("R_n"),
        ),
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("scale"),
            dst=ig.UidCommonNode("S_out"),
        ),
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("scale"),
            dst=ig.UidCommonNode("I_out"),
        ),
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("scale"),
            dst=ig.UidCommonNode("R_out"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("scale"),
            dst=ig.UidCommonNode("NOAP_4"),
        ),
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("S_n"),
            dst=ig.UidCommonNode("S_out"),
        ),
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("I_n"),
            dst=ig.UidCommonNode("I_out"),
        ),
        ig.Edge(
            type="equal",
            src=ig.UidCommonNode("R_n"),
            dst=ig.UidCommonNode("R_out"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_3"),
            dst=ig.UidCommonNode("NOAP_4"),
        ),
    ]

    # TODO: Check the attrs of this object
    gromet_ids = ig.GrometIds(
        g1_name=ver_chime_sir_name,
        g1_uid=ig.UidGromet(chime_sir_name),
        g2_name=ver_chime_sviivr_name,
        g2_uid=ig.UidGromet(chime_sviivr_name),
    )

    return ig.GrometIntersectionGraph(
        uid=ig.UidIntersectionGraph(gig_uid_str),
        gromet_ids=gromet_ids,
        common_nodes=common_nodes,
        oap_nodes=oap_nodes,
        noap_nodes=noap_nodes,
        edges=edges,
    )


# -----------------------------------------------------------------------------
# Script
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    ig.gig_to_json(generate_gig())
