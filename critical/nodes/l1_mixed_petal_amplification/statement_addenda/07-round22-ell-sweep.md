# Round-22 addendum (2026-08-07, coordinator-applied on replay): the ell-sweep executed — F-w1 exhaustively silent at the proper-band frontier; the falsifier normaliser AMENDED

Source: notes/pilots_20260807/l1_ell_sweep/ (gate ALL PASS
three-path with character-identical histograms; degen_word closed
form cross-checked against the full engine; coordinator-replayed).

**THE SWEEP** (L1-N10-ELL, executed locally beyond its brief):
n = 32 to ell = 5 — the deepest reachable PROPER-band cell
(t = 3, Lambda = 10, BOX = 1,606,481,810, exhaustive per word);
n = 24 to ell = 6; n = 64 at ell = 2, 3. The replication gate
reproduced every banked number of record exactly, including both
histograms at (64, 32, 193).

**F-w1 VERDICT: silent at all 14 cells** (max RET/(10*BOX/q) =
0.091), **and EXHAUSTIVELY silent at four cells** (n=24
ell=4,5,6; n=32 ell=5): the word-uniform upper bound UB(c) :=
#{S : g(S).c = 0} (g word-independent) was enumerated over the
ENTIRE legal word space (96 / 9,216 projective words); the only
flagged class — the constant-scalar words c = lambda*(1,..,1) —
was adjudicated exactly: RET = 0 PROVED whenever b <= 1 (U agrees
with the codeword lambda*L_C off the background, forcing
r <= b-1), and 0.0096 of threshold at the b = 2 cell (closed form
1,594,308, validated against the full engine at n=32 ell=3:
375,674 exact agreement). At those cells NO received word of the
chart family can fire F-w1 — the "search missed the max"
objection is closed there. F-w2: no contributor at
sigma > 2*ell+b-2 anywhere.

**THE LAW IN ELL** holds to 0.1% at the three largest cells
(BOX 1.4e8 / 4.1e8 / 1.6e9); worst schedule-word deviation
anywhere 3.1%. No amplification signal at any ell <= 6, n <= 64.

**F-w1 NORMALISER AMENDED (the re-pose of record changes in one
place):** 10*BOX(ell)/q LOOSENS as ell grows (deep shells swell;
N_{k+1}/BOX falls 0.826 -> 0.340 at n=32, making the threshold
2.9x more generous at ell=5 — in exactly the regime clause (b)
says carries the content). **F-w1 of record is now: retained >
10 * N_{k+1}(ell)/q**, the shell-resolved normaliser, against
which the measured law is FLAT: RET = (1-1/q)^{n-k-1} *
N_{k+1}/q to ~1% with no ell dependence (uniform ~11x headroom).
N_{k+1} has the same registered closed form.

**Scope notes:** (i) t = 2 cells (n=24 ell=5,6) have a VACUOUS
band (Lambda = k-1) and are not points on the floor-band curve —
measured, labelled, excluded from the curve. (ii) The off-family
band test: with the band DROPPED, exact-agreement semantics still
enforce sigma <= Lambda at the tested cells (measured max k+3 vs
formal ceiling k+11) — clause (a) is robust beyond its
definition; the band itself is a real 48.6x mass restriction.
(iii) Round-21's "~16% structural excess" of the minimal-degree
word is a COSET-LAYOUT ell=2 phenomenon (mu_2 antipodal petal
symmetry): 15.9%/17.4% at LAYOUT-B ell=2, 0.20% at LAYOUT-B
ell=4, <= 2% at LAYOUT-A everywhere — it does not grow with ell.
(iv) Round-21's d3_ell_sweep.py is UNSAFE outside b = 1 cells
(two failure modes; its unquoted n=16 ell=3 zero is wrong, true
100; NO banked number affected — see the coordinator note in
l1_pma_diag/).

**Clause (b) remains entirely open.** Under the measured law the
census regime (sigma = 1) and consumer regime (sigma = ell-1) are
separated by ~10^12 in log2 mass at official rows (driven by
q^{-sigma}); this says nothing about adversarial words, which is
the open content. Modal requests for the next reachable cells:
L1-N10-ELL-48-4 (n=48 q=97 ell=4, ~23 CPU-h, best value);
L1-N10-ELL-64-4 (n=64 q=193 ell=4, ~895 CPU-h);
L1-N10-ELL-64-5 out of scope (DO NOT LAUNCH, ~5e5 CPU-h/word).
