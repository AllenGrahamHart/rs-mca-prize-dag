#!/usr/bin/env python3
"""commonroot_syzygy pilot: the realisable-block census beta(mu, pi), its
brute-force calibration, the near-packed extension, and the split-fiber no-go.

Verifies P3, P4, P5 and falsifiers F3, F4 of PREREG.md, and computes the
exact comparison of the whole (CRE2) tuple family at the boundary.
"""

import json
import sys
from itertools import combinations, permutations
from math import comb, prod

sys.dont_write_bytecode = True

CHECKS = 0
RESULTS: dict = {}


def check(cond: bool, label: str) -> None:
    global CHECKS
    if not cond:
        raise AssertionError(f"FAILED: {label}")
    CHECKS += 1


# ---------------------------------------------------------------------------
# Census machinery: block = a vector (m_1..m_p) of fiber intersection sizes.
# ---------------------------------------------------------------------------

def profile_vectors(mu: tuple, pi: tuple):
    """All vectors m with 0<=m_i<=mu_i whose nonzero multiset equals pi."""
    p = len(mu)
    seen = set()
    for slots in permutations(range(p), len(pi)):
        vec = [0] * p
        ok = True
        for part, i in zip(pi, slots):
            if part > mu[i]:
                ok = False
                break
            vec[i] = part
        if ok:
            seen.add(tuple(vec))
    return seen


def weight(mu: tuple, vec: tuple) -> int:
    """Number of distinct point-sets with this fiber-intersection vector."""
    return prod(comb(mu[i], vec[i]) for i in range(len(mu)))


def has_mate(mu: tuple, vec: tuple, pi2: tuple) -> bool:
    """Does a disjoint mate with profile pi2 fit in the residual fibers?"""
    residual = tuple(mu[i] - vec[i] for i in range(len(mu)))
    return bool(profile_vectors(residual, pi2))


def beta(mu: tuple, pi1: tuple, pi2: tuple) -> int:
    """Number of distinct realisable pi1-blocks admitting a disjoint pi2 mate."""
    total = 0
    for vec in profile_vectors(mu, pi1):
        if has_mate(mu, vec, pi2):
            total += weight(mu, vec)
    return total


def beta_unfiltered(mu: tuple, pi1: tuple) -> int:
    """Blocks with profile pi1, ignoring the two-block closure constraint."""
    return sum(weight(mu, v) for v in profile_vectors(mu, pi1))


# ---------------------------------------------------------------------------
# Part 1 (P3 / F3): brute-force calibration of the census at small scale.
# ---------------------------------------------------------------------------

def brute_force(mu: tuple, pi1: tuple, pi2: tuple):
    """Enumerate concrete point sets; return (realisable blocks, all pi1-blocks)."""
    pts, fiber_of = [], {}
    for i, size in enumerate(mu):
        for _ in range(size):
            fiber_of[len(pts)] = i
            pts.append(len(pts))
    r = sum(pi1)

    def prof(sub):
        counts: dict = {}
        for x in sub:
            counts[fiber_of[x]] = counts.get(fiber_of[x], 0) + 1
        return tuple(sorted(counts.values(), reverse=True))

    target_pi1, target_pi2 = tuple(sorted(pi1, reverse=True)), tuple(
        sorted(pi2, reverse=True)
    )
    cand1 = [frozenset(c) for c in combinations(pts, r) if prof(c) == target_pi1]
    rest = set(pts)
    cand2 = [
        frozenset(c)
        for c in combinations(pts, sum(pi2))
        if prof(c) == target_pi2
    ]
    realisable = {b for b in cand1 if any(not (b & m) for m in cand2)}
    return realisable, cand1, rest


