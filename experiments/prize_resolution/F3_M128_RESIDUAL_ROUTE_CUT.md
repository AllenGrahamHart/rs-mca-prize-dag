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
(D,Delta_0,Delta_1,Delta_2)=(24,22,16,0),
nu_(X-1 mod 2)=9.
```

Thus even the exact Taylor multiplicity leaves the scalar energy upper bound
above the divisor threshold by more than `15` bits. Taylor valuation alone is
not the missing input. Exact even/odd recursion gives a joint cyclotomic norm
product satisfying

```text
|Norm_128(F) Norm_64(F) Norm_32(F)| > 2^240.
```

This falsifies the uniform joint-product route by more than five bits. But the
three exact norms have gcd exactly `512`: they share no odd prime. A genuine
moment solution needs one row prime with valuation pattern at least `(5,2,1)`
across the order-`128,64,32` norms. The product bound discards precisely this
alignment. The next useful proposition is therefore a common-prime alignment
theorem excluding every official prime from that valuation pattern; a bound
on the product alone is insufficient.

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
