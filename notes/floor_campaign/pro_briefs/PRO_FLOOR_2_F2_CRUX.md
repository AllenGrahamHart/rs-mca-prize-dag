# PRO BRIEF — the F2 crux (u2c extras / the shared census kernel at
# the zero prefix), in the DLI-CLOSE format
# (prepared 2026-07-10 from the F2 flip campaign, log entries 0-16;
#  every cited fact is banked with a digest in the prize DAG)

## The ask

Prove or refute ONE statement, presented in two equivalent faces
(equivalence PROVED, F2_ZERO_PREFIX_EQUIVALENCE_PASS):

FACE A (excess intersection). Let W_j in A^b be the complete
intersection p_1 = ... = p_j = 0 (power sums, regular sequence,
degree j!). The number of points of W_j with coordinates a b-subset
of mu_n (q prime, n | q-1) decomposes as a Bezout-proper part plus
excess supported on the ORBIT SUBLOCI (blocks of coordinates forming
scaled full mu_M-orbits, M > j — these lie in W_j identically and
their torsion points are exactly the coset-union blocks). CLAIM: the
excess is supported ONLY there, and the proper part contracts by
q/L per condition with L <= 2^15.

FACE B (zero-prefix Q). Equivalently (below char q): the number of
monic degree-b divisors of X^n - 1 whose top-j coefficients vanish
is struct^(j) (the exact coset-union census) plus extras^(j), with
extras^(j) <= (L/q) * extras^(j-1), L <= 2^15.

## Why L <= 2^15 flips the floor (banked tolerance chain)

Official rows: t*log2(q) ~ 2.15e12 > n ~ 1.1e12 (generated field,
beta-normalized), window empty at every b; budget n^3 = 2^123.
Extremes b <= min(t, q-1) ~ 2^31 are EMPTY (Newton lemma, banked,
char-corrected). Iterating the claim over the q-free ladder meets the
budget with ~2^{1.05e12} to spare.

## What is already proved (do not re-prove)

- Complementation, top-band rigidity, (t+1)-support rigidity, the
  giant-block closure; struct census exact at all measured cells.
- Newton empty-extremes (b <= min(t, q-1) empty; char-limited form).
- Chord-orbit lemma (exact Jacobi formula, per mu_n-orbit).
- Weil-Newton arc bound (|E_b| <= prod(2 sqrt q + r)/b!, uniform;
  zero reach at official F2 shape — do not attempt Fourier-absolute
  routes at mid-band, see the no-gos).
- Arc-class recursion (structured arc classes = order-1 censuses).
- O1-geometric (struct = torsion points of orbit loci; those loci
  are exactly the improper-intersection support).
- Zero-prefix Q equivalence (the two faces are one object).
- v13 shift-pair second-moment identity (exact SP strata; PROVED).

## No-gos (proved; do not walk these routes)

1. Raw Parseval/L2: N(0) <= sqrt(SP) is exponentially insufficient at
   the window peak. The value 0's specialness must be used.
2. Absolute-value Fourier at mid-band: the m = 1 anchor rows prove
   signed cancellation is astronomical (exact |E_b| = 1 vs partial
   products 2^93); float methods are structurally blind there.

## Empirical support (exact instruments, banked)

- Extras contract at L_x in [0.705, 1.278] (within 30% of flat) at
  every level of every measured row, reaching EXACTLY ZERO at deeper
  levels; the surviving census is 100% structured
  (F2_EXTRAS_FALSIFIER_PASS, 7 rows).
- Census L2-flat everywhere (M2/flat 0.91-1.17); no heavy nonzero
  fibers; the 0-fiber exactly structured at every cell.

## Pre-registered falsifier (immutable)

A row and level j where extras contract by strictly less than
q / 2^15, sustained at >= 3 field scales at matched (n, b, j). The
instrument (f2_extras_falsifier_modal.py) measures exactly this.

## Suggested attack surfaces (from the campaign, in order)

1. FACE A via Fulton excess intersection: the orbit subloci are
   explicit; compute their excess contribution and show the residual
   scheme meets successive torsion divisors properly. The (b,j) =
   (4,2) worked example is in the target brief.
2. FACE B via the v13 machinery: the zero prefix is a Q instance;
   the SP strata are exact; the missing piece is the 0-specialness
   (coset-union mass) separation inside the strata.
3. A splice: R4 Bezout covers the ladder through j ~ t/2 (loss
   log2 j!); any independent argument for the upper half completes.

Full technical spine: prize/notes/f2_campaign/EXTRAS_CONTRACTION_TARGET.md
Campaign log: prize/notes/f2_campaign/F2_CAMPAIGN_LOG.md (entries 0-16).
