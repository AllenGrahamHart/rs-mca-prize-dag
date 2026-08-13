# Proof

## The Gram-rank lemma

Let `B` be the `L` by `n` incidence matrix of the sets and let `1` denote
the all-ones column of length `L`.  Put

```text
H=BB^T-c*1*1^T.
```

Every row of `B` has sum `A`, so

```text
1=(1/A)B*1_n.
```

Thus the image of both `BB^T` and `1*1^T` lies in the column space of `B`,
and

```text
rank(H)<=rank(B)<=n.                                (1)
```

Write `delta_ij=c-|S_i intersect S_j|`.  Then `0<=delta_ij<=c` is an
integer,

```text
tr(H)=L(A-c),
tr(H^2)=L(A-c)^2+2 sum_(i<j) delta_ij^2.            (2)
```

If `s_x` is the incidence multiplicity of coordinate `x`, Cauchy--Schwarz
gives

```text
2 sum_(i<j)|S_i intersect S_j|
 =sum_x s_x^2-LA
 >=L^2 A^2/n-LA.
```

Consequently, with `Delta=sum_(i<j)delta_ij`,

```text
2 Delta <= L*(L*g/n+(A-c)).                         (3)
```

Since `delta_ij^2<=c delta_ij`, equations `(2)--(3)` imply

```text
tr(H^2)<=L*((A-c)^2+c(A-c)+cL*g/n).
```

For a real symmetric matrix,

```text
rank(H)>=tr(H)^2/tr(H^2).
```

Combine this with `(1)` and cancel `L`:

```text
L*((A-c)^2-cg) <= n*A*(A-c).
```

The assumed positivity of `G` proves `(GR1)`.

## The MCA compiler

For a transformed explanation `a`, let `h_a` be its outside-agreement
deficit.  The sparse-direction profile proves

```text
1<=h_a<=e,
one deficit-h explanation owns at most floor(e/h) slopes.
```

Let `u=floor(e/2)`.  Explanations with `h_a<=u` own at most `e` slopes;
all explanations with `h_a>u` own at most one.  If `N_u` is the number in
the first class and `N_e` the total number of distinct explanations, then

```text
|Z|<=e*N_u+(N_e-N_u)=(e-1)N_u+N_e.                 (4)
```

After puncturing `E`, the first class is an ordinary RS list at agreement
`m-u`.  Pairwise agreement is at most `K-1`, so the ordinary Johnson
incidence count gives `N_u<=J_u`.

For the full list, choose an exact `A=m-e` subset of the outside agreement
set of each explanation.  Distinct degree-`<K` explanations give subsets
with pairwise intersection at most `c=K-1`.  The Gram-rank lemma gives
`N_e<=Q_e`.  Substitute these two caps in `(4)` to prove `(GR2)`.

The verifier scans the complete post-Johnson strip with exact integers,
checks both endpoint and adjacent records, and independently tests the
Gram inequality and rank placement on finite set systems.
