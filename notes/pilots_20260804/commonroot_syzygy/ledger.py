#!/usr/bin/env python3
"""commonroot_syzygy pilot: the shared two-block ledger (WTB) and its exact
block budget X.

Verifies P1, P2, P6 and falsifiers F1, F2, F5, F6 of PREREG.md.
Exact integer arithmetic throughout; floats appear only in printed
diagnostics and are labelled.
"""

import json
import sys
from itertools import combinations
from math import prod

sys.dont_write_bytecode = True

CHECKS = 0
RESULTS: dict = {}


def check(cond: bool, label: str) -> None:
    global CHECKS
    if not cond:
        raise AssertionError(f"FAILED: {label}")
    CHECKS += 1


# ---------------------------------------------------------------------------
# Part 1 (P1 / F1): the double count 2|Tau| <= 3|Bset| on exhaustive small
# incidence systems with the (CRE1, m=2) owner cap of 3.
# ---------------------------------------------------------------------------

def all_targets(ground: int, blocksize: int):
    """Every unordered pair of disjoint blocksize-subsets of range(ground)."""
    blocks = [frozenset(c) for c in combinations(range(ground), blocksize)]
    out = []
    for i, b1 in enumerate(blocks):
        for b2 in blocks[i + 1:]:
            if not (b1 & b2):
                out.append((b1, b2))
    return blocks, out


def ledger_holds(family, cap: int) -> tuple[bool, int, int]:
    """Return (2|Tau| <= 3|Bset|, 2|Tau|, 3|Bset|) for a family obeying `cap`."""
    owners: dict = {}
    for tgt in family:
        for blk in tgt:
            owners[blk] = owners.get(blk, 0) + 1
    if any(v > cap for v in owners.values()):
        return (None, 0, 0)
    return (2 * len(family) <= 3 * len(owners), 2 * len(family), 3 * len(owners))


GROUND, BLOCKSIZE = 5, 2
BLOCKS, TARGETS = all_targets(GROUND, BLOCKSIZE)
check(len(BLOCKS) == 10, "block count C(5,2)=10")
check(len(TARGETS) == 15, "disjoint-pair target count = 15")

exhaustive = 0
tight = 0
for mask in range(1 << len(TARGETS)):
    fam = [TARGETS[i] for i in range(len(TARGETS)) if mask >> i & 1]
    ok, lhs, rhs = ledger_holds(fam, cap=3)
    if ok is None:
        continue  # violates the CRE1 owner cap: outside the hypothesis
    exhaustive += 1
    check(ok, f"WTB-plane on family mask={mask}")
    if lhs == rhs:
        tight += 1
RESULTS["exhaustive_admissible_families"] = exhaustive
RESULTS["tight_families"] = tight

# In the (5,2) system no block can reach four owners (only C(3,2)=3 disjoint
# mates exist), so the cap-3 sweep above cannot be made to fail there. Move to
# (6,2), where a block has C(4,2)=6 disjoint mates and the cap genuinely bites.
BLOCKS2, TARGETS2 = all_targets(6, 2)
check(len(BLOCKS2) == 15, "block count C(6,2)=15")
check(len(TARGETS2) == 45, "disjoint-pair target count on (6,2) = 45")

sample_ok = 0
for mask in range(1 << 14):  # first 14 targets only, keeps the sweep small
    fam = [TARGETS2[i] for i in range(14) if mask >> i & 1]
    ok, _, _ = ledger_holds(fam, cap=3)
    if ok is None:
        continue
    check(ok, f"WTB-plane on (6,2) family mask={mask}")
    sample_ok += 1
RESULTS["second_ground_admissible_families"] = sample_ok


def greedy_capped(targets, cap: int):
    """Deterministic maximal family with every block owned at most `cap` times."""
    deg: dict = {}
    fam = []
    for b1, b2 in targets:
        if deg.get(b1, 0) < cap and deg.get(b2, 0) < cap:
            fam.append((b1, b2))
            deg[b1] = deg.get(b1, 0) + 1
            deg[b2] = deg.get(b2, 0) + 1
    return fam


