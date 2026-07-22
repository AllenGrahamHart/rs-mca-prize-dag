# Upstream crosswalk

- repository: `przchojecki/rs-mca`
- reviewed pin: `18cfc199d4612f5dfc01bf6c0155a65a1eaa3832`
- original integration commit: `b9e0feaaa`
- source:
  `experimental/notes/l1/l1_full_list_quotient_proof_program.md`
- imported results: Lemma B3, *Maximal Background-Anchor Injection*, and
  Proposition B4, *Maximal Deficit-Background Stratum Ledger*

The local proof is self-contained and uses local `ell=sigma+1` notation. The
statement preserves upstream's exact fixed-pattern exponent and stratum
ledger. It adds only explicit DAG scope: these are per-chart payments and do
not settle non-intrinsic first-owner aggregation.
