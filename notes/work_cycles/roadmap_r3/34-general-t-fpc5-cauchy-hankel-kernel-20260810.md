### 2026-08-10 general-t FPC5 Cauchy-Hankel kernel

The new PROVED node `l1_fpc5_tpetal_cauchy_hankel_kernel` converts the
owner-free weighted moments into the canonical coefficient-space object.
With

```text
mu_s=sum_(z in T)c(z)z^s/Lambda'(z),
```

the low-numerator equations on `G=sum g_a X^a` are

```text
sum_a mu_(j+a)g_a=0,       0<=j<h-d-1.
```

This is a full-row-rank Hankel block whenever the cell has its saturated
primitive anchor. Its generating function is `chi/Lambda` at infinity, so
the moments obey the exact `Lambda` recurrence. Split candidates are monic
degree-`d` core divisors in this kernel; primitivity is nonvanishing of the
punctured first-row pairing at every selected root, and the background
Cauchy guards remain explicit.

No critical status changes. The live local theorem is now a
base-field-normalized split-divisor census for a full-rank rational
Padé-Hankel kernel with primitive punctures and background guards, followed
by chronology-valid aggregation. Export to `rs-mca` PR #1151 is pending.
