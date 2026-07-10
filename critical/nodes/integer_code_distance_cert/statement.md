# integer_code_distance_cert

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Certify that the fixed k x N' integer matrix (from the row's chosen multipliers) has no ternary kernel vector of weight <= 2l' beyond the cyclotomic relations. A small, explicit, per-row object. Candidate certifiers: Delsarte-LP bounds instantiated on the specific system; structured multiplier DESIGN making distance provable by construction; weight-split enumeration hybrids (MITM below w_0, LP/structure above).

## Attack surface

BAKE-OFF FIRST (QA.18, toy prime chosen small so the height frontier leaves real work): (1) pseudo-Boolean/SAT with proof logging (VeriPB-style) — emits machine-checkable UNSAT certificates for exactly this finite claim, at arbitrary coefficient precision; dossier-ready format; (2) MITM bands as baseline; (3) LP/Delsarte as the theory-side candidate. Measure practical k vs the GV prediction; ship one complete printed toy certificate as the format exemplar. E24's BKZ hunt runs as the search-side complement.

## Falsifier

a ternary kernel vector of the k-multiplier system that IS a genuine collision (E24 would find it independently)
