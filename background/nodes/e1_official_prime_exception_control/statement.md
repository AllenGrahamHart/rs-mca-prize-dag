# e1_official_prime_exception_control

- **status:** TARGET
- **closure:** open

## Statement

For every admissible row in the pair-feasible direct-E1 candidate class at the
current clean candidate predecessor, pin the actual ambient MCA slope field,
generated field, quotient embedding, cyclotomic reduction prime/ideal, and
endpoint. The candidate class is defined independently of the desired
conclusion by

```text
Q = the canonical quotient root set,
B = F_p(Q),
b=|B| >= b_pair_min(K,B*) = ceil((K+B*+1)/3),
B* = floor(|F|/2^128).
```

By `e1_pair_feasible_ambient_generation`, this premise automatically forces
`B=F` at all six named anchors. The generated-field transfer is therefore not
an additional hypothesis of the live pair-feasible target.

The actual quotient orders are

```text
N in {256,512},       h=N/2 in {128,256},
ell=rho N+1.
```

Let `K=A_2(N,ell)` be the exact characteristic-zero
antipodal-rearrangement class count. For the reduction map from those classes
to ambient-field `-e_1` values, let

```text
P = sum_y binom(r_y,2)
```

be the number of unordered pairs of distinct characteristic-zero classes that
collide after reduction. Prove the finite, row-specific inequality

```text
P <= K-B*-1,          B*=floor(|F|/2^128).
```

By `e1_clean_anchor_exact_collision_allowance`, this implies more than `B*`
distinct ambient bad slopes. A direct certificate of more than `B*` distinct
values may bypass this target and feed `unsafe_crossing_family_instantiation`
directly.

The older phrase `N' in {128,256}` referred ambiguously to folded dimensions;
it is not the quotient-order scope of this target. Certificates for finitely
many named exhibit fields do not discharge the route-uniform quantifier.
`unsafe_crossing_family_instantiation` separately owns proof that every
admissible row receives some valid unsafe payload.

For `b<=B*`, direct E1 is impossible. For `B*<b<b_pair_min`, the balanced-
fiber collision floor already exceeds the allowance, so this pair-loss target
is impossible; a sharper direct image theorem or another supplier must pay
that branch.

## Falsifier

A row in the printed candidate class with `P>K-B*-1` refutes this
collision-pair target, even if a sharper direct image argument might still pay
that row. A purported route-wide certifier is also defeated if it leaves any
candidate-class row uncovered or counts slopes in a proper subfield against
the ambient budget.
