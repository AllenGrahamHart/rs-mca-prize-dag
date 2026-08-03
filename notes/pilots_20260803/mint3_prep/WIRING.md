# WIRING proposal — MINT-3 (the round-11/12 kernel packages)

Prepared 2026-08-03 by the third mint-prep pilot (Opus), mirroring the
completed patterns
(`notes/pilots_20260802/band_mint_prep/`, `notes/pilots_20260803/mint2_prep/`).
**Nothing here has been applied**: `dag.json`, `background/`, `critical/`,
`tools/` are untouched. Everything below is a proposal for the
coordinator to audit, adjust and wire.

The brief listed a FIVE-PACKAGE queue. **THREE are drafted; one is
REFUSED as substantially duplicate and un-audited (section 4); item 5 is
an adjudication, delivered in section 5.** All three drafts are
**background** nodes with `statement.md`, `proof.md`, `verify.py`:

```text
drafts/xr_window_system_descent/    ->  background/nodes/xr_window_system_descent/
drafts/xr_pencil_forcing_t0/        ->  background/nodes/xr_pencil_forcing_t0/
drafts/xr_ov_slope_free_reduction/  ->  background/nodes/xr_ov_slope_free_reduction/
```

**Measured under `tools/ramguard tiny`: 5.32 / 0.21 / 0.17 s; check
totals 16 / 12 / 14 = 42 PASS, 0 FAIL.** All pure-python integers,
deterministic, no third-party imports, **no reads outside their own
directory** (this matters more than usual here: the source verifiers for
packages 3 and 4 import *other pilot directories by absolute path*, so
every primitive was re-implemented from scratch). They keep passing after
the move.

**ID collision check (against `dag.json`, 1793 nodes): all three ids are
FREE.** `xr_window_system_descent` is already named in the coordinator's
own mint queue (`CAMPAIGN_LEDGER.md:943-945`).

**After moving, regenerate the verifier manifest**:
`tools/run_all_verifiers.py --refresh-manifest`. Note it hashes
`statement.md` and `proof.md` as **proof assets** as well as `verify.py`,
so all nine files enter the manifest.

**⚠ WORKFLOW CONFLICT, flagged not decided.** `README.md` says
`dag.json` is the source of truth and is edited directly;
`notes/DAG_MANIFEST_CONVENTION.md:1-69` says `dag.json` is generated and
must **never** be edited, with `node.json` shards as the source. **In
this checkout the manifest refactor has NOT landed** —
`tools/compile_dag.py`, `tools/verify_dag_manifests.py` and
`graph/dag_meta.json` are all **absent**, and the three newest mints
(`pb_design_ceiling`, `pb_block_dichotomy`, `f2_antipodal_descent_lemma`)
have **no `node.json`**. So the operative practice is direct `dag.json`
editing, which is what the blocks below assume. **Coordinator's call.**

---

## 1. `xr_window_system_descent`

