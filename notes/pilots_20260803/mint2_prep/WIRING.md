# WIRING proposal — the MINT REMAINDER (F2 lane + P-B lane)

Prepared 2026-08-03 by the second mint-prep pilot (Opus), mirroring the
completed band-lane pattern
(`notes/pilots_20260802/band_mint_prep/{WIRING,AUDIT_CHECKLIST}.md`).
**Nothing here has been applied**: `dag.json`, `background/`,
`critical/`, `tools/` are untouched. Everything below is a proposal for
the coordinator to audit, adjust and wire.

The brief listed FIVE nodes. **FOUR are drafted; one is REFUSED as a
duplicate** — `pb_l1_lemma` is already banked verbatim (section 3
below, AUDIT_CHECKLIST F1). All four drafts are **background** nodes with
`statement.md`, `proof.md`, `verify.py`. Destination paths (drafts to be
moved as-is after audit):

```text
drafts/f2_antipodal_descent_lemma/   ->  background/nodes/f2_antipodal_descent_lemma/
drafts/f2_parity_defect_certificate/ ->  background/nodes/f2_parity_defect_certificate/
drafts/pb_design_ceiling/            ->  background/nodes/pb_design_ceiling/
drafts/pb_block_dichotomy/           ->  background/nodes/pb_block_dichotomy/
```

After moving, `tools/run_all_verifiers.py` discovers `verify*.py` under
`background/nodes/**`, so `tools/verifier_manifest.json` must be
regenerated (four `verify.py` + eight `statement.md`/`proof.md` hashes).
No Modal launcher needed. Measured runtimes under `tools/ramguard`:
**0.03 / 0.71 / 0.67 / 1.84 s**; check totals **11 / 9 / 9 / 8 =
37 PASS, 0 FAIL**. None reads any file outside its own directory (all
pins inlined, provenance paths in comments only), so they keep passing
after the move.

Note on naming: the F2 background namespace already holds 30+ `f2_*`
nodes from the 2026-07-10 campaign generation; the two new ids do not
collide (checked against `dag.json`). `pb_*` is a **new** id prefix — no
node currently starts with `pb_`.

---

## 1. `f2_antipodal_descent_lemma`

