# Cycle 307: MCA rank-11 dense-pair degree-18 seed (2026-08-14)

Cycle 306 showed that arbitrary common-support cancellation leaves a genuine
degree-`3..17` staircase. The new proved node
`rate_half_mca_rank11_dense_pair_degree18_seed_compiler` removes that gap by
changing the 32-record selection.

The low-margin ledger gives

```text
|Z_lo| >= 190604046733790,
number of pair types <= 869784434119.
```

Therefore one actual fixed minimizing pair owns at least

```text
ceil(190604046733790/869784434119)=220
```

distinct slopes. Select eighteen. Re-anchor the heavy-pair component basis
at this dense pair. At most ten other basis pairs are needed. One record from
each and a second record from as many as the fourteen remaining slots permit
leaves at most six singly represented cores. Since each such record has at
most `387` pair exceptions and the complete heavy core is at most `K-4923`,
the selected common support obeys

```text
|C| <= (K-4923)+6*387 = K-2601.
```

A distinct heavy pair supplies one selected explanation outside the dense
pair's affine codeword line. After cancellation, the eighteen dense-pair
explanations still lie on one affine line in the slope. Any interpolation of
degree at most `17` agreeing with that line at eighteen distinct slopes is
the line identically, contradicting the off-line record. Hence the residual
explanation and slope-error degrees are exactly in `18..31`.

Focused verification:

```text
RATE_HALF_MCA_RANK11_DENSE_PAIR_DEGREE18_SEED_PASS
  owner=220 Kmin=2601 degree=18 singles=6 controls=7/7
RATE_HALF_MCA_RANK11_DENSE_PAIR_DEGREE18_SEED_AUDIT_PASS
  owner=220 core=1045975 degree=18 controls=5/5
```

No Modal computation was used.

```text
start:                   145356fe4
DAG delta:               +1 PROVED degree-interface compiler,
                         +2 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: punctured degree-3..17 gap eliminated for the
                         selected unsafe rank-eleven seed
delta-star movement:     none
compute:                 exact local arithmetic and GF(257) control only
next route action:       apply support-collapsed rational extraction at the
                         shortened parameters and expose the exact
                         rational/locator/high-complexity residual router
```
