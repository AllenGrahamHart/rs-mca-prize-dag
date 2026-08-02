"""prize_arith.py -- exact arithmetic of the MC construction at the six rows.

The reduced statement under test (xr_band_occupancy Theorem 2 + reduction):

    "some pencil member w_z has at most B_row * n^2 codewords at agreement
     >= tau = k + ceil(h/2)"

with the standing tangent gate (H3) agr(c, w_z) <= A = k + h.

MC construction: pick M = w = h - 1.  Requirements
    M | n,  M | r' = n - k - w,  w <= M  (equality),  gcd(r'/M, n/M) = 1.
Then the word u = X^(n-1) + c X^(k+w-1) has
    * max agreement exactly k + w = A - 1  (strictly inside the gate), and
    * at least C(N,m)/N codewords at agreement exactly k+w >= tau,
with N = n/M, m = r'/M.

All integer arithmetic exact.
"""

import json
import os
import sys
from math import comb, gcd, log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

# rows transcribed from notes/pilots_20260802/xr_band_occupancy/{theory,reduce}.json
ROWS = [
    # name,           n,                 k,              h,             required/n^2
    ("RowC 1/4",      1024,              256,            5,             34.84816753926702),
    ("RowC 1/8",      1024,              128,            5,             29.847533632286996),
    ("RowC 1/16",     1024,              64,             3,             None),
    ("prize 1/4",     2199023255552,     549755813888,   8589934593,    0.800767298932776),
    ("prize 1/8",     2199023255552,     274877906944,   8589934593,    0.6858649121282252),
    ("prize 1/16",    2199023255552,     137438953472,   4294967297,    0.6596448038293138),
]

res = {"rows": [], "growth": [], "notes": []}

for name, n, k, h, req_over_n2 in ROWS:
    tau = k + -(-h // 2)          # k + ceil(h/2)
    A = k + h
    entry = {"row": name, "n": n, "k": k, "h": h, "A": A, "tau": tau,
             "required_over_n2": req_over_n2,
             "required_bound": None if req_over_n2 is None else req_over_n2 * n * n,
             "candidates": []}
    # every w in [tau-k, h] with w | n, w | (n-k-w) is an MC candidate.
    # w | n and w | (n-k-w) together force w | k, so enumerate divisors of
    # gcd(n,k) inside the window.
    from math import gcd as _gcd
    G = _gcd(n, k)
    divs = []
    d = 1
    while d * d <= G:
        if G % d == 0:
            divs.append(d)
            divs.append(G // d)
        d += 1
    divs = sorted(set(divs))
    best = None
    for w in divs:
        if not (tau - k <= w <= h):
            continue
        if n % w or (n - k - w) % w:
            continue
        M = w
        N, m = n // M, (n - k - w) // M
        if gcd(m, N) != 1:
            cnt = None
            uniform = False
        else:
            cnt = comb(N, m) // N
            uniform = True
        cand = {"w": w, "M": M, "N": N, "m": m, "gcd": gcd(m, N),
                "uniform": uniform,
                "agreement": k + w, "agreement_ge_tau": k + w >= tau,
                "agreement_lt_A": k + w < A,
                "count_log2": None if cnt is None else log2(cnt) if cnt < 2**900 else None,
                "count_bits": None if cnt is None else cnt.bit_length()}
        if cnt is not None:
            cand["count_exact_str"] = str(cnt) if cnt.bit_length() < 400 else (
                str(cnt)[:30] + "..." + str(cnt)[-10:] + " (%d digits)" % len(str(cnt)))
        entry["candidates"].append(cand)
        if cnt is not None and (best is None or cnt > best[1]):
            best = (w, cnt)
    if best:
        w, cnt = best
        entry["best_w"] = w
        entry["best_count_bits"] = cnt.bit_length()
        entry["best_count_log2"] = float(log2(cnt)) if cnt.bit_length() < 1000 else None
        if req_over_n2 is not None:
            need = req_over_n2 * n * n
            entry["required_log2"] = log2(need)
            entry["excess_bits"] = (float(log2(cnt)) - log2(need)
                                    if cnt.bit_length() < 1000 else None)
            entry["REFUTES"] = cnt > need
    res["rows"].append(entry)

# growth at fixed rate 1/2, w = M = 2 (the smallest nontrivial MC instance)
for n in [16, 24, 32, 40, 48, 64, 96, 128, 256, 1024]:
    k = n // 2
    w = M = 2
    rp = n - k - w
    if n % M or rp % M:
        continue
    N, m = n // M, rp // M
    if gcd(m, N) != 1:
        res["growth"].append({"n": n, "k": k, "note": "gcd != 1", "gcd": gcd(m, N)})
        continue
    cnt = comb(N, m) // N
    res["growth"].append({"n": n, "k": k, "w": w, "M": M, "N": N, "m": m,
                          "count": cnt if cnt < 10**18 else None,
                          "count_log2": float(log2(cnt)),
                          "n2": n * n, "count_over_n2": float(cnt / (n * n))
                          if cnt < 10**300 else None,
                          "log2_ratio": float(log2(cnt) - 2 * log2(n))})

print("=== MC construction at the six rows (w = M chosen inside [ceil(h/2), h]) ===")
for e in res["rows"]:
    print("%-12s n=%-14d k=%-13d h=%-11d tau=%-13d A=%d" %
          (e["row"], e["n"], e["k"], e["h"], e["tau"], e["A"]))
    if not e["candidates"]:
        print("    no admissible (w | n, w | r') in [ceil(h/2), h]")
        continue
    for c in e["candidates"]:
        print("    w=M=%-11d N=%-6d m=%-6d gcd=%-3d agr=%-13d (>=tau:%s, <A:%s)  count~2^%s"
              % (c["w"], c["N"], c["m"], c["gcd"], c["agreement"],
                 c["agreement_ge_tau"], c["agreement_lt_A"],
                 ("%.1f" % c["count_log2"]) if c["count_log2"] else "n/a"))
    if e.get("required_log2") is not None:
        print("    REQUIRED <= %.4f n^2 = 2^%.2f   |   MC = 2^%.2f   -> excess %.1f bits  REFUTES=%s"
              % (e["required_over_n2"], e["required_log2"], e["best_count_log2"],
                 e["excess_bits"], e["REFUTES"]))
    print()

print("=== growth at rate 1/2 with w = M = 2 (exact) ===")
print("  n     count = C(n/2, r'/2)/(n/2)          log2   count/n^2")
for g in res["growth"]:
    if "note" in g:
        print("  %-5d (gcd=%d, non-uniform)" % (g["n"], g["gcd"]))
        continue
    print("  %-5d %-32s %6.2f  %s" %
          (g["n"], str(g["count"]) if g["count"] else "(big)",
           g["count_log2"],
           ("%.4g" % g["count_over_n2"]) if g["count_over_n2"] else "-"))

with open(os.path.join(CHK, "prize_arith.json"), "w") as f:
    json.dump(res, f, indent=1)
print("\nwrote checkpoints/prize_arith.json")
