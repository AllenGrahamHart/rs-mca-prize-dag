import modal

app = modal.App("rs-mca-q-threshold")

@app.function(cpu=2.0, memory=4096, timeout=1800)
def q_threshold():
    """Find the exact log2(q) threshold below which the floor family's reach
    covers sigma* at rate 1/2 — i.e., the band closes. Box charge and trigger
    both scale with log2 q: charge = log2q per extra fiber, trigger = log2q - 40."""
    from math import lgamma, log
    LOG2 = log(2.0)
    n, k = 2**41, 2**40
    SIGMA = 8592912738
    def log2C(N, m):
        if m < 0 or m > N: return float("-inf")
        return (lgamma(N + 1) - lgamma(m + 1) - lgamma(N - m + 1)) / LOG2
    def max_depth(lq):
        trig = lq - 40.0
        best = 0
        for e in range(12, 40):
            c = 2 ** e
            if k % c: continue
            N = n // c
            base = k // c
            lo, hi, dmax = 1, N - base, 0
            while lo <= hi:
                mid = (lo + hi) // 2
                if log2C(N, base + mid) - lq * (mid - 1) > trig:
                    dmax, lo = mid, mid + 1
                else:
                    hi = mid - 1
            if dmax * c > best: best = dmax * c
        return best
    # binary search the threshold in log2 q
    lo, hi = 128.0, 256.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if max_depth(mid) >= SIGMA: lo = mid
        else: hi = mid
    return dict(threshold_log2q=round(lo, 6),
                depth_at_threshold=max_depth(lo),
                depth_just_above=max_depth(hi),
                sigma_star=SIGMA,
                open_band_slice_bits=round(256 - lo, 6),
                sanity_256=max_depth(256.0))

@app.local_entrypoint()
def main():
    import json
    print(json.dumps(q_threshold.remote(), indent=1))
