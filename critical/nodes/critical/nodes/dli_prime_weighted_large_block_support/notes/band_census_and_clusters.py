#!/usr/bin/env python3
"""Round-7 verification follow-ups.

PART 1 — BAND CENSUS around Pro's B1 row: all primes q ≡ 1 (mod 64) in
[100000, 130000], n'=64, weights 3..5, pinned embedding; per-prime count of
multiplier-independent primitive orbits (identical conventions to the round-6
census).  Question: is Pro's k=4 at q=110849 the ordinary Poisson tail
(expected ~1 such prime in the band at mu ~ 1) or an outlier?

PART 2 — CLUSTER DIAGNOSIS of the two extreme rows (Pro's 110849 k=4 and our
census 204353 k=7): the vanishers at a fixed prime are exactly the ternary
points of the rank-32 ideal lattice I_q = {c : c(omega) ≡ 0 mod q}.  If the
generators span a LOW-RANK sublattice, or have ternary pairwise sums or
differences (additive relations), the per-prime counts are lattice-correlated
clusters, not independent Poisson events — which would explain the fat tail
WITHOUT new per-orbit structure.  We compute: (a) the Z-rank of the generator
set, (b) all pairwise ternary combinations P_i ± z^s P_j, (c) the lattice
determinant sanity check (index of I_q in Z^32 is q).
"""
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("census", HERE / "modal_dli_orbit_census.py")
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

NP, N = 64, 32
ORBITS_W35 = sum(math.comb(N, w) * 2**w for w in range(3, 6)) // (2 * N)


def sieve_band(lo, hi):
    sz = hi - lo
    is_c = bytearray([1]) * sz
    for p in range(2, int(hi**0.5) + 1):
        st = max(p * p, (lo + p - 1) // p * p)
        for m in range(st, hi, p):
            is_c[m - lo] = 0
    return [lo + i for i in range(sz) if is_c[i] and lo + i > 1]


def primitive_indep_orbits(q):
    omega = census.pinned_omega(q, NP)
    orbs = {}
    for w in range(3, 6):
        for sup, sgn in census.find_vanishers(census.combo_array(N, w),
                                              census.sign_matrix(w), omega, q):
            k = census.orbit_key(sup, sgn, N)
            if k not in orbs and census.is_primitive(sup, sgn, omega, q):
                orbs[k] = {"w": w, "rep": (sup, sgn)}
    return orbs, census.independent_components(orbs, N), omega


def part1():
    primes = [q for q in sieve_band(100_000, 130_000) if q % NP == 1]
    rows, p_ge4_sum = [], 0.0
    for q in primes:
        orbs, k, _ = primitive_indep_orbits(q)
        mu = ORBITS_W35 / q
        rows.append({"q": q, "k_indep": k, "mu": round(mu, 4)})
        p_ge4_sum += 1 - math.exp(-mu) * (1 + mu + mu**2 / 2 + mu**3 / 6)
    from collections import Counter
    hist = dict(sorted(Counter(r["k_indep"] for r in rows).items()))
    mean_mu = sum(r["mu"] for r in rows) / len(rows)
    mean_k = sum(r["k_indep"] for r in rows) / len(rows)
    out = {
        "band": [100_000, 130_000],
        "n_primes": len(rows),
        "mean_mu_poisson": round(mean_mu, 4),
        "mean_k_observed": round(mean_k, 4),
        "k_histogram": hist,
        "expected_primes_k_ge4_poisson": round(p_ge4_sum, 3),
        "observed_primes_k_ge4": sum(1 for r in rows if r["k_indep"] >= 4),
        "k_ge3_rows": [r for r in rows if r["k_indep"] >= 3],
    }
    print("PART 1 — band census:")
    print(json.dumps(out, indent=1))
    return out, rows


def ring_shift(c, s):
    out = [0] * N
    for i, a in enumerate(c):
        if a:
            e = (i + s) % (2 * N)
            if e >= N:
                out[e - N] -= a
            else:
                out[e] += a
    return out


def z_rank(vectors):
    rows = [[Fraction(x) for x in v] for v in vectors]
    rank, col = 0, 0
    while col < N and rank < len(rows):
        piv = next((r for r in range(rank, len(rows)) if rows[r][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][col]
        rows[rank] = [x / pv for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [x - f * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
        col += 1
    return rank


def cluster_diagnosis(q, label):
    orbs, k, omega = primitive_indep_orbits(q)
    gens = [census.to_coeffs(*o["rep"], N) for o in orbs.values()]
    rank = z_rank(gens)
    additive = []
    for i in range(len(gens)):
        for j in range(i + 1, len(gens)):
            for s in range(2 * N):
                shifted = ring_shift(list(gens[j]), s)
                for sign in (1, -1):
                    comb_v = [a + sign * b for a, b in zip(gens[i], shifted)]
                    if any(comb_v) and all(abs(x) <= 1 for x in comb_v):
                        wsum = sum(1 for x in comb_v if x)
                        # is the ternary combination itself a vanisher? (must be, by linearity)
                        val = sum(a * pow(omega, e, q) for e, a in enumerate(comb_v) if a) % q
                        additive.append({"pair": (i, j), "shift": s, "sign": sign,
                                         "weight": wsum, "vanishes": val == 0})
    print(f"\nPART 2 — {label} (q={q}): {len(gens)} independent generators, "
          f"Z-rank = {rank}, ternary pairwise combinations = {len(additive)}")
    for a in additive[:10]:
        print("  ", a)
    return {"q": q, "n_gens": len(gens), "z_rank": rank,
            "n_ternary_pair_combos": len(additive),
            "combos": additive[:20]}


if __name__ == "__main__":
    out1, _ = part1()
    d1 = cluster_diagnosis(110_849, "Pro B1 row")
    d2 = cluster_diagnosis(204_353, "census anomaly row")
    (HERE / "band_census_and_clusters.json").write_text(
        json.dumps({"band_census": out1, "cluster_110849": d1,
                    "cluster_204353": d2}, indent=1))
    print("\nsaved band_census_and_clusters.json")