# Negative control (F1 shape): the owner cap must be load-bearing. Under
# cap 3 the ledger must hold; at some larger cap it must be violable.
control = {}
first_break = None
for cap in range(3, 7):
    fam = greedy_capped(TARGETS2, cap)
    ok, lhs, rhs = ledger_holds(fam, cap=cap)
    control[cap] = {"targets": len(fam), "lhs_2Tau": lhs, "rhs_3B": rhs, "holds": ok}
    if cap == 3:
        check(ok is True, "negative control: cap 3 family satisfies (WTB-plane)")
    if ok is False and first_break is None:
        first_break = cap
check(first_break is not None,
      "negative control: some cap>3 admits a (WTB-plane) violation")
RESULTS["negative_control"] = {"by_cap": control, "first_breaking_cap": first_break}


# ---------------------------------------------------------------------------
# Part 2 (F1, algebraic half): at r = 2ell+1 every block has v >= 3 distinct
# phi values, so the CRE1 (m=2) step is always legal at the boundary.
# ---------------------------------------------------------------------------

def min_parts(r: int, cap: int) -> int:
    """Fewest parts in a partition of r into parts of size at most cap."""
    return -(-r // cap)


for ell in range(1, 400):
    r = 2 * ell + 1
    check(min_parts(r, ell) >= 3, f"v>=3 forced at ell={ell}")
# and the converse: at r = 2ell a two-part block is arithmetically possible,
# which is exactly why the router restricts to r > 2ell.
for ell in range(1, 400):
    check(min_parts(2 * ell, ell) == 2, f"v=2 possible at r=2ell, ell={ell}")
RESULTS["fiber_count_sweep_ell"] = 399


# ---------------------------------------------------------------------------
# Part 3 (P2 / F2 / F5 / F6): the exact block budget X.
# ---------------------------------------------------------------------------

ROWS = (
    ("1/4,1/8", 2**41, 2**33 + 1, 11),
    ("1/16", 2**41, 2**32 + 1, 10),
)


def boundary(n: int, h: int):
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    w = d + ell
    return ell, r, d, sigma, w


def cap_numer_denom(n: int, e: int, w: int, s: int, bset: int):
    """|Tau| <= 3*bset*prod(N-j) / (2*prod(w+j)); return (numer, denom)."""
    N = n - e
    numer = 3 * bset * prod(N - j for j in range(s - 2))
    denom = 2 * prod(w + j for j in range(3, s + 1))
    return numer, denom


def budget_of(n: int, e: int) -> int:
    return (17 * n * n - 25 * (n - e)) // 25


def max_bset(n: int, e: int, w: int, s: int) -> int:
    """Largest integer b with 3*b*prod(N-j) <= 2*budget*prod(w+j)."""
    N = n - e
    lhs_unit = 3 * prod(N - j for j in range(s - 2))
    rhs = 2 * budget_of(n, e) * prod(w + j for j in range(3, s + 1))
    return rhs // lhs_unit


# The exact caps the PROVED (P4F4) verifier prints, reused read-only as the
# consistency anchor for F2/F6.
P4F4_EXPECTED = {
    (11, 2): 333_594_496_688_188_697_227_430,
    (11, 3): 500_391_745_030_230_497_876_741,
    (11, 4): 667_188_993_370_903_933_216_457,
    (11, 5): 833_986_241_710_209_003_246_588,
    (11, 6): 1_000_783_490_048_145_707_967_140,
    (11, 7): 1_167_580_738_384_714_047_378_121,
    (10, 2): 289_152_338_183_910_832_037_167,
    (10, 3): 433_728_507_274_286_589_926_945,
}

xtable = {}
for name, n, h, s in ROWS:
    ell, r, d, sigma, w = boundary(n, h)
    check(ell > sigma + 2, f"{name}: ell > sigma+2")
    check(sigma < r, f"{name}: sigma < r (two-block router applies)")
    row_entry = {
        "n": n, "h": h, "s": s, "ell": ell, "r": r, "d": d,
        "sigma": sigma, "w": w, "tails": {},
    }
    for t in range(2, sigma + 3):
        e = 4 * ell + t
        X = max_bset(n, e, w, s)
        bud = budget_of(n, e)

        # F6 / F2: (WTB) at |Bset| = 6t must reproduce (P4F4) exactly and pay.
        numer, denom = cap_numer_denom(n, e, w, s, 6 * t)
        wtb_cap = numer // denom
        if (s, t) in P4F4_EXPECTED:
            check(wtb_cap == P4F4_EXPECTED[(s, t)],
                  f"{name} t={t}: (WTB) at |Bset|=6t reproduces (P4F4)")
            check(numer <= bud * denom, f"{name} t={t}: (WTB) at 6t pays")
        check(X >= 6 * t, f"{name} t={t}: F2 — X >= 6t")
        check(X < ell, f"{name} t={t}: F5 — X < ell (route is bounded)")

        # X is exactly the threshold: X pays, X+1 does not.
        n_x, d_x = cap_numer_denom(n, e, w, s, X)
        n_x1, d_x1 = cap_numer_denom(n, e, w, s, X + 1)
        check(n_x <= bud * d_x, f"{name} t={t}: X pays")
        check(n_x1 > bud * d_x1, f"{name} t={t}: X+1 does not pay")

        row_entry["tails"][t] = {
            "e": e, "X": X, "six_t": 6 * t,
            "headroom_multiple": X // (6 * t),
            "wtb_cap_at_6t": wtb_cap, "budget": bud,
        }
        xtable[(name, t)] = X
    RESULTS[name] = row_entry


# ---------------------------------------------------------------------------
# Part 4 (P6): behaviour of the payable affine dimension s.
# ---------------------------------------------------------------------------

dim_scan = {}
for name, n, h, s0 in ROWS:
    ell, r, d, sigma, w = boundary(n, h)
    e = 4 * ell + 2
    payable = []
    for s in range(2, 31):
        numer, denom = cap_numer_denom(n, e, w, s, 12)  # |Bset| = 6t at t=2
        if numer <= budget_of(n, e) * denom:
            payable.append(s)
    dim_scan[name] = {
        "payable_s": payable,
        "is_upward_closed": payable == list(range(min(payable), max(payable) + 1))
        and max(payable) == 30,
        "first_payable_s": min(payable) if payable else None,
    }
    # X as a function of s at the fixed tail t=2.
    dim_scan[name]["X_by_s"] = {s: max_bset(n, e, w, s) for s in range(9, 15)}

    # THE NO-GO, asserted rather than printed: at the next affine dimension the
    # block budget is exactly zero, i.e. the ledger fails even for a family
    # realising a SINGLE block. No block-scarcity theorem can reach s0+1.
    for t in range(2, sigma + 3):
        e_t = 4 * ell + t
        check(max_bset(n, e_t, w, s0) > 0, f"{name} t={t}: s={s0} is payable")
        check(max_bset(n, e_t, w, s0 + 1) == 0,
              f"{name} t={t}: NO-GO — X=0 at s={s0+1}")
        n1, d1 = cap_numer_denom(n, e_t, w, s0 + 1, 1)
        check(n1 > budget_of(n, e_t) * d1,
              f"{name} t={t}: even |Bset|=1 exceeds budget at s={s0+1}")
    # the collapse factor per dimension is the exact ratio N/w
    dim_scan[name]["collapse_ratio_N_over_w"] = (n - e) // w
RESULTS["dimension_scan"] = dim_scan

out = {
    "pilot": "commonroot_syzygy",
    "script": "ledger.py",
    "checks": CHECKS,
    "results": RESULTS,
}
with open(
    "notes/pilots_20260804/commonroot_syzygy/ledger.json", "w", encoding="utf-8"
) as fh:
    json.dump(out, fh, indent=2, default=str)

print(f"COMMONROOT_SYZYGY_LEDGER_PASS checks={CHECKS}")
for name, _, _, _ in ROWS:
    ent = RESULTS[name]
    print(f"  row {name}: ell={ent['ell']} r={ent['r']} sigma={ent['sigma']}")
    for t, v in ent["tails"].items():
        print(
            f"    t={t}: 6t={v['six_t']:3d}  X={v['X']:6d}  "
            f"headroom={v['headroom_multiple']}x"
        )
print("  dimension scan:", json.dumps(dim_scan, default=str))
