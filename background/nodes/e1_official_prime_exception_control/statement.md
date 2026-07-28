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
resultant ledgers exclude the two-odd profiles `(2,7)` and `(1,5,1)`.
Difference-mask relaxation, exceptional actual-vector censuses, and exact
norms exclude `(4,2,2)` and `(5,4,1)`. For `(5,4,1)`, two independent
relaxations agree on 2,924,654,040 assignments and leave 1,456 abstractions;
two independent 6,371,187,456-vector exceptional censuses leave 86 primitive
vectors, whose exact FLINT/PARI norms are all below `2^250`. The exact residual
is the sole profile `(6,6)`. Independent odd-difference engines cover all
44,779,702,968 abstract assignments; independent exceptional censuses then
cover 23,638,891,776 actual vectors per engine and leave 1,232 primitive
exceptions. Independent exact norms exclude all 1,232, closing `V=60` and
advancing the live positive even frontier to `V<=58`. At `V=58`, exact slack
gives `L<=17`, the cubic cutoff is `M_3=872`, and parity leaves eight profiles
on 111 affine one-diameter light templates. Folded-chord and direct-negacyclic
engines agree after 2,203,120,896 vectors per engine, leaving 4,812 cubic
exceptions. The conductor theorem removes 3,992; independent FLINT/PARI norms
put all 820 primitive exceptions below `2^250`. Thus `V=58` is empty and the
live positive even frontier is `V<=56`. At `V=56`, exact slack gives `L<=16`,
the cubic cutoff is `M_3=658`, and parity leaves eight profiles on six
antipodal-pair and 148 four-odd affine light templates. Two independent
3,056,582,144-vector censuses leave 12,638 cubic exceptions. The conductor
theorem removes 8,266; independent FLINT/PARI norms put all 4,372 primitive
exceptions below `2^250`. Thus `V=56` is empty and the live frontier is
`V<=54`. At `V=54`, exact slack gives `L<=15`, the cubic cutoff is `M_3=443`,
and parity leaves six profiles on eight three-odd affine light templates. Two
independent 158,783,488-vector censuses leave 2,000 cubic exceptions. The
conductor theorem removes 1,596; independent FLINT/PARI norms put all 404
primitive exceptions below `2^250`. Thus `V=54` is empty and the live frontier
is `V<=52`. At `V=52`, exact slack gives `L<=16`, the cubic cutoff is
`M_3=228`, and diameter parity leaves six two-odd and four six-odd profiles.
Two independent 1,726,770,432-vector censuses close all six two-odd profiles:
the conductor theorem removes 9,564 of the 17,624 cubic exceptions, and
independent FLINT/PARI norms put all 8,060 primitive exceptions below
`2^250`. Two independent 24,492,353,024-vector censuses then close the four
six-odd profiles `(6,5)`, `(5,3,1)`, `(4,1,2)`, and `(6,1,0,1)` on all 1,234
affine templates. The conductor theorem removes 29,206 of their 74,614 cubic
exceptions; independent FLINT/PARI norms put all 45,408 primitive exceptions
below `2^250`. Thus `V=52` is empty and the live positive even frontier is
`V<=50`. At `V=50`, exact slack gives `L<=15`, the last positive
cubic-Hermite cutoff is `M_3=13`, and diameter parity leaves nine profiles on
111 affine one-diameter templates. Independent 2,203,120,896-vector censuses
leave 31,280 cubic exceptions. The conductor theorem removes 14,296;
independent FLINT/PARI norms put all 16,984 primitive exceptions below
`2^250`. Thus `V=50` is empty. At `V=48`, cutoff-free slack and parity leave
six profiles on 154 zero/four-odd affine templates. Independent
3,056,582,144-vector engines find 14,416 profile vectors, including 6,834 at
full conductor. The conductor theorem removes the other 7,582; independent
FLINT/PARI norms put every full-conductor norm below `2^250`. Thus `V=48` is
empty. At `V=46`, cutoff-free slack and parity leave four profiles on eight
three-odd affine templates. Independent 158,783,488-vector engines find 1,888
profile vectors, including 484 at full conductor. The conductor theorem
removes the other 1,404; independent FLINT/PARI norms put every full-conductor
norm below `2^250`. Thus `V=46` is empty and the live positive even frontier
reaches `V<=44`. At `V=44`, cutoff-free slack and parity leave eight profiles
on 1,321 two/six-odd affine templates. Independent 26,219,123,456-vector
engines find 27,998 profile vectors, including 15,002 at full conductor. The
conductor theorem removes the other 12,996; independent FLINT/PARI norms put
every full-conductor norm below `2^250`. Thus `V=44` is empty and the live
positive even frontier reaches `V<=42`. At `V=42`, cutoff-free slack and
parity leave seven profiles on 111 one/five-odd affine templates. Independent
2,203,120,896-vector engines find 10,454 profile vectors, including 4,640 at
full conductor. The conductor theorem removes the other 5,814; independent
FLINT/PARI norms put every full-conductor norm below `2^250`. Thus `V=42` is
empty and the live positive even frontier reaches `V<=40`. At `V=40`,
cutoff-free slack and parity leave six profiles on 154 zero/four-odd affine
templates. Independent 3,056,582,144-vector engines find 6,426 profile
vectors, including 1,900 at full conductor. The conductor theorem removes the
other 4,526; independent FLINT/PARI norms put every full-conductor norm below
`2^250`. Thus `V=40` is empty and the live positive even frontier is `V<=38`.
At `V=38`, cutoff-free slack and parity leave four profiles on eight
one-diameter three-odd affine templates. Independent 158,783,488-vector
engines find 574 profile vectors, including 136 at full conductor. The
conductor theorem removes the other 438; independent FLINT/PARI norms put
every full-conductor norm below `2^250`. Thus `V=38` is empty and the live
positive even frontier is `V<=36`.
At `V=36`, cutoff-free slack and parity leave six profiles on 1,321
two/six-odd affine templates. Independent 26,219,123,456-vector engines find
6,712 profile vectors, including 2,994 at full conductor. The conductor
theorem removes the other 3,718. Six full-conductor whole norms reach
`2^250`, but independent FLINT/PARI ledgers put every odd norm part below
`2^250`. Thus `V=36` is empty and the live positive even frontier is `V<=34`.
At `V=34`, cutoff-free slack and parity leave five profiles on 111
one/five-odd affine templates. Independent 2,203,120,896-vector engines find
2,050 profile vectors, including 488 at full conductor. The conductor theorem
removes the other 1,562. Sixteen full-conductor whole norms reach `2^250`, but
independent FLINT/PARI ledgers put every odd norm part below `2^250`. Thus
`V=34` is empty and the live positive even frontier is `V<=32`.
At `V=32`, cutoff-free slack and parity leave four profiles on 154
zero/four-odd affine templates. Independent 3,056,582,144-vector engines find
688 profile vectors, including 178 at full conductor; two routed profiles are
exactly empty. The conductor theorem removes the other 510. Ten
full-conductor whole norms reach `2^250`, but independent FLINT/PARI ledgers
put every odd norm part below `2^250`. Thus `V=32` is empty and the live
positive even frontier is `V<=30`.
At `V=30`, cutoff-free slack and parity leave two profiles on eight three-odd
affine templates. Independent 158,783,488-vector engines find 294 profile
vectors, including 64 at full conductor. The conductor theorem removes the
other 230. Thirty-two full-conductor whole norms reach `2^250`, but
independent FLINT/PARI ledgers put every odd norm part below `2^250`. Thus
`V=30` is empty and the live positive even frontier is `V<=28`.
At `V=28`, cutoff-free slack and parity leave four profiles on 1,321
two/six-odd affine templates. Independent 26,219,123,456-vector engines find
1,836 profile vectors, including 736 at full conductor. The conductor theorem
removes the other 1,100. Six full-conductor odd norm parts reach `2^250`, but
they comprise three composite integers below `2^251` by independent exact
PARI/FLINT primality tests. Thus `V=28` is empty and the live positive even
frontier is `V<=26`.
At `V=26`, cutoff-free slack and parity leave four profiles on 111 one/five-odd
templates. Independent 2,203,120,896-vector engines find 820 profile vectors,
including 136 at full conductor. The conductor theorem removes the other 684.
Four full-conductor odd norm parts reach `2^250`, but they comprise two
composite integers below `2^251` by exact PARI/FLINT tests. Thus `V=26` is
empty and the live positive even frontier is `V<=24`.
At `N=512,s=2`, exact variance
excludes
`(0,4,0)` and the complete interval-resultant certificate excludes `(1,2,0)`.
Thus any surviving `N=512` collision has `s>=3`.

The distance-band statement is not a square-mass exhaustion. By
`e1_collision_square_mass_reparametrization`, the class difference has
`S=4a+b`, with exact finite bounds `S<=260` for the rate-`1/4` lane and
`S<=132` for the other two lanes. At `N=256,S=16`, the additional splits
`(2,8)`, `(1,12)`, and `(0,16)` are realized by official-size class pairs and
survive the current norm test. The variance campaign covers only `(3,4)`.
Its `V<=24` residual is therefore profile-local evidence, not the next
route-uniform frontier.

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
