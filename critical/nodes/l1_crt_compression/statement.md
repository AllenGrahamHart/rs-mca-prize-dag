# l1_crt_compression

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

[transcribed 2026-07-27 from upstream experimental/notes/l1/l1_full_list_quotient_proof_program.md, read via git -C ../rs-mca show origin/main:<path>. ADJUDICATION: the note's HEADER status 'CONJECTURAL / PROOF PROGRAM' applies to its Conjecture 1 (Full-List Quotient-Budgeted L1); the individual lemmas cited here each carry their own 'Status: PROVED'. This node rests on the proved lemma, NOT on Conjecture 1.] FULL-PETAL CRT COMPRESSION (Lemma 7, Status: PROVED). Assume the sunflower has no unused background. Let I be the exact set of petals touched by a non-planted listed codeword P and suppose every touched petal is full (S_i = T_i for i in I, S_j = empty for j not in I). With t = |I|, ell = sigma + 1, and the missed-core set D and defect d of Lemma 2, the defect is pinned to the window ell <= d <= (t-1) ell, and the codeword is determined by a CRT residue W_{D,I} of degree < t*ell (equivalently, by the vanishing of the top t*ell - d - 1 coefficients of that residue). This is the compression step that makes full-petal strata countable.
