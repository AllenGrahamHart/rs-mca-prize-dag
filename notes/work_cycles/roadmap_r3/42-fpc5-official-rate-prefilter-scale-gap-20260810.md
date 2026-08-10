### 2026-08-10 FPC5 official-rate prefilter scale gap

The exact FPC5 prefilter was specialized over the complete official row set,
not a sample. In the candidate prefixes for rates `1/4,1/8,1/16`, the source
equation gives `ell>=k/4`; ordinary Johnson feasibility then eliminates every
`t>=4` cell symbolically. Two independent exact-integer verifiers exhaust the
remaining `t=2,3` cells.

The result removes all `(PF6)` cells through `M=12,28,56`, narrowing the
critical large-source target to

```text
rate 1/2: M>=5,   rate 1/4: M>=13,
rate 1/8: M>=29,  rate 1/16: M>=57.
```

Boundary survivors at `n=8192` and `M=13,29,57` show that this arithmetic
sieve is sharp. They are parameter tuples, not contributor witnesses; the
remaining split-and-guard aggregate is unchanged in kind. The replay audits
59,904 exact cells, uses no floating point, and required no Modal spend.

Burn-down: result `NARROWED`; one PROVED node added, one critical target
tightened, no status weakened, no assumptions added. Upstream open PR #1151
still supplies the structural chart for the retained cells but no aggregate
payment, so the next positive target remains the guarded split-divisor count
on the now substantially smaller scale range.
