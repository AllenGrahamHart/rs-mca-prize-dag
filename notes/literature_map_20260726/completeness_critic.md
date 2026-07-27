<!-- Generated 2026-07-26/27 by the ultracode literature-sweep workflow wf_799040ff-a28
     (67 agents; 10 blind sweep lanes -> rank -> 14 deep reads -> per-doc cross-reference
     against the 23 open targets -> 3-lens adversarial hypothesis verification -> synthesis).
     PLANNER STATUS: banked as REFERENCE, not consumed. Every DIRECT_USE / import candidate
     below requires the normal audit gate (replay + subtraction check) before any node moves. -->

# COMPLETENESS CRITIQUE — Proximity Prize literature sweep (round 1)

**Scoping note (honest):** the synthesis text I received is **truncated mid-sentence inside §3 target 11** (`…certifies nonexistence outright when q > (2l')^{φ(N)}, and ot`). Everything below is judged against §1, §2.1–2.8 and §3 targets 1–11 plus the 11 lane summaries. Per-target sections for targets 12–23 and §§4–8 (including the "three attribution corrections" §1 forward-references) were **not in my input** — the parent must re-check (c)-class findings against those. All external claims I add below were verified by live search this session (accessed=yes at search-snippet level unless marked).

---

## (a) MODALITIES NOT SWEPT

| # | Missing modality | Evidence it matters | Fix |
|---|---|---|---|
| **A1** | **Author-homepage / mirror retrieval.** Every lane hit Cloudflare 403 on ePrint/ACM PDFs and *no lane tried an alternate host*. This is the sweep's largest single defect: ~30 load-bearing rows are `accessed=no`. | list-decoding lane: "Outstanding must-reads I could NOT access — the two STOC 2026 proximity-gaps papers (ACM 403)". **Both are freely available**: BCHKS25 full text at `https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf`; STOC26 ToC at `acm-stoc.org/stoc2026/accepted-papers.html` and `conference-publishing.com/toc/STOC26/noabs`. `eprint.iacr.org/2026/858.pdf` resolves in the search index. | Retry with `.pdf` suffix, ECCC `report/YYYY/NNN/download/`, ar5iv/alphaxiv, Semantic Scholar `openAccessPdf`, author pages, institutional repos. |
| **A2** | **Coding-theory venues.** Zero IEEE-IT / ISIT / ITW / DCC / FFA / AMC findings. The sweep is ePrint + arXiv(cs.CC, math.NT) only. | Justesen–Høholdt (IEEE-IT 2001), BKR (IEEE-IT 2010), Guruswami–Rudra (IEEE-IT 2006), van Lint–Wilson (IEEE-IT 1986) all `accessed=no` or absent. | Dedicated IEEE-IT/ISIT lane (see B1, B6). |
| **A3** | **Forward-citation graph.** No "cited by" pass on *any* load-bearing ancestor. | The #1 actionable import (Mattarei 2007) is reached only through one 2026 arXiv paper's quotation. | Semantic Scholar Graph API (`/paper/DOI:…/citations`), OpenAlex, zbMATH, MathSciNet, Google Scholar on: Mattarei 2007, García–Voloch 1988, Lenstra 1979, Dvornicich–Zannier 2002, Myerson, Lam–Leung. |
| **A4** | **Talk / video / program modality.** No conference-program or seminar sweep. | Habegger — target 5's "primary yield", marked `accessed=no` — has a public lecture: IAS, "On small sums of roots of unity", `https://www.ias.edu/video/puias/20170309-PhilippHabegger`. STOC 2026 accepted-paper DOIs exist and went unused. | Program pages + talk video + slides; seminar announcements are the *earliest* scoop signal and were never swept. |
| **A5** | **Security-audit / engineering blog layer.** grey-agentic concluded "no HN/Reddit threads; X activity essentially only @prz_chojecki" — but a live commentary layer exists and was missed. | `blog.zksecurity.xyz/posts/proximity-conjecture/`; `veridise.com/blog/learn-blockchain/proximity-gap-and-correlated-agreement/`; `hexens.io/blog/proximity-gaps` ("The Ethereum Proximity Prize"); `hozk.io` explainer. | These carry parameter tables and name who is working; cheap to sweep. |
| **A6** | **Formalization ecosystem** beyond ZkLinalg + simple-rbr-fri. | **ArkLib** — Lean 4 spec library that *already defines* polynomial folding, evaluation domains, RS codes and FRI; **EF Verified-zkEVM / `github.com/Verified-zkEVM/rust-lean`** applied to Plonky3 and RISC Zero. Prize explicitly encourages Lean. | This is a submission-path *and* co-credit modality, not just literature. |
| **A7** | **Non-English / thesis / monograph.** Zero. | Russian school (Shkredov, Konyagin, Kalmynin publish in Mat. Zametki / Izvestiya / Chebyshevskii Sb.); Chinese school (Li–Wan, Sci. China Math.; Shangguan/Ge/Xing). Explicit constants usually live in monographs: Konyagin–Shparlinski *Character Sums with Exponential Functions*; Berndt–Evans–Williams *Gauss and Jacobi Sums*; Lidl–Niederreiter. No PhD theses swept (theses routinely carry the explicit constants journals omit). | |
| **A8** | **Data/table modality.** No OEIS, no LMFDB, no Magma/PARI computational-NT notes. | Targets 14–23 are a norm-divisibility question and target 10 a subset-sum count — both have table/database analogues. | LMFDB cyclotomic fields + class numbers; OEIS on vanishing-sum weights. |

