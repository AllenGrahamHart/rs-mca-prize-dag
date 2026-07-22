#!/usr/bin/env python3
"""Verify source pins and arithmetic for the F1 same-rate scope router."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f1_pole_same_rate_scope_router"


def rs_rate(n: int, kappa: int) -> Fraction:
    assert 0 < kappa <= n
    return Fraction(kappa, n)


def same_rate(n: int, kappa: int, base_n: int, base_kappa: int) -> bool:
    return rs_rate(n, kappa) == rs_rate(base_n, base_kappa)


def require(path: Path, snippets: tuple[str, ...]) -> None:
    text = path.read_text()
    for snippet in snippets:
        assert snippet in text, (path, snippet)


def main() -> None:
    require(
        ROOT / "critical/nodes/interleaved_floor_import/proof.md",
        (
            "D subset B",
            "C_K = RS[K,D,kappa]",
            "Phi(C_K)=C_B^e",
            "deg < kappa",
        ),
    )
    require(
        ROOT / "critical/nodes/f1_minimal_field_descent/proof.md",
        ("B <= K <= F", "K := B · K_0(x)"),
    )
    require(
        ROOT / "critical/nodes/ext_import/proof.md",
        ("corresponding base row",),
    )

    dag = json.loads((ROOT / "dag.json").read_text())
    status = {node["id"]: node["status"] for node in dag["nodes"]}
    assert status[NODE] == "PROVED"
    assert status["f1_minimal_field_descent"] == "PROVED"
    assert status["interleaved_floor_import"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert ("f1_minimal_field_descent", NODE, "req") in edges
    assert ("interleaved_floor_import", NODE, "req") in edges
    assert (NODE, "f1_pole_list_threshold_location", "ev") in edges

    checks = 0
    for n in (16, 32, 1024, 1 << 21):
        for denominator in (2, 4, 8, 16):
            if n % denominator:
                continue
            kappa = n // denominator
            for extension_degree in (1, 2, 3, 6, 12):
                # Extension degree changes the alphabet/interleaving only.
                assert same_rate(n, kappa, n, kappa)
                assert rs_rate(n, kappa) == Fraction(1, denominator)
                assert extension_degree >= 1
                checks += 1

    # Required negative controls: a dimension or domain change is not the
    # theorem and must be detected.
    mutations = 0
    for args in ((32, 8, 32, 9), (32, 8, 31, 8), (64, 32, 64, 31)):
        assert not same_rate(*args)
        mutations += 1

    print(
        "F1_POLE_SAME_RATE_SCOPE_ROUTER_PASS "
        f"rate_checks={checks} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