```json
{
 "id": "f2_antipodal_descent_lemma",
 "title": "F2 antipodal descent lemma: in the 2-power Frobenius tower over p with v_2(p-1) = e >= 2 every rung's descent pairs are ANTIPODAL {y,-y}; hence every deployed window is parity-homogeneous (all Delta even), the mode k = p is slice-dead (|R_p| = 1, flat = 0 EXACTLY), and window SELECTION is impossible in principle",
 "status": "PROVED",
 "closure": "proof",
 "statement": "p odd prime, e := v_2(p-1) >= 2, n_j = 2^{e+j}, q_j = p^{2^j}. THEOREM: (i) v_2(q_j - 1) = e+j for every j >= 0 (2-adic LTE: p^{2^j}-1 = (p-1)(p+1)prod_{i=1}^{j-1}(p^{2^i}+1), with v_2(p+1) = 1 since e >= 2 forces p == 1 mod 4, and v_2(p^{2^i}+1) = 1 since an odd square is 1 mod 8); (ii) mu_{n_j} <= F_{q_j}^*, and mu_{n_j} ^ F_{q_{j-1}} = mu_{n_{j-1}} for j >= 1 (gcd(n_j, q_{j-1}-1) = 2^{e+j-1}); (iii) every y of order exactly n_j satisfies y^{q_{j-1}} = -y (q_{j-1}-1 = 2^{e+j-1} u with u odd, and y^{2^{e+j-1}} = -1). COROLLARY A: the rung-j Frobenius conjugate pairs are exactly the ANTIPODAL pairs {y,-y}. COROLLARY B (in the banked first-descent window model -- F_{p^2} = F_p(w), pair reps with w-component in [1,(p-1)/2], s^pm = Tr(c y^{pm}), sigma = s + p[2s>p] in Z/2p, Delta = sigma^+ - sigma^-): s^- = -s^+, and sigma is exactly the CENTRED representative of s mod p hence an ODD function, so sigma^- = -sigma^+ and Delta_i = 2 sigma_i^+ is EVEN for every i, every frequency c, every rung -- every deployed window is parity-homogeneous. COROLLARY C: omega^p = -1 and p is odd, so R_p = (1/m) sum_i (-1)^{Delta_i} = 1, hence max_{k odd}|R_k| = 1 and flat = 0 EXACTLY (not approximately). COROLLARY D: all-Delta-even is COORDINATEWISE, so every non-empty sub-window inherits it -- window SELECTION cannot repair the degeneracy; the escape, if any, is in FREQUENCY space. NOT claimed: the degeneracy law (n_ord/gcd(n_ord,p-1) == 2 <=> all Delta even) is CENSUSED (194 rows, 0 violations), measured not proved -- only the => direction for rung subgroups is proved here; the corollary -log2 rho_b <= log2 p + o(1) (the 1/p ceiling ladder is exact at toy scale with measured saturation, the o(1) is not proved); generic-frequency flatness (T3, OPEN -- needs an incomplete-character-sum bound, not attempted); the K1 mass obligations (O1) E_{c in K1}[exp S_c] <= 2^{n/2+o(n)}, (O2) the same at fixed b, (O3) PP5.0 carrying the pullback ramification 2^d -- these are OPEN constructive obligations (the fixed-sector ABSORPTION route was REFUTED, Theorem B), untouched here; and the law FAILS if n has an odd part or if e = 1. Verified: LTE at the official KoalaBear prime p = 2^31-2^24+1 (e = 24) for all 16 rungs by two independent routes, the antipodal identity at rung 1 (64 genuine elements), all-Delta-even EXHAUSTIVELY over all 2,976 frequencies of F_{p^2}^* at four primes, R_p = 1 exactly, sub-window inheritance, and NON-VACUITY (the full-group window at the same primes has odd Delta and |R_p| < 1). Provenance notes/pilots_20260802/f2_deployed_windows/tower.py:22-43 (statement + proof of record), REPORT.md:23-33,45, FABLE_AUDIT.md:27-33 (independent hand-derivation).",
 "refs": [
  "background/nodes/f2_antipodal_descent_lemma/statement.md",
  "background/nodes/f2_antipodal_descent_lemma/proof.md",
  "background/nodes/f2_antipodal_descent_lemma/verify.py"
 ]
}
```

## 2. `f2_parity_defect_certificate`

