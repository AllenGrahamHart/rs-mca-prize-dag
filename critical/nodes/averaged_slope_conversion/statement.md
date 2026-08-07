# Averaged locator-to-slope conversion

- **status:** PROVED
- **closure:** exact occupancy inequality

Let `A` be a deterministic family of exact `(k+t)`-supports. For a random
independent pair of words, let `X_z(A)` be the number of supports contributing
the finite slope `z`, let

```text
N(A)=sum_z X_z(A),
Y(A)=#{z:X_z(A)>0},
```

and let `C_t(A)` be the exact fixed-slope ordered second factorial moment
proved by `averaged_xr`. Then

```text
E[Y(A)] >= E[N(A)]-(q/2)C_t(A).
```

Consequently, for every integer `B>=1`, if

```text
nu(A)=E[N(A)]-(q/2)C_t(A) > B-1,
```

some received pair has at least `B` distinct finite bad slopes witnessed by
`A`. Prize use takes `B=B*+1`, so the strict certificate is `nu(A)>B*`.

This theorem is valid for every deterministic family. A prize-level unpaid
payload must separately supply post-paid ownership, its exact strict-overlap
profile, and the ambient-field interpretation.

## Round-22 addendum (2026-08-07, coordinator-applied on replay): THEOREM AT — concentration ANTI-transport

With N = Sum_z X_z, Y = #{z : X_z > 0}, and RHS := N - (1/2) Sum_z
X_z(X_z - 1) (the exact right-hand side of this node's conversion, so
nu(A) = E[RHS]):

    RHS <= (3/2) N - N^2 / (2Y).

Hence Y <= N/3 forces RHS <= 0, i.e. nu(A) <= 0 < B*. Under uniform
concentration kappa = N/Y the identity RHS = N (3 - kappa)/2 is exact;
the threshold constant is exactly 3 (largest ratio admitting RHS > 0
is 14/5, verified exhaustively over ALL occupancy vectors with
N <= 14 in exact Fraction arithmetic; 1550-check suite replayed by
the coordinator, fail-closed control exits 1).

CONSEQUENCE (the round-21 lead reversed): THEOREM BB's deep-stratum
shell concentration (kappa = 2^33: 256 shells of 2^41) gives
RHS = N(3 - 2^33)/2 < 0 for every N >= 1 — shell concentration
DESTROYS this node's occupancy functional rather than supplying it.
E[N(A)] = |A| (1 - q^{-t}) q^{1-t} depends on A only through |A|;
every structural property enters only through C_t(A) >= 0, which
carries a MINUS sign. What a positive nu(A) bound needs is large |A|
plus a PROVED anti-concentration/spreading certificate keeping
C_t(A) small — the NEGATION of BB's conclusion — plus this node's
payload hypotheses. Source: notes/pilots_20260807/bb_nu_transport/
(PROOFS.md THEOREM AT; transport.py).
