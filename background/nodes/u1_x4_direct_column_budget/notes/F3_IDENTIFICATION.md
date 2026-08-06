# F3 IDENTIFICATION (2026-07-07): trades = top shift-pair stratum —
# PROVED WELD (F2-grade); unconditional fiber cap; the flip honestly blocked

## 1. The identification (PROVED, two lines)

An F3 trade is an unordered pair of disjoint h-subsets P, Q of mu_n with
equal e_1..e_{h-1} (the instrument's signature; equal full signature is
impossible for disjoint pairs — equal locators force equal root sets).
Equal e_1..e_{h-1} for monic degree-h locators says exactly
ell_P - ell_Q = c, a NONZERO CONSTANT. Hence:

    F3 trades = sp_{h-1}(h; mu_n)/2  — upstream's TOP SHIFT-PAIR STRATUM
    (grande_finale thm:capg-second-moment top form (A, c): A, A-c both
    split, disjoint roots), the m = h instance of the second-moment
    ledger; "toral" = their quotient-pullback class (coset pairs,
    cf. prop:sp-pullback / thm:coeff-quotient-extract).

MACHINE CHECK (f3_identification_check_modal.py): DP_ordered =
2 x census_unordered AND toral split matches, digit-exact, at
(16,3,17): 704 = 2x352; (16,3,97): 32 = 2x16; (16,4,17): 252 = 2x126
(120 nontoral + 6 toral); (16,4,97): 12 = 2x6; (32,4,97): 792 = 2x396.
Plus two RETROACTIVE cross-instrument matches: the fleet's sp DP (built
for the upstream falsifier run) and F3's census (built for the floor
campaign) agreed before tonight without either knowing.

## 2. Unconditional fiber cap (PROVED — moving-root = sunflower)

For a fixed signature s = (e_1..e_{h-1}), the candidate locators form
the one-parameter pencil {A_s - c : c in F}. Upstream's PROVED
thm:bc-moving-root (each moving domain point kills at most one pencil
parameter — the SAME incidence argument as our f5_sunflower_pencil_lemma;
the two programs proved the same lemma independently) gives:

    max_z N_{h-1}(z) <= floor(n/h)   (split members of any pencil),

an unconditional shallow-Q instance (vs the trivial C(n,h)), whence
F3_unordered <= C(n,h) * (n/h - 1) / 2 unconditionally. Poly-below-
trivial; NOT n^3.

## 3. Why the conditional flip is BLOCKED (banked so nobody re-treads)

Their thm:q-implies-sp consumes Q in MAX-FIBER form: P_h <= (max - 1) *
C(n,h). At m = h this is hopelessly lossy: reaching n^3 needs
max <= 1 + n^3/C(n,h) ~ 1 at large rows. The premise F3 genuinely needs
is the COLLISION-CENSUS form Sum_z N(N-1) <= 2n^3 at q >= n^2 — which
under the identification IS F3 restated. A conditional close would be
circular. CONCLUSION: F3 does not amber through existing proved
reductions; it joins the kernel as a first-class PROVED WELD (same grade
as F2's t-null <-> null-fiber weld), and its resolution = the shallow-
depth sub-balance collision census — a clean, minimal kernel instance
(h <= 8, w <= 7, one-parameter pencils, fiber cap n/h already proved).

## 4. Consequences

- Kernel fan upgrade: F3 shape-candidate -> PROVED WELD. Three of four
  fan floors now have proved kernel identities (F2, F3, F5-stratum).
- Correspondence bonus: moving-root == sunflower-pencil (independent
  proofs of one lemma on both sides of the seam) joins the weld list.
- The 7->4 path clarifies: F3's amber is not available by transport; all
  roads lead to attacking the kernel's collision-census instances
  directly — the shallow F3 instance being the most attackable yet
  isolated.
