# E1 N=256 local-norm cofactor collapse

- **status:** PROVED
- **closure:** proof plus local reciprocity

Let `zeta` be a primitive `256`-th root, let
`alpha=F(zeta)` have either first-band `N=256,s=5` profile, and
put

```text
R=|Norm_(Q(zeta)/Q)(alpha)|,
mu=v_2(R).
```

For every nonzero such norm,

```text
R/2^mu = 1 mod 256.                                    (1)
```

Suppose a pair-feasible row prime `p` divides `R`, and write
`R=p m`. The prime-field reduction gives `p=1 mod 256`. Therefore

```text
m/2^mu = 1 mod 256.                                   (2)
```

The exact cofactor bounds then collapse as follows:

- profile `(3,4,0)`: `1<=mu<=5`, `m<64`, and necessarily
  `m=2^mu`. Thus a collision norm is exactly `R=2^mu p`;
- profile `(4,2,0)`: `mu in {1,2,4,8,16}` and
  `m=2^mu(1+256t)<2^17`. There are exactly `419` resulting
  cofactor values.

In particular, the square-mass-16 profile has only five possible cofactors,
not every integer below 64. This is a necessary norm shape, not a proof that
the odd norm part is prime or lies in a live interval.
