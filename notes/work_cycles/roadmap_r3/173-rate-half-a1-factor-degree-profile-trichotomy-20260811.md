# Cycle 173: rate-half `A=1` factor-degree profile trichotomy (2026-08-11)

The extremal paired split biform has no nonconstant domain content. A
content root would lie in `U_0` because one clean parameter fiber splits
there, but every `U_0` specialization is a nonzero dual-MDS source row.
Consequently the factor domain degrees sum to the exact global degree.

Combining this identity with factorwise incidence saturation and
`2N-3M=-1` removes all factor-degree slack. Every factor obeys

```text
n_j=ceil((3p-3+d_A)m_j/(3e)),
```

and its full degree multiset has exactly one of three profiles: one large
odd factor; two large odd plus one small odd; or one huge even plus one
small odd. Every remaining factor is ordinary even.

```text
result:                  PROVED content-free exact degree trichotomy
DAG delta:               +1 PROVED leaf, 2 req edges
critical status delta:   none
compute:                 25,504 small partitions; no Modal spend
new assumptions:         none
```

This narrows the surviving paired-biform obstruction from an arbitrary
macroscopic factorization to three exact degree profiles. It does not yet
exclude any profile; the next attack must use the Hankel/source equations
inside a macroscopic factor rather than repeat the incidence count.
