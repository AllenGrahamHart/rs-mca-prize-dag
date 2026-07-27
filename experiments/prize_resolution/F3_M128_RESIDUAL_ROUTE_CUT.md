# F3 `m=128` residual energy route cut

## Question

Can the residual `h=10`, Haar mask `011`, be closed merely by replacing the
continuous AM--GM relaxation with the exact attainable integer energies?

## Result

No. The exact eight-group dynamic program in
`f3_m128_h10_mask011_dp.cpp` works directly with signed supports having ten
`+1` and ten `-1` coefficients. The condition `Delta_2=0` is imposed group by
group, and only Pareto-maximal triples `(D,Delta_0,Delta_1)` are retained.

The attainable maximum is

```text
(D,Delta_0,Delta_1)=(22,24,24),
D^32 Delta_0^16 Delta_1^8=22^32 24^24>2^235.
```

The exact ratio is greater than `219051`; equivalently the proposed endpoint
misses by about `17.74` bits. Thus energy integrality alone cannot close this
mask.

The low-memory sampler `f3_m128_residual_search.py` independently shows why
this candidate is easy to miss: ordinary random supports find much smaller
values in the zero-Haar-scale masks, while the all-positive `h=11` mask still
has positive examples within about nine bits of the relaxed threshold.

## Consequence

Do not spend another proof round sharpening only the shared Haar energy
polytope at `m=128`. A successful next step must use information absent from
that polytope, such as the full moment congruences, primitive exact-level
condition, split-locator equations, or a genuine orbit debit. This result
does not construct a primitive shift pair and does not refute the HGE4 node.

## Joint-norm route probe

The deterministic probe `f3_m128_joint_norm_route_probe.py` separates two
possible refinements on one explicit primitive-support fixture at `h=10`,
mask `011`. It has

```text
(D,Delta_0,Delta_1,Delta_2)=(22,22,24,0),
nu_(X-1 mod 2)=9.
```

Thus even the exact Taylor multiplicity leaves the scalar energy upper bound
above the divisor threshold by more than `15` bits. Taylor valuation alone is
not the missing input. In contrast, exact even/odd recursion gives the joint
cyclotomic norm product

```text
|Norm_128(F) Norm_64(F) Norm_32(F)| < 2^235,
```

while the required structural/balance and ambient-prime divisibility is
strictly greater than `2^235`. On this adversarial fixture, retaining the
joint Fourier spectrum gains more than enough to close the mask. This is a
route probe, not a universal inequality: the next useful proposition is a
uniform joint determinant/resultant bound for every mask-`011` support.

## Replay

```bash
g++ -std=c++20 -O2 experiments/prize_resolution/f3_m128_h10_mask011_dp.cpp \
  -o /tmp/f3_m128_h10_mask011_dp
./tools/ramguard tiny -- /tmp/f3_m128_h10_mask011_dp
./tools/ramguard tiny -- \
  python3 experiments/prize_resolution/f3_m128_residual_search.py --trials 20000
./tools/ramguard tiny -- \
  python3 experiments/prize_resolution/f3_m128_joint_norm_route_probe.py
```
