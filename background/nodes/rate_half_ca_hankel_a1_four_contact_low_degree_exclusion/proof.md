# Proof

Work on the core-stripped residual curve `C` of bidegree `(d,e)`. Let `p` be
the colength of its pole-cancellation ideal. Since

```text
4(floor(p/4)+1)>p,                                    (1)
```

a nonzero biform `F` of bidegree `(3,floor(p/4))` clears the poles of the
residual-domain-locator ratio `G/H`.

Choose a component on which the core-stripped contact section is nonzero.
If its domain degree were at most three, its contact degree would be at most

```text
3(e+1)-(rho+1)<0,                                     (2)
```

contrary to `(A1Q2)`. Thus `F` does not contain that component, and the
regular section `FG/H` is nonzero there.

Four contact copies give a nonzero section of

```text
O_C(-s-1,floor(p/4)+ell+4-beta).                      (3)
```

The first degree follows from

```text
(N-s)+3-4(rho+1)=-s-1.
```

The middle surface bundle in the restriction sequence has no sections
because its first degree is negative. After subtracting the equation of
`C`, the kernel bundle is

```text
O(-rho-1,floor(p/4)-e+ell+4-beta).                    (4)
```

Under `(A1Q3)` both degrees in `(4)` are negative, so Kunneth gives zero
`H^1`. The curve bundle in `(3)` has no sections, a contradiction.

For the official prefixes it suffices to use `p<=Delta` and the largest
possible slope slack.

For `s=0`,

```text
Delta=4m-e,       beta=0,       ell<=4e-4m-2.
```

Substitution in `(A1Q3)` proves the strict inequality through
`e=floor(12m/11)-1`. For the official `m=2^37`, equality first occurs at
`e=floor(12m/11)`.

For `s=1`,

```text
Delta=4m-1-2e,    beta=1,       ell<=4e-4m-1.
```

The same integer division proves the strict inequality through
`e=floor(6m/5)-1`. For the official row, equality first occurs at
`floor(6m/5)`.
Both prefixes satisfy `(A1Q2)`. This proves `(A1Q4)`. QED.