```json
{
 "id": "f2_parity_defect_certificate",
 "title": "F2 parity-defect certificate: the exact mode-uniform integer bound max_{k odd}|R_k| <= D/m from the signed parity classes mod p; with the full-group evaluation D = ((p-1)/2)^2 PROVED (and its exact scope a_c b_c != 0 identified -- the record's phrasing was too broad by 2(p-1) frequencies)",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Banked first-descent window model (p odd, n_ord | p^2-1 even and not dividing p-1, frequency c = (a_c,b_c) in F_{p^2}^*, m = (n_ord - gcd(n_ord,p-1))/2 genuine Frobenius pairs, Delta_i in Z/2p, omega = zeta_{2p}, R_k = (1/m) sum_i omega^{k Delta_i}, flat = 1 - max_{k odd}|R_k|). THEOREM 1 (certificate): with c_d := #{i : Delta_i == d (p), Delta_i EVEN} - #{i : ... ODD}, x_d := the EVEN element of {d,d+p}, D := sum_d |c_d|, then for EVERY odd k, (ID) R_k = (1/m) sum_d c_d omega^{k x_d} -- because omega^{k(x+p)} = -omega^{kx} for odd k collapses each residue class -- hence (DEF) max_{k odd}|R_k| <= D/m and (FLAT) flat >= 1 - D/m. D is an exact integer; one integer bounds all p odd modes at once; a class split evenly between the parities has c_d = 0 (perfect local cancellation). THEOREM 2 (full group, n_ord = p^2-1): m = p(p-1)/2 and, for every frequency with a_c != 0 AND b_c != 0, D = ((p-1)/2)^2 EXACTLY, so flat >= (p+1)/(2p) > 1/2. Proof chain (reconstructed -- the record has the VALUE and a 12-instance check, no derivation and no scope condition): with M = (p-1)/2 and kappa(x) = (-1)^{centred rep of x mod p}, a_c != 0 makes a_y sweep F_p bijectively so c_d = A(d) with A(t) = sum_a kappa(a)kappa(a+t); A(t) = (-1)^t (p-2t) for 0 <= t <= M and A is even (parametrise by the centred rep: exactly t of the p values overflow); b_c != 0 makes the support {4 N_0 b_c b : b = 1..M} a HALF-SYSTEM of F_p^*, so |A| takes each of p-2t, t = 1..M, exactly once; D = sum_{t=1}^M (p-2t) = M^2. THEOREM 3 (the exact scope): the hypothesis is NECESSARY and the failure is total on both excluded lines -- b_c = 0 (c in F_p^*) gives s^+ = s^- and Delta == 0; a_c = 0 (c in w F_p^*) gives s^- = -s^+ and all Delta EVEN (the f2_antipodal_descent_lemma mechanism, reached from the frequency side); both give D = m and a vacuous (FLAT). These are exactly the two parity-pure lines. COROLLARY 4 (degenerate branch): any parity-homogeneous window has every c_d >= 0, so D = m and (FLAT) says only flat >= 0; at deployed rung windows the true value is flat = 0, so the certificate is TIGHT BUT EMPTY there. The certificate is informative exactly to the extent the window is parity-INhomogeneous. Also proved: D is invariant under the GLOBAL orientation reversal but NOT under partial flips (verifier exhibits both), so D must always be quoted with its labelling. NOT claimed: this is NOT an (H-flat) certificate for any DEPLOYED window (the full group is a window the tower does not deploy -- its value is as the TEMPLATE for whatever windows the frequency-space case split sends to the slice theorem); (DEF) is an upper bound, not an identity, and no sharpness is claimed outside the degenerate branch; nothing about EVEN modes k (the collapse needs k odd); generic-frequency flatness (T3, OPEN); the multiplicity law (sorted non-zero Delta-counts = [1..p-1]) is MEASURED (exhaustive over all a_c b_c != 0 frequencies at p = 11..23, plus the pilot's p = 41) and is NOT used in any proof; nothing about the K1 mass obligations (O1)-(O3). Verified: (ID) exactly in Z[zeta_p] at every odd k over 24 (p, window, frequency) cases; A(t) at 8 primes; the half-system property exhaustively; THEOREM 2 EXHAUSTIVELY over every frequency of F_{p^2}^* at p = 11,13,19,23,31,41 (3,552 frequencies) including the pilot's own A8 row; THEOREM 3's exception count (exactly p-1 on each line, none elsewhere). Provenance notes/pilots_20260802/f2_deployed_windows/deployed.py:37-56 and :126-147, census.py:65-75, verify.py:300-321 (A8), REPORT.md:37,45, FABLE_AUDIT.md:61-66.",
 "refs": [
  "background/nodes/f2_parity_defect_certificate/statement.md",
  "background/nodes/f2_parity_defect_certificate/proof.md",
  "background/nodes/f2_parity_defect_certificate/verify.py"
 ]
}
```

## 3. `pb_l1_lemma` — **REFUSED, not drafted (already banked)**

No JSON block is proposed. The P-B lane's "L1 lemma" —
`dim C_S = |S|-K` and `dim(C_S ^ C_T) = max(0, |S^T|-K)` — is **the same
lemma** as the band lane's `(L1)`, already **PROVED and wired** on
2026-08-02 at

```text
background/nodes/xr_two_slope_cost_theorem/proof.md:7-23      (proof, QED)
background/nodes/xr_two_slope_cost_theorem/statement.md:23-25 (statement)
background/nodes/xr_two_slope_cost_theorem/verify.py:11,199,219 (check A)
```

