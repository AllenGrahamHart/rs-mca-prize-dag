# XR mismatch accumulated-locator flag normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependencies:**
  `xr_tangent_mismatch_full_external_zero_canonicalization`,
  `xr_mismatch_chart_nongeneric_joint_support_equivalence`,
  `xr_mismatch_nongeneric_invariant_excess_descent`

Fix one selected slope and one compatible branch of the canonical nongeneric
mismatch descent. Work on the original evaluation domain `D_0` with original
dimension `K`, agreement `A=K+h`, and received pair `(u_0,u_1)`. At stage
`j`, let

```text
D_(j+1)=T_j subset D_j,
Z_j subset D_j\T_j,       d_j=|Z_j|,
P_j=Lambda_(Z_j),
Omega_j=disjoint_union_(r<j) Z_r,
L_j=Lambda_(Omega_j)=product_(r<j)P_r,
delta_j=|Omega_j|=sum_(r<j)d_r,
K_j=K-delta_j,            A_j=A-delta_j.             (AL1)
```

Here `T_j` is the discrepancy support of the current normalized explaining
pair, `Z_j` is the full external zero set of the selected mismatch, and the
nongeneric router supplies polynomials `g_i^j` of degree below
`K_j-d_j`. Define lifted global codeword pairs by

```text
C_i^0=c_i,
C_i^(j+1)=C_i^j+L_j P_j g_i^j.                       (AL2)
```

Then every `C_i^j` has degree below `K`. Moreover `C^j` jointly explains
the original received pair on at least `A` coordinates. More precisely, if
`R_j subset T_j` is an exact `(A_j-d_j)`-point local agreement support for
`g^j`, then

```text
Y_(j+1)=Omega_(j+1) disjoint_union R_j,
|Y_(j+1)|=A                                             (AL3)
```

is a global joint-explanation support for `C^(j+1)`.

Let `p_z` be the original selected witness polynomial and define the local
mismatch `q_z^j` by

```text
p_z-(C_0^j+z C_1^j)=L_j q_z^j.                       (AL4)
```

The transition has the exact recursion

```text
q_z^j=P_j(g_z^j),
q_z^(j+1)=g_z^j-(g_0^j+z g_1^j),
p_z-(C_0^(j+1)+z C_1^(j+1))=L_(j+1)q_z^(j+1).        (AL5)
```

Thus the complete locator history is one squarefree product on pairwise
disjoint discrepancy layers. Every descendant difference has the prefix
divisibility

```text
L_(s+1) divides C_i^r-C_i^s       (0<=s<r),           (AL6)
```

and every live stage satisfies

```text
delta_j<=K-1.                                         (AL7)
```

Finally, if two distinct lifted explanations extending a common prefix
`Omega_s` use exact global supports `Y,Y'` containing that prefix, then

```text
|(Y\Omega_s) intersect (Y'\Omega_s)|<=K_s-1.         (AL8)
```

Consequently a branch-width argument may work with bounded-degree locator
flags and residual low-core supports; it must not enumerate arbitrary
sequences of overlapping zero sets. This theorem does not bound the number
of flags, lifted explanations, generic terminal charts, or slopes.
