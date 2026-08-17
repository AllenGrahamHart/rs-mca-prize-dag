# Fixed-union adjacent-support circuit coupling

- **status:** PROVED
- **correction dimension:** `10`

Let `V<=P_K` have dimension ten and empty common zero set. Let `D` be a
fixed set of `u` domain points and let a fixed subspace `W<=V` of dimension
`g` vanish on `D`. Fix `2<=d<=g-1` and put

```text
R=K-u-g >= 0,                    N=m-u >= R+d-1.
```

Let `C_(e,i)` count support-`e` circuit supports containing exactly `i`
points of `D`. For `0<=i<=d-2`,

```text
(d+1-i) C_(d+1,i) + (N-R-d+1+i) C_(d,i)
 <= C(u,i) R C(N,d-i),                              (FAS1)

C_(d,i) <= floor(C(u,i) R C(N,d-1-i)/(d-i)).        (FAS2)
```

For nonnegative integer weights `w_d,w_(d+1)`, let `L_i` be the right side
of `(FAS2)`, `A_i=C(u,i)R C(N,d-i)`, and

```text
lambda_i=(d+1-i)w_d-(N-R-d+1+i)w_(d+1),
J_i=floor((w_(d+1)A_i+max(lambda_i,0)L_i)/(d+1-i)).
```

Then

```text
w_d C_d+w_(d+1) C_(d+1) <= sum_(i=0)^(d-2) J_i
 + w_d (C(u,d-1)R+C(u,d))
 + w_(d+1) (floor(C(u,d-1)RN/2)+C(u,d)R+C(u,d+1)). (FAS3)
```

Thus one fixed union of dimension `g` simultaneously supplies every
adjacent pair through supports `(g-1,g)`. Bounds for disjoint adjacent pairs
may be charged together.

## Falsifier

A fixed union satisfying the hypotheses whose exact adjacent circuit strata
violate `(FAS1)`, or an arithmetic specialization that violates `(FAS3)`.
