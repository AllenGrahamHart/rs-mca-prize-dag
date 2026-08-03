#!/usr/bin/env python3
"""SL-2 pilot: the SUB-DEPTH COSET DESCENT at the six rows of record.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

BP(1) (banked) concludes "structured => d is a power of two" for the
scale PINNED by definitions item 10, M = 2^ceil(log2 d) >= d.  The coset
structure itself forces only M | d.  This file scans the SUB-DEPTH
scales M = 2^j | gcd(n,k) with M < d and decides each (M, d) by two
INDEPENDENT tests:

  LIVENESS (THEOREM L, proved in REPORT section 3 -- the generalization
  of BP(3) from the shift class to every M-quotient-periodic pair).
  For an M-structured depth-d pair the extra agreement of any pencil
  projection beyond the core lies in  g*{0,...,m},  g = gcd(M, b-a) a
  power of two, m = (n-k-d)/M.  Liveness needs extra = h-d EXACTLY.
  M | d and h ODD force g = 1, so liveness needs
        h - d <= m = (n-k-d)/M,   i.e.   M <= cap_d = (n-k-d)//(h-d).
  Hence  M > cap_d  =>  L_P = 0  =>  the pair is NOT counted by N_d.
  (cap_d is the BANKED line cap, xr_band_ledger_theorems THEOREM 3.)

  FIRST MOMENT.  The scale-M joint window system has 2d/M equations in
  a monic degree-m divisor of Y^N - 1, N = n/M (THEOREM D, the descent
  bijection, machine-checked in algebra.py).  So the expected count is
        log2 E = log2 C(N, m) - (2d/M) log2 q,
  to be compared with the budget log2(C_row * n^2).

A scale is CLOSED at depth d if either test excludes it.  Because cap_d
INCREASES with d and the first-moment margin also increases with d, the
two tests are complementary; the row is closed iff the first moment
already works wherever liveness stops working.
"""
import json
from math import comb, gcd, lgamma, log2

LN2 = 0.6931471805599453

ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, A=261, h=5, C=None),
    dict(name="RowC 1/8", n=1024, k=128, A=133, h=5, C=None),
    dict(name="RowC 1/16", n=1024, k=64, A=67, h=3, C=None),
    dict(name="prize 1/4", n=2199023255552, k=549755813888,
         A=558345748481, h=8589934593, C=0.800767298932776),
    dict(name="prize 1/8", n=2199023255552, k=274877906944,
         A=283467841537, h=8589934593, C=0.6858649121282252),
    dict(name="prize 1/16", n=2199023255552, k=137438953472,
         A=141733920769, h=4294967297, C=0.6596448038293138),
]
# h-EVEN control (banked xr_mc_depth_quantization BP(2) positive control)
CONTROL = dict(name="h-even control", n=20, k=8, A=14, h=6, C=None,
               expect_subdepth=True)

LOG2Q_PIN = 250.0        # the PIN q >= 2^250; SMALLEST q is adversary-best
LOG2Q_CAP = 256.0        # FIELD_CAP


def lbinom(n, j):
    if j < 0 or j > n:
        return float("-inf")
    if j == 0 or j == n:
        return 0.0
    return (lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)) / LN2


checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))


