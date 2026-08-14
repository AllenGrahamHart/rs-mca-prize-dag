# Rank-eleven pair-core route cut: the exact wall above the paid strata

- **status:** PROVED (local route cut; zero deployed ledger movement)
- **source:** upstream PR `#1168`
  `[MCA] Cut KoalaBear error rank eleven to dense pair cores`
  (scottdhughes, 2026-08-13), stacked on `#1167` at `491ccdf53`;
  threshold note
  `experimental/notes/thresholds/kb_mca_rank11_pair_core_route_cut_v1.md`.
- **wired:** 2026-08-13 coordinator PR-review session; the certificate-class
  wall reproduced independently (`verify_audit.py`).
- **consumer:** `rate_half_band_crossing_location` (evidence).

## Setting

Post-near stratification of the KoalaBear MCA row
`(n,K,m,w) = (2097152, 1048576, 1116048, 67472)`,
`B_* = 274980728111395087`, deployed sextic line field, error rank
eleven (explanation rank `s = 10`), using `#1166`'s intrinsic near
deletion, one fixed record per post-near bad slope, and the reversible
gauge into an affine ten-flat.

## What is proved

1. **Nonuniform margin resource** (new summed theorem, not a formal
   summation of the minimum-margin statement):
   `sum_gamma theta_gamma <= C_s` with the printed falling/rising
   factorial maximum.
2. **Fixed minimizing pairs:** for cutoff `tau`, ordinary affine-span
   plus the sub-square interleaving collapse caps ordered pairs at
   `Q_s(tau) = floor(C(n-K+s,s)/C(w-tau+s,s))`; an over-budget line
   with `E = B_* - 2w + 1` post-near slopes forces one fixed pair of
   weight `>= ceil(max(0,(tau+1)E - C_s)/Q_s(tau))`. Exception sets
   are disjoint across finite slopes (an outside coordinate determines
   the slope by its affine ratio), so a fixed pair with deficiency
   `delta` owns at most `c_delta = floor((n-m+delta)/delta)` records.
3. **Exact terminals** forced on every over-budget rank-eleven line
   (the two rows' pairs need not coincide):

   | cutoff | fixed-pair weight | owned slopes | deficiency |
   |---:|---:|---:|---:|
   | 6486 | 743449148 | >= 114624 | `delta <= 8` |
   | 1795 | 360132809 | >= 200632 | `delta <= 4` |

4. **Complete declared-certificate-class wall:** with the greedy/Abel
   bound `L(J) = Q_s(1)c_1 + sum_{delta=2}^{J} (Q_s(delta) -
   Q_s(delta-1)) c_delta`, the unique optimum over all legal cutoffs is
   `J = 19737` with

   ```text
   U_high  = 5401690553097387
   U_low   = 808527428378681053
   U_total = 813929118931913384 = U_high + U_low + 2w
   U_total - B_* = 538948390820518297     (misses by a factor > 2.9)
   ```

   The stronger nonuniform relaxation's own optimizer
   (`811958533186703629`) is also over budget. **Rank eleven remains
   unpaid.**
5. **Sharpness control:** a deterministic `GF(7)` constant-code star
   (four parallel slopes on one fixed pair) refutes any
   distinct-neighbor or reduced per-pair-multiplicity inference from
   the current local hypotheses.

## The pre-registered next theorem (upstream, exact)

Couple different fixed minimizing pairs on the identical actual
received line, or route every dense parallel pair-core group
chronology-correctly to an earlier owner — and it must handle the
`delta <= 4`, `200632`-slope terminal above.

## Position in the post-near ledger

Near stratum paid (`2w = 134944`); error ranks `<= 9` paid
(`rate_half_mca_support_local_transversality_compiler`, from `#1166`);
rank 10 paid (`rate_half_mca_rank10_margin_interleaving_split_payment`,
cycle 232, independently converged by `#1167`). This node is the exact
wall at the first unpaid stratum.

## Scope

Zero active-v4 ledger movement; no KoalaBear or prize closure; the
route-cut verdict is per the declared pair/core certificate class —
an alternative coupling theorem may still pay rank eleven.

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_mca_rank11_pair_core_route_cut_import/verify.py
tools/ramguard local -- python3 \
  background/nodes/rate_half_mca_rank11_pair_core_route_cut_import/verify_audit.py
```
