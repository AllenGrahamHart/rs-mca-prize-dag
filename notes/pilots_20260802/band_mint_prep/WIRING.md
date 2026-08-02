# WIRING proposal — the BAND LANE mint package (6 nodes)

Prepared 2026-08-02 by the band mint-prep pilot (Opus), mirroring the
completed norm-gate pattern
(`notes/pilots_20260802/norm_gate_mint_prep/drafts/`). **Nothing here has
been applied**: `dag.json`, `background/`, `critical/` and `tools/` are
untouched. Everything below is a proposal for the coordinator to audit,
adjust and wire.

All six nodes are **background** nodes, each with `statement.md`,
`proof.md`, `verify.py`. Destination paths (drafts to be moved as-is
after audit):

```text
drafts/xr_two_slope_cost_theorem/      ->  background/nodes/xr_two_slope_cost_theorem/
drafts/xr_two_slope_deficit_dichotomy/ ->  background/nodes/xr_two_slope_deficit_dichotomy/
drafts/xr_mc_depth_quantization/       ->  background/nodes/xr_mc_depth_quantization/
drafts/xr_band_key_lemma_pencil_mass/  ->  background/nodes/xr_band_key_lemma_pencil_mass/
drafts/xr_band_ledger_theorems/        ->  background/nodes/xr_band_ledger_theorems/
drafts/xr_support4_structure/          ->  background/nodes/xr_support4_structure/
```

After moving, `tools/run_all_verifiers.py` discovers `verify*.py` under
`background/nodes/**`, so `tools/verifier_manifest.json` must be
regenerated (six `verify.py` + twelve `statement.md`/`proof.md`
hashes). No Modal launcher needed; all six run under
`tools/ramguard tiny` — measured 0.14 / 0.41 / 2.38 / 1.35 / 1.87 /
0.12 s. None reads any file outside its own directory (pins inlined;
provenance paths in comments only), so they keep passing after the
move.

---

## 1. `xr_two_slope_cost_theorem`

```json
{
 "id": "xr_two_slope_cost_theorem",
 "title": "XR two-slope cost theorem: every admissible depth-d two-slope datum imposes condition rank EXACTLY 2h (independent of d, slopes over all of P^1 incl (0:1)); free-slope codim 2h-2; design ceiling in the per-ray accounting of record, datum counts binomial",
 "status": "PROVED",
 "closure": "proof",
 "statement": "RS_k on n distinct points of F_q, A = k+h, C_S the shortened dual (L1: dim C_S = |S|-k, dim(C_S ^ C_T) = max(0,|S^T|-k), proved inline). A depth-d two-slope datum (Z; z_1,S_1; z_2,S_2), |Z| = k+d, |S_j| = A, Z = S_1 ^ S_2, z_1 != z_2 in P^1(F_q), imposes on (u,v) the rows (C0) <c,u> = <c,v> = 0 for c in C_Z and (Cj) <c,u> + z_j<c,v> = 0 for c in C_{S_j}. LEMMA 0 (fibre identity, graded-band-ledger THEOREM 2, minted inline): two live slopes with |S_{z_1} ^ S_{z_2}| >= k force a pair P with S_{z_1} ^ S_{z_2} = Z_P EXACTLY, so the datum shape is what realized two-live-slope band pairs produce. THEOREM: (a) core rows are IMPLIED by ray rows, so R(P) = G_{z_1}(C_{S_1}) + G_{z_2}(C_{S_2}) -- the accounting object is the RAY SYSTEM (BAND_LANE_DEFINITIONS item 11); (b) dim R(P) = 2h for EVERY admissible datum, independent of d, including z in {0,(0:1)} (block-sum transversality via L1); (c) with slopes free the locus has codim 2h-2 (distinct slope pairs have distinct kernels). COROLLARY (design ceiling, per-ray accounting of record): RS_k x RS_k lies in every kernel, so realisability by a non-degenerate received pair forces rank <= 2(n-k)-1; per-RAY, rank <= Vh so V <= (2(n-k)-1)/h and datum counts are BINOMIAL, M <= C(V,2); per-DATUM (historic form) a prescribed-slope family with rank 2hM - delta has N_d = M <= (2(n-k)-1+delta)/(2h), free slopes /(2h-2). Six-row exact values: per-datum 153/179/319 (RowC), 191/223/479 (prize); free 191/223/479 (both); per-ray 307/358/639 / 383/447/959; prize d=1 point budget V* = floor((n-k+1)/(h-1)) = 192/224/480 with C(V*,2) = 18336/24976/114960 (the K_V re-pricing, ~10^22 inside 0.68n^2, margin >= 2.9e19). LOAD-BEARING correction kept: this is a FAMILY-RANK statement charged per ray, never per-datum-additive -- the per-pair reading mispredicts the sunflower (cycle: V rays, M = V, rank Vh, cost h) by exactly 2x and K_V (V rays, M = C(V,2), rank Vh, cost -> 2(d+1)) unboundedly; the banked 191/223/479 are RAY counts. NOT claimed: any occupancy bound (the lemma stays open); SHARP-OCC's strong law (REFUTED by K_V, 5.25x) or weak form n/2 (conjecture); sunflower extremality (REFUTED); core independence (NOT a law); M <= C(V,2) as an admissible-family cap beyond ray independence (= the support-4 gap); official-scale admissibility. Provenance notes/pilots_20260802/xr_occupancy_v2/ THEOREM 1 + corollary, corrected per notes/pilots_20260802/adv_sublinear_rank/ K2.",
 "refs": [
  "background/nodes/xr_two_slope_cost_theorem/statement.md",
  "background/nodes/xr_two_slope_cost_theorem/proof.md",
  "background/nodes/xr_two_slope_cost_theorem/verify.py"
 ]
}
```

