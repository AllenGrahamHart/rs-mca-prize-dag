# Proof

The product-space proof in the quadratic locator-rank gate places `VV` in

```text
S=span({A^2} union
       {A U_i, X A U_i, U_i^2:1<=i<=e}).             (1)
```

The displayed generators are independent. Divide a relation by `A^2` and
put `f_i=B/D_i`. At the two roots of `D_i`, the double-pole coefficients
first kill the coefficient of `f_i^2`; the two simple-pole equations then
kill both coefficients of `(alpha_i+beta_iX)f_i`. The constant dies last.
Hence

```text
dim S=3e+1.                                          (2)
```

For `i!=j`, coprimality makes the map

```text
F[X]_(<=1) x F[X]_(<=1) -> F[X]_(<=3),
(u,v) |-> uD_j+vD_i
```

an isomorphism. Let the unique pair satisfying

```text
B=u_ijD_j+v_ijD_i                                   (3)
```

have leading coefficients `a_ij,c_ij`. Monicity gives
`a_ij+c_ij=1`, and

```text
U_iU_j=u_ij A U_i+v_ij A U_j.                       (4)
```

Let `Lambda` be a linear functional on `S` that annihilates `VV`. Since
`A^2`, `A U_i`, and `U_i^2` are products, it is determined by

```text
y_i=Lambda(X A U_i).                                (5)
```

Equation `(4)` says that it annihilates every cross product exactly when

```text
a_ij y_i+c_ij y_j=0       for every i!=j.           (6)
```

We interpret `(6)` geometrically. In the three-dimensional affine space of
polynomials of degree at most two, define the line

```text
L_i(y_i)={y_iB+tD_i:deg t<=1, [X]t=-y_i}.           (7)
```

The leading condition cancels the cubic term, and the direction of this
line is `D_i`. The lines `L_i(y_i)` and `L_j(y_j)` intersect if and only if
`(6)` holds. Indeed, an intersection is equivalent to

```text
(y_i-y_j)B=t_jD_j-t_iD_i.                           (8)
```

Using `(3)`, take

```text
t_j=(y_i-y_j)u_ij,       t_i=-(y_i-y_j)v_ij.
```

Their required leading coefficients are equivalent to `(6)` because
`a_ij+c_ij=1`. The converse follows from uniqueness in `(3)`.

Thus every annihilating functional gives pairwise-intersecting affine
lines `(7)`. By `(GSDFC1)`, three of their directions are linearly
independent. Three pairwise-intersecting lines are either concurrent or
coplanar; the latter would put their directions in a two-dimensional vector
space. They are therefore concurrent. Any remaining line meets the first
two inside their plane and also meets the third, whose only point in that
plane is the common point. Hence all lines pass through one polynomial
`R` of degree at most two. Membership in `(7)` says exactly

```text
D_i | R-y_iB.                                       (9)
```

Conversely, a solution of `(9)` makes all lines `(7)` concurrent. The pair
intersection calculation gives `(6)`, so `(5)` defines a functional on `S`
annihilating every product.

These constructions are linear and inverse. If every `y_i=0`, then `(9)`
makes the degree-at-most-two polynomial `R` divisible by all pairwise
coprime `D_i`, hence `R=0`. Therefore the map from `K` to the annihilator of
`VV` in `S^*` is injective as well as surjective. Equations `(2)` and `(9)`
give `(GSDFC4)`.

It remains to bound the defect dimension. Suppose two independent solutions
`(R,y)` and `(S,z)` belonged to `K`. The projection from `K` to its
quadratic coordinate is injective: if `R=0`, coprimality of `B` and every
`D_i` forces all `y_i=0`. Thus `R,S` are linearly independent. For every
`i`, elimination of `B` gives

```text
D_i | z_iR-y_iS.                                    (10)
```

If the degree-at-most-two polynomial on the right is nonzero, `(10)` puts
`D_i` in `span{R,S}`. If it is zero, independence of `R,S` forces
`y_i=z_i=0`; then `D_i` divides both `R` and `S`, again making them
dependent. Thus every `D_i` lies in one two-dimensional space, contradicting
`(GSDFC1)`. Hence `dim K<=1`, proving `(GSDFC4a)` and the exact two ranks in
the statement.

For a nonzero solution, `R` cannot vanish identically. If `y_i=0`, then
`D_i|R`, which can occur for at most one `i`. Otherwise `R` is nonzero at
both roots of `D_i` because `B` is coprime to `D_i`, and `(9)` gives
`(GSDFC5)`. If `y_i=y_j!=0`, equation `(6)` and
`a_ij+c_ij=1` give `y_i=0`, a contradiction. Hence the nonzero levels are
pairwise distinct.

Finally, every product in `VV` has degree at most `4e+2`, while the official
active row set has `6e+3` distinct points. Evaluation there is injective,
so its quadratic locator matrix has rank `dim(VV)`. QED.
