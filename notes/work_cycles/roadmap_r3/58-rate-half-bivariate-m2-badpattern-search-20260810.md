# Cycle 58: rate-half bivariate m=2 bad-pattern search (2026-08-10)

## Question

After the `m=1` row-surplus fence, test the narrower prospective theorem:
does a canonical pair union that violates the exact closing intersection cap
force the deficiency-aware matrix to have no blockwise-nonzero kernel?

## Bounded campaign

Thirty-two Modal workers ran for 45 seconds each with 256 MB memory. Each
worker checkpointed aggregate counts on return. The complete campaign found

```text
random trials                         1,276,996
exact near-saturated incidence rows    841,449
open bad-overlap pair cases           1,795,113
rank-deficient matrices                       0
blockwise kernels                             0
degree-rho extensions                         0
full Hankel witnesses                         0
```

The search used `m=2`, `N=32`, `rho=7`, `T=9`, one global deficiency unit,
the smooth domain `mu_32` in `F_97`, and every exact minimum-pair support in
the open band. A survivor would next have faced degree-`rho` interpolation,
maximal parameter-span, complete split-slope census, and Hankel-rank checks.
No matrix reached those gates.

## Interpretation

The contrast is clean: the genuine `m=1` failure has rank defect one on all
ten canonical supports, while none of 1.79 million bad `m=2` support cases
had any rank defect. This is strong heuristic evidence that bad overlap and
kernel existence are incompatible once `m>1` structure appears.

It remains non-probative for the official theorem: the campaign is random,
uses one field, and samples `m=2`, not `m=2^37`. The next mathematical task is
to identify the minor or rank decomposition responsible for the observed
separation. No critical status changes.
