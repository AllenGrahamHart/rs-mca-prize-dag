#!/usr/bin/env python3
"""Verify Mattarei prime-subfield descent and deployed-row arithmetic."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_affine_coset_pair_prime_subfield_descent"
DEPENDENCY = "f3_affine_coset_pair_mattarei_bound"
CONSUMER = "f3_h3_dsp8_correlation_bound"


def valuation_two(value: int) -> int:
    answer = 0
    while value % 2 == 0:
        answer += 1
        value //= 2
    return answer


def arithmetic_check() -> None:
    p = 2**31 - 2**24 + 1
    n = 2**21
    assert p == 2130706433
    assert p - 1 == 127 * 2**24
    assert (p - 1) % n == 0
    index = (p - 1) // n
    assert index == 1016
    assert index**3 == 1048772096
    assert index**3 > 4 * n
    assert p % 3 == 2

    mersenne = 2**31 - 1
    assert valuation_two(mersenne - 1) == 1
    assert (mersenne - 1) % n != 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    text = "".join(
        "".join((base / name).read_text().replace("`", "").split())
        for name in ("statement.md", "proof.md", "audit.md")
    )
    for marker in (
        "{xinF_q:L_1(x),L_2(x)inK}={xinF_p:L_1(x),L_2(x)inK}",
        "1016^3=1048772096>4n",
        "p=2(mod3)",
        "v_2(p_M-1)=1",
        "descent,notanextension",
    ):
        assert marker in text, marker


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_AFFINE_COSET_PAIR_PRIME_SUBFIELD_DESCENT_PASS "
        "koalabear_index=1016 cube_preimage=n mersenne_v2=1"
    )


if __name__ == "__main__":
    main()
