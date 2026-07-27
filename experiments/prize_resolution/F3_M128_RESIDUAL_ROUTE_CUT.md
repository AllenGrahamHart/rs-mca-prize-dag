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

## Replay

```bash
g++ -std=c++20 -O2 experiments/prize_resolution/f3_m128_h10_mask011_dp.cpp \
  -o /tmp/f3_m128_h10_mask011_dp
./tools/ramguard tiny -- /tmp/f3_m128_h10_mask011_dp
./tools/ramguard tiny -- \
  python3 experiments/prize_resolution/f3_m128_residual_search.py --trials 20000
```