```json
{
 "id": "xr_window_system_descent",
 "title": "Window-system descent: LEMMA W (the depth-d window system as a Toeplitz syndrome system, iff both directions) with the band-lane reading of the banked divisor correspondence; THEOREM D (exact mu_M-coset descent bijection, settling definitions item 6's 'syndromes descend' FOR THE WINDOW SYSTEM); THEOREM L (M-quotient-periodic pairs with h ODD force M <= cap_d, killing M = 2^21..2^31 unconditionally at the prize rows); THEOREM R (full Toeplitz rank d on the tangent-gated class via Berlekamp-Massey, so no blow-up can be linear); the BP(1) sub-depth scope catch; SL-2 itself NOT answered",
 "status": "PROVED",
 "closure": "proof",
 "statement": "C = RS_k on H = mu_n (n | q-1, split), A = k+h, received pair (u,v), joint-explanation pair P = (f,g) with core Z_P = {x : f(x)=u(x), g(x)=v(x)}, |Z_P| = k+d, depth d, r' = n-k-d, T = H \\ Z the core complement. BAND PROPER here means the PILOT's upper window d in [ceil(h/2), h-2] (PREREG.md:26), NOT definitions item 2's [1, h-2] -- the distinction is carried everywhere. LEMMA W (PROVED, both directions): a codeword P (deg < k) with (u-P) vanishing on H\\T exists <=> the coefficients of u E_T mod (X^n - 1) in degrees n-d..n-1 all vanish; these are d equations LINEAR in E_T's coefficients with coefficient matrix the Toeplitz matrix of the syndrome window (u_k,...,u_{n-1}); the joint system is the same with 2d equations. COROLLARY W2 (the coordinates): T <-> E_T is a bijection onto the monic degree-r' divisors of X^n - 1, and the joint system cuts a codim <= 2d affine subspace. SUBTRACTION (hard law 5), LOAD-BEARING: the divisor correspondence is NOT new -- it is banked upstream in the locator/Hankel lane at critical/nodes/counting_frame/statement.md:9 ('Locators of co-supports are squarefree degree-j divisors of X^n - 1 -- a FINITE set of size C(n,j)'), critical/nodes/v8_ledger/statement.md:9, and the set is already named D_j at critical/nodes/spi_exceptional_class/proof.md:87; the '2d linear conditions' half is banked at notes/band_heart_consolidation_20260803/CONSOLIDATION.md:59-62 off the KEY LEMMA (background/nodes/xr_band_key_lemma_pencil_mass). LEMMA W is minted here as the BAND-LANE INSTANTIATION -- the contribution is the explicit Toeplitz syndrome form, the iff against an independent oracle, and the joint version, NOT the correspondence. SCOPE FENCE: a banked REFUTATION applies to the neighbouring phrasing (CONSOLIDATION.md:102-117) -- '(k+d)-sets Z with A(Z)=B(Z)=0' is FALSE as a <= 0.68n^2 claim; the correct object is codeword pairs whose joint agreement set has size EXACTLY k+d. This node's cores are MAXIMAL, never raw subsets, and no counting claim is drawn from the correspondence. THEOREM D: for M | gcd(n,k), M | d -- (a) T is a mu_M-coset union <=> E_T(X) = G(X^M) (PROVED here in BOTH directions; the source checks only one); (b) equation j touches only syndrome positions = j (mod M); (c) with the syndrome window in a single class rho mod M, scale-M cores upstairs are in EXACT BIJECTION with cores of the quotient instance RS_{k/M} on mu_{n/M} at depth d/M with word U_s = u_{rho+sM} (RECONSTRUCTED -- the source gives no derivation). COROLLARY D6: syndromes descend, so definitions item 6's quotient convention is CORRECT -- FOR THE WINDOW SYSTEM ONLY; P3-EVASION (mixed-class pencils) shows the strip filter itself can still be evaded, which is why THEOREM L is needed. THEOREM L (RECONSTRUCTED, two gaps NAMED): for a separately M-quotient-periodic depth-d pair with h ODD, M > cap_d = floor((n-k-d)/(h-d)) forces L_P = 0, so the pair is not counted by N_d. cap_d is BANKED (xr_band_ledger_theorems/statement.md:38-44 THEOREM 3 at J = k+d), consumed not re-derived. At the prize rows this closes M = 2^21..2^31 (1/4, 1/8) and 2^21..2^30 (1/16) UNCONDITIONALLY. THEOREM R (PROVED, transplanted from toeplitz.py:7-19): on the tangent-gated class rank R(u,d) = d exactly -- a row dependency IS a linear recurrence on the syndromes, n-k >= 2d lets Berlekamp-Massey turn it into an error locator of degree <= d-1, i.e. a codeword agreeing on >= n-d+1 points, which the tangent gate forbids; sharpness verified by the converse (distance L < d drops rank to exactly L). Consequence: no adversary can buy a family by degenerating the LINEAR part -- ANY BLOW-UP MUST BE ARITHMETIC. Adjacency flagged: the Hankel lane already calls ker M(Z) the Berlekamp-Massey kernel (critical/nodes/f_termination_hankel/notes/pro_brief_broad.md:24-28) and hankel_rank_profile_entropy is PROVED. BP(1) SCOPE CATCH (context; the corrected scope of record is the applied addendum at background/nodes/xr_mc_depth_quantization/statement.md:151-163): BP(1) is proved only AT THE PINNED SCALE M = 2^ceil(log2 d) >= d; sub-depth scales M < d are NON-EMPTY inside the band proper at all three prize rows and are excluded by THEOREM L (M >= 2^21) and by first moment below that. Non-vacuity exhibited: a scale-M=2, d=4 family whose item-10 scale is 4. The scoping question was PARTIALLY ANTICIPATED at notes/pilots_20260802/band_mint_prep/AUDIT_CHECKLIST.md:175-181 item 7; the pilot's catch is sharper (it exhibits the scales) but is not wholly unforeseen. NOT claimed: SL-2 ITSELF IS OPEN (an unstructured family at band-proper depth with > 0.68 n^2 members -- the assigned falsifier was pre-registered NOT to fire and did not; SL-3 sub-criticality, itself a CONJECTURE, means no toy can exhibit the blow-up); SL-2-RES, the residual, is NOT proved -- 'aperiodic band-proper core count <= 0.68 n^2, equivalently how many monic degree-r' divisors of X^n - 1 lie on a codimension-2d affine subspace?' -- and it MUST carry h ODD and q >= 2^209 (both load-bearing: the h-even control fails twice over; the q-pin has 41.52 bits of headroom at the binding row prize 1/4, log2 q_critical = 208.47593); the M <= 2^20 closure is HEURISTIC-GRADE (a first-moment EXPECTATION, not a certified bound; margins >= 3.09e5 bits, and the code's own proved/heuristic partition is carried verbatim); THEOREM L at h EVEN is FALSE as an exclusion (the h-even control has proved_scales = []); the OFF-CLASS RANK PENALTY (PREREG P6) is MEASURED, and its pre-registered rank-ADDITIVITY was never checked; Route 1/2 negatives are PROVED NEGATIVES ABOUT THE ROUTES, not about SL-2; no count claim rests on any fixture; the joint codimension is exactly 2d only where the two row-spaces meet trivially, which is NOT proved. HONESTY: this pilot has NO REPORT.md, THEOREM L's cited proof ('REPORT section 3') DOES NOT EXIST, and the coordinator's replay covered algebra.py + descent.py (539 of 677 checks) but NOT toeplitz.py, where THEOREM R lives. Provenance notes/pilots_20260803/sl2_unstructured/{PREREG.md:35-43,49-56,57-63,77-82, algebra.py:12-29,142-154, descent.py:15-20, toeplitz.py:7-19, FABLE_AUDIT.md:12-46}, mint queued at FABLE_AUDIT.md:40-43.",
 "refs": [
  "background/nodes/xr_window_system_descent/statement.md",
  "background/nodes/xr_window_system_descent/proof.md",
  "background/nodes/xr_window_system_descent/verify.py"
 ]
}
```

