# hankel_slope_large_sieve conditional proof
## Predicate node
- `diffuse_triple_shadow`
## Claim
The diffuse triple-shadow theorem implies the supported-slope estimate.
## Proof (Pro, refereed)
One unpaid support per slope; <= 2n are fresh-rank (dim K^n + K^n); every
non-fresh one lies in a minimal stagnating dependency; the Vandermonde lemma
confines dual supports to triple-covered shadows; a k+1 triple core =>
tangent-paid (the 2x2 slope solve); else diffuse m >= 4 => poly by the
predicate. Sum: poly slopes; times conj_f's fiber bound => R2.

## Stress evidence

The amber-stress scan

```text
python3 experiments/amber_stress/diffuse_shadow_circuit_scan.py
```

models first rank-stagnating locator/slope circuits over small
finite-field Hankel rows.  In the current run it found `11,785` minimal
dependent circuits and no case where the triple-covered agreement shadow had
size `< k+1`.  The `m = 3` circuits were tangent-core in the tested rows; the
`m >= 4` non-tangent circuits landed in the diffuse residue.  This supports
the implication's reduction surface, but the live premise remains the
polynomial count in `diffuse_triple_shadow`.
