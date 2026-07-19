# Proof

Because the deleted roots are `{b,-b,c,-c}`, their divisor is

```text
E(z)=(1-bz)(1+bz)(1-cz)(1+cz)
    =(1-b^2z^2)(1-c^2z^2).                          (1)
```

It is a polynomial in `w=z^2`. The normalized formal fourth root is unique,
so it too is a series in `w`. Thus `a_(2j)=f_j` and `a_(2j+1)=0` for every
`j`.

On the maximal generic floor, the dependency has

```text
d=8h-8,       r=2h-3,
a_(2h-2)=a_(2h-1)=0,       a_(2h)!=0.               (2)
```

Since the official `d` is divisible by `16`, write `d=16M`. Equation `(2)`
then gives `h=2M+1` and `r=4M-1`. Its three displayed coefficients are

```text
a_(4M)=f_(2M),       a_(4M+1)=0,
a_(4M+2)=f_(2M+1).                                  (3)
```

This proves `(DPP3)` and the automatic primary zero.

The low window of the dependency stops at degree `h-1=2M`; deleting its odd
terms gives `L_0` in `(DPP4)`. The shifted window begins at `2h=4M+2`.
Writing its local index as `2j` gives

```text
a_(2h+2j)=f_(2M+1+j),       0<=j<=M,                (4)
```

while every odd local index vanishes. Hence the dependency's congruence

```text
L T=a_(2h)C^2 mod z^h                               (5)
```

is exactly `(DPP5)` modulo `w^(M+1)`. The normalized square root is unique
because two is invertible. Since its square is even, uniqueness also makes
the root even. The two forbidden secondary degrees are

```text
h-2=2M-1,       h-1=2M.                             (6)
```

The first vanishes automatically and the second is `[w^M]C_0`, proving
`(DPP6)`.

It remains to remove common scaling. Both `u` and `v` are nonzero
`(d/2)`-th roots, and distinct antipodal pairs give `u!=v`. Put `x=uw` and
`t=v/u`. Then `t^(d/2)=t^(8M)=1`, `t!=1`, and `(1)` becomes

```text
(1-x)(1-tx).                                        (7)
```

The coefficient relation is `f_j=u^jF_j(t)`. In `(DPP3)` the nonzero factor
`u^j` can be discarded. In `(DPP5)`, the shifted window contributes the
common factor `u^(2M+1)`, which cancels the identical factor in
`f_(2M+1)`; changing `w` to `x` multiplies the last root coefficient by the
nonzero factor `u^M`. Therefore all three conditions are exactly `(DPP9)`.

Finally, logarithmically differentiating

```text
(1-(1+t)x+tx^2) (sum_j F_jx^j)^4=1
```

and comparing the coefficient of `x^(j-1)` gives `(DPP8)`. It computes every
quantity in `(DPP9)` from the single torsion ratio `t`. QED.