## 2. `xr_pencil_forcing_t0`

```json
{
 "id": "xr_pencil_forcing_t0",
 "title": "Pencil forcing T0: in a gate-clean zero-escape block system with V >= 5 and dim Ann >= 1, the blocks CANNOT be covered by two DISTINCT pencils each carrying >= 3 blocks (equivalently M <= 1), proved via LEMMAS 2-5 -- with P-SHARE (distinct pencils share <= 1 fibre, sharpening unified's <= 2 and keeping the pinning out of the V = 4 no-content regime) -- and with the t <= 2e-3 band NAMED as an explicit residual; T1 and T2 are FALSE, refuted on 18 fixtures; the C = 1/2 anchor needs a SECOND node (UPB) that is banked but unminted",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Block system B(V,t,t_0,k) as v5_occupancy: U = A_0 |_| A_1 |_| ... |_| A_V, |A_0| = t_0, |A_a| = t, S_a = U \\ A_a, distinct slopes z_a; |U| = t_0+Vt, A = t_0+(V-1)t, h = A-k, m = t+h, sigma = t_0+(V-3)t, e = k-sigma = 2t-h; admissible t >= 2, t+1 <= h <= 2t-1, so 1 <= e <= t-1; band-proper depth d = h-t. B_a := prod_{x in A_a}(X-x); a PENCIL is a 2-dimensional subspace of F_q[X]_{<=t} containing all the B_a; a FIBRE is the root set of a member. Ann is the annihilator (collapse <=> Ann = 0); NON-COLLAPSING means dim Ann >= 1. The gate here is the COMBINATORIAL gate on supports (min mult >= 3, pair >= k+1, trip <= k-1, 1 <= pair-k <= h-2), NOT unified's six-part SPECTRAL FULL GATE on a received pair -- they are different objects and t means different things in the two pilots. Q0 (definitional, load-bearing): any two disjoint equal-size blocks are fibres of a common pencil, so 'pencil-structured' is VACUOUS at family size 2 -- which is why T0 quantifies over pencils carrying >= 3 blocks. T0 (PROVED, with a named residual): for a gate-clean zero-escape system with V >= 5 and dim Ann >= 1, the blocks cannot be covered by two DISTINCT pencils carrying >= 3 blocks each. P-SHARE (PROVED): two distinct pencil-structured live families share at most ONE live slope -- sharpened from unified PREREG Q5's <= 2, and LOAD-BEARING, because at 2 shared the pinning subfamily could be V = 4, exactly the proved no-content regime where the W1/W2 counterexamples live, voiding the anchor's reduction. Supporting: LEMMA 2 (r-formula: dim span{B_a off the pair} = 2 <=> d_ij = 1, needing >= 3 blocks off the pair, i.e. V >= 5); LEMMA 3 (normal form f_0 = B_j^Z s_0, f_1 = B_i^Z s_1); LEMMA 4 (rogue criterion B_j in <f_0,f_1> <=> s_0 ~ zeta_j -- this GENERALISES the pre-registered Q4 criterion 'Z_j empty', transplant LEMMA 4 not Q4); LEMMA 5 (the intersection lemma, the ONLY lemma with a written proof: P' ^ <B_i,B_j> is 0, <B_i> or <B_j>, and in every case contains NO THIRD BLOCK; its degree hypothesis |Z| < t is AUTOMATIC since |Z| <= e-1 <= t-2, so LEMMA 5 is unconditional and the residual does NOT attach to it). T1 ('>= V-1 blocks in one pencil') and T2 ('all V blocks') are FALSE, constructively refuted on 18 fixtures; the coordinator adopted the consequence that la_pencil_rigidity's V >= 5 non-existence EVIDENCE is VOID (random partitions are blind to a codim-4 condition) while its proved theorems replay clean -- the conjecture died, the theorems held. NOT claimed: THE RESIDUAL -- T0's CASE (b) needs t >= e + max|Z|, unconditional for e <= 3 and t >= 2e-2, and the band t <= 2e-3 is NOT PROVED and INCLUDES THE PRIZE SHAPES (read 2e-3 as 2e MINUS 3 in the integer parameter e, NOT scientific notation). DERIVED here and machine-checked: t <= 2e-3 <=> h >= 3d+3, and the admissible window forces t >= 5, so the band is EMPTY for t <= 4 and its smallest shape is exactly (t,e) = (5,4) -- which is why case (b) is unconditional for e <= 3, and that exact shape was itself swept exhaustively and carries two live fixtures on which T0 held. Support for the band is EMPIRICAL: 54+12 COMPLETE two-pencil sweeps (completeness machine-checked against a 400,000 budget, not assumed) found zero, and dim G = 1 in all 134 non-collapsing systems OBSERVED -- the source words that as 'was observed', not as a theorem. P-DISJ is NARROWED NOT CLOSED (an inherited gap; the gate only forces each point into <= V-3 blocks, and the overlap cross-check never executed because no non-collapsing system was found). THE C = 1/2 ANCHOR IS NOT PROVED BY THIS NODE: it stands on {UPB e=1 + T0 + P-SHARE}, and UPB -- the unconditional C = 1/2 at e = 1 for ALL live slopes, with NO pencil hypothesis -- is an EXTERNAL BANKED INPUT (notes/pilots_20260803/unified_pencil_bound/, ledger CAMPAIGN_LEDGER.md:838-849) that is NOT restated here; it is banked-but-unminted and MISSING from the round-12 mint queue, so a second node is owed. M <= 1 is established at e = 1 only without T0, because the Ann-monotone 3+3 pinning consumes v5 THEOREM C', which is proved at e = 1 and 'at e >= 2 MEASURED only'. COMBINATORIAL M <= 1 is FALSE (170 multi-pencil matchings; independently re-exhibited here at q=17); what kills them is REALISABILITY, and that negative is reported by its own source 'as a NEGATIVE, not as support for the anchor' because realise_family never returned a pair, so the gate was never evaluated on a multi-pencil config. No bound on |Gamma|, no occupancy claim, no discharge of heart 7. HONESTY: this pilot has NO REPORT.md and there is NO continuous prose proof of T0 anywhere on disk; the lemma NUMBERING exists only as check-label strings in verify.py; LEMMA 4 and CASE (b) have NO written proof at all; the coordinator hand-checked EXACTLY LEMMA 5, the case-(b) cross-multiplication, and the T0 => M <= 1 => C = 1/2 chain -- LEMMAS 2/3/4 were machine-replayed only; P-SHARE's SLOPE form is recorded in the source as a check hard-coded to True, and is COMPUTED in this node's verifier. Provenance notes/pilots_20260803/f9_pencil_forcing/{PREREG.md:22-24,44-61,85-101,132-154,185-208, verify.py, verify.json, FABLE_AUDIT.md:3-38}, ledger CAMPAIGN_LEDGER.md:918-930.",
 "refs": [
  "background/nodes/xr_pencil_forcing_t0/statement.md",
  "background/nodes/xr_pencil_forcing_t0/proof.md",
  "background/nodes/xr_pencil_forcing_t0/verify.py"
 ]
}
```

