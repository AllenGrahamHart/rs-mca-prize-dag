# F3 h=3 shifted-product splitting reduction

Status: PROVED EXACT REDUCTION; COMPLETE-SPLITTING COUNT OPEN.

## Anchored level polynomial

Let `{P,Q}` be a nonzero-trace h=3 accident, modulo common dilation by
`H`, and orient its two sides.  Choose an anchor `q_0 in Q` and put

```text
r_i=q_0/p_i in H,                 i=1,2,3,
F_r(T)=product_i (1-T r_i).
```

The two monic cubics with root sets `P` and `Q` have the same quadratic and
linear coefficients.  Their difference is constant.  Consequently
`product_i(q-p_i)` is independent of `q in Q`, and division by the common
nonzero factor `-product_i p_i` gives

```text
F_r(q/q_0)=F_r(1),                q in Q.
```

Writing `Q/q_0={1,lambda,mu}`, the three distinct elements
`1,lambda,mu in H` are exactly the roots of `F_r(T)-F_r(1)`.  If

```text
e_j=e_j(r_1,r_2,r_3),
```

then

```text
F_r(T)-F_r(1)=-(T-1) G_r(T),
G_r(T)=e_3 T^2+(e_3-e_2)T+(e_1-e_2+e_3).
```

Thus one oriented anchored accident is equivalent to an unordered distinct
triple `{r_1,r_2,r_3}` for which `G_r` has two distinct roots in
`H\{1}`, subject only to the reconstructed sides being disjoint and having
nonzero common trace.  Conversely, such a split quadratic reconstructs

```text
P={r_1^(-1),r_2^(-1),r_3^(-1)},
Q={1,lambda,mu}.
```

Since `F_r` takes one value on all of `Q`, the monic cubic with roots `Q`
differs from the monic cubic with roots `P` by a constant.  Hence the
reconstruction has equal `e_1,e_2` and is inverse to anchoring.

## Exact multiplicity

Common dilation acts freely on nonzero-trace accidents and cannot swap their
two sides.  Every unordered accident orbit therefore has:

```text
2 orientations * 3 anchors * 6 orderings of r = 36
```

ordered split triples.  If `S_nz` denotes the ordered `r` count above, then

```text
S_nz=36 A_3^nz.
```

The exact remaining nonzero target is equivalently

```text
S_nz <= 36*4096*n = 147456*n.
```

This is the same open child as the normalized-cell L2 and parabola-excess
forms, not an additional premise.

## Shifted-energy envelope

Comparing constant terms in

```text
F_r(T)-F_r(1)=-e_3(T-1)(T-lambda)(T-mu)
```

gives

```text
product_i(1-r_i)=1-e_3 lambda mu in 1-H.
```

Let `A=(1-H)\{0}` and let

```text
N_3to1(A)=#{(a_1,a_2,a_3,a_4) in A^4: a_1 a_2 a_3=a_4}.
```

Every ordered split triple injects into this relation, so

```text
S_nz <= N_3to1(A).
```

Moreover, with `r_AA(t)` and `r_A/A(t)` denoting product and quotient
representation functions,

```text
N_3to1(A)=sum_t r_AA(t) r_A/A(t)
          <= E_x(A)
```

by Cauchy--Schwarz, because both squared norms equal the multiplicative
energy of `A`.

This proves a genuine charging lemma

```text
A_3^nz <= E_x((1-H)\{0})/36.
```

For the actual floor, stop one line earlier.  The exact three-to-one
quantity already gives

```text
A_3^nz <= N_3to1((1-H)\{0})/36,
```

and h=3 closes if it is below the finite threshold in
`F3_H3_THREE_TO_ONE_DIRECT_FLOOR.md`.  This is strictly weaker than an energy
bound because the Cauchy--Schwarz step forgets multiplicative Fourier phases.

It does not close the official target: the published shifted-subgroup energy
bound is of order `n^2 log n`, while the required split count is linear in
`n`.  The complete-splitting condition on `G_r`, which the energy envelope
forgets, is exactly the remaining source of the needed factor.

## Exact filter inside shifted energy

The condition forgotten by the envelope can be printed explicitly.  Put

```text
a_i=1-r_i in A,                    a_4=a_1 a_2 a_3,
h=1-a_4 in H,
K=h/(r_1 r_2 r_3),
L=(e_2(r)-e_3(r))/e_3(r).
```

On the product-relation locus, `K in H`.  The residual quadratic is

```text
G_r(T)=e_3(r) (T^2-LT+K).
```

It splits at the required subgroup pair exactly when

```text
(K,L)=(lambda*mu,lambda+mu)
```

for distinct `lambda,mu in H\{1}`.  In ratio form this implies

```text
J=L^2/K=(lambda+mu)^2/(lambda*mu),
J=(a_1 a_2 a_3-a_1-a_2-a_3+2)^2
  / ((a_1-1)(a_2-1)(a_3-1)(a_1 a_2 a_3-1)).
```

Conversely the `J` condition reconstructs the pair after retaining the
square-class compatibility `K*(lambda/mu) in H^2` and the sign of `L`.
Thus the precise next theorem is equidistribution of this explicit `J` map on
the shifted-energy relation.  A result that counts all shifted-energy tuples
has deliberately discarded the factor still needed by the prize bound.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_shifted_product_splitting_reduction.py
```

Expected digest:

```text
H3_SHIFTED_PRODUCT_SPLITTING_REDUCTION_PASS rows=3
```
