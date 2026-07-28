#!/usr/bin/env python3
"""Verify the exact E1 class-pair/folded-kernel dictionary."""

from __future__ import annotations

import hashlib
import json
from functools import cache
from itertools import product
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_low_square_mass_weighted_kernel_dictionary"
TARGET = "e1_official_low_square_mass_pair_budget"

ROWS = (
    ("RowC 1/4", 256, 128, 65, 16, 15,
     2132541774042092125849554674828524585055987163412031204420185928301781984965,
     1090, (3, 4, 16),
     2899001011559056192880793575925270505545118720240019736,
     1471225270732300083690),
    ("RowC 1/8", 256, 128, 33, 16, 15,
     5198328219133082279450279571536097879858211,
     275, (3, 4, 16), 4550972295647251657752808370587724056,
     2284491),
    ("RowC 1/16", 512, 256, 33, 4, 4,
     34251385177613611176287134568778412711317979539714751534312745145,
     301, (0, 4, 4), 69817906094980867044033802642511381589872306283912,
     981163346005184),
    ("prize 1/4", 256, 128, 65, 18, 15,
     35712526268255974159379339912208386438781917770706964119574629107623252261,
     1086, (4, 2, 18),
     1621868867923804840915753105221596984497856637426519762,
     44038734542050218762),
    ("prize 1/8", 256, 128, 33, 18, 15,
     62622678770648913918718317914905517790930,
     271, (4, 2, 18), 1873053318886373426584792000465260242,
     66866),
    ("prize 1/16", 512, 256, 33, 6, 4,
     573589463880641840437695913758879780711186889526196156445743653,
     300, (1, 2, 6), 25912134061920884044549116258313478062341656144934,
     44271881467575),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@cache
def multiplicity(h: int, ell: int, a: int, b: int) -> int:
    n0 = h - a - b
    if n0 < 0:
        return 0
    T = min(ell, 2 * h - ell)
    total = 0
    for j in range(b + 1):
        for r in range(n0 + 1):
            tx = a + j + r
            ty = a + b - j + r
            if tx <= T and ty <= T and (tx - ell) % 2 == 0 and (ty - ell) % 2 == 0:
                total += comb(b, j) * comb(n0, r) * 2**r
    return total


def direct_small_model(h: int, ell: int) -> dict[tuple[int, ...], int]:
    T = min(ell, 2 * h - ell)
    classes = []
    for x in product((-1, 0, 1), repeat=h):
        t = sum(v != 0 for v in x)
        if t <= T and (t - ell) % 2 == 0:
            classes.append(x)
    counts: dict[tuple[int, ...], int] = {}
    for x in classes:
        for y in classes:
            d = tuple(vx - vy for vx, vy in zip(x, y))
            if any(d):
                counts[d] = counts.get(d, 0) + 1
    return counts


def main() -> None:
    checks = 0

    # Direct class-pair enumeration tests the formula independently at small h.
    for h, ell in ((4, 2), (5, 3)):
        counts = direct_small_model(h, ell)
        for d, actual in counts.items():
            a = sum(abs(v) == 2 for v in d)
            b = sum(abs(v) == 1 for v in d)
            assert multiplicity(h, ell, a, b) == actual
            assert counts[tuple(-v for v in d)] == actual
            checks += 2

    for (name, N, h, ell, d0, even_a_min, edge_cap,
         expected_count, expected_profile, expected_max, expected_vector_cap) in ROWS:
        eligible = []
        for a in range(h + 1):
            for b in range(h - a + 1):
                S = 4 * a + b
                if not 0 < S <= 2 * ell:
                    continue
                if not ((b > 0 and S >= d0) or (b == 0 and a >= even_a_min)):
                    continue
                weight = multiplicity(h, ell, a, b)
                if weight:
                    eligible.append((weight, a, b, S))
        maximum, a, b, S = max(eligible)
        vector_cap = 2 * edge_cap // maximum
        assert len(eligible) == expected_count, name
        assert (a, b, S) == expected_profile, name
        assert maximum == expected_max, name
        assert vector_cap == expected_vector_cap, name
        assert maximum * vector_cap <= 2 * edge_cap, name
        assert maximum * (vector_cap + 1) > 2 * edge_cap, name
        checks += 6

    pins = json.loads((Path(__file__).with_name("source_pin.json")).read_text())
    for file_key, hash_key in (
        ("square_mass_statement_file", "square_mass_statement_sha256"),
        ("norm_radius_statement_file", "norm_radius_statement_sha256"),
        ("plotkin_statement_file", "plotkin_statement_sha256"),
        ("prize_floor_statement_file", "prize_floor_statement_sha256"),
    ):
        assert sha256(ROOT / pins[file_key]) == pins[hash_key]
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    for supplier in (
        "e1_collision_square_mass_reparametrization",
        "e1_prime_field_l2_norm_collision_radius",
        "e1_low_square_mass_plotkin_coloring_compiler",
        "e1_prize_field_floor_even_norm_exclusion",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    checks += 4

    print(
        "E1_LOW_SQUARE_MASS_WEIGHTED_KERNEL_DICTIONARY_PASS "
        f"rows={len(ROWS)} tight_oriented_cap=66866 checks={checks}"
    )


if __name__ == "__main__":
    main()