## 3. `xr_ov_slope_free_reduction`

```json
{
 "id": "xr_ov_slope_free_reduction",
 "title": "OV reduced slope-free: THEOREM 1's gate<->MDS dictionary (pair-unions ALWAYS independent, triple-unions ALWAYS dependent -- so no vanishing-set argument can ever close OV); THEOREM 2 (Jperp = 0 => Ann = 0 for EVERY slope tuple, removing the slope quantifier and re-labelling the sliver's 3.3e12-tuple evidence as wrong-space); THEOREM 5 (the r = d branch is empty under L=1 + uniform multiplicity, covering PG(2,3)); residual r > d OPEN, CONJECTURE OV OPEN, consumers BLOCKED -- this node is evidence and structure, NOT a close",
 "status": "PROVED",
 "closure": "proof",
 "statement": "U = union of supports, n_U = |U|, |S_a| = k+h, A_a = U \\ S_a with |A_a| = t, m = n_U - k, w_ab = |A_a ^ A_b|, d = |S_a^S_b| - k, I_ab = S_a ^ S_b; W = F^U/RS_k|_U (dim m), e_x = class of delta_x, W_a = span{e_x : x in A_a}; Ann = {(lam,mu) in W x W : lam + z_a mu in W_a for all a}. MDS FACT: {e_x : x in B} is independent iff |B| <= m. GATE-CLEAN = zero escape (m_x <= V-3) AND pairwise |S_a^S_b| >= k+1 AND (T) |S_a^S_b^S_c| <= k-1 AND strict depth 1 <= d_ab <= h-2 for every pair. NOTATION FIXED HERE: the source writes W both for the quotient and for union A_a, and lam both for the overlap parameter and for an annihilator component; this node writes W only for the quotient, Y for the block union, L for the overlap parameter. THEOREM 1 (PROVED, hand-verified) -- the gate<->MDS dictionary: pairwise gate <=> |A_a u A_b| = m-d <= m-1, so pair-unions are ALWAYS INDEPENDENT; gate (T) <=> |A_a u A_b u A_c| >= m+1, so triple-unions are ALWAYS DEPENDENT; zero escape <=> the intersection of all pair-unions is EMPTY. THE WALL EXPLANATION, the load-bearing consequence: every one-shot argument of the sibling collapse pilot's shape needs one DEPENDENT pair-union or one INDEPENDENT triple-union, and the gates forbid both always -- so OV CANNOT be closed by 'vanishing on >= k points' and no sharpening of that shape will do it. THEOREM 2 (PROVED, hand-verified) -- the slope-free reduction, and THE result: with Jperp := ^_{a<b}(W_a + W_b), which depends only on U and the blocks and in which THE SLOPES DO NOT OCCUR, Jperp = 0 implies Ann = 0 for EVERY slope tuple; equivalently Ann != 0 forces dim Jperp >= 2. Non-degenerate branch: the annihilator's 2-plane lies in every W_a + W_b; degenerate branch dies on zero escape. CONSEQUENCE, a correction to the record: overlap_sliver's 3.3e12 SLOPE-TUPLE evidence was gathered in the WRONG SEARCH SPACE because the obstruction is support-level; the right space is POINT SETS, swept at 8,400 configurations with 0 hits (applied by the coordinator as a dated addendum at notes/pilots_20260803/overlap_sliver/FABLE_AUDIT.md:33-40). The sufficient threshold is dim Jperp <= 1, not = 0. THEOREMS 3/4 (derivation-in-statement, machine-corroborated, NOT hand-verified): Jperp ~ {v k-flat on every I_ab}/RS_k, and if all interpolants f_ab coincide then Jperp = 0; with r := deg v - k, k-flatness means M_ab | v - f_ab so r >= d, and r = d <=> e_1..e_d(I_ab) are constant across pairs, in particular sigma_a + sigma_b - sigma_ab = C. THEOREM 5 (PROVED, hand-verified) -- shared-point forcing: gate-clean, zero-escape, L = 1, UNIFORM multiplicity m_x = mu on Y, char F not dividing V-1-mu, THEN the r = d branch of Jperp is EMPTY. Proof: summing the e_1 identity over b != a gives (V-1-mu) sigma_a = (V-1)C - S, the same constant for every a; zero escape gives V-1-mu >= 2; so all sigma_a are equal, all sigma_ab equal, and with L = 1 all pairwise intersection points coincide at one y with m_y = V > V-3, contradicting zero escape. This covers PG(2,3) exactly (V=13, t=h=4, k=5, d=1, L=1, mu=4, V-1-mu=8). The e_1 separator, solved for the POINT SET: PG(2,3) and MINWIT give solution dim 1 with ALL coordinate pairs forced to collide (constants only, no usable point set) while the DISJOINT X1-shape control gives dim 5 with 0 collisions -- the mechanism is alive on disjoint blocks and dead on overlapping ones, which is OV's content proved for this branch; structural reason: the only known non-collapsing mechanism is 'blocks are the fibres of a pencil', and FIBRES ARE PAIRWISE DISJOINT. SUBTRACTION (hard law 5): 'collapse <=> Ann = 0' is ALREADY BANKED at background/nodes/xr_support4_structure/statement.md:233 and is CITED, not re-derived -- THEOREM 2's contribution is only the Jperp => Ann implication; PG(2,3)'s extremality is ALREADY BANKED (notes/band_heart_consolidation_20260803/CONSOLIDATION.md:170-171, CAMPAIGN_LEDGER.md:768-769 'sharp at PG(2,3)'), so 'covers PG(2,3)' is a RE-USE of the banked extremal witness; LEMMA R (rank = 2m kills exact-A liveness) is banked at notes/BAND_LANE_DEFINITIONS.md:110-111. NOT claimed: CONJECTURE OV IS OPEN -- statement of record notes/pilots_20260803/overlap_sliver/REPORT.md:26-30, board entry notes/PRIZE_RESOLUTION_ROADMAP.md:17012-17013 -- neither proved nor refuted, and THIS NODE MUST NOT BE CITED AS A CLOSE. The residual is the r > d branch: for d = 1, dim Jperp >= 1 iff the m vectors (e_j(A_a u A_b)) over pairs are DEPENDENT, and THEOREM 5 kills only the dependency u_1 in <u_0>; dependencies involving e_2..e_{m-1} are OPEN, and the pilot states 'I did NOT find a reduction of r > d to r = d, and I do not claim one'. Named next attack: the s = 1 telescoping cocycle (three-block relations alone do not force alpha = 0). THEOREM 5 IS NOT SHARP and its hypotheses were not removed (L = 1, uniform multiplicity, char F not dividing V-1-mu, r = d only); MINWIT lies OUTSIDE them and is dead anyway. THEOREM 2 is SUFFICIENT, not an equivalence -- the converse is nowhere claimed. CONSUMERS STAY BLOCKED: overlap_sliver's V <= |U|/2 upgrade and crosslane_cashout's VERDICT A (|K| close) may NOT cite this as a close, only to RE-SCOPE the obligation. TOY SCALE ONLY (q <= 10007 for the exact e_1 algebra, q <= 41 for all Jperp/Ann work, n_U <= 15, V <= 13; no prize-row instance tested); COMBINATORIAL GATES ONLY (no realising (u,v) band pair exhibited); the L >= 2 sample is THIN (2 systems, the coordinator's noted weakest cell); OV is VACUOUS at V = 4, so the banked X1/X2/X3 witnesses do not touch it. HONESTY, LOAD-BEARING: the OV pilot's REPORT.md write was HARNESS-BLOCKED and NO REPORT.md EXISTS; the full statements and proofs survive only in an out-of-tree subagent transcript, which is not citable from a permanent node. Every proof in this node is therefore RECONSTRUCTED from PREREG.md, FABLE_AUDIT.md's hand-check descriptions, verify.py and verify.json. RECOMMENDED BEFORE WIRING: persist ov_conjecture/REPORT.md verbatim, exactly as was done for the sibling at notes/pilots_20260803/zero_escape_collapse/REPORT.md:3-4. THEOREMS 3/4 were NOT hand-verified. Provenance notes/pilots_20260803/ov_conjecture/{PREREG.md:5-9,13-19,30-34,42-83,87-113, FABLE_AUDIT.md:1-31, verify.py, verify.json}, ledger CAMPAIGN_LEDGER.md:934-941.",
 "refs": [
  "background/nodes/xr_ov_slope_free_reduction/statement.md",
  "background/nodes/xr_ov_slope_free_reduction/proof.md",
  "background/nodes/xr_ov_slope_free_reduction/verify.py"
 ]
}
```

