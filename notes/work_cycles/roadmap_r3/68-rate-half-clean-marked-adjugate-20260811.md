# Cycle 68: clean marked adjugate subset ledger (2026-08-11)

## Cycle pins

```text
our start:       63e23f08c
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## Marked square pencil

Let `M(t)` be the full `(4m+1) x 4m` rectangular Hankel pencil and contract
its consecutive rows at the marked point:

```text
L(t)=H_1(t)-x_0H_0(t).
```

The row-contraction kernel is the domain Veronese vector at `x_0`. Pairing
it with the two shifted left-kernel vectors gives
`Q(t;x_0)` and `x_0Q(t;x_0)`. Since this polynomial is generically nonzero,
the contraction is injective on the image of `M` and

```text
rank_F(t)L(t)=rho=4m-1.
```

## Adjugate and regular factor

Symmetry and the primitive kernel give

```text
adj L(t)=D(t)q(t)q(t)^T,       deg D=2m-1.
```

The rank-`rho` compound of the rectangular pencil identifies the scalar
exactly:

```text
D(t)=c Delta(t)Q(t;x_0)
    =c Delta(t)A_0(t)S(t),
deg Delta=m-1.
```

Here `Delta` is the regular size-`m-1` Kronecker determinant. This retains
root multiplicity; a set-theoretic rank-drop argument would not suffice.

## Cauchy-Binet ledger

On the marked support `U`, write

```text
mu_x(t)=(x-x_0)(omega_x^(0)+t omega_x^(1)),
R_U=(x^i)_(0<=i<=rho,x in U).
```

Then `L=R_U diag(mu)R_U^T`, and every adjugate entry has the exact expansion

```text
D q_iq_j=(-1)^(i+j) sum_(|J|=rho)
 det(R_(hat j,J))det(R_(hat i,J)) product_(x in J)mu_x.
```

The corner minors are ordinary nonzero Vandermondes. Interior generalized
Vandermonde minors may vanish; the theorem explicitly retains that route
fence. The marked fibre factor has exactly `m-1` distinct supported roots
and `Delta` has degree `m-1`, so at least

```text
4m+1-2(m-1)=2m+3
```

supported slopes specialize the ledger to a nonzero rank-one outer square
of a fully split locator. The exact `m=1`, `F_17` witness independently
replays the boundary factor at parameter infinity.

The proved node is
`rate_half_ca_hankel_clean_endpoint_marked_adjugate_subset_ledger`.

## Burn-down

```text
result:                  NARROWED; exact subset cofactor ledger
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next route-deciding theorem should use the corner Vandermonde identity,
or its sparse Forney-weight specialization, together with the simultaneous
degree-`m` motion across the `2m+3` guaranteed supported slopes. Raw subset
counts and termwise noncancellation are invalid routes.
