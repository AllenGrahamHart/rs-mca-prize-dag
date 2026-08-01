# Brief 4 — the low-core spread heart (P-B)

**Node:** `critical/nodes/xr_lowcore_spread_heart/` · **status TARGET** ·
**consumer:** `xr_smallcore_spread_count` · **upstream:** OVERLAP
(low-core side of `prob:mca-spread-routing`, open, template-level only).

## The mystery in one paragraph

The dual of brief 3: bound the *spread* slopes — those whose selected
agreement support intersects every other selected support in at most `K-1`
coordinates — by `8n^3`. This is a Boolean additive-energy statement about
support indicators, and it is the single deepest unconverted question on
the board: unlike brief 3, here a genuine partial case program **already
exists and works** — it just runs out at a named frontier (cross-difference
aggregation), which is exactly where the conversion ask lives.

## Formal pose

For every globally generic-branch received pair `(u,v)`, with the
support-wise first-match post-strip selector, let `Gamma_lo` be the set of
live slopes whose selected agreement support intersects every other
selected agreement support in `<= K-1` coordinates (singletons included).

```text
P-B:   |Gamma_lo| <= 8 n^3.
```

Dihedral-symmetric and extension-type slopes remain inside the predicate
allocation. Pairs with a joint explanation on another `A`-support route to
P-A2's combined clause (brief 3) — they are not an extra obligation here.

## The partial case program that already works (read this first)

The width parameter `t` (of oriented shift fibers on support indicators)
already stratifies the problem, and the large-width half is DONE:

- **`t >= K`: closed.** Every oriented shift fiber of width `t >= K` has
  multiplicity at most one — proved, including the complete terminal
  Plotkin range on all six rows.
- **`h+1 <= t <= K-1`: the open middle.** For every repeated difference in
  this range, full-side locator division produces **two smaller globally
  generic P-B instances** with parameters `(N-2t, K-t, A-t)` and unchanged
  excess `h` — a genuine descent, proved. The resulting affine-rank bound
  pays the two boundary widths `K-1, K-2` per fixed difference.
- **First aggregate below `K`: banked.** `xr_lowcore_near_k_difference_packing`:
  at width `t = K-c`, residuals intersect in at most `c-1`, so disjoint
  ownership of their `c`-subsets gives an exact packing count — the first
  cross-difference aggregate.
- The all-LineRay affine-core theorem and covering-free charges pay all
  currently recorded low selector ranks in the generic scope.

**What remains open, precisely:** (i) cross-difference aggregation across
the middle range (the per-difference descent does not yet sum: differences
can share descent instances, and naive summation double-counts); (ii) the
descent's reduced dimensions `>= 3` (the recursion is only priced for the
two boundary widths per difference).

## Guards

- This is a **Boolean additive-energy split, not CAP25's local
  locator-SPI degree** (node text pins this; the CAP25 route was examined
  and is a different object — do not import its bounds).
- The selector (support-wise first-match post-strip) is normative; results
  for other selectors need a transport lemma.
- Joint-explanation pairs route to P-A2; proposals must not re-pay them.

## The conversion ask

This brief is the closest to done of the six: a descent + a packing
theorem exist, and the missing piece is an **aggregation combinatorics**
question that looks self-contained:

1. **Ownership scheme across differences.** The near-`K` packing node won
   by giving each residual a disjoint `c`-subset to own. Ask: a global
   ownership scheme for the whole middle range `h+1 <= t <= K-1` — each
   (difference, descent-instance) pair charged to an explicit witness with
   provably bounded multiplicity. If the witness multiplicity is `O(1)`
   with a named constant, P-B closes by summation over the (finite) width
   range. This is a finite combinatorial design problem, not analysis.
2. **Recursion pricing.** The descent `(N,K,A) -> (N-2t, K-t, A-t)` with
   fixed `h` terminates in `<= K/h`-ish steps. Ask: a potential function
   `Phi(N,K,A)` with `Phi` decreasing along descent and
   `|Gamma_lo| <= Phi <= 8n^3` at the roots. Even a candidate `Phi`
   validated on the six rows' exact parameters would let our fleet grind
   the inductive verification per width class (bounded exact computation —
   the same machinery as the K3 orbit deletions).
3. **Energy reformulation.** As a Boolean additive-energy split: the open
   middle is the energy of repeated differences in a window. Recent
   additive-combinatorics tooling (Plünnecke-type inequalities on
   indicator sumsets, Shkredov-style energy decompositions) has never been
   systematically tried here **under the exact-constants rule** — an
   energy bound with explicit constants on the window would convert
   directly.

**Sharpest question:** does the `c`-subset ownership of
`xr_lowcore_near_k_difference_packing` extend to a two-parameter ownership
`(c, difference)` with multiplicity `<= 2`? Our reading is that the sole
obstruction to closing the middle range is precisely the multiplicity
control when differences share residual geometry — a statement a fresh
combinatorial eye may recognize as a known design-theory lemma.

## Pointers

- Node: `critical/nodes/xr_lowcore_spread_heart/`.
- Banked neighbors: `xr_lowcore_near_k_difference_packing`,
  the LineRay affine-core theorem, `xr_smallcore_spread_count` (consumer).
- The six clean-rate rows' exact parameters: node `dependency_subdag.md`.