## 4. `xr_gamma_coset_reduction` — **REFUSED this round, not drafted**

No JSON block is proposed. **Two independent grounds, either sufficient:**

**(i) Three of its five claims are already the BANKED WORDING OF
RECORD.** `notes/pilots_20260802/band_adjudication/REPORT.md:113-125`
is an **applied coordinator amendment** that already contains, verbatim:
`|Gamma_j| <= n . E_j` as "the unconditional REDUCTION (THEOREM D)"; the
`E_1 = 1` case as THEOREM Y; "**The prize rows have w = M hence
j <= w-1**"; the correction of "X governs" to necessary-not-sufficient;
and "the **one-parameter averaging gap**" as the named obstruction.
THEOREM G's repricing is likewise already applied to the r3.2 board at
`notes/PRIZE_RESOLUTION_ROADMAP.md:17014-17017` ("E_j = |Gamma_j| in
coset coordinates, within 9 bits, NOT a smaller object"). Minting these
again would be a hard-law-5 violation.

**(ii) The only genuinely unbanked residue — THEOREM G's two-sided
sandwich and THEOREM H's rigidity `d <= (j-1)+gcd(j,n)` — comes from a
pilot with NO COORDINATOR AUDIT AT ALL.**
`notes/pilots_20260803/ej_coset_spread/` contains **no `FABLE_AUDIT.md`**
(confirmed by directory listing); its only coordinator record is three
sentences in the campaign ledger. The brief's honesty rule is explicit —
*statuses PROVED only where the source pilot **and** coordinator audit
agree it is proved*. **No audit exists, so no PROVED status can be
issued.** That pilot also carries the round's only failing checks (2 of
4,744,495), a pre-checkpoint 13-failure run visible only in prose, and
two in-run corrections.

