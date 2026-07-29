# E1 profile-36 orbit debit

## Status

Exact draft lemma, not a DAG node. The proof is algebraic and the arithmetic
replay is committed, but Modal is over its spend limit. No pair-budget or
cofactor node is promoted here.

## Statement

Fix a pair-feasible prize rate-`1/8` row and a collision in profile
`(3,6,S=18)` with pure dyadic cofactor `m in {2,4,8}`. One full affine
coefficient orbit contributes exactly 256 oriented folded kernel vectors to
`D_p(33)`: 128 translations at the unique vanishing primitive root, and their
128 global negatives.

Consequently, if `C_36` is the number of colliding full affine coefficient
orbits across those cofactors, their exact weighted-kernel debit is

```text
256 M_33(3,6) C_36,
M_33(3,6)=1386246316188473270092082114587711840.
```

The coarse profile-only allowance is sharp at

```text
C_36 <= 367.
```

At 367 orbits the profile uses 93,952 of the 93,962 oriented-vector units and
leaves ten maximum-weight units. Orbit 368 alone uses 94,208 and exceeds the
coarse budget.

## Proof

Write `Norm(F)=2^mu p` with `mu in {1,2,3}`. Since `p` is odd and appears to
the first power, exactly one primitive root `zeta^u` modulo `p` is a simple
zero of `F`. Two distinct primitive roots, or a multiple zero, would make
`p^2` divide the cyclotomic norm.

For every `b in Z/256`,

```text
X^b F(X^u)
```

vanishes at the fixed root `zeta`. Multiplication by `X^b` is signed cyclic
translation in the folded 128-coordinate model: the first 128 values give
support translations and adding 128 gives the corresponding global negative.
It preserves the coefficient profile and dictionary weight. Exact singleton
multiplicity one, two, or three forbids a period-64 support: a period-64
six-set is paired and its low Hasse derivatives cancel. No larger nontrivial
translation period can partition six points because its orbit length is a
power of two greater than two. Thus all 256 signed translates are distinct.

The unique primitive root makes these the complete fixed-root slice of that
full affine coefficient orbit, so the contribution is exactly 256, not only
a lower bound. Distinct affine coefficient orbits give disjoint slices.

The proved weighted dictionary then multiplies each vector by
`M_33(3,6)`. Exact division gives

```text
floor(2 E_max / (256 M_33(3,6))) = 367,
367*256 = 93952,                  368*256 = 94208.
```

## Scope

This does not assert `C_36<=367`. It changes the required output of the next
search: exact emptiness of `m=2,4,8` is sufficient but unnecessary. A packet
that bounds their combined collision-orbit count, and charges all other
profiles in the same weighted ledger, can close the pair-budget target.

The argument uses the pure dyadic cofactor. Cofactors containing 257 can have
different odd-part accounting and are already closed in this profile. The
candidate `m=16` branch is also pure dyadic and obeys the same debit, but its
primary packet already reports zero unresolved vectors and awaits only its
independent audit.

## Guards

1. `C_36` counts full affine coefficient orbits, including heavy positions
   and every coefficient sign. A singleton-support orbit is not one unit of
   this ledger.
2. The unit action is the order-256 cyclotomic Galois action. The support
   atlas sees units modulo 128 only because the second lift is the sign twist;
   implementations must restore that twist before counting root incidences.
3. The 256-vector slice is `b in Z/256`. In folded coordinates it appears as
   128 distinct support translations and their global negatives. Do not add a
   second factor two for orientation.
4. A norm-interval survivor is not automatically a collision orbit. It enters
   `C_36` only after one row prime and its unique primitive-root incidence are
   certified, or as a rigorously counted worst-case survivor in an upper-bound
   packet.
5. `C_36<=367` pays only the profile-36 coarse budget when every other debit
   is zero. In the actual target, all other profiles must be charged in the
   exact weighted sum.
6. Nothing here proves `C_36<=367`; the result is a compiler for the next
   search output.

## Replay

```bash
./tools/ramguard modal -- modal run \
  experiments/prize_resolution/e1_profile_36_orbit_debit_modal.py
```