The only difference is the symbol (`K` in the P-B gauge, `k` in the band
gauge). Minting it again would be a hard-law-5 violation (duplicate
claim of novelty for a banked result). **Recommended action:** no new
node; the P-B-specific corollary (the transversality reading) is minted
INLINE as Lemma 0 of `pb_design_ceiling`, exactly as the band lane put
its fibre identity inline in `xr_two_slope_cost_theorem` (that wave's
F0.b). See AUDIT_CHECKLIST F1 — including the fact that the P-B lane's
statement of that corollary is **one-directional as written** and is
corrected in the draft.

## 4. `pb_design_ceiling`

```json
{
 "id": "pb_design_ceiling",
 "title": "P-B design ceiling: an INDEPENDENT prescribed-slope witness family realised non-degenerately has M <= (2(n-K)-1)/h <= 960 at all six official rows, so any P-B counterexample is >= 1 - 2^-23 FORCED; the independence hypothesis is load-bearing (a realised, spread, zero-collision mu_n-orbit of size 20 exceeds both ceilings) and the free-slope form is NOT proved",
 "status": "PROVED",
 "closure": "proof",
 "statement": "RS_K on n distinct points, A = K+h, r = n-K; C_S the shortened dual; a WITNESS is (z,S) with |S| = A and (u+zv)|_S in RS_K|_S, i.e. the h rows <c,u> + z<c,v> = 0 for c in C_S, row block G_z(C_S) of dim h; SPREAD = all pairwise |S_a ^ S_b| <= K-1. SUBTRACTION (hard law 5): the MECHANISM is banked and CITED, not re-derived -- (L1) dim(C_S ^ C_T) = max(0,|S^T|-K) at background/nodes/xr_two_slope_cost_theorem/proof.md:7-23, (L2) RS_K x RS_K in every kernel so a non-degenerate realisation forces rank <= 2(n-K)-1 at the same file :96-108, and the per-ray ceiling with the six-row values 307/358/639 / 383/447/959 at statement.md:74-91 + proof.md:110-136. LEMMA 0 (CORRECTED, inline): C_S ^ C_T = 0 iff |S^T| <= K, so SPREAD IMPLIES pairwise transversality but the CONVERSE FAILS exactly at core = K -- the P-B lane states this as an equivalence ('spread <=> pairwise-transverse condition spaces', pb_h4_hunt/REPORT.md:29), which is one-directional as written, and the gap (core exactly K) is Gamma_hi for the budget, so the distinction is load-bearing. THEOREM 1 (ceiling): if the M ray blocks are INDEPENDENT (rank = Mh) and the family is realised by (u,v) not in RS_K x RS_K, then Mh <= 2r-1, i.e. M <= floor((2r-1)/h) = 307/358/639 (RowC) and 383/447/959 (prize). COROLLARY (forcedness): in ANY realised family a maximal independent sub-family has <= 959 members, so a P-B counterexample (> 8n^3 members) has at most 960/8n^3 <= 2^-23.68 of its members independently designable -- every P-B counterexample is at least 1 - 2^-23 FORCED; per-row bit margins 24.74/24.52/23.68 (RowC) and 117.42/117.20/116.09 (prize), computed from the PROVED prescribed-slope ceiling (the pilot's 23.1-117.4 come from the free-slope number; both readings give <= ~960 and 1 - 2^-23). THEOREM 2 (free-slope form -- NOT PROVED, recorded): M <= (2r-1)/(h-1) = 383/447/959 on both triples is a DETERMINANTAL COUNT, called 'the true ceiling SHOULD be' by its own source (expC.py:352-364); the general-position step is exactly what Theorem 3 refutes; and note the banked proved table has the per-DATUM floor((2r-1)/(2h-2)) = 191/223/479 with 2*191 = 382 != 383, so the per-support form is not a corollary of the banked entry. The forcedness corollary does NOT use this form. THEOREM 3 (independence is necessary -- REFUTATION by exhibit): at n=20, q=41, K=4, h=3 the monomial pencil U = X^7, V = -X^6 on mu_20 has (all 77,520 supports scanned) 40 witnesses in 2 full mu_20-orbits, one of which is a SPREAD (max core 3 = K-1, ZERO self-collision) family of M = 20 supports with 20 DISTINCT slopes, condition rank 31 of 60 rows against 2r = 32 -- realised non-degenerately, and exceeding BOTH ceilings (10 prescribed, 15 free). Hence the ceiling bounds only independently-imposable families, never realised families as such, and 'RANK DEFICIT FORCES SELF-COLLISION' IS FALSE. Recorded, not claimed: that class buys DEFICIT WITHOUT EXCESS (40 witnesses vs mean supply 46.115). NOT claimed: any bound on |Gamma_lo|; that the ceiling discharges (H4) (it does not -- REPORT.md:63 'nothing here is proved about P-B'); L1 (banked); the free-slope ceiling (Theorem 2), which was NOT attained in the pilot's own extension test (max_greedy_spread = 12 vs 15); that the design space is exhausted (the pencil model is a 2h-dim slice of the 2(n-K)-dim word model -- the largest recorded gap); the SELECTOR CATCH (see pb_block_dichotomy). Gauge note carried: strip/genericity gates read off WORDS are vacuous under degree-<K gauge and must be stated on (alpha,beta) mod RS_K; this node is gauge-safe (it speaks only of C_S and condition rows). Provenance notes/pilots_20260802/pb_h4_hunt/{REPORT.md:14,29,31,47,48, FABLE_AUDIT.md:9-14,48}, checkpoints EXPC_lemma/rank/plant/orbit/extend.json + OFFICIAL.json.",
 "refs": [
  "background/nodes/pb_design_ceiling/statement.md",
  "background/nodes/pb_design_ceiling/proof.md",
  "background/nodes/pb_design_ceiling/verify.py"
 ]
}
```

