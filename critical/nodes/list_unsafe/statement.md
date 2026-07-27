# list_unsafe

- **status:** see dag.json (single source of truth; dag status PROVED)
- **closure:** proof
- **statement provenance:** written 2026-07-27 during the empty-statement remediation; see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md

## Statement

[transcribed 2026-07-27 from the upstream source read via git -C ../rs-mca show origin/main:experimental/notes/roadmaps/proof_sketch/s7_list_side.md#2, tagged 'PROVED-cited + verified']. THE UNSAFE HALF AT THE PRIZE GATE IS UNCONDITIONAL. By thm:qcore, quotient cores produce >= C(n/M - 1, k/M) codewords at agreement k + sigma whenever M | k and sigma < M — INDEPENDENTLY of q: a pure count, with no norm threshold and no value-set collision question, since the codewords are distinct by construction. Verified exponent check: log2 C(n/M-1, k/M) ~ (n/M) H(rho) (1017.7 vs 1024 at n = 2^20, M = 2^10). Crossing 2^128 requires a 2-power M | k with sigma < M <= n H(rho)/128, and dyadic domains supply every such scale (verified plentiful at n = 2^41). The resulting list-unsafe slack windows are [H/256, H/128] at rate 1/2 and the tabulated analogues at 1/4, 1/8, 1/16.
