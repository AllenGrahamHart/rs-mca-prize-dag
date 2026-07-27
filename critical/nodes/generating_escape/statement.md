# generating_escape

- **status:** see dag.json (single source of truth; dag status PROVED)
- **closure:** proof
- **statement provenance:** written 2026-07-27 during the empty-statement remediation; see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md

## Statement

GENERATING ROWS ESCAPE THE POLE MECHANISM [transcribed 2026-07-27 from proof_sketch/s6_extension_lift.md#3, tagged 'verified']. The pole mechanism requires F \ B nonempty, i.e. a NON-generating row (q_gen < q_line). Admissibility forces such rows to be tiny at the base: q_line = q_gen^m with m >= 2 and q_line < 2^256 give q_gen < 2^128, hence base gate B*_gen = floor(q_gen/2^128) <= 1 and base reserve tau*(rho,q_gen) >= H(rho)/128. For PRIME fields the question vanishes (no proper subfields); for extension rows the minimal field containing mu_n is F_p^ord, and the pinned row is exactly the generating case (ord(17 mod 512) = 32). Therefore: generating rows (q_gen = q_line) leave B_ext degenerate and the S2 corridor stands; non-generating rows are bound by the imported S7 window.
