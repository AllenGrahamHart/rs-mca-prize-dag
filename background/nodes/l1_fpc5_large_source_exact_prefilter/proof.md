# Proof: large-source exact prefilter

Use the full-petal support size `h=t ell`. The fixed-support defect theorem
gives the list threshold

```text
h>=d+g,       g=ell-b.                               (1)
```

After rearrangement, `(1)` is exactly

```text
u=d+ell-h<=b.                                        (2)
```

Therefore `u>b` is impossible, proving the empty clause.

The same fixed-support theorem gives singleton size when `r=2d-h<0` and the
ordinary Johnson payment `(PF5)` when `r>=0` and its denominator is positive.

For the second singleton clause, apply the proved background-overlap theorem
with

```text
a=N-d,       s=h-d,       g=ell-b.
```

Its strict singleton inequality is

```text
a+s<ell+g.
```

Substitution gives

```text
N-d+t ell-d<2ell-b,
```

which is precisely `(PF2)`.

Finally suppose `b>0`, `0<=u<=b`, and `r>=0`. The proved joint
core/background Johnson theorem applies after choosing canonically `u`
background agreement points. Its denominator is exactly `(PF3)` and its
bound is `(PF4)`.

An unpaid nonsingleton cell must avoid every preceding payment. Negating the
strict inequalities gives `(PF6)`. The FPC5 degree cap is

```text
d<=min(ell(M-2)-1,N).
```

Combining it with `(2)` and the negation of `(PF2)`, using integrality, gives
`(PF7)`. QED.