**Recommendation.** (a) For THEOREM D / Y / scope: **cite
`band_adjudication/REPORT.md:113-125`; do not mint.** (b) For THEOREM
G/H: **commission a coordinator audit of `ej_coset_spread` first**, then
mint as a *separate* node — never merged with the gamma half, whose
evidentiary status is completely different (gamma: 9,415 checks, 0
failures, 0/9 falsifiers, e2/e3 coordinator-replayed, five ADOPTED items;
ej: no audit). A merged node would launder ej's provenance up to
gamma's. (c) If a node is wanted this round regardless, the only
defensible one is **THEOREM H alone**, stated for **band-solutions**
(not admissible solutions — a strictly larger family), with `(H4)`'s
hypothesis given in the **code's corrected form**
`2[(j-1)+gcd(j,n)] <= w-2j`, **not** the PREREG's `w >= 4j`. See
AUDIT_CHECKLIST F2 for the full evidence.

## 5. Item 5 — adjudication (recommendation, not a decision)

See AUDIT_CHECKLIST section 5 for the evidence. Summary:

| item | recommendation |
|---|---|
| escape-1 **THEOREM D** (3-drop kernel floor) + COROLLARY D1 | **NODE NOW** — the one addition I would defend |
| **D-tightness** | fold into the above as a MEASURED sharpness clause; already stated at `xr_support4_structure/statement.md:262-263` |
| **E1-PENCIL** | **pilot-banked; refuse** |
| sl1 **THEOREM A** | eligible but **do not mint alone** — no consumer without E |
| sl1 **THEOREM E** | **pilot-banked** — dangles on SL-2 |
| sl1 **THEOREM F** | **refuse — DUPLICATE**; make it an addendum instead |
| sl1 **THEOREM U** | **pilot-banked** — post-hoc, no consumer |

