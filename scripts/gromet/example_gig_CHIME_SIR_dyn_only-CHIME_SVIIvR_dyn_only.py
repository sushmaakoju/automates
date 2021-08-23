import gromet_intersection_graph as ig


# -----------------------------------------------------------------------------
# GroMEt instance
# -----------------------------------------------------------------------------


def generate_gig() -> GrometIntersectionGraph:

    # TODO: implement correct nodes based off of this guide
    common_nodes = [
        ig.CommonNode(
            uid=ig.UidCommonNode("S_in"),
            # type='input',
            g1_variable=[ig.UidVariable("S")],
            g2_variable=[ig.UidVariable("V:sir.s_in")],
        ),
        ig.CommonNode(
            uid=ig.UidCommonNode("S_out"),
            # type='output',
            g1_variable=[ig.UidVariable("S_2")],
            g2_variable=[ig.UidVariable("V:sir.s_out")],
        ),
    ]

    # TODO: implement correct nodes based off of this guide
    oap_nodes = [
        ig.OAPNode(
            uid=ig.UidCommonNode("OAP_1"),
            g1_variables=[
                ig.UidVariable("infected"),
                ig.UidVariable("recovered"),
                ig.UidVariable("dt"),
            ],
            g2_variables=[
                ig.UidVariable("V:sir.n"),
                ig.UidVariable("V:sir.s_n"),
                ig.UidVariable("V:sir.i_n"),
                ig.UidVariable("V:sir.r_n"),
                ig.UidVariable("V:sir.scale"),
            ],
        ),
    ]

    edges = [
        ig.Edge(
            type="no_overlap",
            src=ig.UidCommonNode("S_in"),
            dst=ig.UidCommonNode("OAP_1"),
        ),
    ]

    # TODO: Check the attrs of this object
    gromet_ids = ig.GrometIds(
        g1_name="CHIME_SIR_v01",
        g1_uid=ig.UidGromet("CHIME_SIR"),
        g2_name="CHIME_SVIIvR_v01",
        g2_uid=ig.UidGromet("CHIME_SVIIvR"),
    )

    # TODO: Check the attrs of this object
    gig = ig.GrometIntersectionGraph(
        uid=ig.UidIntersectionGraph("GIG.CHIME_SIR_v01<->CHIME_SVIIvR_v01"),
        gromet_ids=gromet_ids,
        common_nodes=common_nodes,
        oap_nodes=oap_nodes,
        noap_nodes=None,
        edges=edges,
    )

    return gig


# -----------------------------------------------------------------------------
# Script
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    ig.gig_to_json(generate_gig())