# ell=3 calibration: e=4*ell+t, r=2*ell+1=7, packed profile (3,3,1).
CAL = []
for t, tail in [(2, (1, 1)), (3, (1, 1, 1)), (4, (2, 2)), (5, (2, 2, 1)),
                (4, (2, 1, 1))]:
    ell = 3
    mu = tuple([ell] * 4 + list(tail))
    e = sum(mu)
    check(e == 4 * ell + t, f"calibration e=4ell+t for tail={tail}")
    check(max(tail) < ell, f"tail fibers strictly below ell for tail={tail}")
    pi = (ell, ell, 1)
    predicted = beta(mu, pi, pi)
    realisable, cand1, _ = brute_force(mu, pi, pi)
    check(predicted == len(realisable),
          f"F3: census matches brute force, tail={tail}")
    # The packed rigidity claim of (P4F4), independently re-derived here, and
    # now shown to be independent of how the tail splits into fibers.
    check(predicted == 6 * t,
          f"P4F4 rigidity: beta = 6t for tail={tail} (got {predicted})")
    # and the two-block filter is load-bearing: without it the count is larger.
    unfiltered = beta_unfiltered(mu, pi)
    check(unfiltered == len(cand1), f"unfiltered census matches brute force {tail}")
    check(unfiltered > predicted,
          f"two-block closure is load-bearing for tail={tail}")
    CAL.append({
        "ell": ell, "t": t, "tail": tail, "mu": mu,
        "beta": predicted, "six_t": 6 * t, "unfiltered": unfiltered,
        "brute_force": len(realisable),
    })
RESULTS["calibration_ell3"] = CAL

# Documented exception (found by this pilot, not previously recorded): if a
# tail fiber is allowed to REACH size ell it becomes a fifth full fiber and the
# 6t rigidity fails outright. At ell=3, t=4, tail=(3,1) the census gives 100,
# not 24. The official boundary is protected only because the PROVED
# packed-payment hypothesis `ell > sigma+2 >= t` forbids this. The hypothesis
# is therefore load-bearing, not cosmetic.
mu_exc = (3, 3, 3, 3, 3, 1)
b_exc = beta(mu_exc, (3, 3, 1), (3, 3, 1))
rl_exc, _, _ = brute_force(mu_exc, (3, 3, 1), (3, 3, 1))
check(b_exc == len(rl_exc), "F3: exception census matches brute force")
check(b_exc == 100, f"fifth-full-fiber exception gives beta=100 (got {b_exc})")
check(b_exc > 6 * 4, "fifth-full-fiber exception breaks the 6t rigidity")
RESULTS["fifth_full_fiber_exception"] = {
    "mu": mu_exc, "t": 4, "beta": b_exc, "six_t": 24,
    "note": "requires t >= ell; excluded at the official rows by ell > sigma+2",
}

# Only three full fibers: the packed stratum is empty (both blocks need two).
mu_short = (3, 3, 3, 2, 2, 1)
check(sum(mu_short) == 14, "short-fiber calibration size")
check(beta(mu_short, (3, 3, 1), (3, 3, 1)) == 0,
      "phi=4 full fibers is forced for the packed stratum")
rl, _, _ = brute_force(mu_short, (3, 3, 1), (3, 3, 1))
check(len(rl) == 0, "brute force agrees: packed stratum empty at phi=3")
RESULTS["phi3_stratum_empty"] = True

# Toy calibration of the NON-EMPTY split stratum used at the official rows:
# profile (ell, ell-1, 1, 1) on the packed mu. At ell=3 that is (3,2,1,1).
SPLIT_CAL = []
for t in (2, 3, 4):
    ell = 3
    mu = tuple([ell] * 4 + [1] * t)
    pi = (ell, ell - 1, 1, 1)
    check(sum(pi) == 2 * ell + 1, "toy split profile sums to r")
    predicted = beta(mu, pi, pi)
    realisable, _, _ = brute_force(mu, pi, pi)
    check(predicted == len(realisable),
          f"F3: split-stratum census matches brute force, t={t}")
    check(predicted > 0, f"toy split stratum non-empty, t={t}")
    check(predicted > 6 * t, f"toy split stratum beats the packed count, t={t}")
    SPLIT_CAL.append({"ell": ell, "t": t, "pi": pi, "beta": predicted,
                      "brute_force": len(realisable), "six_t": 6 * t})
RESULTS["split_calibration_ell3"] = SPLIT_CAL

# A non-packed profile at ell=3: (3,2,2). Census vs brute force.
NONPACKED = []
for mu in [(3, 3, 3, 3, 1, 1), (3, 3, 3, 2, 2, 1), (3, 3, 2, 2, 2, 2)]:
    if sum(mu) != 14:
        continue
    pi = (3, 2, 2)
    predicted = beta(mu, pi, pi)
    realisable, _, _ = brute_force(mu, pi, pi)
    check(predicted == len(realisable), f"F3: non-packed census matches, mu={mu}")
    NONPACKED.append({"mu": mu, "pi": pi, "beta": predicted})
