# M_B vs f1-ledger comparison at the KoalaBear-shaped row (2026-07-07)

The gating pre-PR audit item from CIRCLE_SCOPE_AUDIT.md §3: do our
f1/tower per-level denominators reproduce the magnitudes of upstream's
PROVED subfield census floors M_B(d1) at a KoalaBear-shaped official
row? Replay scripts: `mb_audit.py`, `mb_exact_margin.py` (this dir;
local, exact integer arithmetic + lgamma cross-check, seconds).

VERDICT IN FIVE LINES:
1. WELD CONFIRMED — their floor IS our tangent column's base-field mean
   (proved one-line identity; replayed to every printed digit).
2. CROSS-PREDICTION (exact) — their published KoalaBear list adjacent
   pair a0 = 1116047/1116048 AND its 22.011-bit margin are exactly the
   crossing of our base tangent mean through the F-row gate.
3. Tower depth at KoalaBear-shaped rows = ONE level (levels p^2, p^3,
   p^6 dead by ~2.09M/4.18M/10.45M bits).
4. ONE REAL FINDING (catch #11, against us): F2 EXTRAS-BUDGET's frozen
   sub-balance window `q^t >= 2^n` is mis-normalized at base-domain
   extension rows — the KoalaBear row itself passes the q-window while
   the true (base-field) value space is above balance by 2^1,740,627.
   Fix: beta-normalize the window to the generated field.
5. No other floor's evidence or statement is touched; the f1/ext
   descent is the architectural shield and now has a proved numeric
   seam-weld behind it.

## 1. The two statements

UPSTREAM (Paper D v13, prop:capg-census-floor, PROVED there): at a row
RS[F, D, K] with D ⊆ B (base field), |D| = n, p = |B|, q = |F|,
agreement m, w' = m−K, interior profile w'+1 ≤ d1 ≤ floor((n−K+1)/2),
m' := K−1+d1: the level-m' identity-prefix witness word has size-m
census at the heaviest prefix at least

    M_B(d1) = C(m', m) · ceil( C(n, m') · p^−(d1−1) )

(part (a): boundary d1 = w'+1 gives Cen ≥ ceil(C(n,m) p^−w')). Their
printed deployed-row violations: 67.1 bits (KoalaBear boundary), 56.0 /
43.9 / 31.3 (interior d1 = w'+2..w'+4); 52.1 / 41.0 / 28.9 / 16.2
(Mersenne-31). NB their printed interior values are the UNCLAMPED
products (the ceiling only strengthens them).

OURS (s6_extension_lift.md + f1_case_tower, PROVED assembly): F-valued
bad-slope mass at non-generating rows is trichotomized; B-rational mass
(case i) is priced by the BASE ledgers (denominator p natively);
tower-confined mass (case iii) by per-level ledgers with denominators
q_K = p^d printed per level; genuinely-F mass forces the pole mechanism
(f1_full_field_pole_forcing) priced by the imported list term.

## 2. THE WELD (proved identity)

