# Proof - PMA source-to-paving bridge

The sets `R_0`, `D`, and `T` are pairwise disjoint. Hence `L_R` is nonzero on
`T`, as are the PMA target values `U_D(x)=c_iL_D(x)`. If `r>d`, a polynomial
`W` of degree at most `d` vanishing on `R_0` is zero. It has no petal
agreements, while the required number `d+1+sigma-r` is at least `d+1>0`
because maximality gives `r<=sigma`. Thus the list is empty.

Assume `r<=d`. The background zeros give a unique factorization

```text
W=L_R Q,       deg Q <= d-r=kappa-1.
```

Division by the nonzero values of `L_R` on `T` preserves every petal
agreement. Moreover

```text
d+1+sigma-r=kappa+sigma,
```

which proves the source dictionary in the statement.

For a listed `Q`, let `A_Q` be its agreement set in `T`. Every
`kappa`-subset of `A_Q` determines `Q` uniquely by interpolation. Therefore
no `kappa`-subset of `T` can be owned by two distinct listed polynomials.
Counting pairs `(Q,I)` with `I subset A_Q` and `|I|=kappa` proves

```text
sum_Q binom(|A_Q|,kappa) <= binom(L,kappa).
```

Since `|A_Q|>=kappa+sigma`, division by the common lower charge gives
`(PMA-PB)`.

It remains to check the upstream chart interface. Choose `xi notin T` and a
parity-check matrix `H^+` for `RS[T union {xi},kappa]`, with weighted
Vandermonde columns `h_x`. Extend `V` by zero at `xi`, and for each `Q` put

```text
c_Q(x)=V(x)-Q(x)  for x in T,
c_Q(xi)=0.
```

The full evaluation vector of `Q` lies in `ker H^+`, so

```text
H^+ c_Q = H^+(V,0) + Q(xi) h_xi.
```

Thus `y_0=H^+(V,0)`, `y_1=h_xi`, and `gamma_Q=Q(xi)` give the affine
syndrome pencil required by PR `#764`. Distinct `Q` give distinct `c_Q`, so
same-slope multiplicity is retained. Also

```text
wt(c_Q)=L-|A_Q| <= L-kappa-sigma=t<R_chart.
```

The support of `c_Q` is contained in `T`. If `h_xi` lay in the span of its
support columns, at most `t+1<=R_chart` columns of the MDS parity matrix would
be dependent, impossible. Hence the transversality premise holds.

Finally, the augmented bases containing `xi` are in bijection with
`kappa`-subsets of `T`. A basis contained in the zero set of `c_Q` is exactly
an interpolation owner counted above, and has at most one owner. Restricting
the upstream basis charge to these pinned bases proves the sharper numerator
`binom(L,kappa)` and completes the proof.
