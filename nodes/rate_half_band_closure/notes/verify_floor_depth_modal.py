import modal

app = modal.App("rs-mca-floor-depth")

@app.function(cpu=2.0, memory=4096, timeout=1800)
def floor_depth():
    """Max quotient-remainder floor depth at rate 1/2 over all 2-power scales.
    lgamma-based log2-binomials; margins reported so boundary cases are honest."""
    from math import lgamma, log
    LOG2 = log(2.0)
    n, k = 2**41, 2**40
    TRIG = 216.0                      # log2((q-n)/k) bound at rate 1/2, q < 2^256
    def log2C(N, m):
        if m < 0 or m > N: return float("-inf")
        return (lgamma(N + 1) - lgamma(m + 1) - lgamma(N - m + 1)) / LOG2
    rows, best = [], (0, None, None)
    for e in range(12, 40):
        c = 2 ** e
        if k % c: continue
        N = n // c
        base = k // c
        if base + 1 > N: continue
        lo, hi, dmax = 1, N - base, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if log2C(N, base + mid) - 256.0 * (mid - 1) > TRIG:
                dmax, lo = mid, mid + 1
            else:
                hi = mid - 1
        if dmax == 0: continue
        margin = log2C(N, base + dmax) - 256.0 * (dmax - 1) - TRIG
        margin_next = log2C(N, base + dmax + 1) - 256.0 * dmax - TRIG
        depth = dmax * c
        rows.append(dict(e=e, c=c, N=N, dmax=dmax, depth=depth,
                         margin_bits=round(margin, 3),
                         next_margin_bits=round(margin_next, 3)))
        if depth > best[0]: best = (depth, e, dmax)
    sigma_star = 8592912738
    return dict(rows=rows, max_depth=best[0], best_scale_e=best[1],
                best_d=best[2], sigma_star=sigma_star,
                gap=sigma_star - best[0], banked_band=2978147)

@app.local_entrypoint()
def main():
    import json
    print(json.dumps(floor_depth.remote(), indent=1))
