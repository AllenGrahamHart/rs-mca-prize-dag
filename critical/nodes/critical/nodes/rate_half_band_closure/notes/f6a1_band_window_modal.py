#!/usr/bin/env python3
"""F6-A1 (floor campaign, Modal): the band window-law test at toy rate-1/2 rows.

FLOOR UNDER ATTACK (F6 v2, BAND-DETERMINATION): at admissible rate-1/2
razor rows, the band determination equals the first-moment prediction —
true list counts track the first-moment model through the band between
the floor family's reach and the first-moment crossing.

TOY TRANSPORT (pre-registered BEFORE running; conventions from
cap_envelope verify_sweep.py + e22_core.py):
  Row: D = order-n multiplicative subgroup of F_q^x (q ≡ 1 mod n),
  k = n/2 (rate 1/2). List object at agreement s: #{deg<k polys agreeing
  with a word on >= s domain points}.
  FIRST-MOMENT model at agreement s (>= k): for a RANDOM word,
  E[#agree >= s] = sum_{j>=s} C(n,j) (q-1)^{n-j} ... simplified standard
  form: E[#codewords with agreement exactly j] = C(n,j) q^{k-j} (1-1/q)^{n-j}
  approx; we use the EXACT expectation computed by linearity:
  E_j = C(n, j) * q^(k-j) * (1 - 1/q)^(n-j) for j >= k, and the crossing
  sigma*_toy = max{s : sum_{j >= s} E_j > THR} with THR = q/k (the toy
  unsafe threshold, same normalization as the prize trigger).
  FLOOR REACH_toy = max{d*c : c | k, C(n/c, k/c + d) * q^{-(d-1)} > THR}
  (the quotient-remainder family, conservative box = q).
  TOY BAND = (REACH_toy, sigma*_toy - k] in excess units (nonempty only
  for some (n, q) — the script reports which; only nonempty-band rows
  inform the falsifier).
  MEASUREMENT: exact per-word list counts at band agreements for
  (a) 40 random words, (b) the E15-style planted word (the known
  adversarial class), (c) coset-structured words. Deviation metric:
  observed / first-moment (random words) and observed vs staircase+FM
  model (structured words).
FALSIFIER (pre-registered): sustained (>= 3 q-scales) deviation of the
random-word band counts from the first-moment model beyond Poisson, OR a
structured word class exceeding its charged-column model at band
agreements. Single window accidents and mechanism shortfalls do NOT count.

Exact enumeration cost: #agreement-set checks <= sum_j C(n, j) over band
j's; at n = 16 trivial, n = 20, 24 sharded by agreement-set prefix.
"""
import json
import math
from fractions import Fraction

import modal

app = modal.App("rs-mca-f6a1-band")
image = modal.Image.debian_slim().pip_install("numpy")


