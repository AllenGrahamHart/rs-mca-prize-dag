# PREREG — commonroot_syzygy pilot (round 13, unfreeze)

- **node:** `xr_band_forced_commonroot_syzygy_count` (critical, TARGET)
- **date:** 2026-08-06
- **pilot dir:** `notes/pilots_20260804/commonroot_syzygy/`
- **status at open:** written BEFORE any code is run.

## 0. Correction to the tasking brief

The brief describes this leaf as a fresh wave-46 red needing a
gcd/resultant shared-root census. That framing is **stale**. Reading the
node shows the leaf has already been worked for a full coordinator
work-cycle and carries **15 PROVED supplier routers** in
`background/nodes/xr_deficient_window_*` plus
`xr_window_divisor_maximality_filter`. The gcd/resultant/Berlekamp-Massey
layer the brief proposes is already discharged upstream (LEMMA W /
THEOREM R in `xr_window_system_descent`, and the primitive Pade-pencil
router `xr_deficient_window_primitive_pade_pencil_router` which supplies
`K_d={(SP,SQ)}`, `gcd(P,Q)=1`). Re-deriving it would violate hard law 5
(subtraction). This pilot therefore attacks the **actual** open residual.

## 1. The obligation, verbatim

From `critical/nodes/xr_band_forced_commonroot_syzygy_count/statement.md`:

```text
25 |R_d^D(u,v)| <= 17 n^2 - 25(n-e).               (SL2-D)
```

The residual this pilot targets, verbatim from the same file (lines
125-130):

```text
For the exact packed block profile `(ell,ell,1)`, both blocks use four fixed
full members of the primitive pencil and two points from a tail of size
`t=e-4ell`. A finite plane census pays the next-dimensional exact-packed
stratum for every possible tail on all three rates. This is a stratum bound,
not an additive payment for a family mixing different fiber profiles or a
payment at higher affine dimensions.
```

and verbatim from the closing burn-down of the work cycle
(`notes/work_cycles/roadmap_r3/14-rate-half-20260730-20260803.md:5984-5986`):

```text
next: replace profile partitioning with one weighted two-block ledger that
      pays near-packed profiles, then determine whether the same block census
      can be iterated at higher affine dimensions
```

That is the obligation this pilot accepts: **one shared ledger for mixed
fiber profiles, replacing the profile-local allowance of (P4F4).**

## 2. Setting (all constants inherited, none re-derived)

The tuple-incidence obstruction boundary, from
`xr_deficient_window_packed_four_fiber_plane_payment`:

```text
ell = floor((h-4)/7),  r = 2ell+1,  d = h-r,  sigma = d-ell-1-2r,
e = |D| = 4ell+t,  2 <= t <= sigma+2,  N = n-e,  w = d+ell.
ROWS: (rates 1/4,1/8)  n = 2^41, h = 2^33+1, s = 11
      (rate  1/16)     n = 2^41, h = 2^32+1, s = 10
budget = (17 n^2 - 25(n-e)) / 25.
```

Consumed, never re-derived:
- `(CRE1)`: `N_(A_m)(x_0,...,x_m) <= m+1` — a fixed distinct-`phi`
  `(m+1)`-tuple in `D` lies in a selected block of at most `m+1` targets.
- `xr_deficient_window_two_block_kernel_slack_router`: when `sigma<r`,
  every target has **exactly two** selected blocks and they are **disjoint**
  `r`-subsets of `D`.
- `(FSP2)/(FSP3)`: block `phi`-fiber parts are `<= ell`; hence at
  `r = 2ell+1` every block has `v >= 3` distinct `phi` values.
- `(P4F4)`: `|Tau_pack| B_(s-2) <= 9t binom(N,s-2)`, i.e.
  `|Tau_pack| <= 9t prod_(j=0)^(s-3)(N-j) / prod_(j=3)^s (w+j)`.

## 3. Predictions

**P1 (WTB — the shared two-block ledger).** Let `Tau` be *any* `D`-local
target family at the boundary (arbitrary, possibly mixed, fiber profiles),
with affine hull dimension `s >= 2`. Let `Bset(Tau)` be the set of
*distinct* selected blocks realised anywhere in `Tau`. Then

```text
2 |Tau intersect plane| <= 3 |Bset(Tau)|,                      (WTB-plane)
|Tau| * prod_(j=3)^s (w+j) <= (3/2) |Bset(Tau)| * prod_(j=0)^(s-3)(N-j).
                                                               (WTB)
```

I predict `(WTB)` is provable by a single incidence double count
(`CRE1` at `m=2`, legal because every block has `v>=3`), and that it
reproduces `(P4F4)` **exactly** on substituting `|Bset| = 6t`. No profile
partitioning and no summed stratum-local allowances appear.

**P2 (exact block budget X).** Define

```text
X(row,s,t) = max { integer b : 3 b prod_(j=0)^(s-3)(N-j)
                               <= 2 budget prod_(j=3)^s (w+j) }.
```