## 2. `xr_two_slope_deficit_dichotomy`

```json
{
 "id": "xr_two_slope_deficit_dichotomy",
 "title": "XR two-slope deficit dichotomy: at 2d >= h no proportional differences and no live ray carries two depth-d cores (sunflower mechanism confined to d <= (h-1)/2); THEOREM G -- pairwise dual-rank sharing iff support overlap >= k+1, witnessed by a complementary-depth band pair",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Hypotheses: (H1) the banked k-packing (background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22, consumed not re-derived) and (H3) the tangent gate stated PENCIL-WIDE over P^1(F_q) INCLUDING (0:1); per BAND_LANE_DEFINITIONS item 5 the hypothesis line cites the generic core ceiling (item 4), never 'below cascade'. THEOREM 2 (low/high dichotomy): for 2d >= h, (a) no two distinct depth-d codeword pairs have proportional differences (conventions z* = 0 <=> f_1 = f_2, z* = (0:1) <=> g_1 = g_2) and (b) no ray of agreement <= A carries two distinct depth-d cores -- both through the single integer |Z_1 u Z_2| >= 2(k+d)-(k-1) = k+2d+1 >= A+1; hence the sunflower deficit mechanism ((k-1)-overlap forcing a shared slope) exists ONLY at d <= (h-1)/2. THEOREM G (sharing criterion): for rays (z_1,S_1) != (z_2,S_2) of agreement >= A, (i) dim(C_{S_1} ^ C_{S_2}) = max(0, |S_1 ^ S_2| - k) (L1); (ii) if z_1 != z_2 and |S_1 ^ S_2| >= k+1, the overlap IS -- exactly, by the fibre identity -- the joint agreement set of a codeword pair with BOTH slopes live: a two-slope band pair at depth e = |S_1^S_2| - k; (iii) two cores of depths d, e on one ray satisfy d + e <= h-1. Every unit of pairwise dual-rank sharing is witnessed by another band pair: the deficit structure is self-referential and graded. Plus: distinct cores are always transverse (C_Z ^ C_Z' = 0), so ray-support overlap is the ONLY pairwise sharing channel. NOT claimed: that pairwise sharing exhausts family deficits (support-4 relations exist -- xr_support4_structure; supports <= 3 are zero); any occupancy bound; sunflower extremality (refuted); Theorem 2 does not empty the high band -- it removes the sharing mechanisms there, so each high-depth pair pays its full 2h. Machine record: 371 cumulative witnessed sharing events, 0 violations (hunt_e0.json; per-shape increments 61/129/57/113/11); fresh verifier reproduces 39 witnessed events on fresh fixtures. Provenance notes/pilots_20260802/xr_occupancy_v2/ THEOREMs 2 and G.",
 "refs": [
  "background/nodes/xr_two_slope_deficit_dichotomy/statement.md",
  "background/nodes/xr_two_slope_deficit_dichotomy/proof.md",
  "background/nodes/xr_two_slope_deficit_dichotomy/verify.py"
 ]
}
```

