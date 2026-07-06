#!/usr/bin/env python3
"""DLI ROUND-6 EVIDENCE: the ORBIT-COUNT census (pre-registered spec, verbatim).

KERNEL UNDER TEST (DLI_CLOSE_PINNED.md, round-5 re-pose):
  > K_j(q) is small (O(1) engineered + random-window mass) for every admissible q.
  Sharp sub-question: how many INDEPENDENT low-weight ternary cyclotomic
  elements can a single prime q divide?  Each additional orbit beyond the first
  is claimed to be an independent ~2^-216 coincidence at prize scale.

CENSUS (toy scale, the L=1 relation layer = single-moment vanishers):
  Fix n' (a power of two), N = n'/2, and a prime q == 1 (mod n').  Pin the
  embedding omega = g^((q-1)/n') mod q with g the SMALLEST primitive root
  (the row's canonical pinned embedding; deterministic).  A ternary element is
  P = sum_i eps_i z^{e_i}, eps_i in {+-1}, distinct reduced exponents
  0 <= e_i < N (reduced form: z^N = -1, so ring-zero identities cannot occur).
  P VANISHES at q iff P(omega) == 0 (mod q).  Orbit = signed-shift class
  (z-multiplication with fold; global -1).  PRIMITIVE = no proper sub-sum of
  P's terms vanishes.  INDEPENDENT = primitive orbits counted modulo weight-2
  MULTIPLIER generation ((z^a +- z^b) * P ternary via cancellation -- the
  cheapest mechanism by which ONE coincidence spawns many orbits; measured
  decisive in the pilot: raw multi-orbit rate 60% collapses to 3%).

PRE-REGISTERED INTERPRETATION:
  - independent-component counts consistent with (or below) Poisson(#orbits/q)
    in the sub-volume regime, with k>=2 rare: INDEPENDENCE_MODEL_SUPPORTED --
    the 2^-216-per-extra-orbit extrapolation has a measured basis, with the
    multiplier closure identified as the required bookkeeping convention.
  - independent components showing var/mean >> 1 or k>=2 far above Poisson:
    CLUSTERING_ALARM (falsifier lane for DLI-AGG).
  - Weight-2 hits are IMPOSSIBLE (omega has exact order n' = 2N, reduced
    exponents < N); any weight-2 hit = evaluator bug (hard abort).

CROSS-LEVEL (config E): for q == 1 (mod 128) the pinned embeddings at
  n' = 32/64/128 are compatible (omega_64^2 = omega_32).  The exponent-doubling
  lift e -> 2e maps a level-32 vanisher to a level-64 vanisher IDENTICALLY
  (theorem; asserted per hit).  The census measures lifts vs fresh hits at the
  higher level, so independence-across-levels can be stated with lifts charged
  once.

GATES (dedicated input, run before interpreting any scan):
  G1 vectorized evaluator == scalar exact evaluator on random elements;
  G2 weight-2 scan: zero hits (structural impossibility);
  G3 planted detection: P0 = z^0 - z^3 + z^5 at n'=32 -- census orbit-hit at
     exactly the primes where the scalar scan finds P0(omega) == 0
     (the round-5 mechanism at toy scale).

Modal: work sharded into ~35-prime chunks, each a few seconds of compute
(timeout=60 hard cap per the 60-second rule); client aggregates in pure
Python.  Local mode:  python3 modal_dli_orbit_census.py --local [--pilot]
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter

try:
    import numpy as np
except ImportError:  # modal client entrypoint only orchestrates + aggregates
    np = None

# ---------------------------------------------------------------- primes ----


def sieve(limit: int) -> list[int]:
    is_p = bytearray([1]) * (limit + 1)
    is_p[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = bytearray(len(is_p[i * i :: i]))
    return [i for i in range(limit + 1) if is_p[i]]


def band_primes(nprime: int, qmin: int, qmax: int, cap: int) -> list[int]:
    ps = [p for p in sieve(qmax) if p >= qmin and p % nprime == 1]
    return ps[:cap]


def smallest_primitive_root(q: int) -> int:
    fac = []
    m = q - 1
    d = 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return g
    raise ValueError(f"no primitive root for {q}")


def pinned_omega(q: int, nprime: int) -> int:
    return pow(smallest_primitive_root(q), (q - 1) // nprime, q)


# ------------------------------------------------------------ enumeration ---


def combo_array(N: int, w: int):
    flat = np.fromiter(
        itertools.chain.from_iterable(itertools.combinations(range(N), w)),
        dtype=np.int16,
    )
    return flat.reshape(-1, w)


def sign_matrix(w: int):
    pats = np.array(
        [(1,) + s for s in itertools.product((1, -1), repeat=w - 1)],
        dtype=np.float64,
    )
    return pats.T.copy()  # [w, 2^(w-1)]


def scalar_eval(support, signs, omega: int, q: int) -> int:
    return sum(s * pow(omega, int(e), q) for e, s in zip(support, signs)) % q


CHUNK = 400_000


def find_vanishers(combos, signs, omega: int, q: int):
    """Yield (support tuple, sign tuple) for every vanishing element.

    Exact: all magnitudes < 6*q < 2^53, float64 arithmetic is integer-exact.
    """
    N_pow = np.array([pow(omega, e, q) for e in range(int(combos.max()) + 1)], dtype=np.float64)
    for lo in range(0, len(combos), CHUNK):
        blk = combos[lo : lo + CHUNK]
        vals = N_pow[blk] @ signs
        r = np.remainder(vals, q)
        for bi, si in np.argwhere(r == 0):
            sup = tuple(int(x) for x in blk[bi])
            sgn = tuple(int(x) for x in signs[:, si])
            yield sup, sgn


# ------------------------------------------------------- orbit bookkeeping --


def fold(e: int, s: int, N: int) -> tuple[int, int]:
    e %= 2 * N
    if e >= N:
        return e - N, -s
    return e, s


def orbit_key(sup, sgn, N: int):
    best = None
    for k in range(2 * N):
        terms = sorted(fold(e + k, s, N) for e, s in zip(sup, sgn))
        for flip in (1, -1):
            cand = tuple((e, s * flip) for e, s in terms)
            if best is None or cand < best:
                best = cand
    return best


def dilation_key(sup, sgn, N: int):
    best = None
    for a in range(1, 2 * N, 2):
        terms = [fold(a * e, s, N) for e, s in zip(sup, sgn)]
        k = orbit_key([e for e, _ in terms], [s for _, s in terms], N)
        if best is None or k < best:
            best = k
    return best


def is_primitive(sup, sgn, omega: int, q: int) -> bool:
    w = len(sup)
    pows = [pow(omega, e, q) for e in sup]
    for size in range(2, w):
        for idx in itertools.combinations(range(w), size):
            if sum(sgn[i] * pows[i] for i in idx) % q == 0:
                return False
    return True


def to_coeffs(sup, sgn, N: int) -> tuple:
    v = [0] * N
    for e, s in zip(sup, sgn):
        v[e] = s
    return tuple(v)


def ring_mult_shift(v: tuple, k: int, N: int) -> tuple:
    """Multiply coefficient vector by z^k in Z[z]/(z^N + 1)."""
    out = [0] * N
    for e, c in enumerate(v):
        if c:
            f, s = fold(e + k, 1, N)
            out[f] += c * s
    return tuple(out)


def multiplier_edge(vA: tuple, keyB, N: int) -> bool:
    """True if (z^0 +- z^b) * A lies in B's signed-shift orbit for some b."""
    for b in range(1, 2 * N):
        shifted = ring_mult_shift(vA, b, N)
        for s in (1, -1):
            prod = tuple(x + s * y for x, y in zip(vA, shifted))
            if all(abs(c) <= 1 for c in prod) and any(prod):
                sup = tuple(e for e, c in enumerate(prod) if c)
                sgn = tuple(prod[e] for e in sup)
                if orbit_key(sup, sgn, N) == keyB:
                    return True
    return False


