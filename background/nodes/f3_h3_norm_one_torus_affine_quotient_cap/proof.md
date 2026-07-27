# Proof

For `z in T`, one has `bar(z)=z^(-1)`. If `a z+b` also lies in `T`, then

```text
1=(a z+b)(bar(a)z^(-1)+bar(b)).                     (1)
```

Multiplication by `z` gives

```text
a bar(b) z^2
 +(a bar(a)+b bar(b)-1)z
 +bar(a)b=0.                                        (2)
```

Both the leading and constant coefficients are nonzero because `a,b` are
nonzero. Equation `(2)` is therefore a nonzero quadratic over `E`, with at
most two roots. Every point counted by `I_(a,b)` is one of these roots, which
proves `(NT1)`.

For `a=t`, `b=1-t`, the exclusions `t!=0,1` make both coefficients nonzero.
Moreover `z=1` maps to `1`, so it is one of the at most two points. The
quotient representation excludes this identity point, and the PGL2 identity
therefore gives `R(t)<=1`, proving `(NT2)`.

For `p_M=2^31-1`,

```text
p_M+1=2^31,       n=2^21 | p_M+1.                  (3)
```

The roots of `X^n-1` lie in `F_(p_M^2)` because `n | p_M^2-1`. The unique
order-`n` subgroup in the quartic ambient field is consequently contained in
the quadratic subfield. For every `h in H`, `(3)` also gives

```text
h^(p_M+1)=1,       h^p_M=h^(-1),
```

so `H` lies in the quadratic norm-one torus. If `R(t)>0`, then
`t=d/c` for nonzero `c,d in 1-H`; hence `t in F_(p_M^2)^*`. Thus `(NT2)`
applies to every summand in `X_18`.

Finally, the product fibers partition the ordered pairs in
`A=(1-H)\{0}`. Hence `sum_t P(t)=|A|^2=(n-1)^2`. Nonnegativity, `(NT2)`,
and `(P-18)_+<=P` give `(NT3)`. QED.
