# Cycle 54: rate-half Haboeck dual optimizer (2026-08-10)

## Frontier reconciliation

The upstream open frontier remains concentrated in LIST FPC5, K3 source-line
work, and MCA denominator/clone routing. None of the inspected open PRs closes
a prize endpoint. Canonical Fable has three live, uncommitted rate-half pilots
on the FR, far-CA, and residual routes, so this cycle avoids those surfaces and
finishes the supplier-side question left by its committed Haboeck audit.

## Certified content

For the imported quadratic Haboeck family, `Q_m` is nondecreasing and
unbounded while `a_m` is nonincreasing. Consequently:

```text
m_B=max{m>=3: Q_m<=B}
```

gives the smallest safe agreement available at fixed budget `B`, and

```text
m_s=min{m>=3: a_m<=s}
```

gives the smallest certified numerator available at fixed support `s`.
These are dual exact optimizers over the complete printed theorem family.

The independent audit now reconstructs every row `m=3..96` by binary search,
checks all adjacent floor and ceiling inequalities, certifies strict
monotonicity on the official-cap ladder, and checks both optimizer boundaries.

## Fence and next step

The supplier theorem has no retained support parameter after its threshold is
met. Therefore an arithmetic interpolation between adjacent `m` values cannot
improve the safe bracket. Progress toward `rate_half_band_crossing_location`
must instead supply either a genuinely support-sensitive bound or an
unsafe-side estimate. The critical status remains unchanged.
