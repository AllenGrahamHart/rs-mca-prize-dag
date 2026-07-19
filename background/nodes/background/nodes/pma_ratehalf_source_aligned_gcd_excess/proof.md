# Proof - PMA rate-half source-aligned gcd excess

## 1. The source quotient code

The Chinese remainder theorem gives the unique `E_c` in (AG1), because the
three monic petal locators are pairwise coprime and their product has degree
`3ell`. Divide `L_C E_c` by `L` as in (AG2).

At a root `x` of `L_i`, equation (AG2) gives

```text
P_*(x)=L_C(x)E_c(x)=c_iL_C(x).
```

Thus `P_*` has the required planted values on all `3ell` petal points. Its
degree is less than `3ell`, so uniqueness of interpolation identifies it with
the polynomial used in the core-list reduction.

At a core point `x`, `L_C(x)=0` and `L(x)!=0`. Equation (AG2) becomes

```text
P_*(x)+L(x)Y(x)=0,
```

which proves (AG3).

The map from `(c_1,c_2,c_3)` to `P_*` is injective. If `P_*=0`, then (AG2)
shows that `L` divides `L_C E_c`. Core and petals are disjoint, so
`gcd(L,L_C)=1`; hence `L|E_c`. Since `deg E_c<deg L`, one has `E_c=0`, and
the CRT residues give `c_1=c_2=c_3=0`.

For a nonzero label vector, `P_*` is therefore a nonzero polynomial of degree
less than `3ell`. On the core, `Y(x)=0` exactly when `P_*(x)=0`. It has at
most `3ell-1` such roots, proving (AG4). The same argument proves that the
label-to-core-word map is injective, so its dimension is exactly three.

## 2. Actual overlap, not ambient equality

For `x in C`, equation (AG3) gives

```text
H_i(x)=y(x)
iff P_*(x)+L(x)H_i(x)=0
iff P_i(x)=0.                                        (1)
```

Let `S_i=Z_C(P_i)`. Since `L_C` is squarefree, the degree of a gcd with
`L_C` is the number of its common core roots.

Also

```text
P_1-P_2=L A,       P_1-P_3=L B,
P_2-P_3=L(B-A).                                     (2)
```

The factor `L` has no core root. Equations (1)--(2) therefore give the exact
identities

```text
|S_1 intersect S_2|=u_12,
|S_1 intersect S_3|=u_13,
|S_2 intersect S_3|=u_23,
|S_1 intersect S_2 intersect S_3|=tau.              (3)
```

For any three subsets of an `N`-point set,

```text
sum_i |S_i|
 =|S_1 union S_2 union S_3|
  +sum_(i<j)|S_i intersect S_j|
  -|S_1 intersect S_2 intersect S_3|.               (4)
```

If every `|S_i|>=m`, then (3)--(4) and the bound on the union give

```text
u_12+u_13+u_23-tau>=3m-N.
```

Substitution of `N=4ell+b-2`, `K_0=ell+b-1`, and
`m=2ell+b+a-2` yields (AG6).

If a fixed cell had three contributors, selecting any three would produce
(AG6). Its failure therefore bounds that cell by two. Summing fewer than `n`
defects over four touched triples gives `8n`.
