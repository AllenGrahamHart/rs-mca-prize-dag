# Sharp rate-half FPC5 cross-cofactor coordinate

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Fix one official sharp rate-half `M=4,t=2` source, one touched pair, and one
exact anchor contributor with primitive cofactors `(A_1,A_2)` and monic
defect locator `F_0`. Let `L_0` be the full background locator of degree
`ell-3`.

Let `M` be the complete affine slice of cofactor pairs
`(A'_1,A'_2)` satisfying the guarded congruence and whose associated defect
locator `F` is monic of degree `2ell-3`. Define

```text
Delta_A=A_1A'_2-A'_1A_2,
E=Delta_A/L_0.                                        (CC1)
```

Then `L_0|Delta_A`, `deg E<=ell-3`, and

```text
M -> K[X]_(<=ell-3),       (A'_1,A'_2) -> E            (CC2)
```

is an affine bijection sending the anchor to `0`. In particular, `E`
determines the guarded pair `(F,W)` uniquely before splitness, primitivity,
untouched-petal, and first-owner filters are imposed.

For every distinct exact contributor in this slice,

```text
E!=0,
gcd(E,F_0)=gcd(F,F_0).                                (CC3)
```

Thus the common-error owner in the specialized balanced determinant atlas is
recovered directly from the FPC5 cofactor coordinate. If

```text
D=gcd(E,F_0),       deg D=ell-3-j,                    (CC4)
```

then `0<=j<=ell-3` and the fixed-`D` bounds `(SH8)--(SH9)` apply. The
remaining sharp count is exactly the problem of bounding the set of
coordinates `E` whose reconstructed `F_E` splits on the core and passes all
exact FPC5 guards, aggregated across the realized gcd strata of one anchor.

## Scope

The bijection is for the complete guarded monic linear slice; exact
contributors form a filtered subset. The theorem does not assert that every
`E` reconstructs a split locator, bound the number of realized gcd owners,
or permit a sum over all divisors of `F_0`. It removes background-set and
fixed-pencil multiplicity from the sharp owner problem but does not close it.
