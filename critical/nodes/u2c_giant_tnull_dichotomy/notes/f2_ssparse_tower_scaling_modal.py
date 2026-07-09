#!/usr/bin/env python3
"""F2 campaign (Modal): s-SPARSE TOWER SCALING — the flagged
falsification check (log #39) before the edge application relies on
the tower mechanism.

Per scale n = 2^s0 and sparsity s: the tower bound
  B(E) = min_j 2^j * (2 * span_j(E) + s - 1),
  span_j(E) = min over odd k mod m of max_{e in E, e != 0}
              |k e mod± m|,   m = n / 2^j,
measured on (a) RANDOM s-sparse exponent sets (adversarial baseline;
Dirichlet predicts ~n^{1-1/(s-1)}) and (b) APPLICATION-SHAPED sets
(p-multiples {0, p, 2p, .., (s-2)p} + one window exponent T+1, the
mid-band edge divisor shape; AP-normalization predicts ~s-scale).

PRE-REGISTERED READ: if application-shaped B stays s-scale/polylog
while random B grows near n^{1-1/(s-1)}, the tower route SURVIVES for
the edge application (structured sets evade the Dirichlet
degradation); if application-shaped B also grows n-scale, the tower
route is DEAD for the edge — bank the negative.
"""
import random
import modal

app = modal.App("rs-mca-f2-ssparse-tower")
image = modal.Image.debian_slim()

# (n_log2, s, trials, seed)
JOBS = [(10, 6, 40, 1), (10, 12, 40, 2), (10, 20, 40, 3),
        (12, 6, 25, 4), (12, 12, 25, 5), (12, 20, 25, 6), (12, 33, 25, 7),
        (14, 12, 10, 8), (14, 33, 10, 9)]


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def cell(job):
    s0, s, trials, seed = job
    n = 1 << s0
    rng = random.Random(seed)

    def tower_bound(E):
        best = n
        for j in range(0, s0 - 1):
            m = n >> j
            Em = sorted({e % m for e in E if e % m})
            if not Em:
                bound = (1 << j) * (s - 1)
                best = min(best, bound)
                continue
            sp_best = m
            for k in range(1, m, 2):
                mx = 0
                for e in Em:
                    a = (k * e) % m
                    d = a if a <= m - a else m - a
                    if d > mx:
                        mx = d
                        if mx >= sp_best:
                            break
                if mx < sp_best:
                    sp_best = mx
            bound = (1 << j) * (2 * sp_best + s - 1)
            best = min(best, bound)
        return best

    rand_max = 0
    for _ in range(trials):
        E = rng.sample(range(1, n), s - 1) + [0]
        rand_max = max(rand_max, tower_bound(E))
    # application shape: p odd ~ sqrt-ish scale, AP of p-multiples + window
    app_max = 0
    for _ in range(trials):
        p = rng.choice([31, 37, 41, 43, 53, 61])
        T = (s - 2) * p
        if T + 2 >= n:
            continue
        E = [0] + [i * p for i in range(1, s - 1)] + [T + 1]
        app_max = max(app_max, tower_bound(E))
    return {"n": n, "s": s, "random_max": rand_max, "app_max": app_max,
            "dirichlet_scale": round(n ** (1 - 1 / (s - 1)), 1)}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    print(f"{'n':>7} {'s':>4} {'random B':>9} {'app B':>7} "
          f"{'Dirichlet n^(1-1/(s-1))':>24}")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f"{r['n']:>7} {r['s']:>4} {r['random_max']:>9} "
              f"{r['app_max']:>7} {r['dirichlet_scale']:>24}")
    if fails:
        raise SystemExit(f"F2_SSPARSE_TOWER_FAIL ({fails})")
    print("\nF2_SSPARSE_TOWER_SCALING_PASS")