## 5. `pb_block_dichotomy`

```json
{
 "id": "pb_block_dichotomy",
 "title": "P-B block dichotomy: for every coset-block geometry SPREADNESS and a LIVE SLOPE DIRECTION are incompatible -- deriving (SF-SELFCOLLISION)'s range m <= h rather than assuming it; with the collinearity necessary condition restated in the coordinates the source's own code actually uses",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Pencil model on D = mu_n <= F_q^* (n a 2-power, q prime): U monic of degree A = K+h, deg V < A; S (|S| = A) is an exact-A witness at slope z iff e_j(S) = alpha_j + z beta_j for j = 1..h, i.e. the moment vector E(S) lies on the affine line L = {alpha + z beta} of AG(h,q) -- the design space of degree-A pencils IS the space of affine lines, and a live slope direction means beta != 0 (the gauge-invariant strip gate). BLOCK FAMILY: a fixed core G and a pool of b pairwise-disjoint blocks of common size m disjoint from G; S_J = G u (union_{j in J} B_j) over a-subsets J, |S_J| = |G| + am = A. CLAIM 1 (spread threshold): |S_J ^ S_J'| = |G| + m|J ^ J'|, so the maximum pairwise core is A - m and, for b >= a+1, the family is SPREAD iff m >= h+1. CLAIM 2 ((SF-SELFCOLLISION), DERIVED not assumed): if m <= h then every member has a partner at core A - m >= K, so the whole planted family sits in Gamma_hi. CLAIM 3 (coset blocks and THE DICHOTOMY): for B_j = g_j mu_m, prod_{x in B_j}(X-x) = X^m - g_j^m, so R_{B_j}(Y) = 1 - g_j^m Y^m in F_q[Y]/(Y^{h+1}) (equivalently p_t(B_j) = m g_j^t if m|t else 0); if m > h then R_{B_j} = 1, every E(S_J) is the SAME point, beta may be taken 0 -- no live slope direction (one slope, a strip) -- while the family IS spread; if m <= h < 2m then R_{S_J} = R_G - (sum_{j in J} g_j^m) (R_G Y^m mod Y^{h+1}), so the moment vectors move affinely in the single scalar sum g_j^m along a direction supported from coordinate e_m -- a live direction exists -- but by Claim 1 the family is NOT spread. Hence for EVERY coset-block geometry spreadness and a live slope direction are INCOMPATIBLE, and (SF-SELFCOLLISION)'s operative window m <= h < 2m is derived. CLAIM 4 (collinearity is NECESSARY -- reconstructed): if every S_J is a witness of one pencil then the block moment vectors E(B_j) lie on one affine line of AG(h,q); for a = 1 unconditionally, for a >= 2 provided b >= a+2. Engine: R_{S u T} = R_S R_T for disjoint S,T in F_q[Y]/(Y^{h+1}), every R_S is a unit, and multiplication by a fixed unit is a linear bijection hence maps lines to lines; fix a-1 blocks and vary the last, then connect the resulting lines through their >= 2 common points. COORDINATE FLAG (load-bearing): the source states Claim 4 in POWER-SUM coordinates (expE.py:7-8) while its own code computes ELEMENTARY-SYMMETRIC ones (core.moment_vector); Newton's identities are NOT affine, so the two conditions differ in general (verifier: the p-collinear triple (0,0,0),(1,0,0),(2,0,0) has e-images of affine rank 2) -- the statement above is in e-coordinates, and for COSET blocks the two readings coincide (both give direction e_m), so Claims 2-3 are unaffected. HYPOTHESIS FLAG: the source writes b >= a+1; at b = a+1 collinearity is vacuous, and b >= a+2 is needed for a >= 2. HONESTY FLAG: the record asserts this result as 'proved + verified' but contains NO written derivation anywhere (only pb_h4_hunt/REPORT.md:15 and expE.py:4-14, which defers to the report); Claims 1-3 are written out from scratch here (the coset power-sum vanishing is the part the coordinator hand-verified, FABLE_AUDIT.md:19-23) and Claim 4 is reconstructed in corrected coordinates. NOT claimed: the NON-COSET RESIDUE (blocks of size m >= h+1 with collinear moment vectors) is OPEN -- measured FEASIBLE at 4 of 5 toy shapes (independently replayed here: 1140 blocks, richest line 28, 4 disjoint, family C(4,2) = 6, matching EXPE.json exactly) and closed at official scale only by a first-moment count the pilot itself says is NOT a theorem; core-varying and non-block families (out of scope); Gamma_lo = 0 for split-fibre as an IDENTITY consequence -- the SELECTOR CATCH: max core A-m >= K is attained only by adjacent label sets whose partners live at other slopes, so Gamma_lo = 0 additionally needs a SUPPORT-KEYED selector (support-lex first-match measured 0 at 18/18 across nu in [0.05,30]; a UNIFORM selector leaves ~q e^{-nu}, at official RowC 1/4 with nu = 3.0 that is ~2^187 >> 8n^3) -- the K1 closure is a JOINT identity-plus-selector statement and re-couples to the ratified PP4.0 compression-order class, and only the identity half is proved here; any P-B bound; any discharge of (H4). Provenance notes/pilots_20260802/pb_h4_hunt/{REPORT.md:15,60-63, expE.py:1-14, EXPE.json, FABLE_AUDIT.md:12-14,19-23}; consumed by the P-B TARGET's 2026-08-02 scope addendum as (SF-SELFCOLLISION).",
 "refs": [
  "background/nodes/pb_block_dichotomy/statement.md",
  "background/nodes/pb_block_dichotomy/proof.md",
  "background/nodes/pb_block_dichotomy/verify.py"
 ]
}
```