def toy_arithmetic(n, k, q):
    """Toy floor reach, first-moment crossing, band (exact big-int/Fraction)."""
    THR = Fraction(q, k)
    # first-moment tail crossing
    def E_exact(j):
        return (Fraction(math.comb(n, j)) * Fraction(q) ** (k - j)
                * (Fraction(q - 1, q)) ** (n - j))
    sigma_star = None
    tail = Fraction(0)
    for s in range(n, k - 1, -1):
        tail += E_exact(s)
        if tail > THR:
            sigma_star = s  # largest s where tail exceeds THR
            break
    # floor reach: quotient scales c | k, c > 1
    reach = 0
    c = 2
    while c <= k:
        if k % c == 0 and n % c == 0:
            N, base = n // c, k // c
            for d in range(1, N - base + 1):
                fam = Fraction(math.comb(N, base + d)) * Fraction(1, q) ** (d - 1)
                if fam > THR and d * c > reach:
                    reach = d * c
        c *= 2
    return {"THR": float(THR), "sigma_star": sigma_star,
            "floor_reach_excess": reach - 1 if reach else 0,
            "band_lo_agree": k + reach, "band_hi_agree": sigma_star}


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def exact_list_at(payload):
    """Exact #codewords (deg<k polys) agreeing >= s with the given word,
    counted by exhaustive agreement-set enumeration with interpolation.
    Sharded by first agreement index."""
    import itertools
    n, k, q, s, word, shard, nshards = (payload["n"], payload["k"], payload["q"],
                                        payload["s"], payload["word"],
                                        payload["shard"], payload["nshards"])
    # domain: order-n subgroup
    g = None
    for cand in range(2, q):
        if pow(cand, n, q) == 1 and all(pow(cand, n // p, q) != 1
                                        for p in (2, 3, 5, 7, 11, 13) if n % p == 0):
            g = cand
            break
    D = [pow(g, i, q) for i in range(n)]

    def interp_check(idxs):
        """Is there a deg<k poly through word at idxs, and does it agree on
        >= s points total? Count each codeword once via its minimal
        agreement set: use exactly-k-subsets as interpolation anchors and
        dedupe by resulting coefficient tuple."""
        pass

    # enumeration: interpolate through every k-subset of a candidate
    # agreement superset is too slow; instead enumerate k-subsets of the
    # n points (C(n,k) at n=16: 12870 — fine), interpolate, then count
    # the poly's total agreement; dedupe by coefficients.
    seen = {}
    combos = list(itertools.combinations(range(n), k))
    lo = (len(combos) * shard) // nshards
    hi = (len(combos) * (shard + 1)) // nshards
    for idxs in combos[lo:hi]:
        xs = [D[i] for i in idxs]
        ys = [word[i] for i in idxs]
        # Lagrange interpolation mod q -> coefficient tuple
        coeffs = [0] * k
        for xi, yi in zip(xs, ys):
            num = [1]
            den = 1
            for xj in xs:
                if xj == xi:
                    continue
                num = [(a * (-xj)) % q for a in num] + [0]
                for t in range(len(num) - 1):
                    num[t] = (num[t] + ([1] + [0] * (len(num) - 1))[0] * 0) % q
            # simpler: build numerator polynomial iteratively
            num = [1]
            den = 1
            for xj in xs:
                if xj == xi:
                    continue
                new = [0] * (len(num) + 1)
                for t, a in enumerate(num):
                    new[t] = (new[t] - a * xj) % q
                    new[t + 1] = (new[t + 1] + a) % q
                num = new
                den = den * (xi - xj) % q
            scale = yi * pow(den, -1, q) % q
            for t in range(len(num)):
                coeffs[t] = (coeffs[t] + scale * num[t]) % q
        key = tuple(coeffs)
        if key in seen:
            continue
        agree = sum(1 for i in range(n)
                    if sum(c * pow(D[i], t, q) for t, c in enumerate(coeffs)) % q
                    == word[i])
        seen[key] = agree
    return {"counts": {str(s0): sum(1 for a in seen.values() if a >= s0)
                       for s0 in range(k, n + 1)},
            "shard": shard}


@app.local_entrypoint()
def main():
    import random
    rows = []
    for n, ks in [(16, 8)]:
        # q ≡ 1 mod n, three scales
        qs = []
        q = n + 1
        while len(qs) < 3 and q < 20000:
            def isp(m):
                if m < 2:
                    return False
                for p in range(2, int(m**0.5) + 1):
                    if m % p == 0:
                        return False
                return True
            if isp(q):
                qs.append(q)
            q += n
        # spread scales: first, ~10x, ~100x
        qs = [qs[0]]
        for target in (300, 3000):
            qq = target - (target % n) + 1
            while not all(qq % p for p in range(2, int(qq**0.5) + 1)):
                qq += n
            qs.append(qq)
        for q in qs:
            rows.append((n, ks, q))
    report = []
    for n, k, q in rows:
        arith = toy_arithmetic(n, k, q)
        print(f"row n={n} k={k} q={q}: {arith}")
        report.append({"n": n, "k": k, "q": q, "arith": arith})
    with open("/tmp/f6a1_arith.json", "w") as f:
        json.dump(report, f, indent=1)
    print("arithmetic pass done — band-nonempty rows above define the "
          "measurement grid (phase 2 dispatches exact_list_at shards)")
