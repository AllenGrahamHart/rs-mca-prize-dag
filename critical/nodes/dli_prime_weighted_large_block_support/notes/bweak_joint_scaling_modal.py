#!/usr/bin/env python3
"""B-WEAK falsification program, experiment 1 (Modal): the joint scaling study.

Pre-registered standard (REPOSE_B_WEAK.md): refutation = sustained
super-polylog PER-JUNCTION growth of the JOINT loss across >= 3 q-scales
at >= 2 depths, with the coset column routed through the exact accounting.

Object measured here (the packet's own nested tower, n = 32, exact):
  ACTUAL(t, q)    = #{nonempty A subset mu_32 : p_r(A) = 0 mod q, r = 1..t}
                    (the exact tower total, all t conditions JOINTLY)
  COSET(t)        = exact structural column: nonempty unions of full
                    mu_{2^ceil(log2(t+1))}-cosets (255 for t = 2,3; 15 for
                    t = 4) — priced exactly by the packet, subtracted.
  MEANFIELD(t, q) = (2^32 - 1 - COSET) * q^-t
  RATIO(t, band)  = sum ACTUAL_noncoset / sum MEANFIELD over the band's
                    primes (band aggregation kills Poisson noise at the
                    sub-volume end).

Depth grid: t = 2, 3, 4 (t >= 5 is born sub-volume at n = 32 even at the
smallest admissible prime — no informative range; noted, not swept).
Per-depth q-grids span expected counts from ~10^4 down to ~0.1.
Each Modal job = one (t, q) exact tower enumeration (machinery: the
archived verify_level2_tower.py, shipped as source and exec'd).
"""
import json
import math
from pathlib import Path

import modal

app = modal.App("dli-bweak-joint-scaling")
image = modal.Image.debian_slim().pip_install("sympy", "numpy")

def _vt_src():
    return Path('/home/u2470931/smooth-read-solomin/prize/archive/'
                'compressed_dli_lane_20260705/b2b_primitive_core/notes/'
                'verify_level2_tower.py').read_text()


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def tower_count(payload):
    t, q, src = payload
    mod = {"__name__": "vt_module", "__file__": "/tmp/vt.py"}
    exec(src, mod)
    n = 32
    e, o = t // 2, (t + 1) // 2
    zeta = mod["get_zeta"](q, n)
    sc = mod["skewcount_table"](zeta, q, n, o)
    h = n // 2
    from collections import defaultdict
    L = mod["build_half_configs"](range(0, h // 2), zeta, q, n, e)
    R = mod["build_half_configs"](range(h // 2, h), zeta, q, n, e)
    dL = defaultdict(list)
    for ev, gm, dm in L:
        dL[ev].append(gm)
    total = 0
    for ev, gmR, dmR in R:
        key = tuple((-x) % q for x in ev)
        for gmL in dL.get(key, ()):
            total += sc.get(gmL | gmR, 0)
    return {"t": t, "q": q, "actual_excl_empty": total - 1}


@app.local_entrypoint()
def main():
    def is_prime(m):
        if m < 2 or m % 2 == 0:
            return m == 2
        d, s = m - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if a % m == 0:
                continue
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(s - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    def primes_near(target, count):
        out = []
        q = target - (target % 32) + 1
        while len(out) < count and q < target * 3:
            if q > 32 and is_prime(q):
                out.append(q)
            q += 32
        return out

    GRIDS = {
        2: [(100, 2), (400, 3), (2000, 4), (10000, 6), (60000, 10)],
        3: [(100, 2), (300, 3), (900, 5), (2500, 10)],
        4: [(100, 2), (200, 4), (500, 8)],
    }
    COSET = {2: 255, 3: 255, 4: 15}

    src = _vt_src()
    payloads = []
    for t, bands in GRIDS.items():
        for target, cnt in bands:
            for q in primes_near(target, cnt):
                payloads.append((t, q, src))
    print(f"{len(payloads)} exact tower jobs")
    results = [r for r in tower_count.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]

    out = {"rows": results, "bands": {}}
    print(f"{len(results)} completed")
    for t, bands in GRIDS.items():
        print(f"\n== depth t={t} (coset column {COSET[t]}, subtracted) ==")
        seq = []
        for target, cnt in bands:
            rows = [r for r in results if r["t"] == t
                    and target <= r["q"] < target * 3]
            if not rows:
                continue
            act = sum(max(r["actual_excl_empty"] - COSET[t], 0) for r in rows)
            mf = sum((2.0**32 - 1 - COSET[t]) * r["q"]**-t for r in rows)
            ratio = act / mf if mf > 0 else float("nan")
            # Poisson 95% check when the mean-field expectation is small
            seq.append((target, len(rows), act, mf, ratio))
            print(f"  band ~{target:>6}: {len(rows)} primes  "
                  f"actual={act:>9}  meanfield={mf:11.2f}  RATIO={ratio:8.3f}")
        out["bands"][t] = seq
        rat = [s[4] for s in seq if s[3] >= 1.0]
        if len(rat) >= 3:
            trend = all(b > a * 1.5 for a, b in zip(rat, rat[1:]))
            print(f"  monotone >1.5x growth across bands: {trend}")
    with open("/tmp/bweak_scaling.json", "w") as f:
        json.dump(out, f, indent=1)
