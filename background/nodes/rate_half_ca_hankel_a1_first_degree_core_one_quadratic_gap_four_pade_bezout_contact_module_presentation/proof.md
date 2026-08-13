# Proof

Work over the completed local DVR at `tau`; scaling by the unit leading
coefficient makes `Q` monic without changing any Smith invariant. The
global kernel relation says

```text
Phi(X^iQ)=0,       0<=i<d.                         (1)
```

A direct divided-difference calculation gives

```text
[Q(X)K_Q(Y,Z)-K_Q(X,Z)Q(Y)]/(X-Y)
 =K_Q(X,Z)K_Q(Y,Z)-Q(Z)R(X,Y,Z),                  (2)
```

where `deg_Z R<d`. Apply `Phi` in the `Z` variable. Equation `(1)` kills
the last term, while the definition of `P_F` turns the left side into the
Bezoutian. Hence

```text
Bez_(Q,P_F)(X,Y)=Phi(K_Q(X,Z)K_Q(Y,Z)).            (3)
```

The coefficient vector of `K_Q(X,Z)` in `Z` is `T_Q^T` times the
coefficient vector in `X`. Therefore `(3)` is exactly the Gram identity

```text
Bez_(Q,P_F)=T_Q H T_Q^T.                          (4)
```

The matrix `T_Q` is anti-triangular with every anti-diagonal entry equal
to `lc_X(Q)`. Thus

```text
det T_Q=+-lc_X(Q)^d,                              (5)
```

a unit at `tau`. This proves the Smith equivalence in `(BCM3)`.

The full moment matrix acts on polynomials of degree at most `d` and has
the permanent kernel vector `Q`. Replacing the last monomial by `Q` is a
unimodular basis change because its leading coefficient is a unit. In
that basis the matrix is `H direct_sum 0`, so `H` is precisely a regular
quotient block.

For completeness, consider the standard Sylvester presentation of the
pair `(Q,P_F)`. Since `Q` is monic, Euclidean elimination of all powers
`X^j` with `j>=d` uses only unit row and column operations. The resulting
nonidentity block is both:

```text
the Bezout matrix in the divided-difference basis,
the multiplication-by-P_F presentation on A_tau=O_tau[X]/(Q).
```

The Bezout and multiplication blocks are two unit-equivalent forms of
this remaining block. It follows that their cokernels are isomorphic and
equal to `A_tau/P_FA_tau`. Combined with `(4)`, this proves `(BCM4)` and
the full contact-module presentation. QED.
