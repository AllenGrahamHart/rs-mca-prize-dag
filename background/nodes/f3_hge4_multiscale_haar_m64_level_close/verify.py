#!/usr/bin/env python3
"""Verify the multiscale Haar endpoint and the complete m=64 level close."""

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_multiscale_haar_m64_level_close"


def subset_gate(m: int, h: int, s: int, positive_mask: int) -> bool:
    """Exact cross-multiplied form of (MHN8)."""
    H = (h - 1) // 2
    ell = H.bit_length()
    A = m // 4
    orders = [m // (1 << (a + 1)) for a in range(ell)]
    rs = [((H // (1 << a)) + 1) // 2 for a in range(ell)]
    positive = [a for a in range(ell) if positive_mask & (1 << a)]
    zero = [a for a in range(ell) if not positive_mask & (1 << a)]
    Bs = {a: orders[a] // 4 for a in positive}
    W = A + sum(Bs.values())
    row_exp = h // 2 + sum(rs[a] for a in positive)

    norm_orders = [m] + [orders[a] for a in positive]
    two_exp = sum(
        min(order, orders[a]) // 2
        for order in norm_orders
        for a in zero
    )
    upper_two_exp = sum((a + 1) * Bs[a] for a in positive)

    left = (1 << two_exp) * (1 << s) ** (2 * row_exp) * W**W
    right = (1 << upper_two_exp) * (4 * h) ** W * A**A
    for value in Bs.values():
        right *= value**value
    return left >= right


# Exact h=4 quarter-orbit dynamic program. The Taylor mask records
# coefficients 1,...,8 modulo two; an empty mask means nu>=9.
TAYLOR_DEPTH = 8
states = {(0, 0, 0, 0, 0)}
state_counts = []
for orbit in range(16):
    exponents = (orbit, orbit + 16, orbit + 32, orbit + 48)
    local = []
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            for c in (-1, 0, 1):
                for d in (-1, 0, 1):
                    values = (a, b, c, d)
                    mask = 0
                    for exponent, value in zip(exponents, values):
                        if value:
                            for j in range(1, TAYLOR_DEPTH + 1):
                                mask ^= (comb(exponent, j) & 1) << (j - 1)
                    local.append(
                        (
                            values.count(1),
                            values.count(-1),
                            (a - c) ** 2 + (b - d) ** 2,
                            (a + c - b - d) ** 2,
                            mask,
                        )
                    )

    next_states = set()
    for plus, minus, odd_energy, haar_energy, mask in states:
        for lp, lm, ld, lh, lmask in local:
            if plus + lp <= 4 and minus + lm <= 4:
                next_states.add(
                    (
                        plus + lp,
                        minus + lm,
                        odd_energy + ld,
                        haar_energy + lh,
                        mask ^ lmask,
                    )
                )
    states = next_states
    state_counts.append(len(states))

assert state_counts[-1] == 28_171
sharp = 10**24 // 4
sharp_seen = False
endpoint_states = 0
for plus, minus, odd_energy, haar_energy, mask in states:
    if plus != 4 or minus != 4 or odd_energy == 0 or haar_energy == 0:
        continue
    nu = next(
        (j for j in range(1, TAYLOR_DEPTH + 1) if mask & (1 << (j - 1))),
        TAYLOR_DEPTH + 1,
    )
    numerator = odd_energy**16 * haar_energy**8
    assert 4 * numerator <= 10**24 * (1 << (2 * nu))
    if numerator == sharp * (1 << (2 * nu)):
        assert (odd_energy, haar_energy, nu) == (10, 10, 1)
        sharp_seen = True
    endpoint_states += 1
assert sharp_seen
assert sharp < 1 << 78

# h=4, Delta_0=0: 2^16 p^2 is already too large.
assert (1 << 16) * (1 << 26) ** 2 > 16**16

# Every Haar zero/nonzero pattern closes h=5 at the smallest official n.
assert all(subset_gate(64, 5, 13, mask) for mask in range(4))

# The inherited exact ambient predicate closes h=6,...,15 at n=2^13.
for h in range(6, 16):
    u_h = h // 2
    v_h = (h - 1) // 2 + 2
    assert (1 << 13) ** (2 * u_h) >= (4 * h - v_h) ** 16

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[NODE]["status"] == "PROVED"
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert ("f3_hge4_exact_ratio_tower_orbit_compiler", NODE, "req") in edges
assert ("f3_hge4_ambient_norm_level_contraction", NODE, "req") in edges
assert (NODE, "f3_hge4_norm_gate_count", "ev") in edges

statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
for marker in ("(MHN4)", "(MHN6)", "(MHN9)", "(MHN10)", "m=128"):
    assert marker in statement
assert "28,171" in proof and "`T_2(S)`" in proof

print(
    "F3_HGE4_MULTISCALE_HAAR_M64_LEVEL_CLOSE_PASS",
    f"states={state_counts[-1]}",
    f"endpoint_states={endpoint_states}",
    "m64_debit=0",
)
