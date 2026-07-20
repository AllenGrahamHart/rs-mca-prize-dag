# Proof

The smooth domain and exact support partition give

```text
X^N-1=(X-s)(X-x_0)A(X)B(X)C(X).                     (1)
```

Multiplicativity of the resultant in its first argument yields

```text
R_D=Q(z;s)Q(z;x_0)Res_X(A,Q)Res_X(B,Q)H.             (2)
```

At a root `a` in pair `i`, the pair-Lagrange normal form is

```text
Q(z;a)=c_a z L_i(z),
L_i(z)=product_(j!=i)(z-xi_j)/Delta_i.               (3)
```

Multiplying `(3)` over the two roots in every one of the `e` pairs gives

```text
Res_X(A,Q)=
 [product_(a in R_A)c_a]
 z^(2e) I(z)^(2e-2)/product_i Delta_i^2.             (4)
```

At a triple point, `Q(z;t)=Phi(z)A(t)` and
`Phi=I/Delta_0`. Hence

```text
Res_X(B,Q)=
 [product_(t in T)A(t)] I(z)^3/Delta_0^3.            (5)
```

Substituting `(4)--(5)` into `(2)` and using `r=2e+1` gives

```text
R_D=kappa_0 Q(z;s)Q(z;x_0)z^(2e)I(z)^rH(z).          (6)
```

Multiplication by `z` turns `z^(2e+1)` into `z^r`, proving `(SSN4)`.
All factors in `kappa_0` are nonzero by distinctness of the internal slopes,
nonvanishing of the internal fiber scalars, and disjointness of the
exceptional and triple supports.

The resultant-power equivalence says that the external design exists exactly
when its row gate holds and

```text
H=L P_Z^r                                             (7)
```

for the unique squarefree split degree-`3e` external locator. Substitute
`(7)` into `(SSN4)` to obtain `(SSN5)`. Conversely, cancellation of the
nonzero polynomial factors in `(SSN4)--(SSN5)` recovers `(7)`, so the
criterion is equivalent in both directions. The roots of `z`, `I`, and
`P_Z` are respectively the exceptional, internal, and external supported
slopes, proving `(SSN6)`. Rearranging `(SSN4)` proves `(SSN7)`. QED.
