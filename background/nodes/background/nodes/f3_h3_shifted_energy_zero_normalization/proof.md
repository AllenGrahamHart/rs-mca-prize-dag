# Proof

For a finite set `X`, write

```text
r_X(t)=#{(x,y) in X^2:xy=t},       E_x(X)=sum_t r_X(t)^2.
```

The set `S=H-1` has `n` elements and contains zero exactly once. Hence

```text
r_S(0)=2n-1:
```

there are `n` ordered pairs with first coordinate zero and `n` with second
coordinate zero, with `(0,0)` counted in both lists. For every nonzero `t`,
both factors in a representation of `t` are nonzero, so

```text
r_S(t)=r_A(t).
```

Squaring and summing proves `(ZN1)`.

Negation preserves multiplicative energy, so

```text
E_x(A)=E_x((1-H)\{0}).
```

The dependency `f3_h3_identity_deficit_energy_close` proves that

```text
E_x((1-H)\{0}) <= (145/4)(n-1)^2
```

implies C36'. Subtracting `(2n-1)^2` from `(ZN2)` and applying `(ZN1)`
therefore proves the compiler. Expanding the two squares gives `(ZN3)`.

For `(ZN4)`, add `n^4/p` to the centered source estimate and compare with
`(ZN2)`. Official rows have `p>=n^2`; equality is impossible because `p` is
prime and `n^2` is a proper power of two. Thus `p>n^2` and `n^4/p<n^2`,
which gives the first inequality in `(ZN5)`.

After division by `n^2`, the remaining lower bound is

```text
157/4-153/(2n)+149/(4n^2).
```

It is increasing for `n>=1`, and at the smallest official order `n=8192` it
is strictly greater than `981/25=39.24`. This proves `(ZN5)`.

The source distinction is material. Macourt--Shkredov--Shparlinski,
Corollary 4.1, states the energy of the whole shift `H+lambda`; it does not
delete a zero that occurs when `-lambda in H`. The exact correction above is
therefore required before calibrating its implicit error term.
