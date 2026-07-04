#!/usr/bin/env python3
"""
Deterministic verifier for cap_envelope_parameter_sweep.

Recomputes every reported (rate, c, d) point of sweep_results.md from scratch
with EXACT big-integer arithmetic and re-checks:
  (H) every hypothesis of cor:extension-pole-quotient-remainder-floor
      (cs25_cap_v12.tex, ~line 542) via its supporting lemma
      lem:quotient-remainder-prefix (~line 734), full-fiber s=0;
  (T) the exact trigger  log2 L > 256 - log2 k, i.e.  C(N,m) > 2^(256 d - e);
  (M) maximality of d at this c (the point d+1 fails to trigger);
  (G) the reported net grid-step gain  net = d*2^step / N - 1  (exact rational).

Model / conventions (see sweep_results.md for the tex quotes):
  n = 2^41 ;  q < 2^256 ;  D = order-n multiplicative coset in B^x, B ⊊ F.
  Full fiber s=0, m = k/c + d, A0 = m c, sigma = A0-(k+1), w = w_c(0,sigma)=d-1.
  Box charge is the certificate-free ambient box |B|^w with the CONSERVATIVE
  bound b=|B| < q < 2^256 (over-charge: a proper subfield in fact has b<2^128,
  so the true L is even larger). Hence  log2 L = log2 C(N,m) - 256 w.
  Trigger uses (q-n)/k < q/k < 2^(256-e), stronger than the extension
  corollary's own (q-b)/k, so both the CA and the genuinely-extension-valued
  conclusions fire.  step: grid step = 2^-9 at 1/4 & 1/8, 2^-10 at 1/16.
"""
import math
from fractions import Fraction

N_EXP = 41                      # n = 2^41

# reported points: (label, e=log2 k, step_exp, j=log2 c, d, expected_net_fraction)
POINTS = [
    ("rate 1/4  optimum",  39,  9, 25,  209,   Fraction(81, 128)),
    ("rate 1/8  optimum",  38,  9, 21, 2251,   Fraction(203, 2048)),
    ("rate 1/16 optimum",  37, 10, 28,   11,   Fraction(3, 8)),
    ("rate 1/8  template", 38,  9, 28,   17,   Fraction(1, 16)),
]

# per-rate required net gain (grid steps). task-registered value, then ledger X_acl.
REQUIRED = {39: ("1/4", 0.318, 0.367), 38: ("1/8", 0.023, 0.023), 37: ("1/16", 0.304, 0.304)}


def log2_bigint(x: int) -> float:
    bl = x.bit_length()
    if bl <= 60:
        return math.log2(x)
    return (bl - 60) + math.log2(x >> (bl - 60))


def check(label, e, step_exp, j, d, expected_net):
    n = 1 << N_EXP
    k = 1 << e
    c = 1 << j
    N = 1 << (N_EXP - j)          # N = n/c
    m0 = 1 << (e - j)             # k/c  (integral since j<=e)
    m = m0 + d
    A0 = m * c                    # = k + d c
    sigma = A0 - (k + 1)
    w = sigma // c                # w_c(0,sigma) = floor(sigma/c)

    hyp = {
        "c | k  (j<=e)":                     j <= e,
        "c | n  (j<=41)":                    j <= N_EXP,
        "k/c integral":                      (k % c) == 0,
        "K=k+1 < n":                         (k + 1) < n,
        "0 <= m <= N":                       0 <= m <= N,
        "A0 = m c > k  (interval nonempty)": A0 > k,
        "A0 <= n  (delta0 = 1-A0/n >= 0)":   A0 <= n,
        "s=0: side-cond mc+s<=n vacuous":    True,
        "w == d-1  (full-fiber prefix wt)":  w == d - 1,
    }
    hyp_ok = all(hyp.values())

    comb = math.comb(N, m)                       # exact big integer C(N,m)
    trigger = comb > (1 << (256 * d - e))        # exact: log2 C > 256 d - e
    comb_next = math.comb(N, m + 1)
    maximal = not (comb_next > (1 << (256 * (d + 1) - e)))

    log2L = log2_bigint(comb) - 256 * w
    margin = log2L - (256 - e)
    net = Fraction(d << step_exp, N) - 1
    net_ok = (net == expected_net)

    ok = hyp_ok and trigger and maximal and net_ok
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: c=2^{j}, d={d}, N=2^{N_EXP-j}, "
          f"m={m}, w={w}")
    print(f"        log2 C(N,m)={log2_bigint(comb):.3f}  log2 L={log2L:.3f}  "
          f"thr={256-e}  margin={margin:.2f} bits")
    print(f"        hypotheses={hyp_ok}  trigger={trigger}  maximal_d={maximal}")
    print(f"        net gain = {net} = {float(net):.6f} grid steps "
          f"(total {float(net)+1:.6f}); expected {expected_net} -> {net_ok}")
    if not hyp_ok:
        for kk, vv in hyp.items():
            if not vv:
                print(f"          !! HYPOTHESIS FAILS: {kk}")
    if e in REQUIRED:
        rn, req_task, req_ledger = REQUIRED[e]
        print(f"        required(rate {rn}): task>={req_task}  ledger X_acl>={req_ledger}"
              f"   -> {'MET' if float(net) >= req_ledger else ('MET(task) SHORT(ledger)' if float(net)>=req_task else 'SHORT')}")
    return ok


if __name__ == "__main__":
    allok = True
    for p in POINTS:
        allok &= check(*p)
        print()
    print("ALL POINTS PASS" if allok else "SOME POINTS FAILED")
