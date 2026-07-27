# l1_program_frontier

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

[transcribed 2026-07-27 from upstream experimental/notes/l1/l1_full_list_quotient_proof_program.md, read via git -C ../rs-mca show origin/main:<path>. ADJUDICATION: the note's HEADER status 'CONJECTURAL / PROOF PROGRAM' applies to its Conjecture 1 (Full-List Quotient-Budgeted L1); the individual lemmas cited here each carry their own 'Status: PROVED'. This node rests on the proved lemma, NOT on Conjecture 1.] THE L1 PROGRAM FRONTIER (Theorem J, Full-List Johnson Region, Status: PROVED). For any RS evaluation domain H of size n, C = RS[H,k], and received word U, with ImgFib_U(s) = {P : deg P < k, |{x in H : U(x) = P(x)}| >= s}: (1) if 2s > n+k-1 then |ImgFib_U(s)| <= 1; (2) if s^2 > n(k-1) then |ImgFib_U(s)| <= n(n-k+1)/(s^2 - n(k-1)). Since Q_1^list(U,s) <= |ImgFib_U(s)|, Conjecture 1 holds with a polynomial primitive remainder throughout the ORDINARY JOHNSON REGION s^2 > n(k-1), WITHOUT any quotient-budget term. THE FRONTIER (what this node pins): the remaining L1 difficulty is not ordinary pairwise packing but the SUB-JOHNSON range s^2 <= n(k-1); in that range the quotient ledger, sunflower reductions, and aperiodic extension counts are genuinely needed. SCOPE: this node claims the proved base region and the location of the frontier — it does NOT claim Conjecture 1.
