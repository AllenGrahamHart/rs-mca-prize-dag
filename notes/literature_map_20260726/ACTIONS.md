# Literature sweep — planner actions (2026-07-27)

Distilled from `LITERATURE_MAP.md` (115KB, workflow wf_799040ff-a28, 67 agents).
**Nothing here has been consumed into the DAG.** Every import below is a
CANDIDATE and must pass the normal audit gate (independent replay + subtraction
check) before any node moves. Grades are the sweep's; the verdicts are mine.

## A. Verdict on shortcuts

All 8 pre-registered direct-hit hypotheses REFUTED under 3-lens adversarial
verification (`hypothesis_verdicts.json`). **No external result closes any of the
23 open targets.** The recurring killer is regime mismatch — most instructively
the seeded Lam–Leung idea (characteristic-0 theorem vs our characteristic-p
slots), which our own `S5_LAM_LEUNG_TRANSPORT.md` had already handled.

## B. Credit / framing corrections owed (before ANY outward-facing text)

1. **PR #1106 (headliner D) is dominated.** DannyExperiments'
   agreement-weighted transverse-secant theorem
   (`experimental/notes/thresholds/agreement_weighted_transverse_secant.md`,
   merged upstream ea4eb078) has a *weaker* hypothesis (per-witness
   transversality, implied by our global CF1) and a *stronger* constant —
   symbolic ratio `(nu+h)/(h(nu+1)) ~ 1/(nu+1)`. **Verified independently by
   exact arithmetic 2026-07-27:** at KoalaBear he pays nu=10
   (78,289,526,705,722,101 <= B*) where ours fails (861,057,176,799,343,503);
   he first fails at nu=11. ACTION TAKEN: #1106 reverted to DRAFT. Rework as a
   corollary or drop.
2. **Headliner E (collinearity floor) is a known corollary.** The line/Hamming-
   ball lemma is **Srivastava arXiv:2410.09031 Lemma 4.1** (not Chen–Zhang —
   full-text grep shows "collinear" appears zero times there), relayed as Garg
   arXiv:2502.14358 Lemma 4.2. Our floor is the k=2 case, and it is
   independently coextensive with Przemek's own `thm:affine-span-list` at s=1
   (`grande_finale.tex:498`) — both fire at exactly a >= 1,466,015,503,701.
   Present as corollary + citation; no in-repo novelty claim to retract.
3. **Headliner F is now an audit of published work.** ChoShort26 (ePrint
   2026/1463, rec. 2026-07-17) publishes the four maximal-dimension Proth prize
   rows, their B values, the two-sign integer certificate, and the exact
   thresholds a* = n − B + 1. Our four-adjacent-pair replays must cite it.

## C. Route-moving intelligence (the payload)

- **Target 2 `rate_half_band_closure` — the biggest movement on the board.**
  ChoConj26 (ePrint 2026/1479) eq. (5.3) **is** this target at the official
  KoalaBear row, and it publishes a rigorous unsafe certificate at the
  predecessor agreement 1116047 — **collapsing the band to one agreement step
  wide**. Independently, KKH26 (2026/782) + Kambiré (arXiv:2604.09724) truncate
  the band from ABOVE on our exact domain class (per-row ceiling 1 − rho − 2/s*).
  Squeeze from both sides is now the cheapest live route to a red.
- **Target 6 `f3_h3_dsp8_correlation_bound` — one real import candidate, with a
  contradiction attached.** Mattarei's refinement of Garcia–Voloch, quoted as
  Lemma 5.4 of Cochrane arXiv:2602.04111: `r(c) <= 3*2^(-2/3) t^(2/3)`, with
  hypotheses (k>=4, t <= k^3/4) verified across the ENTIRE f3 official window.
  Substituted for our in-house 51/16 on the order-n quotient-line factor alone,
  the DSP8 class-blind coefficient falls 2382.1 -> 1412.4 against allowance
  1914.975 (**26% margin**), clearing the PROVED NSB4 barrier on p = 1 mod 3.
  **BLOCKERS — do not consume before resolving:** (i) Mattarei's 1.88988 sits
  BELOW our own PROVED NSB2 floor 2^(5/3) = 3.1748; these are only compatible if
  his auxiliary construction lies outside the NSB1 one-auxiliary-polynomial
  class — resolve or one of the two is wrong; (ii) the two-coset (twisted
  Fermat) extension for t not in H is unproved; (iii) **the Mattarei paper
  itself was NOT accessed** (Finite Fields Appl. 13 (2007) 773-777) — the
  constant is second-hand.
- **Target 8 `l1_mixed_petal_amplification` — a proved external barrier.**
  ChoConj26 Prop. 3.5 (ambient moment-order barrier, eq. 3.7): an n^C loss costs
  21C bits at n=2^21 against margins of 22.1969 bits (KoalaBear MCA) and 3.2589
  bits (Mersenne-31 MCA). Any polynomial-loss petal bound with C >= 2 decides
  nothing at any benchmark row. This constrains the route, not the truth.
- **Targets 14–23 (WCL slots) are entirely ours and entirely arithmetic.**
  Char-0 emptiness is **free by degree** — deg Phi_{512L} = 256L equals the
  support-window width [0,256L) exactly for L in {1,2,4} — strictly simpler than
  the Lenstra/Lam–Leung/Mann/Conway–Jones/CDK route. All live content is the
  mod-q norm-divisibility question under v_2(q−1) >= 41, q < 2^256; no external
  theorem addresses it. Lam–Leung's own char-p sequel (arXiv:math/9605216)
  states there is "no viable conjecture" on the char-p weight set, and at
  official rows Phi_{512L} splits completely mod q, so their Thm 2.6 transfer
  hypothesis fails maximally. **Priority-date risk:** KKH (Krachun–Kazanin–
  Haböck, ePrint 2026/782) work in exactly this object class with the same
  norm-gate reformulation; their bounds are vacuous at q < 2^256 (7^256 ~ 2^719)
  so there is no result overlap — but the group is close.

## D. Prize rules (hard gates confirmed from proximityprize.org)

$1M pool, Ethereum Foundation, judges Boneh/Fenzi/Arnon (themselves ineligible).
**Peer-reviewed acceptance is REQUIRED**, plus public ePrint/arXiv posting — the
first public timestamp counts as the submission date. No deadline, no rubric, no
leaderboard, no announced winners. Partial and complementary results may SPLIT
awards. AI-aided work is allowed if human-verified. ABF rev-2 Definition 2.12 is
now coset-form verbatim, vindicating our conservative coset reading.

## E. Process fix (applied)

The #1106 miss happened because the subtraction check covered
`grande_finale.tex` + `proximity_prize_results_v4.tex` but NOT the merged
`experimental/notes/**` corpus, where the dominating theorem lived. Hard Law 5
in `notes/OPUS5_WORKER_GOAL.md` widened accordingly.

## F. Open follow-ups for a later round (see completeness_critic.md)

Access failures to retry: the ABF and CS25 PDFs (Cloudflare 403 throughout), and
the Mattarei 2007 paper (blocker (iii) above).