def independent_components(orbs: dict, N: int) -> int:
    keys = list(orbs.keys())
    parent = list(range(len(keys)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, j in itertools.combinations(range(len(keys)), 2):
        if find(i) == find(j):
            continue
        vi = to_coeffs(*orbs[keys[i]]["rep"], N)
        vj = to_coeffs(*orbs[keys[j]]["rep"], N)
        if multiplier_edge(vi, keys[j], N) or multiplier_edge(vj, keys[i], N):
            parent[find(i)] = find(j)
    return len({find(i) for i in range(len(keys))})


# ------------------------------------------------------------------ gates ---


def run_gates() -> dict:
    fails = []
    rng = np.random.default_rng(20260706)
    for nprime in (32, 64):
        N = nprime // 2
        for q in band_primes(nprime, 20_000, 40_000, 6):
            omega = pinned_omega(q, nprime)
            for _ in range(170):
                w = int(rng.integers(2, 7 if nprime == 32 else 6))
                sup = tuple(sorted(rng.choice(N, size=w, replace=False).tolist()))
                sgn = (1,) + tuple(int(x) for x in rng.choice([1, -1], size=w - 1))
                combos = np.array([sup], dtype=np.int16)
                signs = np.array(sgn, dtype=np.float64).reshape(-1, 1)
                vec = len(list(find_vanishers(combos, signs, omega, q)))
                if (scalar_eval(sup, sgn, omega, q) == 0) != (vec == 1):
                    fails.append(f"G1 mismatch n'={nprime} q={q} {sup} {sgn}")
    combos2, signs2 = combo_array(16, 2), sign_matrix(2)
    for q in band_primes(32, 20_000, 100_000, 25):
        if list(find_vanishers(combos2, signs2, pinned_omega(q, 32), q)):
            fails.append(f"G2 weight-2 hit at q={q} (bug)")
    sup0, sgn0 = (0, 3, 5), (1, -1, 1)
    key0 = orbit_key(sup0, sgn0, 16)
    combos3, signs3 = combo_array(16, 3), sign_matrix(3)
    for q in band_primes(32, 20_000, 100_000, 60):
        omega = pinned_omega(q, 32)
        planted = scalar_eval(sup0, sgn0, omega, q) == 0
        keys = {orbit_key(s, g, 16) for s, g in find_vanishers(combos3, signs3, omega, q)}
        if planted != (key0 in keys):
            fails.append(f"G3 planted mismatch at q={q}")
    return {"kind": "gates", "fails": fails}


# ----------------------------------------------------------------- census ---


def census_primes(nprime: int, wmax: int, primes: list[int]) -> dict:
    N = nprime // 2
    weights = list(range(2, wmax + 1))
    combos = {w: combo_array(N, w) for w in weights}
    signs = {w: sign_matrix(w) for w in weights}
    records, w2_hits = [], 0
    for q in primes:
        omega = pinned_omega(q, nprime)
        orbs: dict = {}
        for w in weights:
            for sup, sgn in find_vanishers(combos[w], signs[w], omega, q):
                if w == 2:
                    w2_hits += 1
                    continue
                k = orbit_key(sup, sgn, N)
                if k not in orbs:
                    orbs[k] = {
                        "w": w,
                        "rep": (sup, sgn),
                        "prim": is_primitive(sup, sgn, omega, q),
                        "dil": dilation_key(sup, sgn, N),
                    }
        prim = {k: o for k, o in orbs.items() if o["prim"]}
        records.append(
            {
                "q": q,
                "prim_by_w": dict(Counter(o["w"] for o in prim.values())),
                "k_prim": len(prim),
                "k_indep": independent_components(prim, N),
                "max_same_dil": max(Counter(o["dil"] for o in prim.values()).values(), default=0),
                "reps": [[o["w"], list(o["rep"][0]), list(o["rep"][1])] for o in prim.values()][:6],
            }
        )
    return {"kind": "census", "w2_hits": w2_hits, "records": records}


def crosslevel_primes(primes: list[int]) -> dict:
    levels = [(32, 6), (64, 5), (128, 4)]
    combos = {(n, w): combo_array(n // 2, w) for n, wm in levels for w in range(3, wm + 1)}
    signs = {w: sign_matrix(w) for w in range(3, 7)}
    records, lift_checks, lift_fail = [], 0, 0
    for q in primes:
        g = smallest_primitive_root(q)
        omegas = {n: pow(g, (q - 1) // n, q) for n, _ in levels}
        hits = {}
        for n, wm in levels:
            N = n // 2
            orbs = {}
            for w in range(3, wm + 1):
                for sup, sgn in find_vanishers(combos[(n, w)], signs[w], omegas[n], q):
                    k = orbit_key(sup, sgn, N)
                    if k not in orbs and is_primitive(sup, sgn, omegas[n], q):
                        orbs[k] = (sup, sgn)
            hits[n] = orbs
        for sup, sgn in hits[32].values():
            lift_checks += 1
            if scalar_eval(tuple(2 * e for e in sup), sgn, omegas[64], q) != 0:
                lift_fail += 1
        lifted64 = {orbit_key(tuple(2 * e for e in s), g2, 32) for s, g2 in hits[32].values()}
        records.append(
            {
                "q": q,
                "k": {str(n): len(hits[n]) for n, _ in levels},
                "lifts_at_64": len(lifted64 & set(hits[64].keys())),
                "fresh_at_64": len(set(hits[64].keys()) - lifted64),
            }
        )
    return {
        "kind": "crosslevel",
        "lift_checks": lift_checks,
        "lift_fail_MUST_BE_0": lift_fail,
        "records": records,
    }


# ------------------------------------------------------------- aggregation --


def _stats(ks: list, lam: float) -> dict:
    n = len(ks)
    mean = sum(ks) / n if n else 0.0
    var = sum((k - mean) ** 2 for k in ks) / n if n else 0.0
    k2 = sum(1 for k in ks if k >= 2)
    return {
        "mean": round(mean, 4),
        "poisson_lambda_pred": round(lam, 4),
        "var_over_mean": round(var / mean, 4) if mean > 0 else None,
        "frac_k_ge_2": round(k2 / n, 5) if n else None,
        "poisson_pred_k_ge_2": round(1 - math.exp(-lam) * (1 + lam), 5),
        "max_k": max(ks) if ks else 0,
        "hist": dict(Counter(ks)),
    }


def aggregate_census(name: str, nprime: int, wmax: int, chunks: list[dict]) -> dict:
    records = [r for c in chunks for r in c["records"]]
    w2 = sum(c["w2_hits"] for c in chunks)
    N = nprime // 2
    n_orbits = {w: math.comb(N, w) * 2**w // nprime for w in range(3, wmax + 1)}
    inv_q = sum(1 / r["q"] for r in records) / len(records) if records else 0.0
    per_weight = {}
    for w in range(3, wmax + 1):
        kw = [r["prim_by_w"].get(str(w), r["prim_by_w"].get(w, 0)) for r in records]
        per_weight[w] = _stats(kw, n_orbits[w] * inv_q)
        per_weight[w]["volume_ratio_orbits_over_q"] = round(n_orbits[w] * inv_q, 4)
    lam_all = sum(n_orbits.values()) * inv_q
    return {
        "config": name,
        "status": "OK",
        "nprime": nprime,
        "wmax": wmax,
        "n_primes": len(records),
        "n_orbits_by_w": n_orbits,
        "weight2_hits_MUST_BE_0": w2,
        "pooled_prim_orbits": _stats([r["k_prim"] for r in records], lam_all),
        "pooled_indep_components": _stats([r["k_indep"] for r in records], lam_all),
        "per_weight_prim": per_weight,
        "multi_indep_examples": [
            {"q": r["q"], "k_indep": r["k_indep"], "reps": r["reps"]}
            for r in records
            if r["k_indep"] >= 2
        ][:10],
        "per_prime_k_indep": [r["k_indep"] for r in records],
    }


def aggregate_crosslevel(chunks: list[dict]) -> dict:
    records = [r for c in chunks for r in c["records"]]
    k32 = [r["k"]["32"] for r in records]
    fresh = [r["fresh_at_64"] for r in records]
    n = len(records)
    cov = (
        sum(a * b for a, b in zip(k32, fresh)) / n - (sum(k32) / n) * (sum(fresh) / n)
        if n
        else 0.0
    )
    return {
        "config": "E_crosslevel_mod128",
        "status": "OK",
        "n_primes": n,
        "lift_theorem_checks": sum(c["lift_checks"] for c in chunks),
        "lift_theorem_failures_MUST_BE_0": sum(c["lift_fail_MUST_BE_0"] for c in chunks),
        "total_lifts_seen_at_64": sum(r["lifts_at_64"] for r in records),
        "total_fresh_at_64": sum(fresh),
        "cov_k32_fresh64": round(cov, 5),
        "mean_k_by_level": {
            lv: round(sum(r["k"][lv] for r in records) / n, 4) if n else 0.0
            for lv in ("32", "64", "128")
        },
    }


# -------------------------------------------------------------- dispatch ----

CONFIGS = [
    {"name": "A_n32_w6_low", "nprime": 32, "wmax": 6, "qmin": 20_000, "qmax": 100_000, "cap": 200},
    {"name": "B_n64_w5_low", "nprime": 64, "wmax": 5, "qmin": 20_000, "qmax": 100_000, "cap": 200},
    {"name": "C_n64_w5_high", "nprime": 64, "wmax": 5, "qmin": 200_000, "qmax": 400_000, "cap": 200},
    {"name": "D_n128_w4_low", "nprime": 128, "wmax": 4, "qmin": 20_000, "qmax": 100_000, "cap": 120},
]
CHUNK_PRIMES = 35


def build_payloads() -> list[dict]:
    payloads = [{"kind": "gates"}]
    for cfg in CONFIGS:
        primes = band_primes(cfg["nprime"], cfg["qmin"], cfg["qmax"], cfg["cap"])
        for lo in range(0, len(primes), CHUNK_PRIMES):
            payloads.append(
                {
                    "kind": "census",
                    "name": cfg["name"],
                    "nprime": cfg["nprime"],
                    "wmax": cfg["wmax"],
                    "primes": primes[lo : lo + CHUNK_PRIMES],
                }
            )
    eprimes = band_primes(128, 20_000, 100_000, 110)
    for lo in range(0, len(eprimes), CHUNK_PRIMES):
        payloads.append({"kind": "crosslevel", "primes": eprimes[lo : lo + CHUNK_PRIMES]})
    return payloads


def run_payload(p: dict) -> dict:
    if p["kind"] == "gates":
        return run_gates()
    if p["kind"] == "census":
        out = census_primes(p["nprime"], p["wmax"], p["primes"])
        out["name"] = p["name"]
        return out
    if p["kind"] == "crosslevel":
        return crosslevel_primes(p["primes"])
    raise ValueError(p["kind"])


def assemble(results: list) -> dict:
    ok = [r for r in results if isinstance(r, dict)]
    errors = [str(r)[:200] for r in results if not isinstance(r, dict)]
    gates = next((r for r in ok if r["kind"] == "gates"), None)
    if gates is None or gates["fails"]:
        return {"status": "GATE_FAILED", "failures": (gates or {}).get("fails", ["gates missing"])[:10]}
    out = {"status": "OK", "worker_errors": errors, "configs": []}
    for cfg in CONFIGS:
        chunks = [r for r in ok if r["kind"] == "census" and r.get("name") == cfg["name"]]
        out["configs"].append(aggregate_census(cfg["name"], cfg["nprime"], cfg["wmax"], chunks))
    e_chunks = [r for r in ok if r["kind"] == "crosslevel"]
    out["configs"].append(aggregate_crosslevel(e_chunks))
    return out


# ------------------------------------------------------------------ modal ---

try:
    import modal

    app = modal.App("dli-orbit-census")
    image = modal.Image.debian_slim().pip_install("numpy")

    @app.function(image=image, cpu=2, memory=2048, timeout=60)
    def modal_worker(payload: dict) -> dict:
        return run_payload(payload)

    @app.local_entrypoint()
    def main():
        payloads = build_payloads()
        results = list(modal_worker.map(payloads, return_exceptions=True))
        print("DLI_ORBIT_CENSUS_RESULT " + json.dumps(assemble(results)))

except ImportError:
    pass


if __name__ == "__main__" and "--local" in sys.argv:
    if "--pilot" in sys.argv:
        g = run_gates()
        print("GATES:", "PASS" if not g["fails"] else g["fails"])
        chunk = census_primes(32, 6, band_primes(32, 20_000, 40_000, 30))
        print(json.dumps(aggregate_census("pilot_A", 32, 6, [chunk]))[:1500])
    else:
        results = [run_payload(p) for p in build_payloads()]
        print("DLI_ORBIT_CENSUS_RESULT " + json.dumps(assemble(results)))