---

## (b) SUSPICIOUSLY EMPTY TOPIC CLUSTERS (ranked by expected value)

**B1 — Interleaved-code list decoding as a classical topic. ZERO findings; the grand LIST challenge is *literally about interleaved codes* `C^{==m}`.**
Verified live: **Gopalan–Guruswami–Raghavendra, "List Decoding Tensor Products and Interleaved Codes", STOC 2009 / SICOMP, arXiv:0811.4395, ECCC TR08-105** — proves the *list-decoding radius is unchanged under m-wise interleaving*, and gives an explicit worst-case list-size bound `ℓ(C^⊙m, η) ≤ A·ℓ(C,η)^B` for every `η < δ`, with sharper bounds via generalized Hamming weights. This is a published theorem about the exact quantity in the grand LIST challenge and appears **nowhere** in the synthesis. Also absent: Bleichenbacher–Kiayias–Yung (TCS 379, 2007), Coppersmith–Sudan, Brown–Minder–Shokrollahi (ISIT 2004), Schmidt–Sidorenko–Bossert, Puchinger–Rosenkilde (arXiv:1701.06555), Metzner–Kapturowski. **Risk: attribution/scoop exposure on target 1 and targets 14–23, plus a possibly free `m`-wise → `m=1` reduction.**

**B2 — Quantitative shifted-multiplicative-subgroup intersection. ZERO findings, yet this is the exact object of the sweep's #1 actionable import.** The additive-combinatorics lane found only the 2025–26 *qualitative* rigidity wave (Kalmynin / Kim–Yip–Yoo / Cochrane) and missed the quantitative core: **Heath-Brown–Konyagin** (Q. J. Math. 51 (2000) 221–235 — Stepanov's method, explicitly *"simplified earlier results by García and Voloch"*), **Shkredov** "On additive shifts of multiplicative subgroups" arXiv:1102.1172, "Intersections of shifts of multiplicative subgroups" Math. Notes 100 (2016) doi 10.1134/S0001434616070154, arXiv:1302.3839. Critically, a **multi-shift** explicit bound exists: `|R ∩ (R+μ₁) ∩ … ∩ (R+μ_k)| ≤ 4(k+1)(|R|^{1/(2k+1)}+1)^{k+1}` for `|R| > k·2^{2k+4}`. **DSP8 is a multi-shift statistic** — this is strictly the right shape and gives an import route *independent of the unread Mattarei*. Also missing: Bourgain–Garaev, Cilleruelo–Garaev, Corvaja–Zannier on `x^k+y^k=1` in subgroups.

**B3 — Diagonal / twisted Fermat point counts. ZERO findings — yet "the two-coset (twisted Fermat) extension" is named blocker (a) on the #1 item.** Verified live: García–Voloch's own theorem is stated for **`N_n(a,b,q)`**, i.e. the general (already-twisted) diagonal curve `ax^n + by^n = c`, with bound `≤ ((s²−s−2)/4 + 4/(s+3))n² + 2n(q−1−d)/(s+3) + d`, superior to Weil for `n ≥ √q/2`. **If this holds, blocker (a) may dissolve at the source.** Sources: García–Voloch, *J. Number Theory* **30** (1988) **345–356**; Zieve, "Rational points on some Fermat curves and surfaces over finite fields"; arXiv:1804.04442; Weil/Wolfmann/Baumert–McEliece diagonal-equation counts.

