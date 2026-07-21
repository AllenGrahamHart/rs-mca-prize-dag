# Dependency sub-DAG

```text
rate_half_cyclic_rotated_prefix_floor [PROVED, unsafe evidence] --+
rate_half_list_integer_johnson_safe_anchor [PROVED, safe evidence]+--> rate_half_list_adjacent_crossing [TARGET]
rate_half_list_low_budget_exact_crossing [PROVED, B*=1,2] -------+
list_crossing_localization [PROVED, monotonicity] ----------------+
matching adjacent upper/lower pair [OPEN CONTENT] ----------------+

rate_half_list_adjacent_crossing [TARGET]
  -> list_adjacency_closing [CONDITIONAL]
  -> list_large_m_scope_closure [CONDITIONAL, transitively]
  -> list_grand [CONDITIONAL]
```

The new leaf is not a decomposition into speculative propositions. It names an
already-admitted missing premise in the existing conditional packet.

The cyclic prefix floor is also a direct proved requirement of
`list_adjacency_closing`, keeping the lower-bracket provenance on the critical
path. Its edge into this red leaf is evidence because critical TARGETs must
remain logical leaves. The Johnson anchor is likewise evidence: it proves a
safe endpoint but not predecessor unsafety in the remaining `B*>=3` branches.
The low-budget theorem is evidence because it closes only `B*=1,2`.

The budget-three path evidence now also contains the proved finite branch

```text
rate_half_list_budget_three_multifiber_vandermonde_exclusion [PROVED]
  -> rate_half_list_budget_three_fiber_two_path_exclusion [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The first node pays common fiber sizes `m>=3`; the second pays `m=2`. Fiber
size one and the mixed/partial/primitive path branches remain, so this does
not become a required premise or promote the target.

The remaining common-`X^2` cycle branch is routed into the existing quotient
pencil:

```text
multifiber setup + antipodal weld/primitive/degree theorems
  -> rate_half_list_budget_three_fiber_two_cycle_quotient_embedding [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

At the prize maximum the `c=0` stratum is the same matched census at quotient
order `2^40`, alongside the fiber-four antipodal instance at order `2^39`.
The `c=1,2` denominator-mismatch strata are separate. Emptiness of all three
remains open.

The parameter-uniform boundary chain now transfers one stage further:

```text
cycle quartic-pencil router + reverse/gap/two-window/canonical theorems
  -> rate_half_list_budget_three_fiber_two_cycle_boundary_transfer [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

This transfer stops before the old one-parameter Mobius-ratio and norm gates
on `c=1,2`, where completion-root matching differs from denominator-lift
matching.

The matched branch now continues one stage farther:

```text
cycle boundary transfer + even factorization + maximal field collapse
  -> rate_half_list_budget_three_fiber_two_cycle_matched_lift_field_router [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

At `M=2^36`, every survivor in the matched two-antipodal-denominator
subbranch has its normalized source/outer quadruple and Mobius matching over
`F_p`. The other matched denominator geometries, doubled-order
scalar/Jacobi/norm transfer, and new `c=1,2` completion-root couplings remain
open.

The matched parity branch now has its exact post-field compiler:

```text
matched field router + constant ODE + harmonic certificates
  -> rate_half_list_budget_three_fiber_two_cycle_matched_post_field_compiler [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The compiler repairs the final gate to `T/q_out=W^4`, closes the harmonic
branch, and transfers the constant/Legendre and gcd stages. The trace-Jacobi
and cyclotomic-norm scale transfer remains open.

The exclusion interface now reaches that endpoint:

```text
matched post-field compiler + trace/Jacobi/norm transformations
  -> rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The remaining matched-parity task is algorithmic or analytic evaluation of
the printed norms and signed gcds, followed by the corrected post-field
filters for every survivor. No large run is authorized.

The denominator-mismatch coupling is also finite:

```text
fiber-two cycle boundary transfer
  -> rate_half_list_budget_three_fiber_two_cycle_mismatch_invariant_coupling_router [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

Its `c=1` and `c=2` packets have respectively 24 and six binary-quartic
invariant tests. Their exclusion against the coefficient-gap and canonical
span equations remains open.

The selected `c=2` lane has the following sharper exact interface:

```text
joint actual-pair torsion selector [PROVED]
  -> normalized pair/torsion compiler [PROVED]
       + maximal field-degree collapse [PROVED]
         -> c=2 torsion-field router [PROVED]
              -> rate_half_list_adjacent_crossing [TARGET, evidence]

two-window square reduction [PROVED]
  -> c=2 secondary differential certifier [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The torsion terminal forces splitting and square class, leaving distinct
quartets in `mu_(2^40)`. The remaining parity-forcing target is not installed
as a premise. If proved, the existing c2 parity trace/Jacobi router sends it
to the shared CR-002 norm interface.

The part already containing one antipodal pair now splits off exactly:

```text
normalized c2 gap/span compiler [PROVED] --+
                                             +--> c2 one-antipodal primary/torsion reducer [PROVED]
c2 torsion-field router [PROVED] -----------+                     |
                                                                   +--evidence--> adjacent crossing [TARGET]
```

This reducer replaces root-labelled data by the sign-free `(X,P)` circuit.
It leaves both its emptiness and the antipodal-free C2-PAR stratum open.

The preferred field-aware interface is one step smaller:

```text
one-antipodal reducer + torsion-field router
  -> c2 one-antipodal product/ratio trace compiler [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

It works with prime-field ratio trace `Z` and product `P`, couples their
half-order signs, and removes the old square-root search.

The complete-candidate route also has a root-cell Fourier reduction:

```text
cycle boundary transfer + normalized c2 gap/span compiler
  + one-antipodal product/ratio compiler
    -> c2 one-antipodal canonical-cell Fourier ladder [PROVED]
         -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

It forces exact moment prefixes and a negation-invariant/large-mismatch
dichotomy but does not classify either alternative or prove `C2-PAR`.

The unique barycentric direction is sharper:

```text
canonical-cell Fourier ladder [PROVED]
  -> one-antipodal barycentric negation syndrome [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

Its first nonzero syndrome is exact and forces support at least `3H+1`; the
minimum-support derivative packet and all larger supports remain open.

The same direction now has a cell-free polynomial endpoint:

```text
barycentric negation syndrome [PROVED]
  -> barycentric support-polynomial compiler [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

Minimum support is one exact subgroup split-divisor test for `J`; neither
that test nor larger support is yet excluded.

The support and collision routes now recombine by canonical degree:

```text
support-polynomial compiler + collision-or-high-support router
  + secondary differential + field/Stepanov inputs
    -> one-antipodal degree-defect global gate router [PROVED]
         -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The maximal-degree branch inherits the Euler, infinity, selected-affine, and
Stepanov gates at every support. Degree-deficient packets have an exact even
support-defect ledger. The split-divisor endpoint is still equality-only.
