# E32 profile-(3,5,1) route report

The abstract nested-layer cap is 1760, above the exact `V=64` cubic cutoff
1517. The complete mod-16 quotient relaxation also remains above the cutoff:

```text
order 128: 1,828,183 allocations, exact maximum 1610,
order  64: 1,165,828 allocations, exact maximum 1594.
```

Modal app `ap-SGBtxxgNaabwqswwXpXYE6` completed all 32 shards under the
60-second function cap. The compact result records a maximizing allocation in
each chamber. `e32_profile351_quotient_probe_check.py` reconstructs both
objectives and the complete allocation totals locally from the independent
Python implementation.

These allocations are quotient-relaxation witnesses, not actual
autocorrelation vectors or collisions. They prove only that the uncoupled
three-layer quotient compiler cannot exclude `(3,5,1)` at `M_3=1517`.
Further quotient enumeration is retired. The next attack must use the exact
zero/two-diameter light geometry or another coupling absent from the quotient
allocation.
