# Proof

## Autocorrelation reduction

At every primitive odd conjugate, the antisymmetric negacyclic coefficient
pair gives

```text
y_u=|F(zeta_256^u)|^2
   =20+sum_(d=1)^63 A_d(zeta_256^(ud)+zeta_256^(-ud)).   (1)
```

Parseval gives

```text
V=(1/64)sum_(u odd modulo sign)(y_u-20)^2=2E.           (2)
```

Because the `A_d` are integers, every spectrum with `E<=4` has exactly one
of the following shapes:

```text
E=1: one entry +-1;
E=2: two entries +-1;
E=3: three entries +-1;
E=4: four entries +-1, or one entry +-2.               (3)
```

This gives the four binomial counts in the statement.

## Exact norm attached to a spectrum

For a nonzero spectrum `A`, put `D=max{d:A_d!=0}` and

```text
H_A(X)=20X^D+sum_d A_d(X^(D+d)+X^(D-d)).               (4)
```

Multiplication by `X^D` has resultant of absolute value one against
`X^128+1`. Equation (1), paired over the `128` primitive roots, therefore
gives the exact identity

```text
|Res(X^128+1,H_A)|=|Norm(F(zeta_256))|^2.              (5)
```

Thus the positive integer square root of the resultant in (5) depends only
on the abstract autocorrelation spectrum. No coefficient-vector
realizability assumption is needed for an exclusion.

## Exhaustion

The three pinned FLINT programs enumerate (3) directly, construct (4), take
the exact integer resultant, verify that it is a square, and compare its
positive square root `R` with the exact official interval.

For energies one and two, all `7938` spectra are tested against every legal
cofactor. For energy three, the `317688` spectra are first routed by their
exact 2-adic valuation and then tested against the matching legal cofactors.
Both enumerations have empty viable lists.

For energy four, there are `9530766` spectra. For each norm the program
computes

```text
m_min=ceil(R/p_max),       m_max=floor(R/p_min).        (6)
```

The interval in (6) has width at most one. Across the complete census it
contains no integer at all, a condition stronger than failure of the legal
cofactor sieve. The `128` shards all returned and the aggregate viable list
is empty. Hence no official collision has `E<=4`, proving (P44-E). QED.
