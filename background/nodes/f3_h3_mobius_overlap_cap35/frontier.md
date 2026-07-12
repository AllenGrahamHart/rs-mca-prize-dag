# Frontier

## Proved around the leaf

- `N_3to1(A)=sum_t P(t)R(t)` exactly.
- `R(1)=n-1` and `sum_{t!=1}R(t)=(n-1)(n-2)`.
- `P(1)` is the one-shift subgroup intersection already bounded by Stepanov:
  `P(1)<4n^(2/3)`.
- `(M35)` therefore implies C36' on every official row; the exact compiler is
  replayed by `verify.py`.
- The first twelve official primes at `n=8192` have overlap maximum between
  `14` and `20` (Modal run `ap-SSyWX6F4I6C3DMzaKwx3rk`).

## Disposition

The pointwise cap was replaced on the critical path by the weaker weighted
node `f3_h3_mobius_excess_half`. Proving `(M35)` still closes that leaf with
zero excess, but rich fibers with small quotient weight no longer have to be
excluded. Numerical survival is evidence only.
