# Proof

The exact nonidentity quotient mass is

```text
sum_(t!=1)R(t)=(n-1)(n-2).                         (1)
```

The swap involution on ordered product representations has exactly `D(t)`
fixed points. Hence

```text
P(t)=D(t) (mod 2).                                 (2)
```

On the low part `P(t)<=35`, equation `(2)` gives the sharper pointwise bound

```text
e(t)<=16+1_(D(t)>0).                               (3)
```

Indeed, if `D(t)=0`, then `P(t)` is even and at most `34`, so `e(t)<=16`;
the indicator pays the only remaining case. Summing `(3)` and using `(1)`
shows that the low contribution to `X_18` is at most

```text
16(n-1)(n-2)+S_D.                                  (4)
```

It remains to bound the exceptional diagonal-target mass. The set
`{t:D(t)>0}` is the image of a subset of `(1-H)\{0}` under squaring, so it
has at most `n-1` elements. For `t!=1`, the quotient fiber is the affine
intersection

```text
R(t)+1=#{z in H:1-t(1-z) in H}.                    (5)
```

The extra point is `z=1`; because `t` is nonzero, it is the unique point of
this intersection whose source or target shifted factor vanishes. The two
affine forms in `(5)` are nonconstant and nonproportional because `t!=1`.
The proved affine coset-pair Stepanov theorem therefore gives,
conservatively,

```text
R(t)<(51/16)n^(2/3),
S_D<(51/16)(n-1)n^(2/3).                           (6)
```

Every official order has `n=2^s`, `s>=13`, and hence `n^(1/3)>20`. Thus

```text
(n-1)n^(2/3)<n^(5/3)<n^2/20.                      (7)
```

After multiplying `(4)` by the outer coefficient `17`, the C36' allowance
left for the high part is `B_par` from `(SQE2)`. Equations `(6)--(7)` give

```text
B_par
 >300n^2-272(n-1)(n-2)-(867/16)(n-1)n^(2/3)
 >28n^2+816n-544-(867/320)n^2
 >(8093/320)n^2.                                   (8)
```

The high part has `e(t)>=18`, equivalently `P(t)>=36`, and a positive term
has `R(t)>=1`. Equations `(4)` and `(8)` prove `(SQE2)--(SQE3)`. This is the
parity-sharpened `L=0,E=17` continuation of the Pareto diagonal.

Let `m` be the number of small unordered product representations at a
retained target. The excess ladder and disjoint-six gate give

```text
m>=7+ceil(e/2)>=16,       e<=2(m-7),               (9)
```

and the class-sensitive floors

```text
d_0(m)=ceil(m(m-4)/2)-2m-6,
d_A(m)=ceil(m(m-2)/2)-4(m-1)-8.                   (10)
```

The Pareto dependency proves that the ratios `2(m-7)/d_c(m)` decrease for
`m>=11`. At `m=16`,

```text
d_0(16)=58,       d_A(16)=44,
18/58=9/29,       18/44=9/22.                    (11)
```

Equations `(9)--(11)` prove `(SQE5)`. Multiply by `17R(t)` and sum. Since

```text
17*(9/29)*(234697/48960)=8093/320,
```

and `(9/22)/(9/29)=29/22`, condition `(SQE6)` bounds the left side of
`(SQE3)` by `B_par(n)` exactly. The lower bound `(8)` shows that `(SQE7)`
implies `(SQE6)`. This proves the row-sensitive and uniform strengthened
moment compilers.

The same dependency computes the average disjoint-six degrees from `(10)`.
At `m=16` they are at least eight in class `0` and six in class `A`, and the
degree floors only increase with `m`. Thus a selected star has at least nine
or seven distinct product-representation vertices.

It remains to couple the sole quotient lift without assuming a second one.
The zero-locus theorem says that `lambda_(E,Q)=0`, for `Q=(z,w)`, exactly
when

```text
{x,y,z}={q,-q,-q^2},       w=q^4,                 (12)
```

where `E={x,y}`. Fix `Q`. If `z=q` or `z=-q`, both choices in `(12)` give the
same unordered product pair

```text
E={-z,-z^2},       w=z^4.                          (13)
```

If `z=-q^2`, the two possible signs of `q` give the same pair

```text
E={q,-q},       w=z^2.                             (14)
```

Therefore a fixed ordered `Q` has at most the two zero-coupling product
centers `(13)--(14)`. Since either product star contains at least seven
vertices, choose a vertex `E_*` outside them. This proves `(SQE9)`.

Every normalized product difference in `J_star` and the coupling
`lambda_(E_*,Q)` vanish in the same degree-one official row-prime ideal.
They are algebraic integers, and the coupling is nonzero by construction.
Thus `I_17` is a nonzero ideal contained in the row-prime ideal. Norm reverses
ideal inclusion, proving the norm divisibility in `(SQE10)`. The selected
ordered lift remains part of the packet, so this step does not forget the
predicate `R(t)>=1`. QED.
