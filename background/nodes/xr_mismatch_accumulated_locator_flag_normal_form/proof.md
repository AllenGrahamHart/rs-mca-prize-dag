# Proof

Induct on the branch depth. At stage zero, `Omega_0` is empty, `L_0=1`,
and `(AL4)` is the definition of the original mismatch.

The domains are nested because the next chart is formed on the old
discrepancy support `T_j`. Since `Z_j` lies in `D_j\T_j`, while every earlier
zero layer lies outside `D_j`, the sets `Z_j` are pairwise disjoint and
`L_(j+1)=L_jP_j` is their squarefree locator. This proves `(AL1)`.

The full-zero theorem gives

```text
q_z^j=P_j g_z^j,       deg g_z^j<K_j-d_j.
```

Nongenericity supplies a pair `(g_0^j,g_1^j)` with the same degree bound and
an exact support `R_j subset T_j` of size `A_j-d_j` on which

```text
(u_i-C_i^j)/L_j=P_jg_i^j.                            (1)
```

All divisions are valid on `D_j`, since the roots of `L_j` were removed in
earlier discrepancy layers.

Define `C_i^(j+1)` by `(AL2)`. Its increment has degree below

```text
delta_j+d_j+(K_j-d_j)=K,
```

so it remains an original degree-below-`K` codeword. On every old root in
`Omega_j`, the increment vanishes and the induction hypothesis says that
`C^j` agrees with the received pair. On `Z_j`, both the current normalized
error and `P_j` vanish. On `R_j`, equation `(1)` says exactly that the
increment changes `C^j` into the received pair. Hence `C^(j+1)` agrees on

```text
Omega_j disjoint_union Z_j disjoint_union R_j.
```

Its size is

```text
delta_j+d_j+(A_j-d_j)=delta_j+A_j=A,
```

proving `(AL3)` and the global explanation claim.

Subtract `(AL2)` from `(AL4)` and use `q_z^j=P_jg_z^j`:

```text
p_z-(C_0^(j+1)+zC_1^(j+1))
 =L_jP_j(g_z^j-g_0^j-zg_1^j)
 =L_(j+1)q_z^(j+1).
```

This proves `(AL5)` and closes the induction. It also gives
`deg q_z^(j+1)<K_j-d_j=K_(j+1)`.

For `r>s`, telescope the lifted-pair increments:

```text
C_i^r-C_i^s=sum_(j=s)^(r-1)L_(j+1)g_i^j.
```

Every locator in this sum is divisible by `L_(s+1)`, proving `(AL6)`. A
live stage has `K_j>=1`; since `K_j=K-delta_j`, this is `(AL7)`.

Distinct original degree-below-`K` codeword pairs explaining the same
received pair have exact `A`-supports intersecting in at most `K-1`
coordinates. If both supports contain the common `delta_s`-point prefix,
delete it from their intersection to obtain

```text
|(Y\Omega_s) intersect (Y'\Omega_s)|
 <=K-1-delta_s=K_s-1.
```

This proves `(AL8)`. QED.
