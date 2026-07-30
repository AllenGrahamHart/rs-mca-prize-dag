# KoalaBear m2 universal source-row interpolation compiler

- **status:** PROVED
- **scope:** every actual residual `Q=6,s=6,u=2` source component, including
  stabilizer types `(m,r,delta)=(2,2,4),(2,4,2),(2,8,1)`
- **dependencies:** `rate_half_kb_m2_v4_outer_recurrence_router` and the
  branch-independent saturation clause of
  `rate_half_kb_q6_u2_complete_source_conic_exclusion`
- **consumer:** `rate_half_band_closure`

The node ID retains `m2_r4` for compatibility, but no step below uses an
order-two stabilizer or the value `r=4`.

Let `alpha_1,...,alpha_12` be the distinct source labels and let
`[q_i(X)]` be the projective nonzero binary quartic row divisors proposed
for an actual bidegree-`(2,4)` source component. Write

```text
q_i(X)=sum_(b=0)^4 q_(i,b) X^b.
```

Let `P` be any `9 x 12` parity-check matrix for evaluations of
degree-at-most-two polynomials at the twelve labels. Form the `45 x 12`
matrix

```text
N_(s,b),i=P_(s,i) q_(i,b).                          (KBSI-1)
```

There is a biform `H(T,X)` of bidegree at most `(2,4)` and twelve nonzero
scalars `c_i` satisfying

```text
H(alpha_i,X)=c_i q_i(X)                            (KBSI-2)
```

if and only if `N` has a kernel vector `c=(c_i)` with full support. For a
fixed `c`, the biform is unique. Thus failure of the full-support kernel
deletes a proposed source-star packet exactly.

Let `A(T)=product_i(T-alpha_i)` and let `B(X)` be the complete source form.
For an actual packet, complete-source saturation gives

```text
product_i q_i(X)=constant * B(X)^2,                (KBSI-3)
Res_T(A(T),H(T,X))=constant * B(X)^2.              (KBSI-4)
```

All identities count divisor multiplicity, including ramified coordinate
fibers. In the lifted diagonal coordinates `B(X)` is projectively
`A(X^2)`, so `(KBSI-4)` becomes

```text
Res_T(A,H)=constant * A(X^2)^2.                    (KBSI-5)
```

Passing this compiler constructs only a source biform. Exact T-degree two,
X-degree four, irreducibility, distinct deck conjugate, branch-specific
symmetry, endpoint norm/resolvent, and the outer self-correspondence remain
separate checks. No orientation, stabilizer type, owner, payment, row, or
Prize result is closed.

## Falsifier

An actual source packet with no full-support kernel in `(KBSI-1)`, a
full-support kernel producing no bidegree-at-most-`(2,4)` interpolant,
failure of uniqueness, or an actual complete-source packet violating
`(KBSI-3)--(KBSI-5)`.