## 3. `xr_mc_depth_quantization`

```json
{
 "id": "xr_mc_depth_quantization",
 "title": "XR MC depth quantization + THEOREM BP: MC-family band pairs are diagonal at depth exactly w; structured => d a power of two (BP1); parity excludes every band-proper depth at all six rows (BP3, preferred); slope-confinement trichotomy on the shift class (BP2)",
 "status": "PROVED",
 "closure": "proof",
 "statement": "MC word u = X^{n-1} + cX^{k+w-1} on H = x_0 mu_n, r' = n-k-w, family = unions T of m = r'/M cosets of mu_M with prod T = gamma (MC-1/2/3 consumed from xr_band_key_lemma_pencil_mass); shift pencil v = u/X^j, j <= M-1 (the unique class keeping the family joint; X^{M-1} | P_T). THEOREM 5 (quantization): distinct coset unions share <= r'-M points, so cross pairs (P_T, Q_{T'}) have joint agreement <= k+w-M <= k: the only MC-family band pairs are DIAGONAL (P_T,Q_T), depth exactly w; N_d = 0 at every band-proper depth (two shapes re-verified exhaustively; five in the pilot record). BP(1): a coset-union core complement with M = 2^ceil(log2 d) forces M | d, hence M = d: structured => d a POWER OF TWO; at the six rows (h odd) the unique 2-power in [ceil(h/2), h] is h-1, the upper band-proper window carries NO structured depth, excess h is not structured. BP(3) (parity, STRICTLY STRONGER, preferred per the occupancy-v2 REPORT's own deferral): on the shift class the direction map zeta_P(i) = -x_i^j has mu_g-coset fibres, g = gcd(j,n); a depth-d forced ray has agreement (k+d)+g, live iff g = h-d; at the six rows g is a 2-power and h odd makes h-d odd for every structured d >= 2, while d = 1 admits no shift: N_d^{coset} = 0 at EVERY band-proper depth -- the band proper is unreachable by coset constructions, F1 not fired by this class. BP(2) (trichotomy, scope = shift class): g < h-d invisible; g = h-d live with Gamma inside {-x^j : x in H}, |Gamma| <= n/(h-d), and exclusivity is automatic (g = h-d forces 2d >= h+1, then xr_two_slope_deficit_dichotomy T2(b)), so N_d <= n/(2(h-d)) -- LINEAR; g > h-d breaks the gate (T2/P2). The h-EVEN control (n=20, h=6, d=4, j=2: N_4 = 2, |Gamma| = 10 = n/(h-d)) shows the mechanism is REAL: official protection is PARITY, not impossibility. Cascade-tier population: at the prize rows w = M = h-1 is forced; the family sits AT the cascade tier with C(N,m)/N members; under SELECTED-support L_P (item 8) N_{h-1} <= n/2 (k-packing exclusivity); under 'any exact-A ray' it would be 2^130-2^197 -- the definition is load-bearing and pinned. NOT claimed: BP(2) beyond the shift class (general v UNPROVED); protection against non-coset families (char-p accidentals exist off-shape); MC-4 completeness beyond its char-0 scope (machine-checked empirically at one shape, q = 65537); that the MC pair reaches the generic branch (it is quotient-periodic, P3 fires first -- quotient-convention adjudication open, item 6); Gamma set claims at j >= 2 (refuted; cardinality |Gamma| <= n survives -- adv_gamma_minus_h amendment); any occupancy bound. Provenance notes/pilots_20260802/xr_occupancy_v2/ THEOREM 5 merged with notes/pilots_20260802/band_adjudication/ THEOREM BP (135 checks, 0 fails; fresh replication here matches the checkpoints exactly).",
 "refs": [
  "background/nodes/xr_mc_depth_quantization/statement.md",
  "background/nodes/xr_mc_depth_quantization/proof.md",
  "background/nodes/xr_mc_depth_quantization/verify.py"
 ]
}
```

## 4. `xr_band_key_lemma_pencil_mass`

