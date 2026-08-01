# Brief 3 — the high-core collision count (P-A1 / P-A2)

**Node:** `critical/nodes/xr_highcore_collision_count/` · **status TARGET** ·
**upstream:** OVERLAP with `prob:mca-spread-routing` in
`experimental/grande_finale.tex` (przchojecki/rs-mca, v4 of 2026-07-24,
open there; his moving-root theorem explicitly does NOT pay these clauses).

## The mystery in one paragraph

At each of the six clean-rate candidate rows, the number of "colliding"
live slopes after the strip phase should be cubically bounded: at most
`8n^3` slopes whose selected agreement support shares a size-`k` core with
another live member (generic branch, P-A1), and at most `16n^3` retained
support-mismatch slopes in total (non-generic branch with a joint
codeword-pair explanation, P-A2). These are *counting* statements about an
algebraically-defined slope family, the constants are frozen, extensive
partial structure exists — and the counting mechanism that yields `n^3`
does not.

## Formal pose

For every globally generic-branch received pair `(u,v)`:

```text
P-A1:  #{ post-strip live slopes whose selected agreement support
          shares a size-k core with another live member }  <=  8 n^3.
```

The count is on **distinct slopes** — not raw supports, and not the
W-collision second moment (see Guards).

For every received pair having a joint codeword-pair explanation on an
`A`-support, after removing only quotient slopes and genuinely
recovered-line tangent slopes:

```text
P-A2:  #{ retained support-mismatch slopes }  <=  16 n^3
```

with **one combined reserve** (no separate high/low `8n^3` split is
required). Dihedral-symmetric and extension-type slopes stay inside the
predicate allocation. Global joint `A`-proximity is a routing condition,
not a payment.

## Structure already proved (footholds)

- **Uniform-cell compiler, no collapsed exception:** at affine kernel rank
  `a`, any collapsed rank-two trade on active union `a+2` would force two
  active errors to share `(k-a)+(a+2) = k+2` zeros against the post-strip
  cap `k`; hence after quotienting regular Plucker face syzygies, every
  surviving rank-two trade has active union `>= a+3`. (In the node's
  statement; this removed the last exceptional face.)
- The canonical mismatch descent and the support-local LineRay charge are
  the recorded attack instruments for P-A2; genericity-based auxiliary
  charges apply to P-A1.
- A W-collision *moment* identity exists in the banked background (F5 P9),
  but converting a moment bound to a distinct-slope count loses exactly the
  factor the mystery hides in.

## Death ledger / guards

- **Do not count via the W-collision moment** — the node text pins the
  count to distinct slopes precisely because the moment route was tried
  and does not close (the moment controls multiplicity-weighted counts).
- Upstream's moving-root theorem does NOT pay P-A1/P-A2/P-B (crosswalk
  nonclaim, audited): it lives on arbitrary MDS kernel-ray charts, not
  proved pencils. Do not cite it as a payment.
- The `16n^3` constant is frozen (it absorbed a former separate
  mismatch-bridge obligation without change — see statement).

## The conversion ask

The cubic shape `n^3` begs for a three-index case enumeration. Concrete
candidate decompositions we have not completed:

1. **Rank-stratified cells (the compiler's own axis):** the uniform-cell
   compiler stratifies by affine kernel rank `a`; the `a+3` union bound is
   already a per-stratum structural theorem. Missing: a per-stratum count
   `c_a * n^(<=3)` with `sum_a c_a <= 8`, and a completeness theorem that
   post-strip live slopes are covered by the strata. If each stratum's
   count reduces to counting rational points on an explicit bounded-degree
   variety, this is an m2-style program (our exact-algebra fleet decides
   such cells routinely).
2. **Core-sharing graph:** the P-A1 predicate defines a graph on live
   slopes (edges = shared size-`k` core). The claim is a bound on
   non-isolated vertices. Is there a degeneracy/orientation argument —
   every edge charged to an explicit algebraic witness (a codeword pair, a
   Plucker face) of which there are at most `8n^3`? A complete witness
   enumeration = a case program.
3. **Per-rate reduction:** "six clean-rate candidates" is already a finite
   outer loop. If the inner statement can be made row-uniform (same
   argument, six instantiations), any case tree needs building once.

**Sharpest question:** exhibit a finite witness family `W` (explicit,
algebraic, `|W| <= 8n^3` provable by degree counting) and an injection
from colliding slopes into `W`. Every successful count in this project's
banked lanes ((a+3)-union, the packing nodes of brief 4) has this
witness-injection shape; nobody has written the witness family for P-A1.

## Pointers

- Node: `critical/nodes/xr_highcore_collision_count/` (statement + attack).
- Consumer chain: the xr pair feeds the spread/count layer of the
  proximity determination at the six clean rates (see
  `xr_smallcore_spread_count` and the node's `dependency_subdag.md`).
- Related banked instruments: F5 P9 W-collision identity (background),
  LineRay affine-core theorem, `xr_lowcore_near_k_difference_packing`.

> **[CORRECTION 2026-08-01 — from the Pro dossier's stress test, audited
> and accepted.]** (1) Route 1 as stated ("counting rational points on an
> explicit bounded-degree variety") is REFUTED: over a 256-bit admissible
> field even an affine line exceeds the 8n^3 budget by ~130 bits — every
> terminal cell must be empty, zero-dimensional with a q-free degree
> bound, or uniquely reconstructed from an n-indexed support key.
> (2) Route 2's core-sharing-graph half is REFUTED: a greedy induced
> matching produces 2^758 / 2^494 / 2^309 isolated two-slope components
> (d_C=0) satisfying every support-only condition on the RowC rows —
> support structure cannot bound component counts; RS realization is
> mandatory. The witness-charging half survives as the dossier's
> payment-key rule (q-free n-indexed keys with printed multiplicity).
> Also fenced: Maxwell surplus does not force rank two (F_5 span{I_3});
> the extension collision ledger is compatibility, not a count (2^134
> abstract records at the first RowC shell); and pathwise P-A2 laws do
> not control breadth (a 34-transition binary tree beats 16n^3). See
> `responses/BRIEF3_PRO_DOSSIER.md` and `responses/BRIEF3_DOSSIER_AUDIT.md`.
