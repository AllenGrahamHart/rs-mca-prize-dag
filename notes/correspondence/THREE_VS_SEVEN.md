# Their 3 vs our 7: differential analysis (2026-07-07, pre-PR homework)

Upstream (v13 raw, przchojecki/rs-mca): conditional closure = Q + BC + SP
(prop:capg-final-active-package). Ours: prize CONDITIONAL on 7 hardened
floors. Both top-level deliverables are the SAME shape (adjacent-pair
staircase: our mca_grand/list_grand vs their cor:capg-adjacent-pairs).
The difference is the middle (assembly) and the leaves.

## Exact statements of their three

- **Q (prefix/quotient flatness):** max-fiber of the elementary-symmetric
  prefix map Phi_w(M) = ((-1)^j e_j(M))_j on m-subsets of D:
  max_z |Phi_w^{-1}(z)| <= kappa * C(n,m) * |B|^{-w}, kappa = n^{O(1)}
  (asymptotic) or explicit row constants (finite). Equivalent split:
  MODE-AT-NULL (N_w(z) <= N_w(0) for all z) + exact null-fiber ledger.
- **BC (split-pencil census):** divisor-pencil count of Lambda_D at
  interior balanced profiles <= e^{o(n)} * max(1, M_B(d1), C(n,w)q^{1-w'})
  where M_B(d1) is their PROVED subfield census floor. Community actively
  discharging BC into Q (PR #393: interior charts -> depth-(w+1) Q).
- **SP (primitive shift-pairs):** in their PROVED exact second-moment
  identity Sum_z N_w(z)^2 = C(n,m) + Sum_e P_e, bound the primitive part
  of sp_w(e; D') (pairs of monic D'-split polynomials, disjoint roots,
  top w+1 coefficients equal) by poly(n) * (pullback + diagonal).

## The structural difference (the headline)

THEIR route: prove the known unsafe construction (identity-prefix floor)
is EXTREMAL — one witness family's statistics are flat/mode-at-null; the
safe side follows because nothing beats the construction. OUR route:
budget every residual column of B_C <= B_tan+B_quot+B_ap+B_ext over ALL
received words at official rows. "Prove your construction is the worst"
vs "prove everything else fits its budget." Two different logical routes
to the same sandwich, with DIFFERENT hard kernels:
- their assembly has NO tower — it never meets our hardest object
  (B-WEAK's multi-level joint E_U[Pi rho]);
- our assembly has no mode-at-null — we never need pointwise extremality
  of a specific witness family (the exact statement-shape our window law
  says is dangerous: uniform quantifiers die, averages survive).

## The sharp bridge: F2 <-> Q (same mathematical object)

Our F2 t-null blocks ARE the null fibers of their prefix map (vanishing
power sums <-> vanishing elementary symmetrics via Newton, w < p): our
EXTRAS-BUDGET says #(Phi_t^{-1}(0) minus coset unions) <= n^3 at
sub-balance rows; their mode-at-null says the null fiber is the max;
their Q bounds it by kappa*C(n,m)p^{-t}. Composite: null fiber =
structured mass + small extras, and is the mode. EVIDENCE MESHES:
- their head-depth theorems (w <= 22 KoalaBear, +32394-bit margin;
  fibers = C(N,m)p^{-w}(1+eps) EXACTLY) prove the dense-regime analogue
  of F2 outright at shallow strata — actual theorems, stronger than our
  hardened-only status there;
- our sub-balance censuses (extras identically 0; structural constant
  700 = pure coset unions; coprime-ideal obstruction; complement
  involution) cover the sparse/Poisson regime their calibration flags as
  the danger zone (their max-to-mean grows at the Poisson boundary:
  4.10 at depth 3 (41,20,10); max 11 vs mean 2.7 Poisson tail) — our
  instruments say the z=0 fiber there is structured + zero extras.
- CAUTION: the two programs' windows sit at different (m, w) scalings
  (their deployed crossings in the ultra-dense bulk, mean ~ q/k; our
  official t=2 windows deep sub-balance). The regime geometry must be
  mapped before claiming any implication.
- RESOLVED 2026-07-07 (MB_VS_F1_LEDGER.md): the M_B seam audit ran.
  WELD PROVED (their floor = our base tangent-column mean, identity
  m'−K = d1−1); all eight printed floor values replayed; their
  KoalaBear list pair a0 = 1116047 and its 22.011-bit margin reproduced
  EXACTLY by our tangent mean vs F-row gate (exact integers); and their
  beta-correction transported one real fix back to us: F2's window is
  now generated-field-normalized (catch #11). Work items 1 and the a0
  half of 2 below are discharged.

## Mapping table with honesty grades

| theirs | ours | grade |
|---|---|---|
| Q (null fiber + mode) | F2 EXTRAS + F1 B-WEAK (average form) | STRONG (same object; uniform-vs-average form gap) |
| SP (primitive pair 2nd moment) | F3 n^3-COLUMN + F5 16n^3 (post-strip primitive pair control) | TEMPLATE-LEVEL (same "strip then bound primitive" shape; different objects: split-poly shift pairs vs aligned-support families) |
| BC (pencil census vs floor) | F7 ENVELOPE + F4 PETAL (census vs certified envelope) | TEMPLATE-LEVEL; BC is being discharged into Q upstream |
| finite adjacent-pair conjecture | F6 BAND-DETERMINATION | SHAPE-IDENTICAL ("true determination = model prediction at the transition") |
| entropy envelope g*(rho, beta) | (no closed-form delta* on our side) | theirs only |
| base-field beta-dependence + M_B floors | (our statements mostly at q; toys prime-field) | theirs only — OUR AUDIT DEBT |
| (tower/joint object) | F1 B-WEAK multi-level | ours only (their assembly avoids it) |
| (exact-list staircase column) | F3/x4 architecture | ours only (assembly-specific) |

Honest scoping: F3, F4, F5, F6 are residuals OF OUR ASSEMBLY (a different
assembly need not meet them — theirs doesn't); F1/F2/F7 are closest to
intrinsic objects. Symmetrically, mode-at-null is a residual of THEIR
assembly. The 3-vs-7 count measures factorization depth, not remaining
mathematics; trajectories: theirs -> 2 (BC->Q), ours -> 5 (F4/F5 leads).

## Strength/risk comparison

- Their FINITE forms are margin-critical: adjacent-pair margins 22.2,
  22.0, 3.3, 3.1 bits; "an unspecified n^C costs 21C bits" — three of
  four rows cannot absorb even n^1. Their own text: poly-loss Q closes
  ONLY the asymptotic frontier (reserve O(log n)); the printed pairs need
  (1+o(1)) constant-factor extremality. Sharper claim, higher risk.
- Our floors carry ~2^100 slacks by design (weakest-form): weaker
  per-statement content, far more attack-resistant (30 families, 0 kills).
- Their evidence style: proved head-depth theorems + Lean-checked integer
  staircase arithmetic + calibration censuses (labeled "enters no proof").
  Our style: pre-registered falsifiers + adversarial campaigns + replay.
  Complementary, graftable in both directions.

## Their falsifiability targets are OUR instrument fleet's home turf

Their pre-registered falsifiers: "super-polynomial primitive prefix
fiber" / "super-polynomial primitive split-pencil family," both
machine-checkable, both structurally identical to attacks we already run
(F2 engineered-accident hunts; F5 spread stacking). Running our fleet on
THEIR objects (esp. Q's dense-bulk prediction at primitive scales, and
SP's top stratum sp_w(w+1)) = arriving at the PR bearing evidence.

## Pre-PR work list

1. BASE-FIELD AUDIT of our 7 statements at extension-field official rows
   (which denominators are q vs p = |B|; check their PROVED M_B floor
   family classifies as structured/charged in our dictionaries — if any
   M_B population lands in an "extras" column of ours, the floor's
   statement needs the |B|-normalized correction BEFORE posting).
2. Regime map: place our official-row windows and their deployed
   crossings on the same (m, w, balance) chart; identify where the F2<->Q
   bridge is exact vs regime-shifted.
3. Falsification runs on their Q/SP falsifier objects at toy scales
   (our Modal fleet; pre-registered standards, their conventions).
4. Only then: the correspondence PR (map + evidence + no status claims
   about their conjectures beyond what our instruments measured).
