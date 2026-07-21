#!/usr/bin/env python3
"""Verify the DSP8 nodal trace-orbit energy router."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_trace_orbit_energy_router"
DEPENDENCIES = {
    "f3_h3_dsp8_nodal_trace_parameter_router",
    "f3_h3_dsp8_nodal_cube_preimage_envelope",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def orbit_and_fourier_check() -> None:
    for n0 in range(0, 61, 6):
        for n1 in range(0, 61, 6):
            for n2 in range(0, 61, 6):
                counts = (n0, n1, n2)
                total = sum(counts)
                sum_squares = sum(value * value for value in counts)
                pair_sum = n0 * n1 + n0 * n2 + n1 * n2
                bias_square = sum_squares - pair_sum
                energy = sum(value * (value - 6) for value in counts)
                assert 3 * sum_squares == total * total + 2 * bias_square
                assert energy == (total * total + 2 * bias_square) // 3 - 6 * total
                assert energy >= 0


def constants_check() -> None:
    coefficient = Fraction(867, 16)
    allowance = Fraction(76599, 40)
    energy_cap = Fraction(51066, 1445)
    assert coefficient * energy_cap == allowance

    sparse_cap = Fraction(59, 10) ** 2
    assert sparse_cap == Fraction(3481, 100)
    assert energy_cap - sparse_cap == Fraction(15311, 28900)
    assert coefficient * sparse_cap == Fraction(3018027, 1600)
    assert allowance - coefficient * sparse_cap == Fraction(45933, 1600)

    three_root_point_cap = Fraction(51, 16) * Fraction(2081, 1000)
    assert three_root_point_cap == Fraction(106131, 16000)
    assert three_root_point_cap > Fraction(59, 10)

    assert Fraction(1 + 2 * Fraction(4, 5) ** 2, 3) == Fraction(19, 25)
    assert 1443**3 == 3004685307
    assert 1443**3 > 3 * 1000**3
    routed = (
        17
        * Fraction(51, 16) ** 3
        * Fraction(19, 25)
        * Fraction(4329, 1000)
    )
    assert routed == Fraction(185481515817, 102400000)
    assert routed < 1812
    margin = allowance - routed
    assert margin == Fraction(10611924183, 102400000)
    assert margin > 103


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "E_tr=sum_(c^3=1)N_c(N_c-6)",
        "<(867/16)n^(2/3)E_tr",
        "E_tr=(N^2+2|S|^2)/3-6N",
        "E_tr<=(51066/1445)n^(4/3)",
        "N<=(59/10)n^(2/3)",
        "(59/10)n^(2/3)<N<(106131/16000)n^(2/3)",
        "|S|<=4N/5",
        "doesnotprove`(NTE6)`outside`(NTE6a)`",
    ):
        assert marker in statement


def main() -> None:
    orbit_and_fourier_check()
    constants_check()
    packet_check()
    print("F3_H3_DSP8_NODAL_TRACE_ORBIT_ENERGY_ROUTER_PASS cells=1331")


if __name__ == "__main__":
    main()
