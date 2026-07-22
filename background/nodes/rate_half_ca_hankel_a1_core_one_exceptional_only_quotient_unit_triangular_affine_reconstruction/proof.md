# Proof

The reciprocal definitions give `f_0=E q_bar` and
`l_0=Delta_inf`. The Bezout normalization proves both
`gcd(P_cl,E q_bar)=1` and `gcd(Delta_inf,E q_bar)=1`, hence `(QTA2)`.

Write the interpolation normal form coefficientwise as

```text
w_k=w_k^0+P_cl(t)(t a_k+b_k).                       (1)
```

For `k<N_sq`, the coefficient of `Y^k` in

```text
L W_vee-FS=E Y^N_sq                                 (2)
```

is zero. Isolate its terms containing the not-yet-known `w_k,s_k`. The
result is

```text
C_k^0+l_0P_cl(t a_k+b_k)-f_0s_k=0.                  (3)
```

All terms in `C_k^0` involve only fixed data or earlier reconstructed
coefficients. Reducing `(3)` modulo `f_0` and using `(QTA2)` gives `(QTA4)`.
Because `deg f_0=e>2` on the official face, at most one affine polynomial
represents that residue class. Such a polynomial exists exactly when the
canonical remainder `rho_k` has degree at most one; its coefficients are
the unique `a_k,b_k`. Exact division of `(3)` by `f_0` then gives `(QTA6)`.

Induction for `k=0,...,r-1` reconstructs all coefficients of `A_W,B_W` and
the corresponding coefficients of `S`. With `W_vee` fixed, equation `(2)`
has at most one quotient `S` because `F` is nonzero. Therefore exact
polynomial division, followed by the inherited degree-box checks, is
necessary and sufficient for the remaining unit identity. This is `(QTA7)`.
QED.
