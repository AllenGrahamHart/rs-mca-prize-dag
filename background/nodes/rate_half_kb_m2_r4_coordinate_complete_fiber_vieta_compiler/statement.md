# KoalaBear m2 r4 coordinate complete-fiber Vieta compiler

- **status:** PROVED
- **scope:** every actual coordinate-order-two component in the residual
  `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_v4_outer_recurrence_router`,
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` and
  `rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler`
- **consumer:** `rate_half_band_closure`

Use the proved coordinates `tau(T)=-T`, `b(X)=-X`, and `W=X^2`.  Put

```text
Omega=K disjoint_union {eta} disjoint_union L^c,   |Omega|=12.
```

For every `kappa in Omega`, choose one source point `x_kappa` above it.
If its component star is `{a_kappa,b_kappa}`, deck transport gives the
other star `{-a_kappa,-b_kappa}`.  Define

```text
p_kappa=a_kappa b_kappa,
q_kappa=x_kappa(a_kappa+b_kappa).                 (KBCV-1)
```

These records do not depend on the choice of source point or edge order.
In an affine chart containing all twelve labels, every positive-parity
packet has a nonzero coefficient vector in the kernel of the `24 x 8`
system

```text
A_0(kappa)-p_kappa A_2(kappa)=0,
kappa B_1(kappa)+q_kappa A_2(kappa)=0             (KBCV-2+)
```

and `A_2(kappa)!=0` at all twelve rows.  Every negative-parity packet has
a nonzero coefficient vector in the kernel of the `24 x 7` system

```text
B_0(kappa)-p_kappa B_2(kappa)=0,
A_1(kappa)+q_kappa B_2(kappa)=0                  (KBCV-2-)
```

and `x_kappa B_2(kappa)!=0` at all twelve rows.

The product halves are square-root-free.  In homogeneous coordinates
`kappa=[u:v]`, define

```text
M_+(kappa)=[-p v^2,-p uv,-p u^2, v^2,uv,u^2],
M_-(kappa)=[-p v,-p u, v,u].                     (KBCV-3)
```

Then every actual packet satisfies

```text
rank M_+(Omega)<=5,       rank M_-(Omega)<=3.     (KBCV-4)
```

In particular, positive parity has the six-fiber separator

```text
det M_+(K union {eta})=0.                         (KBCV-5)
```

Negative parity has a further exact combinatorial consequence.  Its product
ratio `B_0/B_2` cannot be constant: otherwise every star incident to a fixed
label would have the same unique partner, forcing one edge to have weight at
least four and defect at least six.  Hence it is a nonconstant Mobius map and
is injective.  The twelve values `p_kappa` are therefore pairwise distinct.
In particular, among the five `K` edge orbits every antipodal loop type occurs
at most once and each cross-pair supports at most its two signed product
types.  The 14 pair-multiplicity skeletons allowed by the two degree profiles
reduce to exactly seven:

```text
(4,4,2): (0,1,0;2,2,0), (1,1,0;1,1,1),
           (1,1,1;2,0,0),
(4,3,3): (0,0,0;2,2,1), (1,0,0;1,1,2),
           (1,0,1;2,0,1), (1,1,1;1,1,0).         (KBCV-6)
```

Here `(l_0,l_1,l_2;m_01,m_02,m_12)` records loop and cross-pair
multiplicities, after fixing the exceptional-degree pair and quotienting by
the swap of the two equal-degree pairs.

The complete systems realize all 24 prescribed source stars directly.
Consequently, once the exact source-facet and complete-source conditions
are retained, the forced colored support and companion quotient identity
are consequences rather than separate discovery equations.  They remain
valuable independent audit checks.

For the exact `F_29` profile-only witness, the five-row `K` product matrix
has rank five, while `M_+(K union {eta})` has determinant `10`.  Thus the
new six-fiber gate rejects that witness before any resultant calculation.

The separator alone is not universal even on exact abstract packets.  On
the defect-zero fixture from the source-facet theorem, assign the six signed
pair representatives

```text
(A,B,C,D,E,F)=(1,4,6,9,7,5) in F_29.
```

Its `K+eta` matrix has rank five with kernel
`(28,15,5;2,5,1)` and the quadratic denominator has values
`(19,18,23,19,8,2)`, all nonzero.  The complete twelve-row product matrix
has rank six and rejects it.  An exact census of all `7P6=5040` assignments
of six distinct signed square-pairs finds 140 separator survivors and zero
complete-product survivors.  This is fixed-fixture route evidence, not a
universal complete-product exclusion.

This compiler proves that `(KBCV-5)` alone cannot be the universal abstract
packet deletion.  It does not prove the complete positive gate universally
nonzero or exclude the seven negative skeletons in `(KBCV-6)`.
It deletes no coordinate orientation, owner, payment, row, or Prize result.

## Falsifier

An actual coordinate packet whose twelve deck-paired edge records are not
well defined by `(KBCV-1)`, fail the relevant complete Vieta system, violate
`(KBCV-4)--(KBCV-5)`, or whose complete system does not realize its 24 stars.
