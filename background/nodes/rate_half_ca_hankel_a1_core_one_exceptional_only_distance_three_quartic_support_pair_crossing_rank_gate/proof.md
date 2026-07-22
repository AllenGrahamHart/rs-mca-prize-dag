# Proof

Fix `l` and let `P_l=Y_l` be the quartic supplied by `(QLK5)`. At the two
roots of a pair `D_k`, `k!=l`, equation `(QLK3)` gives

```text
P_l(a_k)=lambda_k^3 f_lk(a_k),
P_l(b_k)=lambda_k^3 f_lk(b_k),                       (1)

f_lk(x)=r_k(x)^3D_l(x)^2/[C(x)(xi_l-xi_k)^2].       (2)
```

Every displayed factor is nonzero. Eliminate the shared nonzero multiplier
`lambda_k^3`:

```text
f_lk(b_k)P_l(a_k)-f_lk(a_k)P_l(b_k)=0.              (3)
```

The constants `(xi_l-xi_k)^(-2)` and
`(xi_kI'(xi_k))^(-3)` are common to the two roots and may be removed. Put
`A_k=A/D_k`. The remaining root weight is

```text
B(x)^3A_k(x)^3D_l(x)^2/C(x).                         (4)
```

The smooth subgroup derivative identity and
`A'(x)=D_k'(x)A_k(x)` at a root of `D_k` turn `(4)` into

```text
G_l(x)/[N D_k'(x)^3].                                (5)
```

Since `D_k'(b_k)=-D_k'(a_k)`, substitution of `(5)` into `(3)` gives

```text
G_l(b_k)P_l(a_k)+G_l(a_k)P_l(b_k)=0.                (6)
```

Expanding `P_l` proves `(QPC2)--(QPC4)`. Equation `(1)` and nonvanishing of
all factors prove `(QPC5)`. Rank five leaves only the zero polynomial and is
therefore impossible. If every kernel polynomial vanishes at one fixed
root of `A/D_l`, `(QPC5)` is likewise impossible. QED.

For the final route fence, replace the actual smooth weight in `(QPC1)` by
an arbitrary nonzero function `H` on the exceptional roots and put
`G_l=H D_l^2`. If `H(b_k)=-H(a_k)`, substitution of `P_l=D_l^2` into the
`k`th crossing gives

```text
D_l(a_k)^2D_l(b_k)^2[H(b_k)+H(a_k)]=0.
```

Thus every crossing vanishes. This proves the asserted abstract antiweight
escape and shows why the smooth-domain formula for `H` is load-bearing.
