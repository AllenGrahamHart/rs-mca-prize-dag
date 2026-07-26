# LANE-L CROSSWALK — findings of record (2026-07-26)

Upstream read at origin/main = b13de811 (fetch confirmed; chain: fb6d9555 "Prioritize
post-Johnson RS list bounds" -> 5ecb9ab5 v3 synthesis -> f6a20fa3 v4 promote ->
07e6d0e7 wave 1071-1086 -> 78e67c40 "Integrate rate-half cyclic list floor" (co-author
AllenGrahamHart) -> b13de811 saturated-BC status fix).
Ours read at prize @ master c700cff8. READ-ONLY throughout; no GitHub writes.

## 1. Lane L contract (agents.md:174-198, verbatim semantics)

Goal: "a better ordinary Reed-Solomon list-size bound at a radius beyond the Johnson
radius". Output unit: codewords in ONE Hamming ball. Explicitly NOT MCA.
Routes: DIRECT_LIST / COMPUTATIONAL / indirect via open-proximity.tex Thm 5.2 (BCHKS25)
or Thm 5.3 (CS25) "with the theorem's radius shift, intrinsic-radius condition, and
C versus C^+ code shift printed explicitly".
Packet format: row / object / radius-agreement / Johnson comparison / bound / route /
CA_or_MCA_input / code_shift / status.
Johnson convention (extracted from his own integrated packet): Johnson agreement =
sqrt(n(k-1)); "strictly beyond Johnson" == a^2 < n(k-1) (agreement below the Johnson
agreement; radius above the Johnson radius).
Current state he records: (i) M31 conversion packet = conditional CS25 bridge +
BCHKS25 route cut; (ii) fixed-G endpoint Plotkin cap 2310492 (two M31 endpoint
subfamilies); (iii) OUR rate-half cyclic quotient-rotation floor
ceil(C(255,129)/256) at agreement 1116691496959. Open ask: "a broader unconditional
upper bound or a matching upper/lower bracket on a precisely declared family."

## 2. What 78e67c40 TOOK from our prefix floor (full diff read)

Took (into experimental/experiments.tex, new section
"Direct Lane L Result: a Rate-Half Cyclic List Floor", status PROVED/Direct-list):
- The GENERAL quotient-rotation theorem: C=RS[F_q,D,n/2], c|n/2, N=n/c, 1<=d<=N/2-1,
  m=N/2+d, 0<s<c: some word has >= ceil(C(N-1,m)/(N q^(d-1))) codewords at exact
  agreement n/2+dc+s. (General s IS included, hence s-independence of the count is
  implicitly taken.)
- The specialization n=2^41, c=2^33, N=256, d=1, m=129, s=c-1: agreement
  a = 2^40+2^34-1 = 1116691496959, bound ceil(C(255,129)/256) (243 bits, printed in
  full), Johnson check a^2 < 2^41(2^40-1), declared prime q_0 = 3*2^41+1 =
  6597069766657 with a Pocklington certificate, "exceeds q/2^128 for every q<2^256".
- Full Lane-L packet block: row/object/radius/Johnson/bound/route=Direct-list/
  no CA-MCA input/code shift C (no C^+)/status PROVED.
- Attribution: "integrates the mathematical content of AllenGrahamHart's PR #1051",
  source commit 0b339ebb pinned.

