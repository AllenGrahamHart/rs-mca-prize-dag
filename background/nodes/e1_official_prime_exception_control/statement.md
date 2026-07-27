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

By `e1_pair_feasible_prime_field_reduction`, the same branch also forces

```text
F=F_p,       q=p,       p=1 mod N.
```

Thus the prime-field premise of `kernel_lattice_reframing` is proved rather
than assumed on the live named-anchor target.

The folded Parseval bound in `e1_prime_field_l2_norm_collision_radius` also
proves that any surviving collision has raw swap distance

```text
s>=5 for N=256,       s>=2 for N=512.
```

In the first surviving `N=256` band, only folded profiles
`(4,2,0),(3,4,0)` remain. In `(3,4,0)`, exact logarithmic variance excludes
`V=0` and `V>=136`; a sparse-autocorrelation refinement
and the subsequent exact endpoint chain leave only positive even `V<=60`.
At `V=64`, exact cubic/parity arithmetic leaves autocorrelation profiles
`(4,7)`, `(0,8)`, and `(3,5,1)`; an exact light-template census excludes
`(0,8)`. The other two profiles share 148 exact affine light templates, each
with a repeated light-chord wedge; two independent joint censuses then exclude
`(3,5,1)` with exact `M_3=1392<1517`. Two independent resultant censuses and
the conductor theorem exclude `(4,7)`, closing `V=64`. At `V=62`, exact slack
and parity leave `(3,7)`, `(2,5,1)`, and `(1,3,2)` on eight affine light
templates. Independent 158,783,488-vector censuses exclude the latter two
globally and the full-conductor part of `(3,7)` by `M_3<1302`; the conductor
theorem excludes its complement, closing `V=62`. At `V=60`, exact slack gives
`L<=18`, the cubic cutoff is `M_3=1087`, and parity leaves eight profiles.
Exact quotient allocation excludes `(0,3,2)`, `(6,2,0,1)`, and `(3,0,3)`.
Two independent 87-template censuses plus independent FLINT/PARI exact-
resultant ledgers exclude the two-odd profiles `(2,7)` and `(1,5,1)`. The
exact residual is `(6,6)`, `(5,4,1)`, and `(4,2,2)`, all with six odd light
classes. A direct affine-orbit census has a proved floor of 21,773,185,792
signed vectors and is not an authorized route. At `N=512,s=2`, exact variance
excludes
`(0,4,0)` and the complete interval-resultant certificate excludes `(1,2,0)`.
Thus any surviving `N=512` collision has `s>=3`.

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
