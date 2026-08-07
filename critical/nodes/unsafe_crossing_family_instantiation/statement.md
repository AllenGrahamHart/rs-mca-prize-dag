# unsafe_crossing_family_instantiation

- **status:** TARGET
- **closure:** open

## Statement

For every admissible row and its proposed first-safe agreement `a_safe`, emit
an exact certificate at `a_safe-1` in at least one of the following forms.

### Q: quotient floor

Pin a quotient order `N'` satisfying every hypothesis of `qfloor_exact`, prove
that its canonical witness radius reaches `a_safe-1`, and prove

```text
Acl(N',ell') > B*.
```

### V: direct value set

Exhibit and certify more than `B*` pairwise-distinct ambient-field slopes,
each bad at `a_safe-1` for one received pair.

### M: averaged occupancy

Exhibit a deterministic post-paid support family `A`, its exact strict-overlap
profile, and the exact inequality

```text
nu(A) = E[N(A)] - (q/2) C_t(A) > B*.
```

The certificate must pin the ambient MCA slope field, generated/base-field
transfer, first-match ownership, and endpoint monotonicity. A family that is
merely “collided” is not an `M` certificate.

## Falsifier

An admissible row with exact `B_C(a_safe-1) <= B*` refutes this target and the
proposed adjacent endpoint. A purported payload is invalid if any scope,
ownership, endpoint, exact-count, or normalization check fails.

## Addendum (2026-08-07, round-21 closability probe — THEOREM BB closes no part)

Probe verdict (notes/pilots_20260807/red_closability_probes/): BB
bounds the LIST functional L_1(a); this node counts the MCA
bad-slope functional B_C(a) — and the inference L_1 > B* => B_C >
B* is REFUTED by an exact finite countermodel (RS[F_5, |D|=4, k=2]:
L_1 = 6 > B* = 5 >= B_C = 5). Independently: BB's row coverage
(e >= 3 full, e = 2 partial, e = 1 never) is DISJOINT from the
pair-feasible residual, which forces e = 1 (dependency_subdag
:105-110); the form and endpoint also mismatch (factor ~1e6). The
already-closed part (the finite deployed-V slice at KoalaBear +
Mersenne-31) is via identity_prefix_flexible_budget_unsafe_floor,
not BB. Lead recorded: BB's METHOD shape (concentration-class
pigeonhole + C-S accident floor) matches what the M-route's nu(A)
needs — different objects, no transfer banked. Roadmap filing
corrected: this is an MCA-lane node (CATCH-P3).