def scan_row(r, log2q, budget_C):
    n, k, h = r["n"], r["k"], r["h"]
    dlo, dhi = -(-h // 2), h - 2           # band proper
    res = dict(name=r["name"], n=n, k=k, h=h, band_proper=[dlo, dhi],
               nonempty=dlo <= dhi, h_odd=(h % 2 == 1), scales=[])
    if dlo > dhi:
        return res
    budget = log2(budget_C * n * n)
    res["budget_bits"] = budget
    # BP(1) class: is there a POWER OF TWO in the band proper?  (M >= d)
    pow2 = [1 << j for j in range(0, 64) if dlo <= (1 << j) <= dhi]
    res["bp1_powers_of_two_in_band"] = pow2
    ck("BP(1): no power of two in the band proper (h odd)", r["name"],
       (not pow2) if h % 2 else True, dict(found=pow2, h=h))

    gk = gcd(n, k)
    worst = None
    for j in range(1, 64):
        M = 1 << j
        if M > dhi or gk % M:
            continue
        mults = [d for d in (((dlo + M - 1) // M) * M, (dhi // M) * M)
                 if dlo <= d <= dhi]
        if not mults:
            continue
        dmin = ((dlo + M - 1) // M) * M
        dmax = (dhi // M) * M
        if dmin > dhi:
            continue
        count = (dmax - dmin) // M + 1
        # ---- scan every multiple when few; else bisect the two thresholds
        def live_excluded(d):
            rp = n - k - d
            cap = rp // (h - d)
            return M > cap, cap, rp // M

        def fm_margin(d):
            rp = n - k - d
            N, m = n // M, rp // M
            return lbinom(N, m) - (2.0 * d / M) * log2q, N, m

        # liveness holds (i.e. NOT excluded) for large d; find the first
        # d in the ladder where liveness stops excluding
        dL = None
        lo, hi = 0, count - 1
        if not live_excluded(dmin)[0]:
            dL = dmin                       # liveness never excludes
        elif live_excluded(dmax)[0]:
            dL = None                       # liveness always excludes
        else:
            while lo < hi:
                mid = (lo + hi) // 2
                if live_excluded(dmin + mid * M)[0]:
                    lo = mid + 1
                else:
                    hi = mid
            dL = dmin + lo * M
        # first moment excludes for large d; find the last d where it does
        # NOT (margin >= budget means NOT excluded)
        dF = None
        if fm_margin(dmin)[0] < budget:
            dF = None                       # first moment always excludes
        elif fm_margin(dmax)[0] >= budget:
            dF = dmax                       # never excludes
        else:
            lo, hi = 0, count - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if fm_margin(dmin + mid * M)[0] >= budget:
                    lo = mid
                else:
                    hi = mid - 1
            dF = dmin + lo * M
        # the row is closed at this scale iff every d is excluded by one
        # of the two: liveness covers d < dL, first moment covers d > dF
        closed = (dL is None) or (dF is None) or (dF < dL)
        gap = None
        if not closed:
            gap = [dL, dF]
        le_min, cap_min, m_min = live_excluded(dmin)
        fm_min, N, m = fm_margin(dmin)
        # liveness alone closes this scale iff it excludes even at dmax
        # (cap_d is increasing in d) -- those scales are PROVED closed
        entry = dict(j=j, M=M, dmin=dmin, dmax=dmax, count=count,
                     cap_dmin=cap_min, m_dmin=m_min,
                     cap_dmax=(n - k - dmax) // (h - dmax),
                     liveness_closes_all_d=live_excluded(dmax)[0],
                     live_excluded_at_dmin=le_min,
                     fm_margin_at_dmin_bits=fm_min, N=N,
                     quotient=dict(N=N, kq=k // M, dq=dmin // M,
                                   m=m, hq=h // M,
                                   dq_is_quotient_cascade=(
                                       dmin // M == h // M - 1)),
                     first_liveness_gap_d=dL, last_fm_gap_d=dF,
                     closed=closed, gap=gap)
        res["scales"].append(entry)
        ck("every sub-depth scale is closed (liveness OR first moment)",
           f"{r['name']} M=2^{j}", closed, entry)
        # "worst" = the LEAST negative margin, i.e. the adversary's best
        if worst is None or fm_min > worst["fm_margin_at_dmin_bits"]:
            worst = entry
    res["worst_scale"] = worst
    res["any_subdepth_scale"] = bool(res["scales"])
    res["proved_scales"] = [e["M"] for e in res["scales"]
                            if e["liveness_closes_all_d"]]
    res["heuristic_scales"] = [e["M"] for e in res["scales"]
                               if not e["liveness_closes_all_d"]]
    # PREREG P4: sub-depth scales exist at the PRIZE rows, not at RowC
    expect = r.get("expect_subdepth", r["name"].startswith("prize"))
    ck("P4/F2: sub-depth coset scale inside the band proper "
       "(predicted: prize rows YES, RowC rows NO)",
       r["name"], bool(res["scales"]) == expect,
       dict(scales=[e["M"] for e in res["scales"]], expected=expect))
    return res


def main():
    out = dict(log2q_used=LOG2Q_PIN, rows=[])
    for r in ROWS:
        C = r["C"] if r["C"] is not None else 0.68
        out["rows"].append(scan_row(r, LOG2Q_PIN, C))
    out["control"] = scan_row(CONTROL, LOG2Q_PIN, 0.68)
    # cross-check the lgamma path against exact integers at RowC scale
    for (N, m) in [(1024, 765), (512, 300), (2048, 1530)]:
        e = log2(comb(N, m))
        a = lbinom(N, m)
        ck("lgamma path == exact log2 C(N,m)", f"C({N},{m})",
           abs(e - a) < 1e-6, dict(exact=e, lgamma=a))

    # ---- P8: the critical field size for the worst scale of each row
    crit = []
    for rec in out["rows"]:
        if not rec.get("nonempty"):
            continue
        n, k, h = rec["n"], rec["k"], rec["h"]
        b = rec["budget_bits"]
        dlo = rec["band_proper"][0]
        # M = 1 baseline: the UNSTRUCTURED joint first moment at the
        # band-proper floor -- the fundamental q-threshold
        best = dict(row=rec["name"], M=1, d=dlo,
                    log2_q_critical=(lbinom(n, n - k - dlo) - b)
                    / (2.0 * dlo))
        for e in rec["scales"]:
            M, d, N, m = e["M"], e["dmin"], e["N"], e["quotient"]["m"]
            qc = (lbinom(N, m) - b) / (2.0 * d / M)
            if qc > best["log2_q_critical"]:
                best = dict(row=rec["name"], M=M, d=d,
                            log2_q_critical=qc)
        best.update(pin_bits=LOG2Q_PIN,
                    safe=(LOG2Q_PIN > best["log2_q_critical"]),
                    headroom_bits=LOG2Q_PIN - best["log2_q_critical"])
        crit.append(best)
        ck("P8: the pin q >= 2^250 is above the critical field size",
           rec["name"], best["safe"], best)
    out["critical_field"] = crit

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b["check"], b["fixture"], b.get("extra"))
    print()
    for rec in out["rows"] + [out["control"]]:
        print(f"=== {rec['name']}: n={rec['n']} k={rec['k']} h={rec['h']} "
              f"(h {'odd' if rec['h_odd'] else 'EVEN'})  band proper "
              f"[{rec['band_proper'][0]},{rec['band_proper'][1]}]")
        if not rec["nonempty"]:
            print("    band proper EMPTY")
            continue
        print(f"    BP(1) powers of two inside the band: "
              f"{rec['bp1_powers_of_two_in_band']}   budget = "
              f"{rec['budget_bits']:.2f} bits")
        if not rec["scales"]:
            print("    NO sub-depth coset scale exists (M | d impossible)")
            continue
        for e in rec["scales"][-4:]:
            q = e["quotient"]
            print(f"    M=2^{e['j']:<2d}  d in [{e['dmin']},{e['dmax']}] "
                  f"({e['count']} values)  cap_dmin={e['cap_dmin']}  "
                  f"live-excl@dmin={e['live_excluded_at_dmin']}  "
                  f"FM margin@dmin={e['fm_margin_at_dmin_bits']:+.1f} bits"
                  f"  CLOSED={e['closed']}")
            print(f"          quotient: N={q['N']} k'={q['kq']} "
                  f"d'={q['dq']} m={q['m']} h'={q['hq']}  "
                  f"d'=cascade? {q['dq_is_quotient_cascade']}")
        w = rec["worst_scale"]
        print(f"    WORST scale: M=2^{w['j']} at d={w['dmin']}  "
              f"FM margin {w['fm_margin_at_dmin_bits']:+.1f} bits vs "
              f"budget {rec['budget_bits']:.1f}  closed={w['closed']}")
    print()
    for c in crit:
        print(f"critical field  {c['row']:12s} M={c['M']:>12d} "
              f"d={c['d']:>12d}  log2 q_crit = {c['log2_q_critical']:.2f}"
              f"  (pin 250 safe: {c['safe']})")

    out["checks"] = checks
    out["n_checks"] = len(checks)
    out["n_fail"] = len(bad)
    out["verdict"] = "PASS" if not bad else "FAIL"
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