---

## Proposed edges

### A. Internal `req` / `ref` edges

| from | to | kind | justification |
|---|---|---|---|
| `f2_antipodal_descent_lemma` | `f2_parity_defect_certificate` | `req` | the certificate's COROLLARY 4 instantiates the degenerate branch **at deployed rung windows**, consuming that node's Corollary B (all `Delta` even) and Corollary C (`flat = 0`, which is what makes the certificate tight-but-empty there). **FLAG (E.a):** the certificate's Corollary 4 is proved in CONDITIONAL form ("if a window is parity-homogeneous...") and its Theorem 3 re-derives the `sigma`-odd mechanism inline, so the node is logically self-contained; if house convention reserves `req` for logical necessity of the main theorems, downgrade to `ref`. Coordinator's call. |
| `pb_block_dichotomy` | `pb_design_ceiling` | `ref` | pure cross-reference: the ceiling's NOT-claimed section routes the selector clause and the split-fibre story to the dichotomy node. Nothing is consumed. **Drop it if house convention omits pure-differentiation refs.** |

**No `req` between the two P-B nodes**: the dichotomy uses only counting
and coset algebra; it does not consume L1, L2 or the ceiling.

### B. `req` edges from banked nodes into the new four

| from | to | kind | justification |
|---|---|---|---|
| `xr_two_slope_cost_theorem` | `pb_design_ceiling` | `req` | **essential.** (L1) `proof.md:7-23` and (L2) `proof.md:96-108` are consumed verbatim; the P-B ceiling IS that node's Claim 3 re-gauged per support, and Lemma 0 is a one-line corollary of its L1. This edge is what makes the subtraction visible from both sides. |