**B4 — Myerson's own literature. Target 5 is named `f2_growing_order_myerson` and cites zero Myerson papers.** Verified live: Myerson proved `k^{−N} ≤ f(k,N) ≤ N^{−k/4+o(1)}` **in the case both `k` and `N` are even** — i.e. the even/2-power regime the synthesis calls untouched *already has a published upper bound*. Also missing: Ben Barber, "Small sums of five roots of unity" arXiv:2104.15057; *JNT* "On sums of two and three roots of unity" (S0022314X18301045); *JNT* "Solution counts and sums of roots of unity" (S0022314X22000518); Habegger–**Dimitrov** norms of Gaussian periods. **And a fresh-preprint-lane miss inside its own window: arXiv:2607.06098, "Small sums of roots of unity" (July 2026).** Also zero on **uniform cyclotomy / semiprimitive Gauss sums** (Baumert–McEliece–Mykkeltveit) — the exact-evaluation branch when `−1` is a power of `p` mod `n`.

**B5 — Subset sums over finite fields / Li–Wan sieve / deep holes. Near-zero** (Li–Wan appears once, `accessed=no`, in a toolkit list). Target 10 is a subset-sum-of-roots-of-unity count and the KKH/Kambiré construction is literally `r`-fold subset sums. Live literature includes **sharp estimates for the number of `k`-element subsets of a multiplicative subgroup `H ⊂ F_q` summing to a given `b`** — target 10's object verbatim. Locators: arXiv:1702.03028 (subset sums of quadratic residues), arXiv:1910.05894 / FFA "Moment subset sums over finite fields", FFA "On the subset sum problem for finite fields" (S1071579721001064), Li–Wan *Sci. China Math.* 53 (2010) 2351–2362. Separately, **zero deep-hole findings** (Cheng–Murray; Cheng–Wan list/bounded-distance decodability; arXiv:1205.7016, arXiv:1205.6593, arXiv:1605.02423) despite CS25's counterexample being a **deep-hole line**.

**B6 — Cyclic-code minimum-distance machinery. ZERO findings, yet target 11 is `integer_code_distance_cert` at 2-power length.** Missing: BCH / Hartmann–Tzeng / Roos / **van Lint–Wilson AB ("shifting") method** (IEEE-IT 32 (1986) 23–40), and repeated-root / 2-power-length cyclic code literature. Also zero on **Prouhet–Tarry–Escott and Thue–Morse ±1 sequences** — the classical structure for *simultaneous* vanishing of several power sums at 2-power size, which is exactly the shape of the `L=2,4` WCL slots.

**B7 — Barker/Turyn-style 2-adic norm arguments. ZERO** (only Borwein–Choi). The standard Barker-sequence technique is "cyclotomic norm divisibility + 2-adic valuation in `Z[ζ_{2^s}]`" — precisely the technique targets 14–23 need, with a well-developed literature of worked instances.

**B8 — Arcs / MDS / Segre.** Headliner E is a "no 3 collinear" statement; zero findings from the arcs / MDS-conjecture literature where extremal "no `k` collinear" configurations over `F_q` are classified.

**B9 — Protocol primary sources.** §2.8 lists *consumers* but omits the papers that **state** the conjectures under attack: WHIR (ePrint 2024/1586 — Conj. 4.12 cited only via its refutation), STIR (2024/390), BaseFold (2023/1705), DEEP-FRI (2019/336), plus Binius / binary-tower and Blaze/Greyhound. Citing a conjecture only through its refutation is a citation-integrity risk under a peer-review-gated prize.

**B10 — Ring / AG / Galois-ring variants.** Only one item (Gao–Yang–Xu–Kan). Missing e.g. arXiv:2511.04135 (list decoding RS/FRS over Galois rings), arXiv:2604.13431 (explicit rank extractors & subspace designs via function fields), arXiv:2502.07308 (explicit codes approaching generalized Singleton via expanders).

---

## (c) SYNTHESIS CLAIMS NOT TRACEABLE TO A LANE FINDING

