# Pro dossier — Brief 6 (rate_half_list_adjacent_crossing) — received 2026-08-01

> **Provenance:** GPT Pro response to
> `notes/pro_briefs_20260801/BRIEF_6_rate_half_list_adjacent_crossing.md`,
> relayed by the maintainer (same thread as Briefs 4, 1, 2). Pro audited our
> mirror at `52b59cba`. Companion script:
> `verify_brief6_rhl_adj_program_arithmetic.py` (this directory; replayed
> under ramguard 2026-08-01, full PASS — including exact-integer Johnson
> bisection at official scale and a live F_17 unsafe-certificate
> construction).
> **Fable audit:** `BRIEF6_DOSSIER_AUDIT.md` — read first.
> **The dossier's primary finding is now MINTED:**
> `rate_half_list_cyclic_budget_staircase` (PROVED, background).
> Planning document only otherwise — no other DAG status change.

## Executive decision (Pro's)

Fourth conversion target (after 4, 1, 2). Not because the gap is small —
the uniform unsafe point and the classical Johnson anchor are separated by
438,252,759,028 agreements — but because both frontiers are exact,
certificated, and independently movable.

## Two corrections (accepted; addendum in the brief)

1. **The literal (RHL-ADJ) display is trivially true.** `L_1` is
   integer-valued and nonincreasing with `L_1(n+1)=0`, so a least safe
   agreement exists by monotonicity. The open content is the
   **certificate-producing contract**: a row-computable `A(R)` with an
   independently checkable SAFE certificate at `A` and a same-received-word
   UNSAFE certificate at `A-1`. The claim contract should be amended to say
   so (Gate 0); the `B*=0` branch scope should be pinned at the same time.
2. **Bisection needs a TOTAL oracle.** Failure of an upper-bound method is
   UNKNOWN, never UNSAFE; a bisection whose unsafe branch is
   "Johnson didn't prove it" is unsound. 41 certified calls of a total
   `DECIDE_ROW` oracle locate the crossing — but totality is the theorem.

## The primary finding — the budget staircase (verified, minted)

Our own PROVED `rate_half_cyclic_rotated_prefix_floor` is fully
parameterized (`c | n/2`, `0<s<c`, `1<=d<=N/2-1`); at `d=1, s=c-1` it
yields SIX field-independent unsafe tiers:

```text
B* in [1,2]        : L_1(3n/4-1)  > B*      (Lambda(8)=3)
B* in [3,312]      : L_1(5n/8-1)  > B*      (Lambda(16)=313)
B* in [313,~2^23]  : L_1(9n/16-1) > B*      (Lambda(32)=8,286,954)
... two more tiers ...
B* up to 2^128     : L_1(k+2^34-1) > B*     (Lambda(256)>2^242)
```

The forward-facing bracket had recorded only the last, cap-uniform tier.
The staircase strictly raises the certified unsafe frontier `U(q)` on five
budget intervals — banked-theorem consequence, no new mathematics. A
`d>=2` fieldwise optimizer (exact binary search per scale, monotone
feasibility proved) is the PROVABLE strengthening behind it.

## Other verified content

- **Exact-integer Johnson ledger:** `a_IJ(B*)` with predecessor defects —
  B*=1,2,3 all anchor at `3n/4` with defects 1/3/2; the classical
  threshold is exactly `B_0 = 332,114,441,762`; at `B_0` the predecessor
  defect is a 77-bit integer `~ B*^2/sqrt(2)` — proving the finite-defect
  chamber method is intrinsically small-budget.
- **The defect identity (JD):** at `a_IJ - 1`, incidence imbalance +
  pairwise-agreement deficit = Delta_J exactly. At B*=3, Delta_J = 2:
  the whole predecessor geometry is finite BEFORE field algebra. Pro's
  independent coarse derivation gives 8 cells (6 multiplicity histograms x
  deficit-graph orbits 3/1/1), cross-checking our 13-chamber refinement.
- **B=3 is a two-sided decision problem:** chambers terminate in
  REALIZE (official-field witness => crossing at 3n/4) or EXCLUDE
  (uniform theorem) — and if all 13 exclude, the conclusion is
  `L_1(3n/4-1) <= 3` and the safe frontier DESCENDS (not a crossing).
  Solver failure is UNKNOWN, never EXCLUDE. The F_17 toy witness (built
  live in the replay) is a positive control that does NOT lift without a
  four-point transport theorem.
- **Route fences with exact constants:** packing dies at 127-vs-128 from
  full agreement; pairwise-only = Johnson in disguise (rank-flat/affine
  compilers already failed); average fibre bounds need max-fibre
  conversion; different-received-word families never add; 2^215 field
  census fence re-verified.
- **The global safe-side object:** the exact-shell complement-Toeplitz
  normal form (our banked L1 nodes) with first-owner shells summed
  cumulatively over `b >= a`; proposed RHL-STRUCT dichotomy
  (quotient/dihedral/low-cofactor/primitive owners + compatibility
  compiler + primitive profile envelope (PE1)). Per-family caps do NOT
  compose without a compatibility theorem.
- **Frontier accounting:** every theorem prices itself in
  `U(q)` (unsafe frontier up) / `S(q)` (safe frontier down); closure is
  `S = U + 1` per row.

## Program: PP6-SMALL (B=3 decision compiler, first research target) and
PP6-GLOBAL (exact-shell owner grammar -> primitive envelope), gates 0-9,
mutation battery, certificate schemas in the source dossier.

## Full text

Preserved at the maintainer's thread and session record; this summary +
audit + replay script + the minted staircase node are the load-bearing
extract.
