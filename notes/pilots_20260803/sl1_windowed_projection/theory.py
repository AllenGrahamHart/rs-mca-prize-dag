#!/usr/bin/env python3
"""SL-1 windowed reduction — exact six-row arithmetic (pilot 2026-08-03).

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

Evaluates, at the banked six rows, the cost of the WINDOWED upgrade of
THEOREM 2 proved in this pilot:

    N_d  <=  avg_{z in P^1(F_q)} W_d(z)  /  (1 - beta_d/(q+1)),
    beta_d = floor((n-k-d)/(h-d-1)),
    W_d(z) = #{c in C : k+d <= agr(c, w_z) <= A-2}.

Reported:
  1. band-proper range [ceil(h/2), h-2] and the window [k+d, A-2]
  2. beta_d (over-agreement member budget) and cap_d = (n-k-d)//(h-d)
     (the BANKED line cap, xr_band_ledger_theorems THEOREM 3) at both
     endpoints of band proper
  3. the multiplier (1 - beta_d/(q+1))^{-1} at the pinned field and at
     the ABSOLUTE WORST legal field q = n
  4. the clean-member count (q+1) - beta_d
  5. the good-member margin: beta_d * (target N_d) vs q+1, which decides
     whether the min-over-good-members form is available on top of the
     averaged form

Rows: the banked table reproduced verbatim from
notes/pilots_20260803/listsize_program/rows.py:29-42 (itself
xr_band_occupancy/theory.py:34-42).  Reduction constants C from
xr_band_occupancy/reduce.json via that same file.  Nothing re-derived.
"""
import json
from math import log2

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
LOG2Q_PIN = 250.0        # the PIN q >= 2^250 -- conservative here: the
LOG2Q_CAP = 256.0        # correction beta/(q+1) is LARGEST at small q


def main():
    out = []
    checks = []
    for r in ROWS:
        n, k, A, h = r["n"], r["k"], r["A"], r["h"]
        checks.append(("A = k + h", r["name"], A == k + h))
        dlo, dhi = -(-h // 2), h - 2
        rec = dict(name=r["name"], n=n, k=k, A=A, h=h,
                   band_proper=[dlo, dhi], nonempty=dlo <= dhi)
        if dlo > dhi:
            out.append(rec)
            continue
        ends = []
        for d in (dlo, dhi):
            beta = (n - k - d) // (h - d - 1)
            cap = (n - k - d) // (h - d)
            # the window [k+d, A-2] is non-empty exactly because d <= h-2
            wlo, whi = k + d, A - 2
            checks.append(("window non-empty", f"{r['name']} d={d}",
                           wlo <= whi))
            # UNCONDITIONAL: beta_d <= n-k-d < n <= q, so the multiplier
            # is finite for EVERY legal Reed-Solomon field.
            checks.append(("beta_d < n (=> < q for any legal field)",
                           f"{r['name']} d={d}", beta < n))
            e_pin = beta / 2.0 ** LOG2Q_PIN
            e_cap = beta / 2.0 ** LOG2Q_CAP
            worst = (n + 1) / (n + 1 - beta)      # q = n, the smallest field
            ends.append(dict(
                d=d, beta=beta, cap=cap, window=[wlo, whi],
                window_width=whi - wlo + 1,
                log2_beta=log2(beta) if beta else None,
                eps_pin=e_pin, eps_cap=e_cap,
                mult_pin=1.0 / (1.0 - e_pin),
                mult_cap=1.0 / (1.0 - e_cap),
                mult_worst_case_q_eq_n=worst,
                clean_members_log2_pin=LOG2Q_PIN,   # (q+1) - beta ~ q
                loss_bits_pin=-log2(1.0 - e_pin)))
        rec["endpoints"] = ends
        # good-member margin at the occupancy target N_d = C * n^2
        if r["C"] is not None:
            tgt = r["C"] * n * n
            bmax = max(e["beta"] for e in ends)
            rec["target_N_d"] = tgt
            rec["log2_target"] = log2(tgt)
            rec["log2_beta_times_target"] = log2(bmax) + log2(tgt)
            rec["good_set_margin_bits_pin"] = (
                LOG2Q_PIN - (log2(bmax) + log2(tgt)))
            rec["good_set_nonempty_at_pin"] = (
                log2(bmax) + log2(tgt) < LOG2Q_PIN)
        out.append(rec)

    print(f"{'row':12s} {'band proper':>13s} {'d':>11s} {'beta_d':>15s} "
          f"{'cap_d':>15s} {'window':>22s} {'loss (bits)':>13s} "
          f"{'mult @ q=n':>11s}")
    for rec in out:
        if not rec.get("endpoints"):
            print(f"{rec['name']:12s}  band proper EMPTY "
                  f"(h={rec['h']}, [{rec['band_proper'][0]},"
                  f"{rec['band_proper'][1]}])")
            continue
        for i, e in enumerate(rec["endpoints"]):
            nm = rec["name"] if i == 0 else ""
            bp = (f"[{rec['band_proper'][0]},{rec['band_proper'][1]}]"
                  if i == 0 else "")
            print(f"{nm:12s} {bp:>13s} {e['d']:>11d} {e['beta']:>15d} "
                  f"{e['cap']:>15d} "
                  f"{'[' + str(e['window'][0]) + ',' + str(e['window'][1]) + ']':>22s} "
                  f"{e['loss_bits_pin']:>13.3e} "
                  f"{e['mult_worst_case_q_eq_n']:>11.4f}")
    print()
    for rec in out:
        if "good_set_margin_bits_pin" in rec:
            print(f"{rec['name']:12s} target N_d = {rec['C_str'] if False else ''}"
                  f"{rec['log2_target']:.2f} bits; beta*N_d = "
                  f"{rec['log2_beta_times_target']:.2f} bits vs q >= 250 "
                  f"bits -> good-member set NON-EMPTY = "
                  f"{rec['good_set_nonempty_at_pin']} "
                  f"(margin {rec['good_set_margin_bits_pin']:.1f} bits)")
    bad = [c for c in checks if not c[2]]
    print("\nchecks:", len(checks), " failures:", len(bad))
    for b in bad:
        print("  FAIL", b)
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(rows=out, checks=checks,
                       verdict="PASS" if not bad else "FAIL"), fh, indent=1)


if __name__ == "__main__":
    main()
