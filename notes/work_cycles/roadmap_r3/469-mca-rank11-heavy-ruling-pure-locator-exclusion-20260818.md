# Cycle 469: core-saturated pure-locator exclusion

## Starting pins

```text
our SHA: c5dc42851
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED first branch payment

After deterministic pair ownership is fixed, reselect every packet support
to contain its assigned pair core. Pair noncontainment gives `|H_p|<m`, so
this is compatible with an exact size-`m` agreement support. Two distinct
slopes from the same pair have full agreement intersection exactly `H_p`.
As every represented pair contributes two records, the complete packet
support is therefore

```text
C=intersection_p H_p=J,       |C|<K-2.
```

On the canceled row, every represented core has size at least `m'-11`.
Two distinct pair types have residual core intersection at most `K'-1`,
since one nonzero component difference has degree below `K'`. Their union
therefore has size

```text
at least 2(m'-11)-(K'-1)=m'+67451>m'.
```

In a pure-locator certificate, the two slopes from each pair force both
coefficient polynomials to vanish on that pair core. Two represented pair
types make both degree-at-most-`m'` polynomials vanish at more than `m'`
points, so they are zero. The affine locator scalar then vanishes at all 32
slopes, making the homogeneous certificate trivial. Contradiction.

The packet now has only two live outputs:

```text
nontrivial scalar-locator rational profile with deg Q<=67472
or
chi>=2299571.
```

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: pure locator / rational / high complexity -> rational / high complexity
new assumptions: none
next action: constrain Q using the two saturated cores, or pay chi using the pair-block decomposition
```

## Nonclaims

- no rational-profile or high-complexity payment;
- no globalization of the selected packet core;
- no whole-line owner, adjacent-row safety, or MCA closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion/verify_audit.py
```