**C1 — The #1 actionable import is untraceable end-to-end.** The only lane that found Cochrane arXiv:2602.04111 (additive-combinatorics) says **nothing** about Lemma 5.4, Mattarei, `r(c) ≤ 3·2^{−2/3}t^{2/3}`, the hypothesis verification across `13 ≤ s ≤ 41`, or the numbers **2382.1 / 1412.4 / 1914.975 / 26% / 496.5 / 3.7116**. Mattarei is `accessed=no`. So the sweep's headline result rests on *one arXiv paper's quotation of an unread 2007 journal paper* plus unlogged in-house arithmetic. It should be labelled **unverified-blocking**, not "actionable".

**C2 — A digest was demonstrably wrong, and the same failure mode is unaudited everywhere else.** The list-decoding lane asserts Chen–Zhang STOC'25 "contains the line-meets-ball lemma"; the deep read's grep proves it does not (`"ball"` ×1, `"collinear"` ×0) and the true source is Srivastava Lem. 4.1. A second instance is admitted in target 1 ("the digest's `J_2 ~ 4n` was wrong by a factor `n`"). **Every remaining `accessed=no` + numbered-lemma citation inherits that failure rate** — notably **Habegger** (marked `accessed=no`, "via deep-read digest", yet cited with Lem. 6/8/9, Prop. 10, Lem. 16 and formulas, and designated target 5's "primary yield"), AGL23 §5, Justesen–Høholdt, Dvornicich–Zannier, Lam–Leung (*J. Algebra* 2000), Mann, Conway–Jones, Poonen–Rubinstein. **`accessed=no` + numbered-lemma citation is a self-contradictory state and should be a hard blocker class.**

**C3 — A provenance conflation flagged by a lane was then ignored.** bib-resolver: ePrint 2026/1463's live title is "Shortening Bounds for Reed–Solomon MCA" while the bibitem calls it "MDS paving bounds … v9.2", and the v9.2 paving paper exists as a *separate* in-repo file — "the bibitem apparently conflates two related Chojecki manuscripts". The synthesis nonetheless verifies **all** ChoShort26 content against in-repo `RS_MCA_Paving_v9.2.tex` with ePrint access = landing page only. Same pattern for ChoConj26 (2026/1479 PDF unread; local file is `Conjectures_and_Barriers_RS_MCA_v4_1.tex`, version correspondence unverified). **Consequence: §1 items 4–5 and the target-2 `DIRECT_USE` inherit an unverified paper↔file identification, and the credit conclusion "must cite 2026/1463" could attach to the wrong document.**

**C4 — Untraceable assertion:** "Headliner C is unscooped; **the KKH group's circulated preprint is the one priority-date risk**." No lane reports any KKH circulated preprint bearing on the WCL slots (KKH26 is proximity-gap failure). Supply a locator or delete.

**C5 — Lane→synthesis information loss + an in-house argument presented as sweep output.** §1 item 6's "char-0 emptiness is free by degree (`deg Φ_{512L} = 256L` = window width)" is **not** the roots-of-unity lane's argument (Lenstra Thm 2.2 antipodal pairing / Lam–Leung / Sivek parity), and is claimed "strictly stronger and simpler" without the check shown. Meanwhile the lane's **sharpest single result — the hand-verified falsifier `1 + ζ + ζ³ = 0` in `F_9` with `ζ = 1+i` of exact order 8, an odd-weight reduced signed relation at 2-power order** — never surfaces in the synthesis, although it is the crispest available statement of why the mod-`q` layer is live and why char-0 parity cannot be transported.

**C6 — Scope-rule violation.** The synthesis declares "every claim below is sourced from the sweep inputs", but at least six blocks are **derived in-house**, not sourced: the Mattarei numerics (C1); the KKH ceiling formula `1 − ρ − 2/s*` and its four values; the ChoShort26 HD2 `J_2` recomputations; the Danny/PR-#1106 crossover numbers; the `N=8, m=5` "derived route cut"; the target-5 "cheapest experiment". Add an explicit `derived=yes` flag or the scope rule is false.

**C7 — Unreconciled cross-lane contradictions.** additive-combinatorics lists arXiv:2601.10047 as a *live* cross-lane flag; fresh-preprints reports it **withdrawn 2026-06-10**. The synthesis takes withdrawal (correct) but doesn't record that a lane is carrying stale state. Likewise Doron–Venkitesh arXiv:2404.00206 is marked "withdrawal reported in search metadata — verify before citing" and **was never verified** (it still surfaces as a live PDF in search).

**C8 — Internal inconsistency:** "Eight pre-registered direct-hit hypotheses were tested adversarially; **zero survived**. **Two survived** as corrected-attribution findings." Restate.

**C9 — Coverage arithmetic (for the parent to confirm in the truncated remainder):** §1 asserts 23 targets; §3 as delivered enumerates targets 1–11 and §1 item 6 treats 14–23 collectively. **Targets 12 and 13 are never itemized anywhere in the delivered text.** Verify they have per-target lead tables.

---

## (d) HIGHEST-VALUE ROUND-2 QUERIES (ranked, exact strings/URLs)

**D1 — BLOCKING, target 6: get Mattarei + García–Voloch in hand and run the NSB2 consistency check.**
- `doi:10.1016/j.ffa.2006.09.005` — exact title confirmed: S. Mattarei, *"On a bound of Garcia and Voloch for the number of points of a Fermat curve over a prime field"*, **Finite Fields Appl. 13 (2007) 773–777**.
- Author copies: `Mattarei "Fermat curve over a prime field" site:arxiv.org`; Mattarei homepage (Univ. of Lincoln UK / formerly Trento).
- García–Voloch, *"Fermat curves over finite fields"*, **J. Number Theory 30 (1988) 345–356** — pull from Voloch's own preprint pages: `https://www.math.canterbury.ac.nz/~f.voloch/uc-preprint.html`, `https://web.ma.utexas.edu/users/voloch/preprint.html`. **Specifically check whether the `N_n(a,b,q)` statement is already the twisted count → would dissolve named blocker (a).**
- Forward citations: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.ffa.2006.09.005/citations?fields=title,year,externalIds`; same for GV via zbMATH/MathSciNet.
- Deliverable: resolve `1.88988 < 2^{5/3} = 3.1748` against the PROVED NSB2 floor before any downstream use.

**D2 — BLOCKING, targets 6/3/4: quantitative shifted-subgroup intersections (Mattarei-independent second route).**
- Heath-Brown & Konyagin, Q. J. Math. **51** (2000) 221–235.
- Shkredov arXiv:1102.1172; Math. Notes **100** (2016) doi `10.1134/S0001434616070154`; arXiv:1302.3839.
- Queries: `"intersection of shifts of multiplicative subgroups" explicit constant Stepanov`; `|G ∩ (G+1)| multiplicative subgroup upper bound k shifts`; `Corvaja Zannier "x^k + y^k = 1" solutions in subgroups`.
- Deliverable: instantiate `4(k+1)(|R|^{1/(2k+1)}+1)^{k+1}` at our `k`, `|R| = n` and compare against allowance **1914.975**.

**D3 — SCOOP/ATTRIBUTION, grand LIST challenge: interleaved list size.**
- Read **arXiv:0811.4395 / ECCC TR08-105 / STOC'09 / SICOMP** (Gopalan–Guruswami–Raghavendra): the "LDR unchanged under `m`-wise interleaving" theorem and `ℓ(C^⊙m,η) ≤ A·ℓ(C,η)^B`. **Question to answer: does the grand LIST challenge reduce to `m=1` for free, and are any of targets 14–23 corollaries?**
- BKY, *TCS* 379 (2007), `sciencedirect.com/science/article/pii/S0304397507001351`; Coppersmith–Sudan; Brown–Minder–Shokrollahi ISIT 2004; Schmidt–Sidorenko–Bossert; Puchinger–Rosenkilde arXiv:1701.06555.
- Query: `worst-case list size interleaved Reed-Solomon "generalized Hamming weights" bound`.

**D4 — target 5: the Myerson canon + the missed July-2026 preprint.**
- **READ FIRST: arXiv:2607.06098, "Small sums of roots of unity" (2026-07)** — inside the fresh-preprint lane's own window and missed.
- Barber arXiv:2104.15057; JNT S0022314X18301045; JNT S0022314X22000518; Habegger–Dimitrov "The Norm of Gaussian Periods".
- Paywall bypass for the target-5 primary: IAS video `https://www.ias.edu/video/puias/20170309-PhilippHabegger`.
- Query: `semiprimitive Gauss sum uniform cyclotomy exact Gaussian period value "-1 is a power of p" mod n`.

**D5 — target 10: subset sums inside a multiplicative subgroup.**
- Query: `"number of k-subsets" multiplicative subgroup finite field sum to b Li-Wan sieve sharp estimate`.
- arXiv:1702.03028; arXiv:1910.05894; FFA S1071579721001064; Li–Wan *Sci. China Math.* 53 (2010) 2351–2362.
- Purpose: an unconditional count for the center set — exactly where "KKH admissible set ∩ prize cap = ∅" was concluded.

**D6 — targets 11 + 14–23: cyclic-code and PTE machinery.**
- van Lint–Wilson, "On the minimum distance of cyclic codes", IEEE-IT **32** (1986) 23–40 (AB/shifting); Hartmann–Tzeng; Roos.
- Query: `lower bound minimum distance cyclic code length 2^s over F_q q ≡ 1 mod 2^s shifting method`.
- Query: `Prouhet-Tarry-Escott Thue-Morse simultaneous vanishing power sums 2^s signed support window`; Borwein, *Computational Excursions in Analysis and Number Theory* (PTE chapter).
- Query: `Barker sequence conjecture cyclotomic norm 2-adic valuation Z[zeta_{2^s}] Turyn`.

**D7 — MECHANICS, all lanes: fix PDF retrieval before round 2, then obtain the still-unread critical set.**
- Verified alternates: `https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf` (BCHKS25 full text — closes the list-decoding lane's own flagged blocker); `https://acm-stoc.org/stoc2026/accepted-papers.html`; `https://www.conference-publishing.com/toc/STOC26/noabs`; ECCC `eccc.weizmann.ac.il/report/YYYY/NNN/download/`; direct `eprint.iacr.org/NNNN/NNNN.pdf`; ar5iv / alphaxiv / Semantic Scholar `openAccessPdf`.
- **Highest-value unread document in the whole program: ABF ePrint 2026/680 v3.** The entire sweep reads a *v2 reconstruction* (`rs-mca:/open-proximity.tex`, header warns "not the authors' original TeX source"); the survey lane marks the v3 delta **UNVERIFIED**, and two lanes independently report v3 adds a KKH comparison, concrete attack estimates and **new MCA lower bounds**. Everything in §2.1/§2.2's `Relation = C/F` column is provisional until v3 is read.
- Then: KKH26 (2026/782), Jo (2026/1432), ChoShort26 (2026/1463), ChoConj26 (2026/1479), CS25 (2025/2046), Hab25 (2025/2110), S-two (2026/532), AGL23 body, Dvornicich–Zannier (ILL if paywalled).

**D8 — cheap modality fills.**
- `https://blog.zksecurity.xyz/posts/proximity-conjecture/`; `https://veridise.com/blog/learn-blockchain/proximity-gap-and-correlated-agreement/`; `https://hexens.io/blog/proximity-gaps`; `hackmd.io/@zkpunk/CS25`.
- **ArkLib** + `github.com/Verified-zkEVM/rust-lean`: check whether MCA/CA statements are already *stated* in Lean (ready-made formal target **and** co-credit risk).
- Queries: `site:ethresear.ch proximity gap correlated agreement`; `site:zkresear.ch FRI soundness Johnson bound 2026`; `"proximity prize" submission peer review accepted 2026`.

**D9 — scoop watch (recurring).** `("correlated agreement" OR "proximity gaps") seminar talk 2026 smooth Reed-Solomon multiplicative subgroup` restricted to simons.berkeley.edu, ias.edu, weizmann.ac.il, epfl.ch, stanford.edu, unibocconi.it seminar pages. Plus a standing arXiv `math.NT` + `cs.IT` + `cs.CC` new-submissions tail from 2026-07-15 onward — the sweep's window nominally ends 2026-07-26 and already missed arXiv:2607.06098.

**D10 — hygiene: replicate the grep that caught Chen–Zhang.** Full-text grep the remaining "we are unscooped" headliners against their nearest neighbours: `interleav`, `collinear`, `ball`, `slot`, `window`, `Proth` across Srivastava 2410.09031, Garg 2502.14358, GGR 0811.4395, BKY, KKH26, Kambiré 2604.09724, Jo 2026/1432. Also re-check arXiv:2404.00206's abs page directly to settle the Doron–Venkitesh withdrawal question that round 1 left open.