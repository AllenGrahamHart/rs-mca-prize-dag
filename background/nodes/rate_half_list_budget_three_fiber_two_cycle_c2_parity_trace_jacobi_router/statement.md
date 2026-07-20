# Budget-three fiber-two c=2 parity trace-Jacobi router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction`,
  `rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination`,
  `rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_pure_fourth_root_primary_exclusion`

Retain the normalized generic `c=2` chamber when the four denominator roots
are two antipodal pairs. Put

```text
M=2^36,       N=16M=2^40,
Omega={1,-1,r,-r},       tau=r^2,
E(z)=(1-z^2)(1-tau z^2).                              (C2P1)
```

Then `tau in mu_(8M)\{1}` and the complete primary/secondary packet is the
existing univariate parity system

```text
F_(2M)(tau)=0,       F_(2M+1)(tau)!=0,       G_M(tau)=0.
                                                               (C2P2)
```

The pure value `tau=-1` is already excluded at the official primary gap.

Let the canonical outer invariants be `I,J` and put

```text
K(Z)=4I^3 Z(Z-36)^2-J^2(Z+12)^3,
chi=r+r^(-1).                                         (C2P3)
```

The six unordered selected pairs in `Omega` have exactly three trace
classes, each with multiplicity two:

```text
z_0=0,       z_+=2+chi,       z_-=2-chi.              (C2P4)
```

Consequently the full `c=2` completion-root coupling on this parity chamber
is exactly

```text
J=0
or
K(2+chi)K(2-chi)=0.                                  (C2P5)
```

The second expression is invariant under `r->-r` and `r->r^(-1)` and is a
polynomial in

```text
chi^2=tau+tau^(-1)+2.                                 (C2P6)
```

No selected-pair or square-root-lift enumeration remains.

This chamber shares the existing CR-002 Jacobi torsion prefilter. Choose the
base-field square root `q^2=r`, so `q^4=tau`, and put

```text
x=(r+r^(-1))/2,       w=2x^2-1=(tau+tau^(-1))/2,
mathcalJ(w)=J_M^(-1/4,-1/2)(w),
K_-(w)=T_(2M)(w),       K_+(w)=U_(2M-1)(w).           (C2P7)
```

Every parity survivor has one sign `epsilon=q^(16M) in {1,-1}` and satisfies

```text
gcd(mathcalJ,K_epsilon)!=1.                           (C2P8)
```

Thus its odd characteristic divides the same norm pair `R_-,R_+` already
assigned to CR-002: the order-`8M=2^39` minus norm and the 37-level plus
tower through order `2^38`. A no-divisor result for that shared pair closes
the `c=2` parity chamber as well as the matched `c=0` and generic `c=1`
parity chambers. A compatible divisor must still pass `(C2P2)`, `(C2P5)`,
canonical span, splitting, and cycle reconstruction.

This theorem neither proves that every `c=2` denominator is parity nor
evaluates the shared norms. It creates no new large-compute request.
