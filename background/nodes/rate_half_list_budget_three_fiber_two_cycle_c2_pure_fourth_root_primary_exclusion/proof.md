# Proof

For a scaled fourth-root quartet the canonical covariance permits a common
subgroup scaling to `(PFR2)`. The generalized binomial theorem gives

```text
(1-z^4)^(-1/4)
 =sum_(j>=0) (1/4)(1/4+1)...(1/4+j-1)/j! z^(4j),     (1)
```

which is `(PFR3)`.

The official primary index is

```text
m=2H-2=2^38=4*2^36.                                  (2)
```

Thus `(1)` gives `(PFR4)`. It remains only to check that this coefficient
does not vanish in the official characteristic. The maximal-row field-degree
collapse and budget lower bound imply `p>2^40`. Put `J=2^36`. Every factor
of the numerator of `(PFR4)`, after multiplying by four, is

```text
4ell+1,       0<=ell<J,
```

and lies strictly between zero and `4J=2^38<p`. Every factor of `J!` is also
strictly between zero and `p`, while four is invertible. The numerator and
denominator are consequently nonzero in both the prime and quadratic field
lines. Hence `a_m!=0`.

The normalized gap-span compiler requires `a_(2H-2)=0` for every generic
`c=2` survivor. This contradiction excludes the pure fourth-root geometry.
Undoing the common subgroup scaling only multiplies `a_m` by a nonzero
scalar, so the conclusion covers every scaled quartet. QED.
