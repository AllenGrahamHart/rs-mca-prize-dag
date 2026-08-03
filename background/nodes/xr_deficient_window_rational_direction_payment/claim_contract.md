# Claim contract

## Inputs

- A tangent-gated high-band depth `ceil(h/2)<=d<=h-2`.
- A nonzero left kernel `K_d` of the stacked window matrix.
- The maximal selected exact-depth currency from SL-2-RES.
- `q>n`, as permitted by the sufficiently-large-field prize contract.

## Outputs

- The pointwise rational-direction law `(RD)` for every kernel syzygy.
- One syzygy whose common evaluation roots are exactly the whole-kernel
  forced set `G_d`.
- The rank bound `dim K_d<=2(d-|G_d|)`.
- The unconditional payment `N_d^out<=n-|G_d|`.
- The localization implication `N_d^G>0 => |G_d|>=2(h-d)`.

## Exclusions

- No bound on the `G_d`-local family `N_d^G`.
- No count at full stacked rank.
- No replacement of first-match selected rays by arbitrary exact-`A` rays.
- No claim that resistance of the remaining family is evidence of closure.
