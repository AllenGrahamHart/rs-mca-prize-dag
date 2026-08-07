#!/usr/bin/env python3
"""C2'' F-round 3, part C -- F-d-C: is the coset excess BOOKKEEPING or
CORRELATION?

Clause (i) of the pose (C2PP_POSED_20260710.md:22-28) asserts coset-class
contributions "are budget arithmetic, never correlation".  That is the load-
bearing model clause: it licenses stripping the k=0 column before F-a/F-b/F-c
measure anything.  This decides it, exactly, on the banked rows.

Decomposition of the raw junction factor into a MIXTURE-WEIGHT part and an
INTERNAL part:

    raw_ratio = E[sc|null] / E[sc]
              = sum_k w_k^null * m_k^null  /  sum_k w_k^all * m_k^all

NEW named functionals (CATCH-19C, first use here):
  C1 `coset_internal_ratio` iota := (cs0/cn0) / (asum0/an0)
     -- the coset class compared with ITSELF across the conditioning.
        iota == 1 means the coset class is internally uncorrelated.
  C2 `coset_weight_shift` omega  := (cn0/n_null) / (an0/n_all)
     -- how much more often null states land in the coset class.
  C3 `mixture_only_ratio` mu     -- the raw ratio recomputed with every
     class's INTERNAL mean frozen at its unconditional value, i.e. the
     excess attributable to re-weighting alone.
  C4 `internal_only_ratio` nu    -- the raw ratio recomputed with every
     class's WEIGHT frozen at its unconditional value.
     (mu * nu need not equal raw; the residual is the interaction term,
     reported as C5 `interaction_residual`.)

Run: tools/ramguard local -- python3 \
       notes/pilots_20260807/c2pp_diag/fdc_coset_mechanism.py
"""
import sys, math, json, importlib.util

sys.dont_write_bytecode = True
ROOT = "/home/u2470931/smooth-read-solomin/prize"
M1PATH = (ROOT + "/critical/nodes/dli_prime_weighted_large_block_support"
                 "/notes/m1_dli_m1_tower_census_modal.py")
OUT = ROOT + "/notes/pilots_20260807/c2pp_diag/fdc_results.json"
spec = importlib.util.spec_from_file_location("m1", M1PATH)
m1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m1)

N, H = 32, 16
ALLOW = 2.0 ** (21.0 / 33.0)
# the four rows whose raw junction factor exceeds the /33 allowance
ROWS = [(2, 8353), (2, 32801), (4, 97), (4, 193)]
# two control rows that do NOT overflow
CTRL = [(2, 97), (3, 193)]

print("=" * 78)
print("[F-d-C] clause (i): 'budget arithmetic, never correlation' -- tested")
print("=" * 78)
print(f"  allowance 2^(21/33) = {ALLOW:.6f}")
print(f"  {'row':>14} {'raw':>9} {'iota':>9} {'omega':>9} {'mu':>9}"
      f" {'nu':>9} {'resid':>8}")
out = []
for (t, q) in ROWS + CTRL:
    cs = m1.mitm_joint_census_dict(q, N, t)
    cn = m1.even_null_census(q, N, t)
    asum = m1.signed_all_census(q, N, t)
    an = [math.comb(H, k) * (2 ** (H - k)) for k in range(H + 1)]
    n_all = 3 ** H
    assert sum(an) == n_all, "CATCH-Z6 / nonemptiness: class counts must total 3^h"
    n_null, s_null, s_all = sum(cn), sum(cs), sum(asum)
    assert n_null > 0, "nonemptiness: empty null set"
    raw = (s_null / n_null) / (s_all / n_all)

    # per-class weights and internal means
    w_null = [cn[k] / n_null for k in range(H + 1)]
    w_all = [an[k] / n_all for k in range(H + 1)]
    m_null = [(cs[k] / cn[k] if cn[k] else 0.0) for k in range(H + 1)]
    m_all = [(asum[k] / an[k] if an[k] else 0.0) for k in range(H + 1)]

    iota = ((cs[0] / cn[0]) / (asum[0] / an[0])
            if cn[0] and asum[0] else None)
    omega = (cn[0] / n_null) / (an[0] / n_all) if an[0] else None
    den = sum(w_all[k] * m_all[k] for k in range(H + 1))
    mu_num = sum(w_null[k] * m_all[k] for k in range(H + 1))   # weights moved
    nu_num = sum(w_all[k] * m_null[k] for k in range(H + 1))   # means moved
    mu = mu_num / den if den else None
    nu = nu_num / den if den else None
    resid = (raw / (mu * nu)) if (mu and nu) else None

    out.append(dict(t=t, q=q, raw_ratio=raw, coset_internal_ratio=iota,
                    coset_weight_shift=omega, mixture_only_ratio=mu,
                    internal_only_ratio=nu, interaction_residual=resid,
                    overflow=raw > ALLOW, is_control=(t, q) in CTRL))
    fmt = lambda x: "      n/a" if x is None else f"{x:9.4f}"
    print(f"  (t={t},q={q:>5}) {raw:9.4f} {fmt(iota)} {fmt(omega)}"
          f" {fmt(mu)} {fmt(nu)}"
          f" {'     n/a' if resid is None else f'{resid:8.4f}'}"
          + ("   [control]" if (t, q) in CTRL else ""))

print("\n  READ:")
ovf = [o for o in out if o["overflow"]]
mix_dom = [o for o in ovf if o["mixture_only_ratio"] is not None
           and o["internal_only_ratio"] is not None
           and o["mixture_only_ratio"] > o["internal_only_ratio"]]
print(f"    overflow rows where the excess is MIXTURE-dominated "
      f"(mu > nu): {[(o['t'], o['q']) for o in mix_dom]} of "
      f"{[(o['t'], o['q']) for o in ovf]}")
iota1 = [o for o in ovf if o["coset_internal_ratio"] is not None
         and abs(o["coset_internal_ratio"] - 1.0) < 1e-9]
print(f"    overflow rows where the coset class is INTERNALLY "
      f"uncorrelated (iota == 1 exactly): {[(o['t'], o['q']) for o in iota1]}")
print(f"    mu over the overflow rows: "
      f"{[round(o['mixture_only_ratio'], 4) for o in ovf if o['mixture_only_ratio']]}")
print(f"    mu transported 33x (bits): "
      f"{[round(33*math.log2(o['mixture_only_ratio']), 2) for o in ovf if o['mixture_only_ratio'] and o['mixture_only_ratio'] > 0]}"
      f"   [reserve = 21 bits]")

json.dump(dict(allowance=ALLOW, rows=out), open(OUT, "w"), indent=1)
print(f"\n  artifact -> {OUT}")