Nothing else. In particular **no** banked edge into `pb_block_dichotomy`
(it consumes no banked lemma), and **no** banked edge into either F2 node
(both re-derive their model from scratch; the 30+ existing `f2_*`
background nodes are the 2026-07-10 Myerson/extras generation and share
no lemma with these two).

### C. `ev` edges into red/TARGET nodes

| from | to | kind | what it evidences |
|---|---|---|---|
| `pb_design_ceiling` | `xr_lowcore_spread_heart` | `ev` | the TARGET's 2026-08-02 scope addendum clause (c) says verbatim "the residual obligation is ADVERSARIAL PLANTING only (**design ceiling**; ...)". This node is that ceiling, with its honest scope and its refutation attached. |
| `pb_block_dichotomy` | `xr_lowcore_spread_heart` | `ev` | the same addendum clause (c): "In the split-fibre class every admissible live slope is PLANTED (**SF-SELFCOLLISION, proved**)". This node is where (SF-SELFCOLLISION) is derived, and it carries the SELECTOR CATCH that qualifies it. |

`xr_lowcore_spread_heart` is a critical **TARGET (red leaf)**: both
proposed in-edges are `ev`, and neither new node takes any edge FROM a
TARGET.

### D. **F2 lane: NO `ev` edge proposed — FLAGGED for the coordinator**

The natural consumer of both F2 nodes is the **F2 slice theorem /
(H-flat) / PP5.0** sub-lane, whose statement of record is a DRAFT
DOCUMENT, not a DAG node:
`notes/pro_briefs_20260801/responses/F2_SLICE_THEOREM_DRAFT.md` (with the
two 2026-08-02 amendments). A search of `dag.json` finds **no node** for
PP5.0, the slice theorem, (H-flat), or the K1 mass obligations
(O1)-(O3). The existing F2 reds/targets are
`f2_growing_order_myerson` (TARGET, Myerson at growing order — Gaussian
period-norm census deviation) and `f2_conditional_close` (CONDITIONAL on
it); `u2c_giant_tnull_dichotomy` is CONDITIONAL. **None of these is about
window flatness**, so attaching an `ev` edge to any of them would be an
invented dependency.

**Recommendation:** wire the two F2 nodes as standalone PROVED background
nodes now (they are exact, self-verifying and cited downstream by
`f2_fixed_sector/core.py:20-22`), and attach `ev` edges when the slice
theorem / PP5.0 obligation is itself minted. Alternative, if the
coordinator prefers no orphans: hold both until that node exists. See
AUDIT_CHECKLIST F0.c.

### E. Edges deliberately NOT proposed

- **No `req` out of any TARGET** into these nodes (red-leaf law); none of
  the four statements assumes any red content.
- **No `pb_l1_lemma` node and no edge for it** — see section 3. If the
  coordinator wants the duplicate discoverable, the
  `xr_two_slope_cost_theorem --req--> pb_design_ceiling` edge above
  already carries it.
- **Nothing into the band-lane six** — the band column is disjoint from
  the `<= K-1` stratum by the R2 partition of record; `pb_design_ceiling`
  neither strengthens nor weakens them. (It does, however, record a
  scope observation ABOUT `xr_two_slope_cost_theorem` — see
  AUDIT_CHECKLIST **F2.a**, which proposes a node-local addendum there
  rather than an edge.)
- **Nothing m2-related.**