```json
{
 "id": "xr_band_key_lemma_pencil_mass",
 "title": "XR pencil mass identity + KEY LEMMA (pencil support dichotomy, 'joint-explanation event') + the MC family construction with its unconditional ceiling and exact q-free count; no pencil exclusion",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Pencil w_z = u + zv on any n-point evaluation set D in F_q. THEOREM I (pencil mass identity): v nowhere zero => sum_{z in F_q} agr(c, w_z) = n for EVERY function c (fibres of (c-u)/v partition D); I' with zeros: = q e(c) + (n - |Z_v|). Corollaries: #{z in F_q : agr >= a} <= floor(n/a); 2a > n => the lists are PAIRWISE DISJOINT. KEY LEMMA (pencil support dichotomy): for |S| = a >= k the top a-k interpolant coefficients are LINEAR in the word, top(I_S(w_z)) = A(S) + zB(S); either A = B = 0 -- u|_S and v|_S are jointly explained by a codeword pair, a JOINT-EXPLANATION EVENT of size a (renamed from 'cascade event' per BAND_LANE_DEFINITIONS item 5) -- and ALL q+1 members' interpolants on S are codewords, or AT MOST ONE member of P^1 has a codeword with agreement set containing S. Graded consequence: distinct members share a common agreement a-set iff a joint-explanation event of size a exists; 'below cascade' (item 5) iff no shared agreement sets of size >= A-1. MC-1 (window classification, all w): codewords of u = X^{n-1}+cX^{k+w-1} at agreement >= k+w are EXACTLY {T : |T| = r', e_1..e_{w-1} = 0, prod T = gamma = (-1)^{r'+1}c}, injectively, agreement EXACTLY k+w. MC-2 (ceiling): nothing at >= k+w+1 (c != 0) -- the tangent gate holds UNCONDITIONALLY on MC words. MC-3: with M | n, M | r', w <= M, gcd(m,N) = 1, the coset-union family has EXACTLY C(N,m)/N members, q-FREE (coset vanishing polynomial in X^M; product condition = fixed subset-sum mod N, equidistributed by the unit shift). MC-5 (no pencil exclusion): every member of the shift pencil admits the ENTIRE family via P_T + zQ_T, so min over P^1 of L(w_z, k+w) >= C(N,m)/N. SUBTRACTION (hard law 5): the mechanism is banked -- e22_tail_coset_locator_algebra (the locator factorization IS the MC mechanism), rate_half_cyclic_rotated_prefix_floor (#1051; MC = its s=0,d=1 boundary with the q^{d-1} loss removed), crossing PK1 (w=2 shell; equidistribution = its Lemma 5); independently in BCHKS25 s.7 via sumset hypotheses, routed around unconditionally here. NEW: exact q-free count, ceiling at general w, pencil theorem, THEOREM I/I', KEY LEMMA. NOT claimed: ANY list bound -- the retired band-occupancy reduction must never be revived through this node (worst-case lists at tau are 2^130-2^197, all members simultaneously; the occupancy lemma itself is UNAFFECTED either way); I.3-type averaging (circular, and no poly(n) pencil trade-off law is true -- proved negative); MC-4 completeness (char-0, consumed by xr_mc_depth_quantization); the (R1) first-moment half (concentration not carried; MC is the certified half). NAMING FLAG: the mint brief cited xr_band_occupancy/ as source; the true source is notes/pilots_20260802/list_bound_transfer/ (7,792 checks, 0 failures) -- drafted from the true source.",
 "refs": [
  "background/nodes/xr_band_key_lemma_pencil_mass/statement.md",
  "background/nodes/xr_band_key_lemma_pencil_mass/proof.md",
  "background/nodes/xr_band_key_lemma_pencil_mass/verify.py"
 ]
}
```

## 5. `xr_band_ledger_theorems`

