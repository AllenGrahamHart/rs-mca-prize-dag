#!/usr/bin/env python3
r"""
Modal dispatch job for node: single_obstruction_valueset.

============================ PRE-REGISTERED SPEC ============================
(quoted verbatim from prize/nodes/single_obstruction_valueset/statement.md)

  "THE LEMMA UNDER midlarge_h20_A: for h > 20 at official-shape rows, the first
   obstruction O_{h-1}, restricted to anchored cores, takes >= C(n,h)/budget
   distinct values in F_p (equivalently: its fibers are small). EVIDENCE WALL:
   the value-distribution scan -- sample anchored cores at h = 21..40,
   calibration rows, measure O-value collision rates; pre-registered: collision
   rate consistent with uniform => the lemma's shape is right; heavy collisions
   => route dead, fall back to per-h certificates."

  Falsifier: "O-value collision rates far above uniform at any calibration row."
============================================================================

CONSTRUCTION (the obstruction O, faithful to the banked X78/X79 machinery
experimental/scripts/verify_x78_h5_square_shift_supports.py and
verify_x79_h5_obstruction_norm_gate.py, generalized from the hardcoded h=5
degree-10 case to arbitrary h/degree-2h):

  A minimal h-trade has 2h-point support R = P u Q subset mu_n.  Its locator
  L_R = prod_{x in R}(X - x) is monic of degree 2h.  The monic degree-h square
  root S of L_R + lambda is FORCED by the top h+1 coefficients (degrees 2h down
  to h) via the same recursion X78/X79 use for h=5.  The low coefficients of
  S^2 - L_R at degrees X^1..X^{h-1} are the h-1 obstruction values; a finite
  h-trade forces ALL of them to vanish mod p (X79's multi-obstruction gate).
  The "first obstruction" O_{h-1} is the top one: coefficient of X^{h-1} of
  S^2 - L_R.  This scan measures the value distribution / collision rate of
  O_{h-1}(R) over sampled 2h-supports ("anchored cores") vs the uniform-on-F_p
  baseline C(N,2)/p.

CORRECTNESS GATE (must pass in-cloud before the scan):
  G1 (banked X79 fact, h=5): build an explicit h=5 trade L = A*B with B = A
     shifted in the constant term; the generalized forced root must recover the
     midpoint S = (A+B)/2, all 4 obstructions must vanish, lambda = delta^2/4
     is a nonzero square (reproduces verify_x79 algebra_checks).
  G2 (generalization to h in {6,10,21,40}): same trade construction at general
     h -- all h-1 obstructions vanish, lambda a nonzero square.
  G3 (O_{h-1} sensitivity): bumping ONLY the degree-(h-1) coefficient of a trade
     locator by 1 leaves the forced root unchanged and flips O_{h-1} to exactly
     that bump (proves O_{h-1} isolates the X^{h-1} coefficient).

Self-contained (stdlib only; no repo mount).  Prints one JSON line prefixed
with the node name for retrieval from `modal app logs`.
"""

import modal
import json
import math
import random
import time

app = modal.App("rs-mca-single_obstruction_valueset")
image = modal.Image.debian_slim()


# ----------------------------- arithmetic ----------------------------------
_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(m: int) -> bool:
    m = int(m)
    if m < 2:
        return False
    for q in _SMALL_PRIMES:
        if m % q == 0:
            return m == q
    d = m - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in _SMALL_PRIMES:
        x = pow(a, d, m)
        if x == 1 or x == m - 1:
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def next_prime_1mod(n: int, start: int) -> int:
    t = (start - 1) // n
    if t < 1:
        t = 1
    while True:
        p = 1 + n * t
        if p >= start and is_prime(p):
            return p
        t += 1


def primitive_root(p: int) -> int:
    factors = []
    x = p - 1
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise AssertionError("no primitive root")


def mu_domain(p: int, n: int) -> list:
    g = primitive_root(p)
    zeta = pow(g, (p - 1) // n, p)
    return [pow(zeta, i, p) for i in range(n)]


# ----------------------------- polynomials ---------------------------------
def poly_mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def poly_square(a, p):
    return poly_mul(a, a, p)


def locator_from_roots(roots, p):
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs) + 1)
        for i, coeff in enumerate(coeffs):
            nxt[i] = (nxt[i] - coeff * root) % p
            nxt[i + 1] = (nxt[i + 1] + coeff) % p
        coeffs = nxt
    return coeffs


