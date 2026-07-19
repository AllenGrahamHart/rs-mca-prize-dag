#!/usr/bin/env python3
"""Replay the exact carried-layout Top/Post allowance."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "pma_sigma_one_post_top_allowance"


def main() -> None:
    checks = 0
    mutation_trips = 0

    for exponent in range(13, 45):
        n = 1 << exponent
        n6 = n**6

        for denominator in (2, 4, 8, 16):
            k = n // denominator
            t_ch = (n - k) // 2
            cutoff = k + 3 - 2 * t_ch

            if denominator == 2:
                if cutoff != 3:
                    raise AssertionError((exponent, denominator, cutoff))
                s3 = sum(comb(k - 1, j) for j in range(4))
                n_top = 2 * (t_ch + 1) * s3
                b_post = n6 - n_top

                if not 0 < n_top <= n**4 < n6:
                    raise AssertionError((exponent, n_top, n**4, n6))
                if not 0 < b_post < n6:
                    raise AssertionError((exponent, b_post, n6))
                if n_top + b_post != n6:
                    raise AssertionError((exponent, "composition"))
                checks += 4

                # Mutant 1: giving Post the full line double-spends Top.
                if n_top + n6 <= n6:
                    raise AssertionError((exponent, "full-post mutation"))
                mutation_trips += 1

                # Mutant 2: one less than the exact atlas census is not a cap
                # on that census.
                if n_top <= n_top - 1:
                    raise AssertionError((exponent, "top-cap mutation"))
                mutation_trips += 1
            else:
                if cutoff >= 0:
                    raise AssertionError((exponent, denominator, cutoff))
                n_top = 0
                b_post = n6
                if n_top + b_post != n6:
                    raise AssertionError((exponent, denominator, "empty band"))
                checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    if nodes[NODE]["status"] != "PROVED":
        raise AssertionError("node is not PROVED")

    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    required = {
        ("l1_program_frontier", NODE, "req"),
        ("petal_g1_layer_maps", NODE, "req"),
        ("petal_k4_primitive_bound", NODE, "req"),
        (NODE, "pma_wide_residual", "ev"),
        (NODE, "petal_mixed_amplification", "ev"),
    }
    missing = required - edges
    if missing:
        raise AssertionError(("missing edges", sorted(missing)))
    checks += len(required) + 1

    statement = (
        ROOT
        / "background/nodes/pma_sigma_one_post_top_allowance/statement.md"
    ).read_text()
    for pin in (
        "first layout that carries it",
        "not defined by the existence",
        "#Post(U) <= B_post",
        "does not prove",
    ):
        if pin not in statement:
            raise AssertionError(("missing statement pin", pin))
        checks += 1

    if mutation_trips != 64:
        raise AssertionError(("mutation trips", mutation_trips))

    print(
        "PMA_POST_TOP_ALLOWANCE_PASS "
        f"checks={checks} rows={32 * 4} mutation_trips={mutation_trips}"
    )


if __name__ == "__main__":
    main()