---

## Proposed edges

Direction convention (`dag.json`'s own description, confirmed in
`tools/verify_prize_dag.py:269-270`): **edges point FROM a dependency TO
the statement it supports.**

### A. `ev` edges into the red TARGET (red-leaf law)

`xr_graded_tangent_band_charge` is a critical **TARGET** whose
`closure != "artifact"`, so by `verify_prize_dag.py:83-89` **every**
in-edge must be `ev` or `ref`. It already carries 9 `ev` in-edges.

| from | to | kind | what it evidences |
|---|---|---|---|
| `xr_window_system_descent` | `xr_graded_tangent_band_charge` | `ev` | the TARGET's single open input is the **occupancy lemma**; this node supplies the coordinates that question is now posed in (LEMMA W / W2), settles the structured sub-depth half at `M >= 2^21` (THEOREM L), and proves that no blow-up can be *linear* (THEOREM R) — i.e. it fixes what SL-2-RES has to be about |
| `xr_pencil_forcing_t0` | `xr_graded_tangent_band_charge` | `ev` | T0 + P-SHARE are two of the three legs the `C = 1/2` live-pencil bound stands on, and that bound prices the band column the TARGET charges |
| `xr_ov_slope_free_reduction` | `xr_graded_tangent_band_charge` | `ev` | **FLAGGED.** OV's own consumers (`overlap_sliver`'s `V <= |U|/2`, `crosslane_cashout`'s `|K|`) are **not DAG nodes**, and no node exists for CONJECTURE OV. This is the nearest honest consumer: the ledger records "OV pays band cleanup + P-A1's `|K|`" (`PRIZE_RESOLUTION_ROADMAP.md:17012-17013`). **If the coordinator judges this too loose, the alternative is `ref -> xr_support4_structure`** (which already carries the `Ann` duality this node consumes) — that also satisfies reachability. Coordinator's call |

