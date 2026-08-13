# Proof

For distinct points `z_1,...,z_N` over a field, the moment map through
degree `2d` is the `(2d+1) x N` Vandermonde matrix. In `(TSF2)`, adjoining
`A_12` to `U_0` gives 31 points and hence a four-dimensional nullspace;
adjoining `A_11` gives 30 points and a three-dimensional nullspace.

Every set of 27 columns is independent. Therefore no coordinate functional
vanishes identically on either nullspace. Over `F_101`, the union of the at
most 31 coordinate hyperplanes has size strictly below the whole nullspace,
so each nullspace contains a vector with every coordinate nonzero.

Split such a vector `c` between `U_0` and `A_s`. Put

```text
omega_x=c_x             (x in U_0),
theta_a=-c_a            (a in A_s).                (1)
```

The nullspace equations say exactly

```text
sum_(x in U_0)omega_x x^j
 =sum_(a in A_s)theta_a a^j,       0<=j<=26.       (2)
```

All weights are nonzero. The Hankel matrix formed from `(2)` is therefore

```text
V(A_s) diag(theta) V(A_s)^T,                       (3)
```

and has rank `s`, because `s<=14` and the weights and Vandermonde minors
are nonzero. Its kernel consists of

```text
P_A F[X]_(<=13-s),       P_A=product_(a in A_s)(X-a). (4)
```

For `s=12` this has full corank two and regular corank one; for `s=11` it
has full corank three and regular corank two. Since `30` is in both `A_s`
but not `U_0`, `(TSF1)` fails. The multipliers in `(TSF4)` have the allowed
degrees one and two. Because `P_A` is squarefree and `90` lies outside both
sets, `30` is an exact double root of each `Q`. This proves the fence. QED.