```json
{
 "id": "xr_band_ledger_theorems",
 "title": "XR band ledger theorems: line cap under J >= k (the applicable version), ray rigidity (rays not slopes), the interaction strip d_1+d_2 >= h => tangent event, two-column determinacy; master ledger with exact six-row pricing; Theorem 6 recorded as a WARNING",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Hypotheses: (H1) banked k-packing (xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22) + (H3) pencil-wide tangent gate; hypothesis line cites the generic core ceiling (BAND_LANE_DEFINITIONS item 4), never 'below cascade' (item 5); band column [1, h-1] with the cascade tier NAMED, at zero proof cost. T3 (line cap): a pair with |Z_P| = J >= k has L_P <= floor((n-J)/(A-J)) (disjoint off-core blocks); PRECISION: the banked common_code_line_budget prints this formula under a + b - n >= k, which is FALSE at all six rows -- the J >= k version is the one of record, strictly sharper than the F5 sunflower form (n-k)/(t-d); verified TIGHT at d = 1,2,3 and cap+1 point-count unrealisable. T4 (ray rigidity, keyed on RAYS): two distinct pairs with |Z| >= k are subordinate to at most ONE common ray, only via f_1-f_2 = -z(g_1-g_2), z unique; the slope-keyed reading is FALSE (re-selection freedom at 15/76 admissible fixtures -- occupancy-pilot correction; selection = first-match, item 7). T5 + COROLLARY (interaction strip): proportional differences make one codeword agree on all of Z_1 u Z_2, size >= k+d_1+d_2+1, so d_1+d_2 >= h forces a T2/P2 tangent event and the pair leaves the generic branch; overlap-(k-1) makes proportionality AUTOMATIC (the class strips itself; kills the shared-block doubling attack). T7 (two-column determinacy): the direction map zeta_P(i) -- centre-and-direction form for codeword PAIRS (the banked zeta_c is the g = 0 case); two distinct directions at a coordinate determine (u_i, v_i) and hence every other pair's direction: band occupancy becomes point-line incidence in A^2 (the designated lever, recorded as structure). MASTER LEDGER: |Gamma_band| <= SUM_d N_d L(d), L(d) = floor((R-d)/(h-d)); six-row pins recomputed exactly: band-proper SUM L(d) = 828/967/479 (RowC), 36839268578566/43010571891409/44764496190275 (prize); L(h-1) = n-A+1 EXACTLY (cascade separability); the printed n-A+1 column is exceeded on 5 of 6 rows even at N_d = 1 -- the band column must be a THIRD generic column from the 13n^3 headroom, never a B_tan enlargement (as ratified; xr_graded_tangent_band_charge). WARNING (Theorem 6, not a tool): per-ray band multiplicity = punctured-[A,k]-MDS list size at agreement k+1 (below Johnson, unbounded by anything banked); the master inequality is lossy generically but WORST-CASE TIGHT (slack 1.000 attained; exactly 2.000 on the max-N_d sunflower family -- verified here) -- slope-counting buys at most a factor 2. NOT claimed: any occupancy bound (the interleaving collapse is TRUE BUT VACUOUS -- do not cite as progress); Route-S impossibility (refuted); k-packing as new (banked, cited). SUPERSESSION FLAG recorded: the (unminted) band-occupancy unified fibre-strip Theorem 1 contains T4/T5's mechanism extended to z in {0,(0:1)} -- coordinator decision, see AUDIT_CHECKLIST. Provenance notes/pilots_20260802/xr_graded_band_ledger/ + the xr_band_occupancy amendment.",
 "refs": [
  "background/nodes/xr_band_ledger_theorems/statement.md",
  "background/nodes/xr_band_ledger_theorems/proof.md",
  "background/nodes/xr_band_ledger_theorems/verify.py"
 ]
}
```

## 6. `xr_support4_structure`