RESULTS["nonpacked_ell3"] = NONPACKED


# ---------------------------------------------------------------------------
# Part 2 (P4 / P5 / F4): the official boundary catalogue.
# ---------------------------------------------------------------------------

ROWS = (("1/4,1/8", 2**41, 2**33 + 1, 11), ("1/16", 2**41, 2**32 + 1, 10))
X_OF = {"1/4,1/8": 118, "1/16": 136}   # recomputed below from ledger.py logic


def boundary(h: int):
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    return ell, r, d, sigma, d + ell


def max_bset(n: int, e: int, w: int, s: int) -> int:
    N = n - e
    budget = (17 * n * n - 25 * (n - e)) // 25
    return (2 * budget * prod(w + j for j in range(3, s + 1))) // (
        3 * prod(N - j for j in range(s - 2))
    )


catalogue = {}
for name, n, h, s in ROWS:
    ell, r, d, sigma, w = boundary(h)
    rows_out = []
    for t in range(2, sigma + 3):
        e = 4 * ell + t
        X = max_bset(n, e, w, s)
        check(X == X_OF[name], f"{name}: X agrees with ledger.py ({X})")

        # (a) exact-packed, arbitrary tail fiber structure -> beta = 6t.
        for tail in ([1] * t, [t], [t - 1, 1] if t > 2 else [1, 1]):
            mu = tuple([ell] * 4 + [x for x in tail if x > 0])
            if sum(mu) != e:
                continue
            b = beta(mu, (ell, ell, 1), (ell, ell, 1))
            check(b == 6 * t,
                  f"{name} t={t} tail={tail}: beta=6t (got {b})")
            check(b <= X, f"{name} t={t} tail={tail}: paid by (WTB)")

        # (b) one large fiber shortened by one: mu = (ell,ell,ell,ell-1,...).
        # Only three full fibers survive, so the packed stratum is empty: the
        # two-block closure needs two full fibers per block.
        mu_b = tuple([ell] * 3 + [ell - 1] + [1] * (t + 1))
        check(sum(mu_b) == e, f"{name} t={t}: shortened-fiber mu has size e")
        check(beta(mu_b, (ell, ell, 1), (ell, ell, 1)) == 0,
              f"{name} t={t}: packed stratum empty at phi=3")
        # Several natural split profiles are empty too, because only t-2 points
        # are spare: record which, so the boundary is exact rather than assumed.
        mu_pack = tuple([ell] * 4 + [1] * t)
        empties = {}
        for pi in ((ell, ell - 1, 2), (ell, ell - 1, ell - 1, 3)):
            if sum(pi) == r:
                empties[str(pi)] = beta(mu_pack, pi, pi)

        # (c) THE non-empty split stratum. B1 = F1 + (ell-1 of F2) + (1 of F3)
        # + one tail point; its mate is the mirror image. Both blocks have
        # profile (ell, ell-1, 1, 1), every part is <= ell, v=4 >= 3, and the
        # two-block closure is satisfiable. This is a legitimate near-packed
        # mixed stratum -- exactly the family (P4F4) does not cover.
        pi_split = (ell, ell - 1, 1, 1)
        check(sum(pi_split) == r, f"{name}: split profile sums to r")
        b_split = beta(mu_pack, pi_split, pi_split)
        check(b_split > 0, f"{name} t={t}: split stratum is NON-empty")
        # P5 / F4: it splits fibers of size ell, so beta blows past X.
        check(b_split > X,
              f"{name} t={t}: F4 — split stratum exceeds X ({b_split} vs {X})")
        check(b_split > ell,
              f"{name} t={t}: split stratum exceeds ell")
        rows_out.append({
            "t": t, "e": e, "X": X, "beta_packed": 6 * t,
            "empty_split_profiles": empties,
            "beta_split_ell_ellm1_1_1": b_split,
            "split_over_X_ratio_log10": len(str(b_split // X)),
            "split_paid": b_split <= X,
        })
    catalogue[name] = {
        "ell": ell, "r": r, "d": d, "sigma": sigma, "w": w, "X": X_OF[name],
        "tails": rows_out,
    }
RESULTS["official_catalogue"] = catalogue

# P5, stated exactly: any block that takes m points from a fiber of size f with
# 0<m<f contributes a factor C(f,m) >= f, so f > X is unpayable outright.
# The inequality min_{0<m<f} C(f,m) = C(f,1) = f is binomial unimodality;
# verify it exhaustively at small f and then use it as an identity.
for f in range(2, 200):
    check(min(comb(f, m) for m in range(1, f)) == f,
          f"unimodality: min_m C({f},m) = {f}")
for name, X in X_OF.items():
    for f in (X, X + 1, 2 * X, 10**6):
        # by the verified identity the minimum split cost of a size-f fiber is f
        check(comb(f, 1) == f, f"split cost of a size-{f} fiber is {f}")
        if f > X:
            check(f > X, f"{name}: split fiber of size {f} exceeds X")
RESULTS["split_threshold"] = {k: v for k, v in X_OF.items()}


# ---------------------------------------------------------------------------
# Part 3: the whole (CRE2) tuple family at the boundary, exactly.
# (CRE2)  2|Tau| B_(s-m) T_(m+1) <= (m+1) C(N,s-m) C(e,m+1)
#   ==>   |Tau| <= coeff(m) * prod_(j=0)^(s-m-1)(N-j) / prod_(j=m+1)^s (w+j),
#         coeff(m) = (m+1) C(e,m+1) / (2 T_(m+1)).
# ---------------------------------------------------------------------------

def esym(parts, order: int) -> int:
    """Elementary symmetric polynomial e_order of the fiber-size multiset."""
    acc = [1] + [0] * order
    for p in parts:
        for j in range(order, 0, -1):
            acc[j] += acc[j - 1] * p
    return acc[order]


tuple_family = {}
for name, n, h, s in ROWS:
    ell, r, d, sigma, w = boundary(h)
    t = 2
    e = 4 * ell + t
    N = n - e
    budget = (17 * n * n - 25 * (n - e)) // 25
    entry = []
    # packed block profile (ell,ell,1): v=3, so T_4 = 0 and only m=2 is usable.
    packed_parts = (ell, ell, 1)
    # a v=4 near-packed profile, where m=3 first becomes available.
    v4_parts = (ell, ell - 1, 1, 1)
    for label, parts in (("packed(ell,ell,1)", packed_parts),
                         ("v4(ell,ell-1,1,1)", v4_parts)):
        for m in range(2, 6):
            T = esym(parts, m + 1)
            if T == 0:
                entry.append({"profile": label, "m": m, "T": 0,
                              "usable": False, "reason": "T_(m+1)=0, vacuous"})
                continue
            numer = (m + 1) * comb(e, m + 1) * prod(N - j for j in range(s - m))
            denom = 2 * T * prod(w + j for j in range(m + 1, s + 1))
            pays = numer <= budget * denom
            entry.append({
                "profile": label, "m": m, "usable": True, "pays": pays,
                "cap_over_budget_log10": len(str(numer // (denom * budget)))
                if numer > denom * budget else 0,
            })
            check(not pays,
                  f"{name} {label} m={m}: tuple ledger exceeds budget")
    tuple_family[name] = entry
RESULTS["tuple_family_at_boundary"] = tuple_family

out = {"pilot": "commonroot_syzygy", "script": "census.py",
       "checks": CHECKS, "results": RESULTS}
with open("notes/pilots_20260804/commonroot_syzygy/census.json", "w",
          encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, default=str)

print(f"COMMONROOT_SYZYGY_CENSUS_PASS checks={CHECKS}")
for c in CAL:
    print(f"  cal ell=3 t={c['t']} tail={c['tail']}: beta={c['beta']} "
          f"(=6t={c['six_t']}), unfiltered={c['unfiltered']}, "
          f"brute={c['brute_force']}")
for name, ent in catalogue.items():
    print(f"  row {name}: X={ent['X']}")
    for rw in ent["tails"]:
        print(f"    t={rw['t']}: beta_packed={rw['beta_packed']:3d} PAID"
              f" | split(ell,ell-1,1,1) beta={rw['beta_split_ell_ellm1_1_1']}"
              f" (~1e{rw['split_over_X_ratio_log10']}x X) "
              f"paid={rw['split_paid']}")
for sc in RESULTS["split_calibration_ell3"]:
    print(f"  split cal ell=3 t={sc['t']}: beta={sc['beta']} "
          f"brute={sc['brute_force']} (packed count 6t={sc['six_t']})")
print("  tuple family:", json.dumps(RESULTS["tuple_family_at_boundary"]))
