#!/usr/bin/env python3
"""F2 campaign (Modal): FALSIFIER WATCH W3 — the transition band at
(n=32, j=3) via meet-in-the-middle (cycle 120). Populations q^3 up
to ~8e9: 200x beyond the previous 44M watch frontier, in the band
where extras genuinely fluctuate (the deep regime beyond is exactly
zero — cycle 119 — and carries no test).

Exact censuses by MTM:
  rung 1: N = #{T : p_1=p_2=p_3=0}, subsets split 16+16, integer
          sort-merge join on encoded moment keys;
  rung 2: C'' = sum_{delta in {0,+-1}^32, moments 0} 2^{#zeros},
          signed patterns 3^16 per half, per-key weight sums joined.
Alignment (satellite 20 form, integers throughout):
  extras_dev = (q^3 N - 2^32) - 256 (q^3 - 1)        [struct = 2^8]
  denom^2    = q^3 C'' - 4^32                        [ladder identity]
  ratio'     = |extras_dev| / sqrt(denom^2);  per-orbit = ratio'/sqrt(32).

PRE-REGISTERED READS: per-orbit constants in the established O(1)
band (~[0.03, 3]) => the Rademacher model holds in the transition
band at populations 200x every prior watch; kill line: per-orbit
constant > 10 at 3+ primes => T-FLOOR CANDIDATE — bank at maximum
volume. Non-vacuity: report extras itself; at least 3 primes must
have extras != 0 for the watch to have teeth (else extend range
downward).
"""
import math

import modal

app = modal.App("rs-mca-f2-watch-w3")
image = modal.Image.debian_slim().pip_install("numpy")

PRIMES = [193, 257, 353, 449, 577, 641, 769, 929, 1153, 1409,
          1601, 1697, 2113]  # all = 1 mod 32 (997 removed: catch #24)


@app.function(image=image, cpu=4, memory=16384, timeout=280)
def one_prime(q):
    n, j = 32, 3
    assert j <= 3, "struct = 2^(n/4) is the j <= 3 census ONLY (catch #28)"
    assert (q - 1) % n == 0, f"mu_{n} does not exist in F_{q}"
    import numpy as np

    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d)
                x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = [pow(h, i, q) for i in range(n)]
    A, B = D[:16], D[16:]
    q2 = q * q

    def keys_subsets(H):
        pw = np.array([[x % q, x * x % q, pow(x, 3, q)] for x in H],
                      dtype=np.int64)
        m = np.arange(1 << 16, dtype=np.int64)
        v = np.zeros((1 << 16, 3), dtype=np.int64)
        for i in range(16):
            bit = ((m >> i) & 1).astype(bool)
            v[bit] += pw[i]
        v %= q
        return v[:, 0] + q * v[:, 1] + q2 * v[:, 2]

    def join_count(kA, kB, wA=None, wB=None):
        # sum over matching pairs of wA*wB (weights default 1)
        order = np.argsort(kA, kind="stable")
        kAs = kA[order]
        wAs = (wA[order] if wA is not None
               else np.ones(len(kA), dtype=np.float64))
        uniq, start = np.unique(kAs, return_index=True)
        sums = np.add.reduceat(wAs, start)
        # negate B keys: key of (-v) componentwise
        v1 = kB % q
        v2 = (kB // q) % q
        v3 = kB // q2
        nk = ((q - v1) % q) + q * ((q - v2) % q) + q2 * ((q - v3) % q)
        idx = np.searchsorted(uniq, nk)
        idx[idx >= len(uniq)] = 0
        match = uniq[idx] == nk
        wBv = (wB if wB is not None
               else np.ones(len(kB), dtype=np.float64))
        return float((sums[idx] * wBv * match).sum())

    # rung 1 (exact; counts are small integers -> float64 exact)
    kA = keys_subsets(A)
    kB = keys_subsets(B)
    N = int(round(join_count(kA, kB)))

    def keys_signed(H):
        pw = np.array([[x % q, x * x % q, pow(x, 3, q)] for x in H],
                      dtype=np.int64)
        t = np.arange(3 ** 16, dtype=np.int64)
        v = np.zeros((3 ** 16, 3), dtype=np.int64)
        zeros = np.zeros(3 ** 16, dtype=np.int64)
        tt = t.copy()
        for i in range(16):
            d3 = tt % 3  # 0 -> coeff 0, 1 -> +1, 2 -> -1
            tt //= 3
            plus = d3 == 1
            minus = d3 == 2
            v[plus] += pw[i]
            v[minus] -= pw[i]
            zeros += (d3 == 0)
        v %= q
        keys = v[:, 0] + q * v[:, 1] + q2 * v[:, 2]
        w = np.exp2(zeros.astype(np.float64))
        return keys, w

    kA2, wA2 = keys_signed(A)
    kB2, wB2 = keys_signed(B)
    Cpp = join_count(kA2, kB2, wA2, wB2)  # float64; <= 4^32 ~ 1.8e19
    # relative float error ~1e-16*sqrt(#terms) — Cpp needed to ~1e-6
    STRUCT1 = 2 ** 8
    Q3 = q ** 3
    extras = N - STRUCT1
    assert extras >= 0, "census below forced struct floor: invalid row"
    extras_dev = (Q3 * N - 2 ** 32) - STRUCT1 * (Q3 - 1)
    denom2 = Q3 * Cpp - 4.0 ** 32
    ratio = abs(extras_dev) / math.sqrt(denom2)
    return {"q": q, "N": N, "extras": extras,
            "ratio": float(ratio),
            "per_orbit": float(ratio / math.sqrt(32)),
            "pop": float(Q3)}


@app.local_entrypoint()
def main():
    res = list(one_prime.map(PRIMES, return_exceptions=True))
    fails = 0
    teeth = 0
    kills = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        if r["extras"]:
            teeth += 1
        if r["per_orbit"] > 10:
            kills += 1
        print(f"q={r['q']:>5} pop={r['pop']:.1e}: extras={r['extras']:>6} "
              f" ratio'={r['ratio']:8.2f}  per-orbit="
              f"{r['per_orbit']:6.3f}")
    print(f"\nteeth (extras != 0): {teeth} primes; kill-line hits: "
          f"{kills}")
    if kills >= 3:
        print("=> T-FLOOR CANDIDATE — bank at maximum volume")
        fails += 1
    elif teeth >= 3:
        print("=> MODEL HOLDS in the transition band at 200x the "
              "prior frontier")
    else:
        print("=> insufficient teeth — extend range downward")
    if fails:
        raise SystemExit(f"F2_WATCH_W3_FAIL ({fails})")
    print("\nF2_WATCH_W3_PASS")
