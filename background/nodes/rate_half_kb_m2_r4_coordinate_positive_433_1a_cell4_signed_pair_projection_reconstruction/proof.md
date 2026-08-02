# Proof

In the compact plane-kernel model, let `P(w1)` be the reduced signed product
equation and `S(w1)` the reduced signed square equation.  Their degrees in
`w1` are two and four.  FLINT computes `Res_w1(P,S)`, pseudo-reduces it by the
plane equation, removes its univariate `t` content, and reconstructs the exact
factorization `(KBC4SP-1)`.  The two small factors are precisely the forbidden
source labels `w0=-1` and `w0=t^2`; hence any guarded solution lies on `F=0`.

Three coefficient-ring pseudo-division steps give

```text
R(w1)=A(w0,b,t) w1+B(w0,b,t).
```

The computation verifies the exact identity

```text
Res(P,R)=lc(P)^3 Res(P,S).
```

Nine plane pseudo-reductions applied equally to `A` and `B` preserve the
linear equation on the plane wherever the plane leading coefficient is
nonzero.  Exact factorization gives the common scale `(KBC4SP-2)` and the
common polynomial factor `w0+1`.  The exceptional-scale child and original
source guards make every canceled factor invertible on this chart.  Exact
division then gives a common scalar times `L` as the linear coefficient and
the same scalar times `tM` as the constant coefficient.  FLINT proves `L` and
`M` irreducible with the printed shapes, so the primitive coefficients are
coprime.  Equation `(KBC4SP-3)` follows.  If `L!=0`, division reconstructs
`w1`; if `L=0`, the nonzero guard `t` forces `M=0`.  QED.
