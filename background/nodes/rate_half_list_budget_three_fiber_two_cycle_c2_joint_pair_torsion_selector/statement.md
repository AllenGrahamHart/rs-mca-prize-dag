# Budget-three fiber-two c=2 joint pair-torsion selector

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_outer_torsion_trace_gate`

Retain a generic canonical survivor in the `c=2` denominator-mismatch
stratum. Write

```text
N=2^40,
D_*(Y)=product_(A in Omega)(Y-A),
R_D(Z)=product_({A,B} subset Omega)(ZAB-(A+B)^2),
K_O(Z)=4I^3 Z(Z-36)^2-J^2(Z+12)^3.                (JPT1)
```

The four elements of `Omega` are distinct and nonzero, and `K_O` has exact
degree three. Reduce `R_D` modulo `K_O`, and in `F[Z]/(K_O)` put

```text
Rbar=R_D mod K_O,
Q_0=Z-2,
Q_(j+1)=Q_j^2-2 mod K_O,       0<=j<40,
G_2=gcd(K_O,Rbar,Q_40-2).                           (JPT2)
```

Then `G_2` is nonconstant if and only if there is an actual unordered pair
`{A,B} subset Omega` for which

```text
z=(A+B)^2/(AB),       K_O(z)=0,       (A/B)^N=1.    (JPT3)
```

More precisely, over an algebraic closure the distinct zeros of `G_2` are
exactly the trace values `z` of the pairs satisfying `(JPT3)`. Thus
`deg(G_2)<=3`, and only pairs matching one of its zeros need be reconstructed.
The selector uses one degree-six reduction followed by forty squarings and
reductions of degree-at-most-two polynomials modulo a cubic.

This repairs the scope of the outer-only torsion gate: an outer torsion root
which is not the trace of an actual pair of roots of `D_*` is discarded. It
does not prove the selected-pair set empty, impose canonical span or the gap
equations, reconstruct a full cycle, or authorize a large computation.
