# Proof

## The outer component is rational

Let `S=<a,c>` be the full endpoint V4 stabilizer. The normalization of the
outer image is `C=Gamma/S`.

If `g(Gamma)=0`, every quotient is rational. Suppose
`g(Gamma)=1`. The genus-drop theorem gives `#Fix(a)=0`, so `a` is translation
by a nonzero two-torsion point. An involution of an elliptic curve is either
such a translation or a reflection with four fixed points. A two-torsion
translation commutes with every elliptic reflection: after writing a
reflection as `x->P-x`, conjugation by translation by `A` replaces `P` by
`P+2A=P`. But the genus-drop theorem proves

```text
c eta c^(-1)=eta*a != eta.
```

Thus `c` is not a fixed-point-free translation; it is a reflection and has
four fixed points. The product `a*c` is another reflection and also has four
fixed points. Riemann-Hurwitz for `Gamma->Gamma/S` is therefore

```text
0=4(2g(C)-2)+0+4+4,
```

so `g(C)=0`.

The same fixed-point count gives the branch passports. In genus zero all
three nontrivial V4 involutions have two fixed points, producing three base
branch values with inertia `a,c,ac`. In genus one, `a` is unramified and the
four fixed points of each reflection form two V4 orbits, producing inertia
`c,c,ac,ac`.

## Dihedral factor

The two projections

```text
Y,Z:C=P1 -> P1
```

both have degree two. Let `u` and `v` be their deck involutions. They are
distinct: equality would make the two quotient subfields equal, so the
image in `P1 x P1` would be a `(1,1)` graph rather than the actual
`(2,2)` component.

The degree-60 function `R=F(Y)=F(Z)` on `C` is invariant under `u` and `v`.
Its deck group is finite, hence `<u,v>` is a finite dihedral group `D_n` of
order `2n`, with `n>=2`. The quotient tower

```text
C -> C/<u>=P1_Y -> C/D_n=P1
```

has degrees `2` and `n`. The function `R` descends through the final
quotient, which gives

```text
F=G composed q_n.                                   (KBMD-2)
```

After projective changes of source and target, `q_n` is the degree-`n`
Dickson/Chebyshev quotient. Since `deg(F)=30`, equation `(KBMD-2)` gives
`n|30`.

## Pole restriction

A tame degree-`n` dihedral quotient has local ramification indices

```text
1, 2, or n,
```

with one totally ramified point of index `n` and the remaining branch
points of index two. If `y` is a pole of `G`, then every `x` above it has

```text
ord_x(F)=e_(q_n)(x) ord_y(G)=5.                    (KBMD-3)
```

Thus a selected point is either unramified above an order-five pole, or has
index five above a simple pole. If `n!=5`, the second alternative is absent.
Every pole fiber is then unramified and contributes `n` of the six poles of
`F`; hence `n|6`. Intersecting `n|6` with `n|30` and `n>=2` gives
`n=2,3,6`.

For `n=5`, one generic fiber contributes five unramified poles over an
order-five pole of `G`, and the unique totally ramified point contributes
the sixth over a simple pole. Their pole orders sum to `5+1=6=deg(G)`, so
this is the sole index-five profile. Conversely this argument excludes
`n=10,15,30`: none has index five, while an unramified fiber already has
more than six points. This proves `(KBMD-1)` and every stated pole profile.
QED.
