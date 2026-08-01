# KoalaBear m2 r4 positive three-loop neighbor-norm weld

- **status:** REFUTED
- **scope:** the proposed ordinary-resultant/target-incidence weld
- **dependencies tested:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas`,
  and `rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas`
- **consumer:** none; retained as a falsified-route certificate

Write

```text
H(T,X)=D(W)T^2+E(W)+XT B(W),       W=X^2,
P(U)=Res_W(E,U D^2-WB^2),
Q(U)=Res_W(D,E^2-UWB^2).                           (KBP3N-R1)
```

The two algebraic identities

```text
Res_X(H(r,X),E(X^2))=r^4P(r^2),
Res_X(H(r,X),D(X^2))=Q(r^2)                        (KBP3N-R2)
```

are valid, and `P,Q` have degree at most two in `U`.  The separate signed
target-incidence tables are also valid graph computations.  The refuted
step identified their ratio with the divisor-weighted four-neighbor
product:

```text
P(r^2)/Q(r^2) = product of the four graph neighbors of r. (REFUTED)
                                                               (KBP3N-R3)
```

Ordinary roots of `H(r,X)` do not manually double a ramified source-loop
incidence.  Thus `(KBP3N-R2)` cannot be welded to a graph table that counts
the branch fiber with divisor multiplicity.

## Exact counterexample

Over `F_13`, in the 433 root-low common placement, take

```text
(b,c,x,y)=(2,3,2,3),       (d_0,d_1,d_2,beta)=(4,7,6,1).
```

The kernel satisfies both common product/sum records, `beta!=0`, and common
leading support.  The ordinary resultant ratio is

```text
P(U)=6+4U^2,       Q(U)=4+7U^2,
P(1)/Q(1)=8 mod 13.                                (KBP3N-R4)
```

The proposed root-low graph weld instead gives `bc=6 mod 13` at target
`1`.  Hence `8!=6` refutes `(KBP3N-R3)` on the exact admissible common
locus.  The former compressed 433/442 norm gates must not be used.

The PROVED
`rate_half_kb_m2_r4_coordinate_positive_ramified_loop_multiplicity_exclusion`
repairs the route at the correct divisor level: the same order mismatch,
combined with the complete-source square, excludes all positive two- and
three-loop packets directly.

## Falsifier

The fixture `(KBP3N-R4)` is the falsifier.  A repair would require a
divisor-weighted norm with explicit branch corrections; it is unnecessary
for the now-closed two-/three-loop rows.
