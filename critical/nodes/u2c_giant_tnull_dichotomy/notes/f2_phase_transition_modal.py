#!/usr/bin/env python3
"""F2 campaign (Modal): THE DEEP-REGIME PHASE TRANSITION, OBSERVED
(cycle 119). Meet-in-the-middle makes the exact n=32, j=3 census
O(2^16) per prime: extras(q) is measurable across the full phase
diagram, through the deep-regime theorem's boundary.

Per prime q = 1 mod 32: N_total^{(3)} = #{T subset mu_32 :
p_1 = p_2 = p_3 = 0} by MTM (split 16+16, hash side-A moment
vectors, look up negated complements); extras = N_total - 2^8
(struct = mod-4 class unions, satellite 22 / Lam-Leung note).

PRE-REGISTERED READS (satellite 29's theorem, made visible):
  (a) SHALLOW (q^3 << 2^32, i.e. q <~ 1000): extras > 0 common
      (flat census dominates: E[N] ~ 2^32/q^3 >> struct);
  (b) DEEP (q^3 >> 2^32 n^2, i.e. q >~ 20000): extras = 0 for
      almost all primes (cyclotomic rigidity; sporadic primes
      dividing fixed norms allowed, expected rare);
  (c) the transition sits near occupancy 1 (q^3 ~ 2^32, q ~ 1626).
CONFIRM: (a) and (b) both observed with the transition in between;
REFUTE the theorem: any consistent extras > 0 population at deep
primes (would contradict a THEOREM — bank at maximum volume).
"""
import math

import modal

app = modal.App("rs-mca-f2-phase-transition")
image = modal.Image.debian_slim()

# prime batches (q = 1 mod 32), spanning the diagram
BATCHES = [
    ("shallow", 97, 1000, 20), ("mid", 1000, 5000, 20),
    ("boundary", 5000, 20000, 20), ("deep", 20000, 80000, 20),
    ("very-deep", 80000, 300000, 15),
]


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def batch(job):
    label, lo, hi, want = job
    n, j = 32, 3
    STRUCT = 2 ** (n // 4)

    def is_prime(m):
        if m < 2:
            return False
        for d in range(2, int(m ** 0.5) + 1):
            if m % d == 0:
                return False
        return True

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

    # evenly sample primes = 1 mod 32 in [lo, hi)
    primes = []
    step = max(1, (hi - lo) // (want * 40))
    q = lo + (32 - lo % 32) + 1
    while q < hi and len(primes) < want:
        if q % 32 == 1 and is_prime(q):
            primes.append(q)
            q += step * 32
        q += 32
    rows = []
    for q in primes:
        g = next(c for c in range(2, q)
                 if all(pow(c, (q - 1) // r, q) != 1
                        for r in set(pf(q - 1))))
        h = pow(g, (q - 1) // n, q)
        D = [pow(h, i, q) for i in range(n)]
        A, B = D[:16], D[16:]

        def half_vectors(H):
            vecs = [(0, 0, 0)] * (1 << 16)
            pw = [(x % q, x * x % q, pow(x, 3, q)) for x in H]
            for m in range(1, 1 << 16):
                lb = m & (-m)
                i = lb.bit_length() - 1
                pm = vecs[m ^ lb]
                e = pw[i]
                vecs[m] = ((pm[0] + e[0]) % q, (pm[1] + e[1]) % q,
                           (pm[2] + e[2]) % q)
            return vecs

        va = half_vectors(A)
        vb = half_vectors(B)
        from collections import defaultdict
        cnt = defaultdict(int)
        for v in va:
            cnt[v] += 1
        N = 0
        for v in vb:
            N += cnt.get(((q - v[0]) % q, (q - v[1]) % q,
                          (q - v[2]) % q), 0)
        rows.append((q, N - STRUCT))
    return {"label": label, "rows": rows}


@app.local_entrypoint()
def main():
    res = list(batch.map(BATCHES, return_exceptions=True))
    fails = 0
    summary = {}
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        rows = r["rows"]
        nz = [(q, e) for (q, e) in rows if e != 0]
        summary[r["label"]] = (len(rows), len(nz))
        exs = ", ".join(f"{q}:{e}" for q, e in nz[:6])
        print(f"[{r['label']:>9}] {len(rows)} primes, extras != 0 at "
              f"{len(nz)}  ({exs}{'...' if len(nz) > 6 else ''})")
    sh = summary.get("shallow", (0, 0))
    dp = summary.get("deep", (1, 1))
    vd = summary.get("very-deep", (1, 1))
    confirm = (sh[1] > sh[0] // 2 and
               dp[1] <= max(1, dp[0] // 5) and
               vd[1] <= max(1, vd[0] // 5))
    print(f"\nREAD: shallow extras-rate {sh[1]}/{sh[0]}; deep "
          f"{dp[1]}/{dp[0]}; very-deep {vd[1]}/{vd[0]}")
    print("=> PHASE TRANSITION OBSERVED (theorem visible)" if confirm
          else "=> PATTERN UNEXPECTED — examine before banking")
    if fails or not confirm:
        raise SystemExit(f"F2_PHASE_TRANSITION_FLAG ({fails})")
    print("\nF2_PHASE_TRANSITION_PASS")
