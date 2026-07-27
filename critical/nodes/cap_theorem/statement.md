# cap_theorem

- **status:** see dag.json (single source of truth; dag status PROVED)
- **closure:** proof
- **statement provenance:** written 2026-07-27 during the empty-statement remediation; see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md

## Statement

THE UNIVERSAL CAP (Paper D, tex/cs25_cap_v12.tex; the cap line of proof_sketch/s2_paid_ledger.md#3-#4 reads 'cap (proved): eta = 2^-9 (2^-10 at rho = 1/16)'). The Paper D cap construction proves the row UNSAFE at reserve eta = 2^-9 (2^-10 at rate 1/16) — i.e. delta* <= cap — and, per the same source, it does so REGARDLESS of the zone-(b) resolution. Audit state: v12 audit DONE (#177, integrated e7042160; one rounding fix patched by the maintainer). CAVEAT carried from the blueprint: the universal cap is stated 'modulo the imported Crites-Stewart conversion'; v12's self-contained half-Johnson CA variant mitigates this, and the submission dossier's bridge row must state which variant it uses. SCOPE: this is the cap (an upper bracket on delta*) only — it does NOT pin delta* at the adjacent grid point, which is the separate unsafe_at_crossing obligation. [statement written 2026-07-27]
