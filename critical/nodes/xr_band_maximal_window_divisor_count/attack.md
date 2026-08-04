# Attack Plan

## Exact Currency

Count maximal selected locators `R_d`, never all divisors in the affine
window intersection. Record the reconstructed pair, its full agreement
set, selected supports, live slopes, and strip classification for every
candidate family.

## Exact rank split

The monolithic residual has been replaced by two exhaustive targets:

```text
rank J_d=2d
  -> xr_band_fullrank_window_divisor_count,
rank J_d<2d, restricted to pairs whose every selected off-core block
lies in the active residual support D, with |D|>=2(h-d)
  -> xr_band_forced_commonroot_syzygy_count.
```

The proved active-defect router handles the outside-`D` part of every
deficient system with `N_d^out<=n-|D|`; the red leaf receives
the exact complementary budget. Do not recombine the full-rank and
deficient targets by summing their budgets: they are alternative states
of the fixed depth matrix.

## Route 1: arithmetic inverse theorem

Show that more than `17n^2/25` maximal selected locators force a common
cyclotomic divisor pattern or a low-complexity residue-class support.
The conclusion must be one of the classes already removed by P3,
BP parity, or liveness L. A statement about raw locators is insufficient.

## Route 2: maximal-fiber compression

Use the fiber identity

```text
RAW_d^Pi = sum_{e>=d} MAX_e^Pi binom(k+e,k+d)
```

with `Pi` equal to maximal selected liveness plus strip survival. The proved
predicate-filtered inversion gives

```text
MAX_d^Pi=sum_{j>=0}(-1)^j binom(k+d+j,k+d) RAW_(d+j)^Pi,
S_(2a+1)^Pi(d)<=MAX_d^Pi<=S_(2a)^Pi(d).
```

Seek a polynomial, energy, or incidence bound on one even signed truncation.
The predicate must be evaluated on the reconstructed maximal pair and hence
is constant on each fiber. Do not substitute unrelated upper bounds for all
raw moments: the negative terms make that inference invalid.

## Route 3: joint row-space transversality

The two single-word Toeplitz systems each have rank `d`, but their
stacked rank need not be `2d`. The proved
`xr_joint_window_rank_syzygy_router` identifies every deficient case
with a genuinely two-sided, nonproportional Padé syzygy across
the complete syndrome window. Classify these rational directions. A
useful theorem would show that intersection dimension above a stated
threshold forces quotient periodicity or another paid strip. The
complementary full-rank stratum is a pure arithmetic divisor problem.

## Route 4: bounded falsification

Search toy rows for maximal selected families, stratified by stacked
rank and residue support. Computation can discover a construction or
calibrate an inverse theorem, but toy survival cannot prove the prize
row bound. Use Modal for any nontrivial enumeration and retain partial
checkpoints.

## No-Go Fences

- Raw affine-divisor counts are refuted as the target currency.
- First-moment margins are average-case evidence, not a uniform bound.
- Packing by `k`-subsets is exponentially too weak.
- The two single-word ranks do not add without a transversality proof.
- A deficient joint rank is not arbitrary: consume the nonproportional Padé
  syzygy router before introducing another structural conjecture.
- Every deficient pair with a selected off-core point outside the active
  residual support `D` is already paid; only the all-selected-rays
  `D`-local family remains.
- "Aperiodic" must include mixed residue-class systems that evade P3.
