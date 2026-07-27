# l1_defect_layer_bounds

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

[transcribed 2026-07-27 from upstream experimental/notes/l1/l1_full_list_quotient_proof_program.md, read via git -C ../rs-mca show origin/main:<path>. ADJUDICATION: the note's HEADER status 'CONJECTURAL / PROOF PROGRAM' applies to its Conjecture 1 (Full-List Quotient-Budgeted L1); the individual lemmas cited here each carry their own 'Status: PROVED'. This node rests on the proved lemma, NOT on Conjecture 1.] FIXED-DEFECT SUNFLOWER LAYERS ARE POLYNOMIAL (Lemma 3, Status: PROVED). For the sunflower received word, fix an integer d0 >= 0. The number of listed codewords P in ImgFib_U(s) whose agreement set misses at most d0 core points is at most sum_{d=0}^{d0} binom(k-1,d) binom(n-k+1,d+1). In particular, for fixed d0 this contribution is O_{d0}(n^{2 d0 + 1}) — polynomial. SCOPE: the bound is per fixed defect bound d0; it does not control defect growing with n (that residual is the program's next target).