```json
{
 "id": "xr_support4_structure",
 "title": "XR support-4 structure theory: triple-locus localisation, the K_V no-relation THEOREM, rank-2 rigidity, the Mobius cross-ratio criterion, connectivity floor rank >= m (V <= m/2 => occupancy), escape floor; the U-mechanism as third calibration adversary; the zero-escape collapse MEASURED-not-proved",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Ray system (z_a, S_a), a = 1..V, distinct slopes in P^1, |S_a| = A; Rel = {(c_a) : sum e(z_a) (x) c_a = 0}; rank = Vh - dim Rel (per-ray accounting, item 11); supports <= 3 relations are zero (adv_sublinear_rank, consumed); triple gate (T): |S_a^S_b^S_c| <= k-1. S4-1 (localisation, PROVED): at every point a relation has 0 or >= 3 nonzero components (pairwise independence of e(z_a)); every relation lives on the TRIPLE LOCUS. S4-2' (PROVED): supports meeting the triple locus in <= k points carry NO relation (dual weight >= k+1); COROLLARY: the K_V family (triple locus = Y, |Y| = k-1) carries no relation and rank = Vh EXACTLY -- the banked measurement upgraded to a THEOREM. S4-3 (rank-2 rigidity, PROVED): a support-4 relation has all four duals in ONE 2-dim L, no two proportional (else quadruple intersection >= k+1 breaks (T)). S4-4 (Mobius criterion, PROVED): the relation exists iff CR(z_1..z_4) = CR(zeta_1..zeta_4) (Segre (1,1)-divisor condition), unique up to scalar, slope-codimension 1; minimal case |U| = k+2: L = C_U, zeta_y = x_y -- slopes must replicate the holes' evaluation points. S4-14 (connectivity floor, PROVED): MDS sum lemma + pairwise intersection >= k give pi_1(Row) = C_{union}, so m = |union S| - k <= rank <= 2m; the occupancy floor 2 holds AUTOMATICALLY whenever V <= m/2 (item 12). ESCAPE floor (PROVED, the min(h,.) cap load-bearing): rank >= sum_a min(h, |S_a \\ S_a^inf|) under peeling, dim Rel <= sum (|S_a^inf| - k)^+; 'every ray support has >= 2 points lying in at most two supports' => rank >= 2V => the occupancy per-ray charge 2 -- the purely combinatorial escape form of the heart. ZERO-ESCAPE COLLAPSE: MEASURED NOT PROVED -- zero-escape cliques measured at rank = 2m EXACTLY (every realisation a single joint explanation; 3876 + 8855 slope tuples, never 2m-1; 60 fresh tuples here), one of the two NAMED OPEN SUB-ITEMS (prove the collapse; prove V <= m/2 for non-collapsing systems -- all 9 families conform, Fisher gives only V <= k+m). U-MECHANISM (third standing calibration adversary, joining K_V and MC): |U| = k+2, holes y_a, gate SATURATED (triples exactly k-1), duals = minimum-weight e_{y_a} (weight k+1), Mobius-matched slopes give dim Rel = 1, deficit <= 1/ray (no stacking); toy pin rank = Vh - 1 = 19 at (3,5,1,4); RowC 1/4 d=1: U_N = 510 = 51 x C(5,2) vs K_V 384 (x 85/64 = 1.328125) against n/2 = 512 -- SHARP-OCC's weak form survives by a MARGIN OF 2 (sharpest calibration in the program); prize rows UNCHANGED (18336/24976/114960, point budget binds, deficit relative ~1e-10; cluster budget formula consistency-checked NOT re-derived). NOT claimed: the collapse as a theorem; V <= m/2 (conjecture); any occupancy bound (residual heart: an admissible non-collapsing pairwise-intersecting ray system with V > m/2); the double-hole family; D >= 2 pencil optimality. Provenance notes/pilots_20260802/support4_relation/ (301 checks + 4 measurements) on notes/pilots_20260802/adv_sublinear_rank/.",
 "refs": [
  "background/nodes/xr_support4_structure/statement.md",
  "background/nodes/xr_support4_structure/proof.md",
  "background/nodes/xr_support4_structure/verify.py"
 ]
}
```

---

## Proposed edges

### A. Internal `req` edges (all endpoints PROVED — green law holds)

| from | to | kind | justification |
|---|---|---|---|
| `xr_two_slope_cost_theorem` | `xr_two_slope_deficit_dichotomy` | `req` | Theorem G consumes L1 and Lemma 0 (fibre identity) verbatim |
| `xr_band_ledger_theorems` | `xr_two_slope_deficit_dichotomy` | `req` | Theorem 2(a) consumes the T5 union-agreement identity (recapped inline, cited) |
| `xr_two_slope_cost_theorem` | `xr_support4_structure` | `req` | L1 / dual-basis machinery consumed throughout |
| `xr_two_slope_deficit_dichotomy` | `xr_mc_depth_quantization` | `req` | BP(2)'s exclusivity: the live shift class forces `2d >= h+1`, then T2(b) gives one core per ray |
| `xr_band_key_lemma_pencil_mass` | `xr_mc_depth_quantization` | `req` | MC-1/2/3 (member exactness, ceiling, family) are the quantization's inputs |

### B. `req`/`ref` edges from banked nodes into the new six

