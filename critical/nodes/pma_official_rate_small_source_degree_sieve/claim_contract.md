# Claim contract - PMA official-rate small-source degree sieve

## Inputs

1. An exact official row `n=rk`, `r in {2,4,8,16}`.
2. A maximal source decomposition
   `(r-1)k+1=Mell+b`, `0<=b<ell`.
3. An exact core defect `d<=k-1`.
4. For the rate-quarter payment, a full-petal `M=4,t=3` contributor and the
   proved three-petal mu-basis reduction.

## Outputs

1. No strict full-petal residual whenever `M<=r-2`.
2. Empty strict scales `M<=6` at rate `1/8` and `M<=14` at rate `1/16`.
3. The exact rate-quarter upper-branch gate `2b>=ell+8` at `M=4,t=3`.
4. A `4k` bound for its complementary small-background branch.

## Consumer obligation

Remove these cells before attacking the remaining split-core-divisor count.
Do not extrapolate the sieve to `M=r-1`, rounded rates, two-petal modules, or
partial petals.

## Nonclaims

- no count for rate-half `M=4,t=3` upper modules;
- no count for the rate-quarter large-background upper modules;
- no payment for `M=4,t=2`;
- no change to larger-`M` or partial-petal residuals;
- no promotion of `petal_mixed_amplification`.

## Falsifiers

- an official exact-rate maximal source with `M<=r-2` and `ell<=k`;
- a rate-quarter `M=4` row where upper-branch arithmetic disagrees with
  `2b>=ell+8`;
- more than one projective exact saturated contributor for a fixed lower-
  branch defect and touched triple.