m' = K−1+d1  ⟺  d1−1 = m'−K, hence

    p^−(d1−1) = p^(K−m')   and so
    M_B(d1) = C(m', m) · ceil( C(n, m') · p^(K−m') )
            = C(m', m) · ceil( E_tan^B(m') ),

where E_tan^B(m') = C(n,m')·p^(K−m') is exactly the MEAN of our tangent
column at the BASE field: the expected number of base codewords (p^K of
them, each hitting a fixed m'-set with probability p^−m') at agreement
m', each spraying C(m',m) size-m supports (the binomial-moment
bookkeeping both programs share — their prop:capfr1-lattice-census(c),
our tangent-column convention). Their floors say "some word achieves
the tangent mean" (pigeonhole over prefixes); our B_tan column budgets
the mean with slack. SAME OBJECT, SAME NORMALIZATION. Their
identity-prefix witnesses are, in our dictionary, tangent-column mass
routed by f1 case (i) to the base ledger — never "extras", never
challenger-remainder mass.

## 3. Replay (all eight printed values reproduced)

Row parameters confirmed: n = 2^21, K = 2^20, KoalaBear p = 2^31−2^24+1
(log2 p = 30.9887), their deployed list agreement m = 1116046; M31
p = 2^31−1, m = 1116022.

    KoalaBear:  67.1  56.0  43.9  31.3   (upstream: 67.1 56.0 43.9 31.3)
    M31:        52.1  41.0  28.9  16.2   (upstream: 52.1 41.0 28.9 16.2)

Boundary values verified with exact integers (bit-length arithmetic):
67.10, 52.11.

## 4. Cross-prediction: their adjacent pair from our column arithmetic

F-row gate = q·2^−128, log2 = 6·log2(p) − 128 = 57.9321. Exact-integer
sweep of the base tangent mean E_tan^B(m) = C(n,m)·p^(K−m) across their
crossing:

    m = 1116045:  98.27   (+40.34 above gate)
    m = 1116046:  67.10   ( +9.16 above gate)   <- their a0 − 1 (unsafe side)
    m = 1116047:  35.92   (−22.011 below gate)  <- their a0 (safe side)
    m = 1116048:   4.75   (−53.19)

Their published KoalaBear list pair is 1116047/1116048 with margin
22.011 bits. Our computed safe-side gap at 1116047 is 22.0109 — every
printed digit. So: their a0 = min{m : E_tan^B(m) < q·2^−128}, and their
margin IS the gap. The finite list-row program at KoalaBear and our
tangent-column arithmetic are the same integers. (What remains
genuinely theirs: the EXTREMALITY claim that nothing beats this floor —
mode-at-null/Q. What remains genuinely ours: the budget floors for the
non-witness residuals.) The MCA-row margin 22.197 differs by a gate
convention on the MCA side — not chased here; the list-row match is
exact and banked. This discharges the "cross-predict their a0"
half of pre-PR work item 2.

## 5. Per-level tower table (our f1_case_tower denominators)

M_{p^d}(d1) at the KoalaBear row, levels d | 6 (bits):

    d1 = w'+1:   d=1: +67.1   d=2: −2,090,740   d=3: −4,181,546   d=6: −10,453,966
    d1 = w'+2:   d=1: +56.0   d=2: −2,090,782   d=3: −4,181,619   d=6: −10,454,132

The seam is ONE level deep at KoalaBear-shaped rows: only the base
level carries mass; our per-level columns at p^2/p^3 are guard columns
there (correctly priced, vacuously); the q-scale (d = 6) model is
refuted as a GLOBAL normalizer exactly as upstream printed for their
own census problems ("as stated, all three problems are therefore
refuted") — and our architecture never applies q-denominators to
B-rational mass (f1 case-(i) routing + f1_full_field_pole_forcing).

## 6. THE FINDING (catch #11): F2's window is mis-normalized at
##    base-domain extension rows

F2 EXTRAS-BUDGET as frozen: "at rows with q^t ≥ 2^n (sub-balance
everywhere; all official prize-max rows qualify by ~2%): non-coset
t-null extras ≤ n³."

At the KoalaBear-shaped OFFICIAL row (n = 2^21 | 2^24 | p−1, so the
unique order-n subgroup H of the cyclic F* lies in F_p*; D = h·H):

- PROVED (one line): power sums of S ⊆ D satisfy p_j(S) = h^j·σ_j with
  σ_j ∈ F_p — the t-null value space has size p^t, NOT q^t, at every
  coset rep h (scaling conjugacy; wild_row_audit's convention).
- The q-scale window ADMITS the row: t ≥ ceil(n/log2 q) = 11280 gives
  t·log2 q = 2,097,314 ≥ n = 2,097,152 (by 0.008%; with the statement's
  ~2% margin, t = 11505).
- The TRUE value scale fails catastrophically: t·log2 p = 356,525 —
  above balance by a factor 2^1,740,627.
- PROVED (pigeonhole): some depth-t prefix fiber contains at least
  C(n, n/2)/p^t = 2^1,740,616 blocks; coset unions number ≤ 2^(n/t) =
  2^182 — that fiber is overwhelmingly non-coset. Transported budget:
  n³ = 2^63.
- Honest grading: the pigeonhole lands on SOME prefix z, not z = 0
  specifically; the t-null (z = 0) instantiation rests on the verified
  above-balance witness pattern (our p = 97 giant-block family; their
  window populations) and upstream's mode-at-null calibration. But the
  window's JUSTIFICATION ("sub-balance by ~2%") is proved FALSE at the
  true value scale, and the window exists precisely to exclude
  above-balance accident regimes. The frozen wording is untenable.

THE FIX (beta-normalization, mirroring upstream's own printed
corrections): the window condition must be stated at the GENERATED
field B0 = F_p(D):

    |B0|^t ≥ 2^n     (identical to q^t ≥ 2^n at generating rows,
                      where every hardening census ran — B0 = F there;
                      excludes base-domain extension rows, which the
                      f1/ext descent prices at the base row instead).

The hardening evidence (three attack families + Pro window, all at
prime rows) is untouched. The consumer (x4 via b2_modp_giant_extras)
must consume F2 only at generated-field-window rows; non-generating
rows route through f1/ext (s6: the imported list window binds there).
DAG statement patched 2026-07-07 accordingly.

## 7. Sibling-floor scope check (same lens, one line each)

- F1 B-WEAK: the q^(−t+H) normalization and W_cen live in the dli lane
  whose windows are lane-internal; FLAG for the same beta-check
  (follow-up question printed: is W_cen a point-count over F or over
  the generated field at extension rows?). Not resolved here.
- F3 n³-COLUMN / F5 16n³-SPREAD: post-strip remainder columns; the M_B
  population is tangent-column mass, stripped BEFORE these columns see
  the word. Not exposed.
- F4 PETAL: top-band structure at official-like rows; petal objects are
  support-combinatorial (field enters through realization counts);
  FLAG-lite: verify realization denominators at extension rows when the
  petal lane next runs.
- F6 BAND-DETERMINATION: first-moment determination per row; at
  extension rows the first moments must use the generated-field
  denominators for base-confined strata — same beta-rule, INHERITED
  from wherever the moment tables are computed; flag noted in-lane.
- F7 ROWWISE-ENVELOPE: count law ~ K_cell/q^σ with all evidence at
  prime q (97..1153); the envelope's official-convention quantifier
  should carry the same generated-field reading. FLAG (statement-level,
  no evidence contradiction).

## 8. Consequence for the correspondence PR

The PR can now state, with replayable exact arithmetic: (i) their
proved M_B floors and our tangent column are the same object at the
same normalization (weld identity); (ii) their headline KoalaBear list
pair location and margin are reproduced by our column arithmetic to
every printed digit (cross-prediction); (iii) the beta-normalization
lesson their floors taught their own census models applies verbatim to
one of our seven floors' window wording, and we applied it (catch #11 —
found by this audit before a referee did). Items (1) M_B comparison and
the a0 half of (2) regime map from THREE_VS_SEVEN.md's work list are
DISCHARGED.
