# l1_program_frontier

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

[transcribed 2026-07-27 from upstream experimental/notes/l1/l1_full_list_quotient_proof_program.md, read via git -C ../rs-mca show origin/main:<path>. ADJUDICATION: the note's HEADER status 'CONJECTURAL / PROOF PROGRAM' applies to its Conjecture 1 (Full-List Quotient-Budgeted L1); the individual lemmas cited here each carry their own 'Status: PROVED'. This node rests on the proved lemma, NOT on Conjecture 1.] THE L1 PROGRAM FRONTIER (Theorem J, Full-List Johnson Region, Status: PROVED). For any RS evaluation domain H of size n, C = RS[H,k], and received word U, with ImgFib_U(s) = {P : deg P < k, |{x in H : U(x) = P(x)}| >= s}: (1) if 2s > n+k-1 then |ImgFib_U(s)| <= 1; (2) if s^2 > n(k-1) then |ImgFib_U(s)| <= n(n-k+1)/(s^2 - n(k-1)). Since Q_1^list(U,s) <= |ImgFib_U(s)|, Conjecture 1 holds with a polynomial primitive remainder throughout the ORDINARY JOHNSON REGION s^2 > n(k-1), WITHOUT any quotient-budget term. THE FRONTIER (what this node pins): the remaining L1 difficulty is not ordinary pairwise packing but the SUB-JOHNSON range s^2 <= n(k-1); in that range the quotient ledger, sunflower reductions, and aperiodic extension counts are genuinely needed. SCOPE: this node claims the proved base region and the location of the frontier — it does NOT claim Conjecture 1.

## Addendum 2026-08-03 — maelcar #1145/#1146 citation discipline

External evidence, unmerged: PRs #1145 (head `605cc16ff22dd8c02e2780068e0728d16faa7bbd`)
and #1146 (head `f7d8734ead8d673a17e17ca3a5c6adc174e788aa`), maelcar,
experimental/. Trust: their scalar auditors were REPLAYED by us and PASS
(terminal VERIFIED); the reduction/exhaustiveness stages and the C++ census
are UNREPLAYED. Nothing is imported as a theorem and no status moves here.

Subtraction is EMPTY BOTH WAYS at present: our repo contains no `ell = 11`
object, and their fixed-`ell`, fixed-shape, small-prime constants do not touch
our asymptotic sub-Johnson targets (`imgfib`, `l1_mixed_petal_amplification`,
`petal_mixed_amplification`).

**Domination check resolved (2026-08-07).** In the background-free coset
sunflower used by #1145/#1146,

```text
k-1=m*ell,       s=(m+1)ell,       n>=(m+tau)ell,       tau>=5.
```

Therefore

```text
s^2-n(k-1)
 <= ell^2((m+1)^2-m(m+tau))
  = ell^2(1-m(tau-2)) < 0.
```

Every such exact-five row is strictly sub-Johnson, even on the smallest
support domain; enlarging to the ambient evaluation domain only strengthens
the inequality. Theorem J does not cover #1145/#1146. Their sharp finite
constants are genuine special-case information, but they still do not move
our official asymptotic L1 frontier.

**CITATION DISCIPLINE (binding if we ever cite #1146).** Say "for the two
parity supports", NEVER "for ell = 11 exact-five". Their `S_6 <= 20` is proved
for 2 of 252 supports; #1145's own certificate field
`remaining_global_obligations[0]` asks only for `S_6 <= 21` on the other 250.
Also never cite the envelope `(20,22,24,27)` as one state's spectrum — its
increments increase, so no single state attains it; their own witness gives
`(20,22,24,25)`.
