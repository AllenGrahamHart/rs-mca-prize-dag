# Proof - L1 marked constant-shift extremal kernel normal form

As in the multistrip theorem, multiplication by `J` restores every full
locator congruence and gives

```text
gcd(F',W')=J,       deg gcd(F',W')=v.                 (1)
```

The strip bound gives unique `P`-adic decompositions through block `m`.
Every coefficient vector lies in the kernel `E` of `(EK2)`. The common-factor
argument from `l1_marked_constant_shift_multistrip_exclusion` applies without
using the number of rows: rank at least `2m+1` would make `E` at most one-
dimensional and force a common divisor of degree

```text
d+v-m ell>v.
```

Therefore `rank(EK2)<=2m` and `dim E>=2`.

## 1. Exact rank

Suppose `dim E>=3`. Represent each kernel vector by a pair `(A,B)` of
degree-at-most-`m` polynomials. For any two pairs, their cross product has
degree at most `2m` and vanishes at the `2m` labels. Therefore

```text
A_jB_k-A_kB_j=lambda_(j,k)Q.                          (2)
```

If every scalar in `(2)` were zero, all kernel pairs would be polynomial
multiples of one primitive pair. A multiplier space of dimension at least
three forces the primitive pair to have maximum degree at most `m-2`.
Expanding the coefficient vectors in a kernel basis would then factor both
`F'` and `W'` by a polynomial of degree at least

```text
d+v-(m-2)ell>v,
```

contradicting `(1)`.

Otherwise choose `q_0,q_1` with determinant `kappa Q`, `kappa!=0`. For any
third kernel pair `q`, both determinants `det(q_0,q)` and `det(q_1,q)` are
scalar multiples of `Q`. Cramer's rule over `K(Z)` then expresses `q` as a
constant `K`-linear combination of `q_0,q_1`. Thus no third independent pair
exists, again contradicting `dim E>=3`.

Hence `dim E=2` and `(EK2)` has rank `2m`.

## 2. Determinant and coefficient reconstruction

Let `q_0,q_1` be any kernel basis. Their determinant cannot vanish. If it
did, the two pairs would be polynomial multiples of one primitive pair of
maximum degree at most `m-1`; all coefficient vectors would again give a
common factor of degree greater than `v`. The determinant has degree at most
`2m` and vanishes at all `2m` distinct labels, so it is exactly the nonzero
scalar multiple `(EK3)`.

Every coefficient vector of the `P`-adic blocks has a unique expansion in
the basis `q_0,q_1`. Collecting the two scalar coordinates over coefficient
positions `0<=r<ell` gives unique polynomials `H_0,H_1` of degree below
`ell`, proving `(EK4)`.

They are linearly independent. Otherwise all coefficient vectors would lie
on one kernel line, and `F',W'` would have a common factor of degree
`d+v-m ell>v`. If `G=gcd(H_0,H_1)`, equation `(EK4)` makes `G` a common
divisor of `F',W'`; equation `(1)` therefore gives `G|J`. Multiplying `(EK4)`
by the adjugate of its polynomial matrix and using `(EK3)` proves `(EK5)`.

## 3. Sharp family

For `(EK6)`, `deg F=m ell+c=d` and `deg W=m ell`. If `a_i` is a root of
`U`, then `P-a_i` divides `W`, so take `c_i=0`. If `a_i` is a root of `V`,
then modulo `P-a_i` one has

```text
F=1,       W=U(a_i),
```

so take `c_i=U(a_i)`.

Finally, view the resultant `Res_X(F,W)` as a polynomial in `lambda`. At
`lambda=0`, `F=1`, so the resultant is `1`. It is therefore nonzero over the
rational function field in `lambda`, proving `gcd(F,W)=1`. This establishes
the claimed saturated examples and the sharpness of the `2m+1` threshold.
