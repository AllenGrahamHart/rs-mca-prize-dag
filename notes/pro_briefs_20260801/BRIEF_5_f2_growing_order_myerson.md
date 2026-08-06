# Brief 5 — Myerson at growing order (F2)

**Node:** `critical/nodes/f2_growing_order_myerson/` · **status TARGET** ·
campaign capstone (F2 campaign, 84 logged entries) · **upstream:**
IDENTICAL object — the K2 "row-sharp Q atom" (`U_Q`, Sidon-Fourier
payment) in `experimental/grande_finale.tex` `sec:fourier` /
`sec:primitive-q-proof` of przchojecki/rs-mca, open there; the
identification chain is our PROVED `f2_zero_prefix_q_equivalence`
(zero-prefix instance, level `j < char q`); the pruned-vs-raw K2 gap is
OPEN on both sides.

## The mystery in one paragraph

For the Frobenius tower's moving sectors at official rows, the
Gaussian-period-norm census deviation (in the form of Habegger's eq. (2))
must obey a max-to-mean bound — at tolerance `2^(1.05e12)`, equivalently a
per-condition extras loss of at most `2^15` on the p-free ladder. This is a
**growing-subgroup-order** generalization of Myerson's conjecture on
Gaussian periods; every known result and the conjecture itself are
fixed-order. The tolerance is so weak it feels like it should be free —
and after an 84-entry campaign it still is not, because nothing in the
fixed-order literature survives the order growing with the field.

## Formal shape

At official rows, for the moving sectors of the Frobenius tower: the
period-norm census deviation obeys

```text
(max over conditions) <= 2^(1.05e12) * (mean),
equivalently: per-condition extras loss <= 2^15 on the p-free ladder.
```

The precise instrumented statement, ladder, and all constants: the F2
campaign record `notes/f2_campaign/` (entries 0-84; brief v3 is the
self-contained handoff document — start there). The pre-registered
extras-contraction falsifier has **never fired at any scale**.

Quality certificate:
`background/nodes/u2c_giant_tnull_dichotomy/notes/QUALITY_f2_growing_order_myerson.md`.

## History (what the campaign established)

- The identification chain to the upstream K2 atom is PROVED at the
  zero-prefix instance (`f2_zero_prefix_q_equivalence`) — the two projects
  are provably attacking the same object there. The wider pruned-atom
  identification is NOT proved (open gap; a conversion should not assume it).
- The floor campaign hardened the F2 floor against 3 attack families
  (0 deaths) and extracted two structural facts: the **structural constant
  700** and the **coprime-ideal obstruction** (campaign record).
- The standing flip campaign (`notes/f2_campaign/`, ladder L1-L5,
  pre-registered) has produced instruments but no flip; the campaign's own
  assessment calls the remaining entropic-suppression step "the deepest
  (dli-shaped)".
- An effective energy dichotomy for F2 was banked at the kernel summit
  (2026-07-09); its residual is exactly the low-energy/Fourier branch.

## Why it resists

Fixed-order Myerson results ride on the order being constant while the
field grows: the period polynomial's Galois theory is stable and
equidistribution comes from Deligne-type bounds with constants depending
on the order. Here the subgroup order grows with the row, so every
constant in that route blows up — while the claim needs only an absurdly
weak bound. The mismatch between how weak the target is and how completely
the standard route fails is the mystery.

## The conversion ask

1. **Sector case tree.** The moving sectors are finitely many per row, and
   official rows constrain the tower shape. Ask: an enumeration of sector
   classes (by order-growth regime relative to `p`, by tower level, by
   whether the sector meets the coprime-ideal obstruction) such that each
   class either (a) admits a fixed-order-style bound with explicit
   constants (bounded-order classes), or (b) is priced against the `2^15`
   extras budget by an exact census. The E1-ladder move applies verbatim:
   the tolerance is a budget; classes should pay into it, not each be
   uniformly small.
2. **The dichotomy route.** The banked energy dichotomy splits every
   instance into high-energy (paid) and low-energy/Fourier. Ask: does the
   low-energy branch, *at this tolerance*, reduce to finitely many
   character-sum cases decidable by exact computation per official row?
   A tolerance of `2^(1.05e12)` should forgive almost everything — a
   proposal that quantifies exactly *what* it cannot forgive (the true
   hard core, presumably a thin sector family) would itself be the
   conversion.
3. **Import check.** If any post-2024 literature touches growing-order
   Gaussian-period equidistribution (even with terrible constants), the
   identification chain makes it directly applicable at the zero-prefix
   instance. The 2026-07-27 literature sweep found nothing; a second
   sweep with fresh eyes is cheap and worth it.

**Sharpest question:** state the weakest hypothesis on subgroup-order
growth under which ANY nontrivial max-to-mean bound is provable, with
explicit constants. Even `2^(2^40)`-type constants beat the tolerance. If
that hypothesis excludes some official sectors, those become the case
list — and the board's machinery takes over.

## Guards

- Do not assume the pruned-vs-raw K2 identification (open on both sides).
- The falsifier discipline stands: the extras-contraction falsifier is
  pre-registered; proposals should state what would fire it.
- Constants explicit everywhere; "sufficiently large p" without a bound
  does not compose with official rows (which pin `p` families exactly).

> **[CORRECTION + ANSWER 2026-08-01 — from the Pro dossier, audited and
> accepted.]** (1) The "max-to-mean/period-norm" framing above (inherited
> from the node statement) is NOT the executable target: the magnitude
> theory is largely banked, and the live residue is the SIGNED WEIGHTED
> PARITY ALIGNMENT of epsilon_c = (-1)^(K_c+U_c) against exp(S_c) after
> corrected structural-drift subtraction. Exact fence: balanced signs with
> modulus max/mean 3/2 can still have normalized alignment sqrt(N/5) >
> 2^15 — sign-only and magnitude-only theorems are insufficient. A
> consumer-exact sibling (f2_weighted_parity_alignment) is endorsed,
> minted after the PP5.0 seam theorem. (2) Our sharpest question is
> ANSWERED: per-rung 2^(n_r/3) suffices under pessimistic log-additive
> composition (732,996,567,040 of the 1.05e12 bits; n_r/2 fails;
> theta* = 0.4775) — square-root cancellation may be unnecessary, pending
> the seam. One contraction bit per 43 moving coordinates clears the
> campaign proxy. (3) The requested literature re-sweep found one genuine
> post-sweep item (Cornelissen-Hokken-Ringeling, June 2026 revision):
> method lead only — its fixed-k error is vacuous at tower shape and it
> treats Mahler magnitude, not parity. See
> `responses/BRIEF5_PRO_DOSSIER.md` and `responses/BRIEF5_DOSSIER_AUDIT.md`.
