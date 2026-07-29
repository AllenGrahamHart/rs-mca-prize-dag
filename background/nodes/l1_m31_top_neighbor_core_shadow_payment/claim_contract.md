# Claim contract - M31 top-neighbor core-shadow payment

## Proved

- Every fixed degree-`t-r` anchor core supports at most the actual-list
  neighbor count `B_r` in `(CS1)`.
- A fixed degree-`4979` one-root-swap core supports at most `240` top
  neighbors, including all scalar labels across all swap roots.
- The forced M31 dense-top anchor uses at least `4,477,705` distinct
  degree-`4979` core divisors.

## Not claimed

- No bound on the total number of available or realized cores.
- No disjoint ownership of different core payments.
- No use of the decorated Pade identity beyond the predecessor's production
  of actual top neighbors.
- No `Q=147595`, M31 row, adjacent-row, or Prize closure.

## Falsifier

An actual fixed-core neighbor outside the affine flat in the proof, a
violation of the affine-span list theorem, a nonsquarefree top direction, or
failure of the incidence count in `(CS3)`.