Did NOT take (untaken remainder):
1. The interleaved-arity sentence ("same lower bound for every constant common-support
   interleaving arity by diagonal repetition"). NOTE: not Lane-L object (ordinary only).
2. The reusable cap-uniform criterion (CR5) N q^d < 2^128 C(N-1,m) as a criterion, and
   the exact margin ledger (114.650300488 bits at q=2^256 for c=2^33 d=1;
   75.079624489 bits for the historical c=2^22 d=2048 instantiation) — he kept only
   the one-line "243 bits > 2^238" comparison for the chosen instance.
3. Residual-band propagation: unsafe (same 243-bit floor) at EVERY agreement k+sigma,
   1 <= sigma <= 2^34-1, by list monotonicity in the agreement.
4. The extremality remark (s=c-1 cap-uniform instances: c=2^33,d=1 is the unique
   largest agreement excess; our 74 extremality checks).
5. The historical c=2^22, sigma*=8,592,912,738 instantiation (superseded internally).
6. Our two Python replay scripts (explicitly "deliberately not imported").

## 3. Results-of-record v4 (proximity_prize_results_v4.tex @ b13de811) — list-side claims

- thm:saturation-finite: four length-512 shortened rows (k,a)=(256,351),(128,233),
  (64,143),(32,52) "strictly beyond the exact MDS Johnson radius" — MCA/safe-radius
  rows, not ordinary-list bounds (finite small rows; ChoShort26).
- Deployed unsafe floors table: "KoalaBear list 274975238687487221", "M31 list
  16776950" (row-sharp payments), M31 list contract at agreement 1116023, budget
  16777215 — Lane M territory.
- cor:abf "List consequences of CA/MCA bounds": (i) Thm 5.2 hypothesis -> |Lambda(C,delta)|<|F|;
  (ii) Thm 5.3 -> |Lambda(C+,delta)| <= ceil(|F|/(1-eta) * e_CA(C,delta));
  (iii) "In the quadratic staircase range, substituting the exact MCA numerator r+1
  gives the explicit integer consequences stated in [ChoThresholds26, 'Line decoding
  and list-decoding consequences']."  ==> THE INDIRECT ROUTE ON THE QUADRATIC
  STAIRCASE IS ALREADY TAKEN in the results-of-record, credited to his own paper.
- thm:m31-descent: CS25 bridge at M31 (CA numerator <=16777214 => list <=16777215 for
  RS(D,2^20+1)) — conditional, Lane M/L boundary, holmbuar+Danny territory.

## 4. Conversion theorems (open-proximity.tex, section 5)

- Thm 5.2 (BCHKS25): C=RS(F,L,k) rate rho, delta in (0,1-rho). If
  eps_ca(C, delta_fld = delta+2/n, delta_intr = 1-rho-1/n) < 1/(2n)
  then |Lambda(C,delta)| < |F|.  (Radius shift +2/n on the field radius; intrinsic
  radius pinned at 1-rho-1/n; no code shift; conclusion only < |F|.)
- Thm 5.3 (CS25): C=RS(k), C^+=RS(k+1). For delta in (0, dmin(C)), eta in [0,1): if
  eps_ca(C,delta) <= eta (1/k - n/(k|F|)) then
  |Lambda(C^+,delta)| <= ceil( |F|/(1-eta) * eps_ca(C,delta) ).
  (No radius shift; code shift C -> C^+ = RS(k+1).)

## 5. Racing PRs (all holmbuar, all OPEN, all on OUR row+agreement)

- #1097 "Rate-half ordinary list lower improvements" (2026-07-25 09:16): same row
  (F_q, k=2^40, n=2^41), same agreement 1116691496959. (a) Uniform refined constant
  (C(255,129)+C(127,64))/256 = 1109223...612835 (verified integer, replaces our
  ceil; delta = +4.68e34), (b) declared-q_0 lower ~10^126 at same agreement.
  Lean package. Status PROVED, LOCAL_ONLY. Explicitly builds on "the integrated
  cyclic quotient-rotation theorem" (= ours).
- #1099 "Rate-half ordinary list bracket" (07-25 10:37): same agreement. Upper bound
  floor(C(n,k)/C(a,k)) for every received word + c=2 quotient-rotation closed-form
  lower at q_0. => the "matching upper/lower bracket" Lane-L ask. Lean. PROVED.
- #1101 "Zero-remainder rate-half list scale" (07-25 12:25): s=0 boundary scale
  (outside our 0<s<c contract; c=1-type scale), L_1 with bits in
  [1466604010422, 1467447159516]; certified bit bracket for L_max(a) with endpoint
  ratio < 1.43; packing-only obstruction P_pair (bits >= 1923364445404) cutting any
  pure agreement-cardinality+pairwise-intersection route; states "the predecessor
  census of 33 legal dyadic scales remains true under its strict 0<s<c contract".
  Lean. PROVED, ROUTE_CUT.
- #1103/#1098/#1089: Lane L M31 side — fixed-G adjacent pair (5413,72860)/(840822,908269):
  Hahn/Delsarte relaxation exact optimum 20737821 unconditional cap, conditional
  16777214/16032481 under named hypotheses, complementarity identity route cuts.
  Entirely holmbuar's M31 program.
- #1104, #1102, #1088: Lane M (M31 at 2^-100, agreement 1116023) — not Lane L.
- #1090: v4 citation audit (K0). Others: M31 flatness/rank-7 (Lanes M/K).

## 6. Our candidate assets — verdicts with exact Johnson arithmetic

Row constants: n=2^41, k=2^40; n(k-1) = 2417851639227059326156800;
Johnson agreement floor(sqrt(n(k-1))) = 1554944255987 (a_IJ = 1554944255988);
Johnson radius = 644078999565.

(a) rate_half_cyclic_rotated_prefix_floor (PROVED, wave-9/10 audited, verify.py +
    verify_audit.py, margins 75.079624489 / 114.650300488 bits, 74 extremality checks):
    TAKEN at 78e67c40 (exact agreement 1116691496959, post-Johnson gap in agreement
    terms = 438252759028; radius 1082331758593 = Johnson radius + 438252759028).
    Untaken remainder: see section 2; of it, the constant refinement and scale census
    are RACED (#1097, #1101), the bracket ask is RACED (#1099, #1101); CLEAR remainder
    = interleaved-arity transport + band propagation + margin-ledger criterion, all
    minor and (interleaving) outside the Lane-L object definition.

(b) rate_half_list_adjacent_crossing / rate_half_list_low_budget_exact_crossing
    (PROVED for budgets B* in {1,2}: a_L(C) = 3n/4 exact, L_1(3n/4) <= B* < L_1(3n/4-1),
    explicit 2- and 3-codeword witnesses; all-arity transport PROVED):
    3n/4 = 1649267441664; (3n/4)^2 < n(k-1) is FALSE — 94323185677 agreements ABOVE
    the Johnson agreement. Radius 1/4 < 1 - sqrt(1/2). BELOW JOHNSON => DEAD for
    Lane L (both the exact crossing and its witnesses live inside the Johnson radius).
    Note: it IS a genuine exact adjacent-crossing theorem (Lane-adjacent value for the
    prize ledger, not for Lane L).

(c) The k+2^34 / sigma* = 8,592,912,738 band results: k+sigma* = 1108104540514 is
    post-Johnson (True) but the whole band is strictly SUPERSEDED by (a)'s
    1 <= sigma <= 2^34-1 reach (the historical c=2^22 instantiation is recorded as
    superseded in our own node). The only live content is the band-propagation
    sentence (untaken remainder item 3). No standalone packet.

(d) List corridor chain (list_unsafe PROVED / codegree PROVED / qcore PROVED /
    deep_point PROVED / list_safe CONDITIONAL on imgfib (itself CONDITIONAL)):
    The vendored nodes are stubs referencing the legacy proof_sketch/s7_list_side.md
    (NOT present in the prize repo; legacy repo not on disk among
    /home/u2470931/smooth-read-solomin/* candidates checked). No exact row/radius
    integers are printed in-tree; list_safe is conditional-on-conditional.
    NOT SUBMITTABLE as a Lane-L packet without re-deriving the exact window
    arithmetic; Johnson verdict undeterminable from the vendored text. HOLD.

(e) INDIRECT ROUTE — rate_half_quadratic_exact_range (PROVED, background):
    a_RH(q) = n - B + 1, B = floor(q/2^128), valid for 1 <= B <= B_Q = 389500552609
    (2^128 < q < ~2^166.5); exact numerator B at radius B-1 (i.e., numerator r+1 at
    radius r <= r_Q = 389500552608).
    Thm 5.2 push: condition eps < 1/(2n) holds trivially (q > 2nB always since
    2^128 > 2n); conclusion |Lambda(C, delta)| < q at delta = (B-3)/n — agreement
    n-B+3, radius <= B_Q-3. Thm 5.3 push: eta = Bk/(q-n) ~ 3.2e-27; conclusion
    |Lambda(RS(k+1), (B-1)/n)| <= ceil(B/(1-eta)) = B+1 (ceil lands one above B).
    JOHNSON VERDICT: deepest reachable agreement n-B_Q+1 = 1809522702944 =
    Johnson agreement + 254578446957 — INSIDE the Johnson radius by 254578446957
    agreements. Maximum radius reachable = B_Q-1 = 389500552608 vs Johnson radius
    644078999565: shortfall 254578446957. Even the far bracket (B <= 2^39+1, RQ2/RQ3)
    tops out at radius 2^39 = 549755813888, still 94323185677 short — indeed
    (n-k)/2 < Johnson radius for rate 1/2, so NO adjacent/sparse-range MCA
    determination can ever convert past Johnson on this row. And inside Johnson the
    conversion output (list <= B+1 ~ 2^38.5) is vastly weaker than the classical
    Johnson bound (~2.8 at that radius). DEAD twice over — AND the route is ALREADY
    TAKEN in general form as results-v4 cor:abf(iii) (ChoThresholds26 credited).
    This settles the never-before-evaluated question definitively: NO Lane-L
    deliverable exists on this route with currently proved MCA inputs.

(f) Other tree matches: rate_half_fixed_tail_prefix_floor (covers only q < 2^255.92;
    superseded by (a) — DON'T); rate_half_multiplicative_amplification_floor
    (dyadic-scale census F_e <= C(128,65), equality at e=34 — overlaps holmbuar's
    33-scale census + #1101 packing obstruction; internal 2^216 trigger, not Lane-L
    format — DON'T); rate_half_list_integer_johnson_safe_anchor (exact-integer
    Johnson bound itself — AT Johnson, not beyond — DON'T as Lane L; note it is
    already the (RHL-UB) machinery); x4_exactlist_staircase_split, tr_perleaf_list_ident,
    f1_pole_list_threshold_location, list_grand, list_adjacency_closing,
    list_large_m_scope_closure: all CONDITIONAL assemblies/reductions, no printed
    post-Johnson integer packet — DON'T; list_subsqrt_interleaving_collapse (PROVED:
    L <= L_m <= floor(L(q-1)/(q-L)) for 1<=L<q) — the proved bridge for the
    interleaving remark, not itself Lane L.

## 7. Ranked submittable packets

RANK 1 (the only live candidate; SMALL satellite, not a full Lane-L packet):
"Interleaved transport + band propagation addendum to the integrated floor"
  row: (F_q, D, k=2^40, n=2^41, rho=1/2), 2^41 | (q-1), D mult. coset of size 2^41
  object: ordinary LIST (band clause); common-support interleaved lists (transport
          clause, explicitly OUTSIDE the Lane-L unit and fenced as such)
  radius/agreement: every integer agreement a in [2^40+1, 2^40+2^34-1]
          (delta from (2^40-2^34+1)/2^41 up to (2^40-1)/2^41)
  Johnson comparison: every such a has a^2 < 2^41(2^40-1); at the top,
          gap = 1554944255987 - 1116691496959 = 438252759028 agreements
  bound: same integrated lower bound ceil(C(255,129)/256) (or #1097's refined
          constant if merged first) at EVERY agreement in the band, by monotonicity
          of L_1; plus: for every constant arity mu>=1 the same word/codewords
          repeated diagonally give the same lower bound for Lambda_mu, and
          L <= L_m <= floor(L(q-1)/(q-L)) (proved collapse) — no upper claim beyond it
  route: DIRECT_LIST (band) / DIRECT construction (interleaving)
  CA_or_MCA_input: none;  code_shift: C (no C^+);  status: PROVED
  (a) his-words consumer: agents.md Lane L "direct list-side proofs from the
      locator-prefix ... machinery"; experiments.tex sec. rate-half-cyclic-...-floor
      is the direct anchor to extend.
  (b) provenance: critical/nodes/rate_half_cyclic_rotated_prefix_floor (wave-9/10
      audited, verify.py + verify_audit.py) + critical/nodes/
      list_subsqrt_interleaving_collapse (PROVED).
  (c) overlap: 78e67c40 = anchor (band + interleaving NOT taken); #1097/#1099/#1101 =
      no collision (none states the band or any interleaved clause); v4 = silent.
  (d) fence: no upper bound; no MCA/CA claim; interleaved clause is not an
      ordinary-list claim; band bound does not improve at lower agreements.
  (e) effort: one afternoon (one tex subsection + tiny replay); LOW value-density —
      only worth bundling, not as a standalone race entry.

RANK 2 (optional, cosmetic): the margin-ledger criterion (CR5) + 74-check extremality
  ledger as an AUDIT satellite for the integrated section. RACED in spirit by
  holmbuar's 33-scale census (#1101 contract clause); submit only if his census PR
  is rejected. Effort trivial; value near zero while #1097/#1101 are open.

## 8. DON'T list

- Budget-1/2 exact crossings (3n/4): BELOW Johnson — dead for Lane L (valuable
  elsewhere; keep for the prize adjacency ledger, not this lane).
- Indirect MCA->list conversion of rate_half_quadratic_exact_range: lands inside
  Johnson (shortfall 254578446957), output dominated by Johnson bound, and the
  general form is already cor:abf(iii) upstream. TAKEN + DEAD.
- Historical sigma* = 8,592,912,738 band / fixed-tail floor (q<2^255.92): superseded
  by the integrated floor. DEAD.
- Constant refinements / brackets / other scales at agreement 1116691496959:
  RACED by #1097, #1099, #1101 (all Lean-certified, PROVED-labelled). Do not race.
- Multiplicative-amplification floor census: RACED (33-scale census + #1101
  obstruction), wrong format. DON'T.
- M31 fixed-G / Hahn territory (#1103/#1098/#1089): no banked asset of ours competes;
  stay out.
- Corridor chain (list_safe et al.): conditional-on-conditional, exact integers not
  in-tree. NOT READY — do not submit; if ever, requires re-deriving the window
  arithmetic first.
- Johnson safe anchor: it IS the Johnson bound (exact-integer form); not "beyond".
- Anything phrased as an MCA numerator: the workboard explicitly forbids claiming it
  as a list bound.

## 9. Top recommendation

ZERO new Lane-L race PRs now. Our flagship Lane-L asset is already integrated with
attribution (78e67c40) and its profitable neighborhood is being actively mined by
three open, Lean-certified holmbuar PRs that Przemek has not yet triaged. Every other
banked asset of ours is below Johnson, superseded, conditional, or already recorded
upstream (cor:abf(iii)). The only clear remainder (interleaving transport + band
propagation) is low-value and partly outside the lane's declared object; hold it
until #1097/#1099/#1101 are triaged, then — if Przemek integrates them — offer it as
one small follow-up addendum PR to the same experiments.tex section (Rank 1 packet),
citing his integrated section as anchor and #1097's refined constant if merged.
Sequencing: (1) wait for triage of the holmbuar trio; (2) single small addendum PR
(Rank 1) afterwards, at most; (3) redirect Lane-L energy to what the lane still
actually lacks and nobody has: an UNCONDITIONAL POST-JOHNSON UPPER bound on a
declared family — none of our current machinery supplies one (the proved staircase
cannot even reach the Johnson radius from the safe side; (n-k)/2 < Johnson radius),
so this is new-mathematics territory, not a packaging task.