| from | to | kind | justification |
|---|---|---|---|
| `xr_mismatch_chart_nongeneric_joint_support_equivalence` | `xr_two_slope_deficit_dichotomy` | `req` | (H1) k-packing, consumed |
| `xr_mismatch_chart_nongeneric_joint_support_equivalence` | `xr_band_ledger_theorems` | `req` | (H1), consumed |
| `xr_mismatch_chart_nongeneric_joint_support_equivalence` | `xr_support4_structure` | `req` | hypothesis (T) sources from the banked pair-core k-packing |
| `xr_mismatch_chart_nongeneric_joint_support_equivalence` | `xr_mc_depth_quantization` | `req` | Claim 5's cascade-tier exclusivity uses (H1) directly |
| `e22_tail_coset_locator_algebra` | `xr_band_key_lemma_pencil_mass` | `req` | `X^{M-1} \| P_T` (MC-5's shift class) and the locator-window mechanism are the banked factorization |
| `rate_half_cyclic_rotated_prefix_floor` | `xr_band_key_lemma_pencil_mass` | `ref` | attribution: MC is its `s=0, d=1` boundary case (not logically consumed) |
| `common_code_line_budget` | `xr_band_ledger_theorems` | `ref` | precision note only: same formula, inapplicable hypothesis at the six rows — attribution + differentiation, no dependency |

**FLAG (edge-kind):** `common_code_line_budget --ref-->` is deliberate:
nothing is consumed from it; the edge exists so the near-duplicate
formula is discoverable from both sides. If house convention omits
pure-differentiation refs, drop it and keep the statement text.

### C. `ev` edges into the red TARGET (red-leaf law: `ev`/`ref` in-edges only)

`xr_graded_tangent_band_charge` is a **critical TARGET (red leaf)**; all
proposed in-edges are `ev`, and no new node takes any edge FROM a
TARGET. Each edge below matches content the TARGET's statement already
cites:

| from | to | kind | what it evidences in the reduction |
|---|---|---|---|
| `xr_two_slope_cost_theorem` | `xr_graded_tangent_band_charge` | `ev` | "two-slope condition rank exactly 2h per pair (FAMILY-RANK; per-ray accounting of record)" — verbatim the cost side |
| `xr_two_slope_deficit_dichotomy` | `xr_graded_tangent_band_charge` | `ev` | "sunflower cost exactly h (unique known deficit family, d <= (h-1)/2 ONLY)" — the confinement is this node's Theorem 2 |
| `xr_mc_depth_quantization` | `xr_graded_tangent_band_charge` | `ev` | "MC depth-quantized out of the band"; the cascade-tier `N_{h-1} <= n/2` under the pinned selected-support reading |
| `xr_band_ledger_theorems` | `xr_graded_tangent_band_charge` | `ev` | the reduction of record: `\|Gamma_band\| = Sum_d Sum_P L_P`, `L_P <= floor((n-J)/(A-J))`, tight at the cascade tier; the third-column pricing |
| `xr_support4_structure` | `xr_graded_tangent_band_charge` | `ev` | "connectivity floor rank >= m (V <= m/2 => occupancy)"; the escape-form heart + the two named sub-items, verbatim the TARGET's open-input framing |
| `xr_band_key_lemma_pencil_mass` | `xr_graded_tangent_band_charge` | `ev` (OPTIONAL) | the below-cascade <=> shared-agreement-sets semantics + the certified reason the single-word reduction was retired (route history of the column). The minimum defensible set is the FIVE edges above; the coordinator may drop this one |

### D. Edges deliberately NOT proposed

- **No `req` out of any TARGET** into these nodes (red-leaf law), and
  none of the six statements assumes any red content.
- **Nothing into `xr_highcore_collision_count` / `xr_smallcore_spread_count`
  / P-B nodes**: by the R2 partition of record the band column is
  disjoint from the exact-`k` and `<= k-1` strata; these nodes neither
  strengthen nor weaken those predicates.
- **Nothing into `xr_strip_classification_rungs` or
  `xr_pencil_cascade`**: their ratified addenda already carry the Route
  T fold-in; adding ev edges would duplicate the DAG's existing
  cross-references. Coordinator may add
  `xr_band_ledger_theorems --ref--> xr_strip_classification_rungs` if
  the (3') third-column text should be discoverable from the ledger
  node; not proposed by default.
- **No node for the band-occupancy pilot's unified fibre strip (T1) /
  high-depth injectivity (T2) or for occupancy-v2's growth laws** —
  see AUDIT_CHECKLIST item 7 (candidate seventh node) and the
  supersession flag.
- **Nothing m2-related.**
