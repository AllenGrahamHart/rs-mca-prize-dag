# Proof

The core-stratified Kronecker ledger gives one right minimal index `e`.
In the canonical singular block, the coefficients of the primitive minimal
vector are the `e+1` standard basis vectors. Strict equivalence preserves
their rank, so `q_0,...,q_e` are linearly independent and

```text
dim W_q=e+1.                                          (1)
```

The coefficients of `M(z)q(z)=0` are

```text
M_0q_0=0,
M_0q_k+M_1q_(k-1)=0       (1<=k<=e),
M_1q_e=0.                                             (2)
```

Put `B_(i,j)=q_i^TM_1q_j`. Symmetry and `(2)` give, for `i<e` and `j>0`,

```text
B_(i,j)=B_(i+1,j-1).                                  (3)
```

If `i+j<=e`, iterate to `B_(i+j,0)`, which vanishes by the first or last
equation in `(2)`. If `i+j>e`, iterate to `B_(e,i+j-e)=0`. Thus every
`B_(i,j)` is zero. Equations `(2)` then give
`q_i^TM_0q_j=0` as well, proving `(MSF3)`.

After contraction of the fixed core factor, each endpoint syndrome remains
a finite moment sum on `D_res`; contraction only rescales its source
weights. Hence

```text
(M_s)_(a,b)=sum_(x in D_res)omega_x^(s)x^(a+b)
```

for `0<=a,b<=d`. Expanding the pairings in `(MSF3)` gives

```text
q_i^TM_sq_j
 =sum_x omega_x^(s)Q_i(x)Q_j(x).                     (4)
```

Collecting `(4)` over all `i,j` proves `(MSF6)`. The same moment
representation gives

```text
M(U,V)=sum_(x in D_res)mu_x(U,V)nu_xnu_x^T.           (5)
```

Append one additional marked source column `nu_x*` with weight `tau` and
apply Cauchy--Binet to the resulting Vandermonde-diagonal-Vandermonde
factorization. Terms not using the marked column sum to `det M(U,V)`, which
is identically zero because the generic rank is `d`. A nonzero term using
the marked column chooses exactly `d` other, distinct source points. Its two
Vandermonde determinants multiply to their square, and its diagonal weight
is `tau product_(x in J)mu_x`. Therefore

```text
det(M+tau nu_x*nu_x*^T)=tau C_*(U,V),                 (6)
```

which proves `(MSF7)--(MSF8)`. If `x_*` is already a source column, choosing
both copies gives a repeated Vandermonde column and zero, so the same formula
and the exclusion `x_* notin J` remain exact.

Finally the marked-Hankel determinant theorem gives

```text
det(M+tau nu_x*nu_x*^T)=tau D_1Q(U,V;x_*)^2.          (7)
```

The quadratic double-root vertical divisor gives
`Q(U,V;x_*)=c g_*S_B^3`. Comparing `(6),(7)` proves `(MSF9)`. QED.
