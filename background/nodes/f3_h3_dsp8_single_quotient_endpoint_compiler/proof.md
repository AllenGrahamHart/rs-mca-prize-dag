# Proof

The exact nonidentity quotient mass is

```text
sum_(t!=1)R(t)=(n-1)(n-2).                         (1)
```

Split `X_18=sum_(t!=1)e(t)R(t)` at `e(t)=17`. The low part is at most

```text
17 sum_(t!=1)R(t)=17(n-1)(n-2).                    (2)
```

After multiplying `(2)` by the outer coefficient `17`, the C36' allowance
left for the high part is exactly

```text
300n^2-17^2(n-1)(n-2)=B_(0,17)(n).                (3)
```

The high part has `e(t)>=18`, equivalently `P(t)>=36`, and a positive term
has `R(t)>=1`. Expanding `(3)` gives `(SQE1)`, and `(2)--(3)` prove that
`(SQE2)` implies C36'. This is the `L=0,E=17` continuation of the existing
Pareto diagonal; it uses the full quotient mass rather than the
`T_L<=(n-2)^2` estimate, which begins only at `L=1`.

Let `m` be the number of small unordered product representations at a
retained target. The excess ladder and disjoint-six gate give

```text
m>=7+ceil(e/2)>=16,       e<=2(m-7),               (4)
```

and the class-sensitive floors

```text
d_0(m)=ceil(m(m-4)/2)-2m-6,
d_A(m)=ceil(m(m-2)/2)-4(m-1)-8.                    (5)
```

The Pareto dependency proves that the ratios `2(m-7)/d_c(m)` decrease for
`m>=11`. At `m=16`,

```text
d_0(16)=58,       d_A(16)=44,
18/58=9/29,       18/44=9/22.                     (6)
```

Equations `(4)--(6)` prove `(SQE4)`. Multiply by `17R(t)` and sum. Since

```text
17*(9/29)*(319/153)=11,
```

and `(9/22)/(9/29)=29/22`, condition `(SQE5)` bounds the left side of
`(SQE2)` by `11n^2<B_(0,17)(n)`. This proves the moment compiler.

The same dependency computes the average disjoint-six degrees from `(5)`.
At `m=16` they are at least eight in class `0` and six in class `A`, and the
degree floors only increase with `m`. Thus a selected star has at least nine
or seven distinct product-representation vertices.

It remains to couple the sole quotient lift without assuming a second one.
The zero-locus theorem says that `lambda_(E,Q)=0`, for `Q=(z,w)`, exactly
when

```text
{x,y,z}={q,-q,-q^2},       w=q^4,                 (7)
```

where `E={x,y}`. Fix `Q`. If `z=q` or `z=-q`, both choices in `(7)` give the
same unordered product pair

```text
E={-z,-z^2},       w=z^4.                          (8)
```

If `z=-q^2`, the two possible signs of `q` give the same pair

```text
E={q,-q},       w=z^2.                             (9)
```

Therefore a fixed ordered `Q` has at most the two zero-coupling product
centers `(8)--(9)`. Since either product star contains at least seven
vertices, choose a vertex `E_*` outside them. This proves `(SQE7)`.

Every normalized product difference in `J_star` and the coupling
`lambda_(E_*,Q)` vanish in the same degree-one official row-prime ideal.
They are algebraic integers, and the coupling is nonzero by construction.
Thus `I_17` is a nonzero ideal contained in the row-prime ideal. Norm reverses
ideal inclusion, proving the norm divisibility in `(SQE8)`. The selected
ordered lift remains part of the packet, so this step does not forget the
predicate `R(t)>=1`. QED.