**Reachability**: `rev` in `verify_prize_dag.py:247-261` is built from
**all** edge kinds, and
`xr_graded_tangent_band_charge --req--> xr_smallcore_spread_count --req--> ... --> prize`
is a live path. Each new node therefore has an out-edge reaching the
root. **No node here has only in-edges.**

### B. `req` / `ref` edges from banked nodes into the new three

| from | to | kind | justification |
|---|---|---|---|
| `xr_band_ledger_theorems` | `xr_window_system_descent` | `req` | **essential.** `cap_d = floor((n-k-d)/(h-d))` is that node's THEOREM 3 (`statement.md:38-44`) at `J = k+d, A = k+h`, and THEOREM L's entire conclusion is phrased in it. Consumed verbatim, not re-derived |
| `counting_frame` | `xr_window_system_descent` | `ref` | **the hard-law-5 attribution edge.** The divisor correspondence at the heart of LEMMA W is that node's banked content in the locator/Hankel vocabulary. This edge is what makes the subtraction visible from both sides. `ref`, not `req`, because LEMMA W is re-proved here in band-lane notation rather than imported |
| `xr_band_key_lemma_pencil_mass` | `xr_window_system_descent` | `ref` | the "`2d` linear conditions in the top-coefficient space" reading traces to the KEY LEMMA; attribution, not consumption |
| `xr_support4_structure` | `xr_ov_slope_free_reduction` | `req` | **essential.** The duality criterion `collapse <=> Ann = 0` (`statement.md:233`) is consumed by THEOREM 2, which proves only the `Jperp => Ann` half |
| `xr_support4_structure` | `xr_pencil_forcing_t0` | `ref` | **FLAGGED, coordinator's call.** That node carries the ray-system setting and v5's Addendum 3 (`2V <= 3h`), and T0 runs inside the same `B(V,t,t_0,k)` model consuming v5 LEMMA 1's normalisation. But LEMMA 1 itself lives in a *pilot*, not in that node, so `req` would overstate. Proposed as `ref`; upgrade to `req` only if the coordinator reads Addendum 3 as carrying LEMMA 1 |

### C. Internal edges among the new three

| from | to | kind | justification |
|---|---|---|---|
| `xr_window_system_descent` | `xr_mc_depth_quantization` | `req` | **the addendum already applied to that node** (`statement.md:151-163`) states that sub-depth scales "ARE excluded by the SL-2 pilot's THEOREM L" and that "THEOREM D there settles 'syndromes descend'". That addendum **logically depends on this node**, so the edge records an existing consumption rather than creating one. **Safe for criticality**: `xr_mc_depth_quantization`'s only out-edge is `ev`, so it is not in the reverse-`req` closure of the grand nodes and this `req` does not pull the new node onto the critical surface. **Verify that before wiring** |

**No edges proposed between the three new nodes.** They share no lemma:
package 1 is window-system algebra on `mu_n`, package 3 is block-system
pencil algebra, package 4 is quotient-space MDS geometry.

### D. Edges deliberately NOT proposed

- **No `req` out of any TARGET** into these nodes (red-leaf law); none of
  the three statements assumes any red content.
- **No edge for a UPB node** — because **no UPB node exists**. This is a
  **queue gap I am flagging, not filling**: `unified_pencil_bound` is
  BANKED (`CAMPAIGN_LEDGER.md:838-849`) with its own audit, PREREG and
  42-check verifier, is **not minted anywhere** in `critical/` or
  `background/`, and is **absent from the round-12 mint queue**. If only
  `xr_pencil_forcing_t0` is wired, the DAG gets the residual-bearing half
  of the `C = 1/2` anchor and none of the unconditional half.
- **No node and no edge for CONJECTURE OV itself** — there is no OV node,
  and creating one is a status decision (it would be a `TARGET`/red leaf)
  that belongs to the coordinator, not to a mint-prep pilot.
- **Nothing into the band-lane six or the P-B pair** — disjoint content.
- **Nothing m2-related.**
