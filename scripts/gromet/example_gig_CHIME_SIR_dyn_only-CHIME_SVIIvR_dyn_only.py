import gromet_intersection_graph as ig


# -----------------------------------------------------------------------------
# GroMEt instance
# -----------------------------------------------------------------------------


def generate_gig() -> ig.GrometIntersectionGraph:
    chime_sir_name = "CHIME_SIR"
    chime_sviivr_name = "CHIME_SVIIvR"
    ver_chime_sir_name = f"{chime_sir_name}_v01"
    ver_chime_sviivr_name = f"{chime_sviivr_name}_v01"
    gig_uid_str = f"{ver_chime_sir_name}<->{ver_chime_sviivr_name}"

    # TODO: implement correct nodes based off of this guide
    common_nodes = [
        ig.CommonNode(
            uid=ig.UidCommonNode("S_in"),
            # type='input',
            g1_variable=[ig.UidVariable("V:sir.s_in")],
            g2_variable=[ig.UidVariable("V:sir.s_in")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("I_in"),
            # type='input',
            g1_variable=[ig.UidVariable("V:sir.i_in")],
            g2_variable=[ig.UidVariable("V:sir.i_in")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("R_in"),
            # type='input',
            g1_variable=[ig.UidVariable("V:sir.r_in")],
            g2_variable=[ig.UidVariable("V:sir.r_in")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("beta"),
            # type='input',
            g1_variable=[ig.UidVariable("V:sir.beta")],
            g2_variable=[ig.UidVariable("V:sir.beta")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("gamma"),
            # type='input',
            g1_variable=[ig.UidVariable("V:sir.gamma")],
            g2_variable=[ig.UidVariable("V:sir.gamma")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("n"),
            # type='input',
            g1_variable=[ig.UidVariable("V:sir.n")],
            g2_variable=[ig.UidVariable("V:sir.n")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("scale"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:sir.scale")],
            g2_variable=[ig.UidVariable("V:sir.scale")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("S_n"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:sir.s_n")],
            g2_variable=[ig.UidVariable("V:sir.s_n")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("I_n"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:sir.i_n")],
            g2_variable=[ig.UidVariable("V:sir.i_n")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("R_n"),
            # type='internal',
            g1_variable=[ig.UidVariable("V:sir.r_n")],
            g2_variable=[ig.UidVariable("V:sir.r_n")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("S_out"),
            # type='output',
            g1_variable=[ig.UidVariable("V:sir.s_out")],
            g2_variable=[ig.UidVariable("V:sir.s_out")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("I_out"),
            # type='output',
            g1_variable=[ig.UidVariable("V:sir.i_out")],
            g2_variable=[ig.UidVariable("V:sir.i_out")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("R_out"),
            # type='output',
            g1_variable=[ig.UidVariable("V:sir.r_out")],
            g2_variable=[ig.UidVariable("V:sir.r_out")],
        ),
    ]

    oap_nodes = []

    noap_nodes = [
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_1"),
            gromet_name=ver_chime_sviivr_name,
            variables=[
                ig.UidVariable("V:sir.v_r"),
                ig.UidVariable("V:sir.v_s"),
                ig.UidVariable("V:sir.v"),
                ig.UidVariable("V:sir.i_v"),
            ],
        ),
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_2"),
            gromet_name=ver_chime_sviivr_name,
            variables=[
                ig.UidVariable("V:sir.v_n"),
                ig.UidVariable("V:sir.i_v_n"),
            ],
        ),
        ig.NOAPNode(
            uid=ig.UidCommonNode("NOAP_3"),
            gromet_name=ver_chime_sviivr_name,
            variables=[
                ig.UidVariable("V:sir.v"),
                ig.UidVariable("V:sir.i_v"),
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
            dst=ig.UidCommonNode("NOAP_2"),
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
            dst=ig.UidCommonNode("NOAP_2"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("R_in"),
            dst=ig.UidCommonNode("R_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("gamma"),
            dst=ig.UidCommonNode("I_n"),
        ),
        ig.Edge(
            type="g1_subset_g2",
            src=ig.UidCommonNode("gamma"),
            dst=ig.UidCommonNode("R_n"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("gamma"),
            dst=ig.UidCommonNode("NOAP_2"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_1"),
            dst=ig.UidCommonNode("NOAP_2"),
        ),
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("NOAP_1"),
            dst=ig.UidCommonNode("S_n"),
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
            dst=ig.UidCommonNode("NOAP_3"),
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
            src=ig.UidCommonNode("NOAP_2"),
            dst=ig.UidCommonNode("NOAP_3"),
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
