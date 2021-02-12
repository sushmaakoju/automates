import pytest
import os

import numpy as np
import networkx as nx

from automates.model_assembly.interpreter import ImperativeInterpreter
from automates.model_assembly.networks import GroundedFunctionNetwork
from automates.model_assembly.structures import GenericIdentifier


@pytest.mark.skip("Need to handle constants in function call")
def test_mini_pet():
    ITP = ImperativeInterpreter.from_src_dir("tests/data/model_analysis")
    assert hasattr(ITP, "containers")
    assert hasattr(ITP, "variables")
    assert hasattr(ITP, "types")
    assert hasattr(ITP, "documentation")
    ITP.gather_container_stats()
    ITP.label_container_code_types()
    grfns = ITP.build_GrFNs()
    grfn_list = list(grfns.keys())
    # TODO Adarsh: fill this list out
    expected_grfns = sorted(["PETPT", "PETASCE", "PSE", "FLOOD_EVAP"])
    assert sorted(grfn_list) == expected_grfns


def test_pet_files():
    def interpreter_test(filepath, con_name, outfile):
        ITP = ImperativeInterpreter.from_src_file(filepath)
        con_id = GenericIdentifier.from_str(con_name)

        G = GroundedFunctionNetwork.from_AIR(
            con_id, ITP.containers, ITP.variables, ITP.types, []
        )

        A = G.to_AGraph()
        A.draw(outfile, prog="dot")
        return G

    G = interpreter_test(
        "tests/data/program_analysis/PETASCE_simple.for",
        "@container::PETASCE_simple::@global::petasce",
        "PETASCE--GrFN.pdf",
    )

    assert isinstance(G, GroundedFunctionNetwork)
    assert len(G.inputs) == 22
    assert len(G.outputs) == 1

    values = {
        "doy": np.array([20.0], dtype=np.float32),
        "meevp": np.array(["A"], dtype=np.str),
        "msalb": np.array([0.5], dtype=np.float32),
        "srad": np.array([15.0], dtype=np.float32),
        "tmax": np.array([10.0], dtype=np.float32),
        "tmin": np.array([-10.0], dtype=np.float32),
        "xhlai": np.array([10.0], dtype=np.float32),
        "tdew": np.array([20.0], dtype=np.float32),
        "windht": np.array([5.0], dtype=np.float32),
        "windrun": np.array([450.0], dtype=np.float32),
        "xlat": np.array([45.0], dtype=np.float32),
        "xelev": np.array([3000.0], dtype=np.float32),
        "canht": np.array([2.0], dtype=np.float32),
    }

    outputs = G(values)
    res = outputs["eo"][0]
    assert res == np.float(1.3980657068634232)

    G.to_json_file("tmp/ASCE_GrFN.json")
    G2 = GroundedFunctionNetwork.from_json("tmp/ASCE_GrFN.json")
    assert G2 == G

    outputs = G2(values)
    res2 = outputs["eo"][0]
    assert res == res2


def test_single_file_analysis():
    ITP = ImperativeInterpreter.from_src_file("tests/data/program_analysis/PETPNO.for")
    petpno_con_id = GenericIdentifier.from_str("@container::PETPNO::@global::petpno")

    PNO_GrFN = GroundedFunctionNetwork.from_AIR(
        petpno_con_id, ITP.containers, ITP.variables, ITP.types, []
    )
    assert isinstance(PNO_GrFN, GroundedFunctionNetwork)

    A = PNO_GrFN.to_AGraph()
    A.draw("PETPNO--GrFN.pdf", prog="dot")

    PNO_GrFN.to_json_file("tmp/PNO_GrFN.json")
    G = GroundedFunctionNetwork.from_json("tmp/PNO_GrFN.json")
    assert G == PNO_GrFN


def test_file_with_loops():
    ITP = ImperativeInterpreter.from_src_file(
        "tests/data/program_analysis/SIR-Gillespie-SD.f"
    )
    con_id = GenericIdentifier.from_str("@container::SIR-Gillespie-SD::@global::main")
    G = GroundedFunctionNetwork.from_AIR(
        con_id, ITP.containers, ITP.variables, ITP.types, []
    )
    A = G.to_AGraph()
    A.draw("Gillespie-SD--GrFN.pdf", prog="dot")
    assert isinstance(G, GroundedFunctionNetwork)

    G.to_json_file("tmp/Gillespie_GrFN.json")
    G2 = GroundedFunctionNetwork.from_json("tmp/Gillespie_GrFN.json")
    assert G == G2


def test_petpt():
    ITP = ImperativeInterpreter.from_src_file("tests/data/program_analysis/PETPT.for")
    con_id = GenericIdentifier.from_str("@container::PETPT::@global::petpt")

    G = GroundedFunctionNetwork.from_AIR(
        con_id, ITP.containers, ITP.variables, ITP.types, []
    )
    assert isinstance(G, GroundedFunctionNetwork)
    A = G.to_AGraph()
    A.draw("PETPT--GrFN.pdf", prog="dot")
    assert len(G.inputs) == 5
    assert len(G.outputs) == 1


@pytest.mark.skip("Not testing FIBs yet")
def test_FIB_formation():
    petpno_fib = ForwardInfluenceBlanket.from_GrFN(petpno_grfn, petpen_grfn)
    CAG = petpno_fib.CAG_to_AGraph()
    CAG.draw("PETPNO_FIB--CAG.pdf", prog="dot")
    os.remove("PETPNO_FIB--CAG.pdf")


def test_crop_yield_creation():
    ITP = ImperativeInterpreter.from_src_file(
        "tests/data/program_analysis/crop_yield.f"
    )
    con_id = GenericIdentifier.from_str("@container::crop_yield::@global::crop_yield")

    G = GroundedFunctionNetwork.from_AIR(
        con_id, ITP.containers, ITP.variables, ITP.types, []
    )
    assert isinstance(G, GroundedFunctionNetwork)