def square_shift_root(L, p, h):
    """Generalized forced monic degree-h square root of L (monic, degree 2h).
    Identical recursion to X78's hardcoded h=5 (verify_x78 lines 137-162),
    with 5 -> h.  Returns S (length h+1, s[h]=1)."""
    inv2 = pow(2, -1, p)
    s = [0] * (h + 1)
    s[h] = 1
    for degree in range(2 * h - 1, h - 1, -1):
        unknown = degree - h
        known = 0
        lo = max(0, degree - h)
        hi = min(h, degree)
        for i in range(lo, hi + 1):
            j = degree - i
            if not (0 <= j <= h):
                continue
            if i == unknown or j == unknown:
                continue
            known = (known + s[i] * s[j]) % p
        s[unknown] = ((L[degree] - known) * inv2) % p
    return s


def forced_obstructions(L, p, h):
    """Return (S, obstructions[1..h-1], lambda). obstructions[i] = coeff of X^i
    in S^2 - L, i=1..h-1.  O_{h-1} = obstructions[-1]."""
    S = square_shift_root(L, p, h)
    S2 = poly_square(S, p)
    obs = [(S2[i] - L[i]) % p for i in range(1, h)]
    lam = (S2[0] - L[0]) % p
    return S, obs, lam


def is_square_mod(a, p):
    if a % p == 0:
        return True
    return pow(a, (p - 1) // 2, p) == 1


# ------------------------------- the GATE ----------------------------------
def run_gate():
    fails = []

    def ck(name, cond):
        if not cond:
            fails.append(name)

    # G1: banked X79 h=5 fact
    p = 101
    A = locator_from_roots([2, 3, 5, 7, 11], p)  # monic deg 5
    delta = 13
    B = list(A)
    B[0] = (B[0] + delta) % p
    L = poly_mul(A, B, p)  # deg 10
    S, obs, lam = forced_obstructions(L, p, 5)
    midpoint = [((a + b) * pow(2, -1, p)) % p for a, b in zip(A, B)]
    ck("G1 forced root = midpoint (h=5)", S == midpoint)
    ck("G1 all 4 obstructions vanish (h=5 trade)", all(v == 0 for v in obs))
    ck("G1 lambda = delta^2/4 nonzero square", lam == (delta * delta * pow(4, -1, p)) % p and lam != 0 and is_square_mod(lam, p))

    # G2: generalization to several h
    g2 = {}
    for h in (6, 10, 21, 40):
        pp = next_prime_1mod(256, 256 * 256)  # a prime with mu_256 available, plenty of elements
        roots = random.Random(7 * h).sample(range(2, pp - 1), h)
        Ah = locator_from_roots(roots, pp)
        dl = 29
        Bh = list(Ah)
        Bh[0] = (Bh[0] + dl) % pp
        Lh = poly_mul(Ah, Bh, pp)
        Sh, obsh, lamh = forced_obstructions(Lh, pp, h)
        mid = [((a + b) * pow(2, -1, pp)) % pp for a, b in zip(Ah, Bh)]
        ok = (Sh == mid and all(v == 0 for v in obsh) and lamh == (dl * dl * pow(4, -1, pp)) % pp and is_square_mod(lamh, pp))
        g2[h] = ok
        ck(f"G2 h={h} trade -> all {h-1} obstructions vanish, lambda square", ok)

    # G3: O_{h-1} isolates the X^{h-1} coefficient
    h = 10
    pp = next_prime_1mod(256, 256 * 256)
    roots = random.Random(99).sample(range(2, pp - 1), h)
    Ah = locator_from_roots(roots, pp)
    Bh = list(Ah)
    Bh[0] = (Bh[0] + 17) % pp
    Lh = poly_mul(Ah, Bh, pp)
    _, obs0, _ = forced_obstructions(Lh, pp, h)
    Lp = list(Lh)
    Lp[h - 1] = (Lp[h - 1] + 1) % pp  # bump only degree h-1
    _, obs1, _ = forced_obstructions(Lp, pp, h)
    ck("G3 O_{h-1} moves by exactly -1 under a unit bump of coeff X^{h-1}",
       (obs1[-1] - obs0[-1]) % pp == (-1) % pp)
    ck("G3 all other obstructions unchanged by the X^{h-1} bump",
       obs0[:-1] == obs1[:-1])

    return {"gate_pass": len(fails) == 0, "gate_fails": fails, "g2_by_h": g2}


# ------------------------------- the SCAN ----------------------------------
def scan(total_budget_s=8600.0):
    # calibration / official-shape rows: n a power of two, p == 1 mod n.
    # q ~ n^2 and q ~ n^3 (matching the x12 calibration regime).
    rows = []
    for (n, exp) in [(128, 2), (128, 3), (256, 2)]:
        p = next_prime_1mod(n, n ** exp)
        rows.append({"n": n, "q_exp": exp, "p": p, "domain": mu_domain(p, n)})

    hs = list(range(21, 41))
    configs = [(r, h) for r in rows for h in hs]
    budget_per = total_budget_s / max(1, len(configs))

    N_cap = 60000
    out_rows = []
    for (r, h) in configs:
        n, p, dom = r["n"], r["p"], r["domain"]
        two_h = 2 * h
        if two_h > n:
            out_rows.append({"n": n, "q_exp": r["q_exp"], "p": p, "h": h,
                             "skipped": "2h>n", "samples": 0})
            continue
        rng = random.Random(1000 * h + n + r["q_exp"])
        counts = {}
        zero_hits = 0
        N = 0
        t0 = time.time()
        while N < N_cap and (time.time() - t0) < budget_per:
            exps = rng.sample(range(n), two_h)
            roots = [dom[i] for i in exps]
            L = locator_from_roots(roots, p)  # monic deg 2h
            _, obs, _ = forced_obstructions(L, p, h)
            o = obs[-1]  # O_{h-1}
            counts[o] = counts.get(o, 0) + 1
            if o == 0:
                zero_hits += 1
            N += 1
        distinct = len(counts)
        max_fiber = max(counts.values()) if counts else 0
        obs_coll = sum(c * (c - 1) // 2 for c in counts.values())
        # uniform-on-F_p baseline for the same N (birthday):
        exp_coll_uniform = (N * (N - 1) / 2.0) / p if N > 1 else 0.0
        ratio = (obs_coll / exp_coll_uniform) if exp_coll_uniform > 0 else None
        # also compare distinct-value count vs uniform expectation
        exp_distinct_uniform = p * (1.0 - math.exp(-N / p)) if p > 0 else 0.0
        verdict = None
        if ratio is not None:
            verdict = "UNIFORM_CONSISTENT" if ratio <= 3.0 else "HEAVY_COLLISIONS"
        out_rows.append({
            "n": n, "q_exp": r["q_exp"], "p": p, "h": h,
            "samples": N,
            "distinct_O_values": distinct,
            "max_fiber": max_fiber,
            "modal_fiber_frac": round(max_fiber / N, 6) if N else None,
            "O_eq_zero_hits": zero_hits,
            "observed_collision_pairs": obs_coll,
            "expected_collision_pairs_uniform": round(exp_coll_uniform, 3),
            "collision_ratio_vs_uniform": round(ratio, 4) if ratio is not None else None,
            "distinct_expected_uniform": round(exp_distinct_uniform, 2),
            "verdict": verdict,
        })
    any_heavy = any(r.get("verdict") == "HEAVY_COLLISIONS" for r in out_rows)
    return {
        "rows_scanned": [{"n": r["n"], "q_exp": r["q_exp"], "p": r["p"]} for r in rows],
        "h_range": [21, 40],
        "per_config": out_rows,
        "any_heavy_collisions": any_heavy,
        "overall_verdict": ("FALSIFIER_HEAVY_COLLISIONS_FOUND" if any_heavy
                            else "UNIFORM_CONSISTENT_LEMMA_SHAPE_SUPPORTED"),
    }


@app.function(image=image, cpu=4, memory=8192, timeout=10800)
def run():
    gate = run_gate()
    if not gate["gate_pass"]:
        result = {"node": "single_obstruction_valueset", "status": "GATE_FAILED",
                  "gate": gate}
        print("single_obstruction_valueset " + json.dumps(result), flush=True)
        return result
    sc = scan()
    result = {"node": "single_obstruction_valueset", "status": "OK",
              "gate": gate, "scan": sc}
    print("single_obstruction_valueset " + json.dumps(result), flush=True)
    return result


@app.local_entrypoint()
def main():
    call = run.spawn()
    print("SPAWNED single_obstruction_valueset fc_id=" + str(call.object_id))
