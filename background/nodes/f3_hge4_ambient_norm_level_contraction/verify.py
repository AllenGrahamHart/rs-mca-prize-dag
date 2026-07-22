#!/usr/bin/env python3
"""Verify exact ambient HGE4 cutoffs and finite cell accounting."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_ambient_norm_level_contraction"


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


checks = 0
grand_deleted = 0
row_deleted = {}

for s in range(13, 42):
    deleted = 0
    n = 1 << s
    for r in range(4, s + 1):
        m = 1 << r
        cutoff = 2 * ceil_div(m * r, 8 * s)
        assert cutoff <= m // 4
        if r == s:
            assert cutoff == m // 4
        else:
            assert cutoff <= m // 4 - 2

        # The first excluded width has enough ambient norm exponent.
        h = cutoff
        assert 2 * s * (h // 2) >= r * m // 4

        # One width earlier fails this coarse exponent comparison.
        if cutoff > 1:
            h_previous = cutoff - 1
            assert 2 * s * (h_previous // 2) < r * m // 4

        cell_loss = max(0, m // 4 - max(4, cutoff))
        deleted += cell_loss
        checks += 4

    row_deleted[s] = deleted
    grand_deleted += deleted

assert row_deleted[13] == 302
assert row_deleted[20] == 26_194
assert row_deleted[30] == 17_895_668
assert row_deleted[41] == 26_817_356_728
assert grand_deleted == 55_050_457_488

# Independent exact-gate replay on the smallest ambient row. The powers are
# small enough to compare as integers and expose the parity-sensitive bonus.
s = 13
n = 1 << s
exact_bonus = 0
for r in range(4, s + 1):
    m = 1 << r
    cutoff = 2 * ceil_div(m * r, 8 * s)
    for h in range(4, m // 4):
        u_h = h // 2
        v_h = (h - 1) // 2 + 2
        exact = n ** (2 * u_h) >= (4 * h - v_h) ** (m // 4)
        if h >= cutoff:
            assert exact
        elif exact:
            exact_bonus += 1
        checks += 1
assert exact_bonus == 116

s = 41
for r, expected_cutoff, expected_loss in (
    (39, 130_734_614_280, 6_704_339_192),
    (40, 268_173_567_752, 6_704_339_192),
    (41, 549_755_813_888, 0),
):
    m = 1 << r
    cutoff = 2 * ceil_div(m * r, 8 * s)
    assert cutoff == expected_cutoff
    assert max(0, m // 4 - max(4, cutoff)) == expected_loss
    checks += 2

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[NODE]["status"] == "PROVED"
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert ("f3_hge4_exact_ratio_tower_orbit_compiler", NODE, "req") in edges
assert ("f3_hge4_cyclotomic_norm_quarter_width_exclusion", NODE, "req") in edges
assert ("f3_hge4_nonfull_complement_third_gate", NODE, "req") in edges
assert ("f3_hge4_vandermonde_defect_band_exclusion", NODE, "req") in edges
assert ("f3_hge4_primitive_swap_odd_moment_router", NODE, "req") in edges
assert ("f3_hge4_swap_norm_haar_band_exclusion", NODE, "req") in edges
assert (NODE, "f3_hge4_norm_gate_count", "ev") in edges

statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
for marker in (
    "c_(n,m)=2 ceil(mr/(8s))",
    "(ALC2-exact)",
    "55,050,457,488",
    "top level `m=n`",
    "does not bound any",
):
    assert marker in statement
    checks += 1
assert "p^u>n^(2u)>=m^(m/4)" in proof
assert "4h<m" in proof
assert "D<=4h-v_h" in proof and "p^u<=h^(m/4)" in proof

print(
    "F3_HGE4_AMBIENT_NORM_LEVEL_CONTRACTION_PASS",
    f"checks={checks}",
    f"deleted={grand_deleted}",
    f"s13_exact_bonus={exact_bonus}",
)
