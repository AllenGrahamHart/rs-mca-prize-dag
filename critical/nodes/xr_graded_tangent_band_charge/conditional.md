# Conditional proof

Assume `xr_band_high_window_exclusion` (SL-2).

The banked graded-band ledger gives

```text
|Gamma_band| = sum_d sum_{P at depth d} L_P
```

with `L_P` bounded by the exact line cap. The RowC occupancy budgets are
vacuous. On the prize rows, the banked ray-side closure bounds every
low depth by the uniform envelope `25N_d<=17n^2`, and the named cascade
tier has the stronger selected-support bound `N_{h-1}<=n/2`. Thus the
only unpaid range is `ceil(h/2)<=d<=h-2`, identified by consolidation
Update 6.

On that range SL-2 supplies the same envelope. Put

```text
S_R = sum_{d=1}^{h-2} floor((n-k-d)/(h-d)),
H_band(C) = s_lo(C)-16n^3.
```

The master ledger and cascade cap therefore give

```text
|Gamma_band|
 <= floor(17n^2/25) S_R + floor(n/2)(n-A+1)
 <= H_band(C).                                           (*)
```

The second inequality is exact integer arithmetic at the three prize
rows; RowC is already discharged independently. `verify.py` checks the
published divisor-block sums, all six row budgets, and the tightness of
the constant by confirming that replacing `17` by `18` fails at prize
rates `1/8` and `1/16`. Thus `16n^3+|Gamma_band|<=s_lo(C)`, exactly the
consumer interface. QED conditional on SL-2.

The windowed-projection theorem supplies a sufficient route to SL-2,
but the conditional implication uses only the conclusion of SL-2.