I predict `X` is a small positive integer of order `10^2` (NOT of order
`ell ~ 10^9`), and `X >= 6t` exactly on every entry that the `(P4F4)`
table marks paid — `s=11, t=2..7` at rates `1/4,1/8` and `s=10, t=2,3`
at rate `1/16` — and `X < 6t` nowhere on those entries.

**P3 (census formula).** For a stratum with `D`-fiber profile
`mu=(mu_1,...,mu_p)` and an admissible set of block `phi`-profiles, the
number of realisable blocks is exactly

```text
|Bset| = sum over admissible fiber-assignments m of prod_i binom(mu_i, m_i),
```

subject to `sum_i m_i = r`, `0 <= m_i <= mu_i <= ell`, and the two-block
closure constraint `sum_i (mu_i - m_i - m'_i) = t-2` for the disjoint mate.
I predict brute-force subset enumeration at small `(e,r,ell)` reproduces
this count exactly.

**P4 (near-packed extension).** I predict `(WTB)` pays a strictly larger
stratum than `(P4F4)`: precisely those `(mu, profile-class)` strata whose
realisable-block count is `<= X`. In particular I predict it pays every
stratum in which each realised block is a union of full `D`-fibers plus at
most a bounded number of tail points, including profiles other than the
exact-packed `(ell,ell,1)` — so the mixed-profile family is genuinely
covered on a sub-stratum with one shared budget.

**P5 (no-go boundary — the honest half).** I predict the block-scarcity
route **cannot** be pushed to the whole boundary: if any realised block
splits a `D`-fiber `F` non-trivially (`0 < |B ∩ F| < |F|`), then
`|Bset| >= |F|`, so every stratum containing a split of a fiber of size
`> X` is provably unreachable by this ledger. Since fibers may have size
up to `ell ~ 1.2e9 >> X`, the residual after `(WTB)` is non-empty and I
predict I can name its exact boundary.

**P6 (higher affine dimensions).** I predict the ratio
`cap(s)/budget` is monotone in `s` over the range where `(WTB)` is
evaluated, so that the payable set of `s` is an interval, and I will
report its exact endpoints rather than claim `(WTB)` iterates upward
without limit.

## 4. Falsifiers (pre-registered; each kills the corresponding prediction)

**F1.** An incidence system in which every target owns exactly two blocks,
every block is owned by at most three targets, yet `2|Tau| > 3|Bset|`.
(Would kill `(WTB-plane)`.) Equivalently: a boundary block with `v <= 2`
distinct `phi` values at `r = 2ell+1`, which would void the `CRE1` step.

**F2.** `X(row,s,t) < 6t` at any `(s,t)` entry that `(P4F4)` marks paid.
(Would kill `P2` and expose an inconsistency between `(WTB)` and the
PROVED `(P4F4)`; in that case `(WTB)` is wrong, not `(P4F4)`.)

**F3.** A brute-force block count at small `(e,r,ell)` differing from the
`P3` product-of-binomials census. (Would kill `P3`.)

**F4.** A stratum with a non-trivially split `D`-fiber of size `> X` whose
realisable-block count is nevertheless `<= X`. (Would kill `P5` — and
would be *good* news, extending the route.)

**F5.** `X >= ell` at any official row. (Would kill `P5` outright and mean
the geometry route closes the whole boundary. I expect this to fail by
roughly eight orders of magnitude; if it holds, the leaf is much closer
to closed than the campaign believes.)

**F6.** `(WTB)` numerically exceeding `budget` at `|Bset| = 6t` on an
entry `(P4F4)` marks paid. (Consistency; would kill the whole ledger.)

## 5. Compute discipline

- Every run under `tools/ramguard tiny -- python3 ...` from the repo root,
  literal `--`. No bare `python3`. No Modal, no network.
- Exact integer arithmetic only (Python ints). No floats in any load-bearing
  comparison; floats only for printed diagnostics, clearly labelled.
- Brute-force calibration kept exhaustive and small: subset enumeration
  capped so that the enumerated space stays below `10^6` objects.
- If any run needs more than the `tiny` profile, that is a signal to
  redesign, not to raise the profile.

## 6. Subtraction notice

Before claiming novelty I will check the claim against: the 15 PROVED
`xr_deficient_window_*` nodes, `xr_window_divisor_maximality_filter`,
`xr_window_system_descent` (LEMMA W, THEOREM D/L/R), the parent
`xr_band_maximal_window_divisor_count`, and the sibling
`xr_band_fullrank_window_divisor_count`. `(WTB)` is claimed as a
*generalisation* of `(P4F4)`, and `(P4F4)` must fall out of it as the
`|Bset| = 6t` specialisation — if it does not, `(WTB)` is wrong.

## 7. Honesty declaration

This is a RED LEAF. A partial result with an exact boundary is the target
outcome. Anything labelled "empirical law" will be labelled as such and
never promoted to a proved statement. If `(WTB)` turns out to be a
one-line double count that merely re-packages `(P4F4)`, I will say so and
report the no-go half as the pilot's actual content.
