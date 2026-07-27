# common_code_line_budget

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

THE COMMON CODE-LINE RESIDUAL BUDGET (upstream experimental/notes/m2/m2_common_code_line_residual_budget.md, 'PROVED finite theorem for MDS codes'; the verifier there is marked EXPERIMENTAL). Let C <= F^D be MDS of dimension k (so a nonzero codeword has fewer than k zeros on D), |D| = n, a an agreement threshold, and fix a received line ell_z = f + z g. Assume codewords c_f, c_g in C and a common support S0 subset D of size b with f = c_f and g = c_g on S0, and a + b - n >= k. Put Omega = D \ S0, f' = f - c_f, g' = g - c_g, h = max(1, a-b), and c0 = |{x in Omega : f'(x) = g'(x) = 0}|. Then every support-wise noncontained slope at agreement a satisfies |{x in Omega : f'(x) + z g'(x) = 0}| >= h; consequently if h > c0 then #{support-wise noncontained slopes} <= floor((|Omega| - c0)/(h - c0)). This is the support-wise replacement for the ordinary 'the received line is close to a code-line' statement: residual noncontained slopes must be paid by residual zeros OUTSIDE the common support. [transcribed 2026-07-27 from the upstream note]
