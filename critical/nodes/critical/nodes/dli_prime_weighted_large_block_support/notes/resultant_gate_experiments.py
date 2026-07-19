#!/usr/bin/env python3
"""RESULTANT-GATE experiments (round-6 complementary attacks, pre-registered).

THE GATE (one-line theorem, the pairwise analogue of the proved
bounded_coeff_norm_gate): if two ternary elements P1, P2 (reduced, order n')
both vanish at a common embedding omega mod q, then x - omega divides both in
F_q[x], hence q | Res(P1, P2); and Res(P1, P2) != 0 whenever P1, P2 are
coprime over Q.  So every multi-orbit prime is a divisor of an explicit
bounded-height resultant web.

EXPERIMENTS (n' = 32, N = 16 -- exact integer arithmetic throughout):

E1 PRIME-FIRST (round-5 selection model): engineer primes as admissible
   divisors of N(P1) = Res(x^N+1, P1) for random weight-5 P1; census the
   ALIGNED embedding (the root of P1 of order n'); count BONUS independent
   orbits (excluding P1's own multiplier component).
   Pre-registered: if norm-selection does not stack, bonus counts match the
   Poisson coincidence model mu = #orbits/q of a RANDOM prime of that size
   (SELECTION_NEUTRAL); systematic enrichment = alarm (SELECTION_STACKS).

E2 PAIR-FIRST (the two-orbit engineering route): for random ternary-
   independent pairs (P1, P2), factor Res(P1, P2); count admissible prime
   factors (q == 1 mod n', in census range) where a COMMON root of order n'
   exists (both orbits live at one pinned row).  Measures the true success
   rate and the alignment cost of engineering a two-orbit prime.
   Pre-registered: engineering SUCCEEDS at some rate (two-orbit primes exist
   and are findable -- this costs the aggregate only ~2x one orbit and is
   priced); record the rate and the aligned/raw ratio.

E3 GCD-WEB (the k>=3 obstruction): for random triples, compute
   G = gcd(Res(P1,P2), Res(P1,P3), Res(P2,P3)).  A triple-orbit prime must
   divide G.  Pre-registered: G is O(1)-smooth (tiny, no admissible factor)
   for generic triples => tuple-first engineering dead at k >= 3
   (GCD_WEB_TRIVIAL); large structured G = the mechanism Pro could
   weaponize, report verbatim (GCD_WEB_STRUCTURED).

All randomness from a fixed seed (replayable).  Runtime target < 120 s local.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
import random
import signal
import sys
import time
from collections import Counter
from contextlib import contextmanager
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("census", HERE / "modal_dli_orbit_census.py")
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

NPRIME, N = 32, 16
QMIN, QMAX_FLOAT = 20_000, 1 << 49  # float64-exact census range


# ------------------------------------------------------- exact integer alg --


def poly_from(sup, sgn) -> list[int]:
    v = [0] * N
    for e, s in zip(sup, sgn):
        v[e] = s
    return v


def trim(p: list[int]) -> list[int]:
    while p and p[-1] == 0:
        p = p[:-1]
    return p


def resultant(f: list[int], g: list[int]) -> int:
    """Res(f, g) via fraction-free Euclidean algorithm (subresultant PRS)."""
    f, g = trim(list(f)), trim(list(g))
    if not f or not g:
        return 0
    from fractions import Fraction

    A = [Fraction(c) for c in f]
    B = [Fraction(c) for c in g]
    res = Fraction(1)
    while True:
        da, db = len(A) - 1, len(B) - 1
        if db < 0:
            return 0
        if db == 0:
            r = res * B[0] ** da
            assert r.denominator == 1
            return int(r)
        # A = Q*B + R; Res(A,B) = lc(B)^(da-dr) * (-1)^(da*db) * Res(B,R)
        R = A[:]
        lcB = B[-1]
        for i in range(da, db - 1, -1):
            c = R[i] / lcB
            if c:
                for j in range(db + 1):
                    R[i - db + j] -= c * B[j]
        R = R[:db]
        while R and R[-1] == 0:
            R = R[:-1]
        dr = len(R) - 1
        if dr < 0:
            return 0
        res *= B[-1] ** (da - dr) * (-1) ** (da * db)
        A, B = B, R


def is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def brent_rho(n: int, rng: random.Random) -> int:
    if n % 2 == 0:
        return 2
    while True:
        y, c, m = rng.randrange(1, n), rng.randrange(1, n), 128
        g, r, q = 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g


def factorize(n: int, rng: random.Random) -> Counter:
    fac = Counter()
    for p in (2, 3, 5, 7, 11, 13):
        while n % p == 0:
            fac[p] += 1
            n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_probable_prime(m):
            fac[m] += 1
            continue
        d = brent_rho(m, rng)
        stack += [d, m // d]
    return fac


class TrialTimeout(Exception):
    pass


@contextmanager
def time_limit(seconds: int):
    """SIGALRM guard: a pathological trial is logged and skipped, never a hang."""
    def _raise(signum, frame):
        raise TrialTimeout()
    old = signal.signal(signal.SIGALRM, _raise)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


_PR_RNG = random.Random(1)
_PR_CACHE: dict[int, int] = {}


def fast_primitive_root(q: int) -> int:
    """A primitive root mod prime q, factoring q-1 with Brent rho (not trial
    division -- census.smallest_primitive_root hangs for minutes on large q).
    Any primitive root enumerates the same set of order-n' elements, so
    smallest-ness is irrelevant here (we take ALL odd powers below)."""
    if q not in _PR_CACHE:
        parts = list(factorize(q - 1, _PR_RNG))
        g = 2
        while any(pow(g, (q - 1) // p, q) == 1 for p in parts):
            g += 1
        _PR_CACHE[q] = g
    return _PR_CACHE[q]


def order_np_roots(P: list[int], q: int) -> list[int]:
    """Roots of P mod q of multiplicative order exactly n'."""
    g = fast_primitive_root(q)
    out = []
    for t in range(1, NPRIME, 2):
        w = pow(g, (q - 1) * t // NPRIME, q)
        if sum(c * pow(w, e, q) for e, c in enumerate(P) if c) % q == 0:
            out.append(w)
    return out


def random_ternary(rng: random.Random, w: int):
    sup = tuple(sorted(rng.sample(range(N), w)))
    sgn = (1,) + tuple(rng.choice((1, -1)) for _ in range(w - 1))
    return sup, sgn


def census_at(omega: int, q: int, wmax: int = 6):
    """Primitive orbits at a GIVEN embedding + multiplier-independent count."""
    orbs = {}
    for w in range(3, wmax + 1):
        for sup, sgn in census.find_vanishers(
            census.combo_array(N, w), census.sign_matrix(w), omega, q
        ):
            k = census.orbit_key(sup, sgn, N)
            if k not in orbs:
                orbs[k] = {
                    "w": w,
                    "rep": (sup, sgn),
                    "prim": census.is_primitive(sup, sgn, omega, q),
                }
    prim = {k: o for k, o in orbs.items() if o["prim"]}
    return prim, census.independent_components(prim, N)


def mu_at(q: int, wmax: int = 6) -> float:
    return sum(math.comb(N, w) * 2**w // NPRIME for w in range(3, wmax + 1)) / q


# ------------------------------------------------------------ experiments ---


def e1_prime_first(rng: random.Random, trials: int) -> dict:
    XN1 = [1] + [0] * (N - 1) + [1]  # x^16 + 1
    rows, bonus_sum, mu_sum, timeouts = [], 0.0, 0.0, 0
    for i in range(trials):
        if i % 25 == 0:
            print(f"  e1 trial {i}/{trials} t={time.time()-T0:.0f}s", flush=True)
        try:
            with time_limit(20):
                sup, sgn = random_ternary(rng, 5)
                P = poly_from(sup, sgn)
                norm = abs(resultant(XN1, P))
                if norm == 0:
                    continue
                for q in factorize(norm, rng):
                    if q % NPRIME != 1 or not (QMIN <= q < QMAX_FLOAT):
                        continue
                    roots = order_np_roots(P, q)
                    if not roots:
                        continue
                    omega = roots[0]
                    prim, k_indep = census_at(omega, q)
                    key_p1 = census.orbit_key(sup, sgn, N)
                    found = key_p1 in prim
                    bonus = max(0, k_indep - 1)
                    bonus_sum += bonus
                    mu_sum += mu_at(q)
                    rows.append({"q": q, "planted_found": found, "k_indep": k_indep, "bonus": bonus})
        except TrialTimeout:
            timeouts += 1
            print(f"  e1 trial {i} TIMEOUT (>20s), skipped", flush=True)
    return {
        "experiment": "E1_prime_first",
        "trials": trials,
        "trial_timeouts": timeouts,
        "engineered_primes": len(rows),
        "planted_found_all": all(r["planted_found"] for r in rows),
        "bonus_total_observed": bonus_sum,
        "bonus_total_poisson_pred": round(mu_sum, 3),
        "bonus_hist": dict(Counter(r["bonus"] for r in rows)),
        "verdict": "SELECTION_NEUTRAL"
        if bonus_sum <= 2.5 * max(mu_sum, 1e-9) or bonus_sum <= 3
        else "SELECTION_STACKS",
        "rows": rows[:20],
    }


def ideal_norm(polys: list[list[int]]) -> int:
    """|Z[z]/(z^N+1, P_1, ..., P_k)| via row-reduction of all signed shifts.

    The ideal's Z-lattice is generated by z^j * P_i (j = 0..N-1); its index in
    Z^N is the ideal norm (0 -> infinite index would mean rank deficit, which
    cannot happen for nonzero P since z^N+1 has no ternary factors).  Exact
    integer Hermite-style elimination; the norm is the product of pivots.
    """
    rows = []
    for P in polys:
        v = tuple(P) + (0,) * (N - len(P))
        for j in range(N):
            rows.append(list(ring_mult_shift_int(v, j)))
    # integer row echelon via gcd elimination
    norm = 1
    for col in range(N):
        piv = None
        for r in range(len(rows)):
            if rows[r][col] != 0 and all(x == 0 for x in rows[r][:col]):
                if piv is None or abs(rows[r][col]) < abs(rows[piv][col]):
                    piv = r
        if piv is None:
            return 0
        changed = True
        while changed:
            changed = False
            for r in range(len(rows)):
                if r != piv and rows[r][col] != 0 and all(x == 0 for x in rows[r][:col]):
                    f = rows[r][col] // rows[piv][col]
                    rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
                    if rows[r][col] != 0:
                        if abs(rows[r][col]) < abs(rows[piv][col]):
                            piv = r
                        changed = True
        norm *= abs(rows[piv][col])
        rows = [rows[r] for r in range(len(rows)) if r != piv and any(rows[r][col:])]
        rows = [[x for x in row] for row in rows]
    return norm


def ring_mult_shift_int(v: tuple, k: int) -> tuple:
    out = [0] * N
    for e, c in enumerate(v):
        if c:
            f, s = census.fold(e + k, 1, N)
            out[f] += c * s
    return tuple(out)


def e2_pair_first(rng: random.Random, trials: int) -> dict:
    """Two-orbit engineering: N((P1,P2))'s admissible prime divisors are
    EXACTLY the primes where both orbits vanish at a common embedding."""
    rows, n_success, timeouts = [], 0, 0
    for i in range(trials):
        if i % 25 == 0:
            print(f"  e2 trial {i}/{trials} t={time.time()-T0:.0f}s", flush=True)
        try:
            with time_limit(20):
                s1, g1 = random_ternary(rng, 5)
                s2, g2 = random_ternary(rng, 5)
                if census.orbit_key(s1, g1, N) == census.orbit_key(s2, g2, N):
                    continue
                Nn = ideal_norm([poly_from(s1, g1), poly_from(s2, g2)])
                adm = []
                if Nn > 1:
                    adm = [
                        q
                        for q, _ in factorize(Nn, rng).items()
                        if q % NPRIME == 1 and q >= 97
                    ]
                n_success += bool(adm)
                rows.append({"ideal_norm": Nn, "admissible_two_orbit_primes": adm})
        except TrialTimeout:
            timeouts += 1
            print(f"  e2 trial {i} TIMEOUT (>20s), skipped", flush=True)
    norms = [r["ideal_norm"] for r in rows]
    return {
        "experiment": "E2_pair_ideal_norm",
        "pairs": len(rows),
        "trial_timeouts": timeouts,
        "norm_hist_small": dict(Counter(n for n in norms if n <= 64)),
        "norms_gt_64": sorted(n for n in norms if n > 64)[:20],
        "pairs_with_admissible_two_orbit_prime": n_success,
        "success_rate": round(n_success / max(len(rows), 1), 4),
        "examples": [r for r in rows if r["admissible_two_orbit_primes"]][:6],
    }


def e3_triple_ideal(rng: random.Random, trials: int) -> dict:
    """Three-orbit engineering: N((P1,P2,P3))'s admissible divisors are the
    triple-orbit primes.  Pre-registered: trivially small for generic triples."""
    norms, structured, timeouts = [], [], 0
    for i in range(trials):
        if i % 25 == 0:
            print(f"  e3 trial {i}/{trials} t={time.time()-T0:.0f}s", flush=True)
        try:
            with time_limit(20):
                polys = []
                while len(polys) < 3:
                    s, g = random_ternary(rng, 5)
                    if all(census.orbit_key(s, g, N) != census.orbit_key(s2, g2, N) for s2, g2, _ in polys):
                        polys.append((s, g, poly_from(s, g)))
                Nn = ideal_norm([p for _, _, p in polys])
                norms.append(Nn)
                if Nn > 1:
                    adm = [q for q in factorize(Nn, rng) if q % NPRIME == 1 and q >= 97]
                    if adm:
                        structured.append({"norm": Nn, "admissible": adm})
        except TrialTimeout:
            timeouts += 1
            print(f"  e3 trial {i} TIMEOUT (>20s), skipped", flush=True)
    return {
        "experiment": "E3_triple_ideal_norm",
        "triples": len(norms),
        "trial_timeouts": timeouts,
        "norm_hist_small": dict(Counter(n for n in norms if n <= 64)),
        "max_norm": max(norms) if norms else None,
        "triples_with_admissible_prime": len(structured),
        "structured_examples": structured[:5],
        "verdict": "TRIPLE_ENGINEERING_DEAD" if not structured else "TRIPLE_CHANNEL_OPEN",
    }


T0 = time.time()

if __name__ == "__main__":
    rng = random.Random(20260706)
    # GATE: ideal_norm of a single element == |N(P)| == |Res(x^N+1, P)|
    XN1 = [1] + [0] * (N - 1) + [1]
    for _ in range(12):
        s, g = random_ternary(rng, rng.choice((3, 4, 5)))
        P = poly_from(s, g)
        assert ideal_norm([P]) == abs(resultant(XN1, P)), "ideal_norm gate FAILED"
    print("GATE ideal_norm==|N(P)| x12: PASS")
    trials = 60 if "--quick" in sys.argv else 250
    out = {
        "e1": e1_prime_first(rng, trials),
        "e2": e2_pair_first(rng, trials),
        "e3": e3_triple_ideal(rng, trials),
    }
    (HERE / "resultant_gate_results.json").write_text(json.dumps(out, indent=1))
    for k, v in out.items():
        head = {kk: vv for kk, vv in v.items() if kk not in ("rows", "examples", "structured_examples")}
        print(k, json.dumps(head))
