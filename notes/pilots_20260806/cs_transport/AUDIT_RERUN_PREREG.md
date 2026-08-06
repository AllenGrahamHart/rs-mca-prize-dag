# Ideal/Galois multiplicity transport audit - remediation registration

- **date:** 2026-08-06
- **failed run:** Modal app `ap-Ou79WlOvA1ZtBIl8GuaZvV`
- **failure class:** source boundary-label error caught by an independent
  exact bisection

## Authorized correction

The source calculator leaves its bisection upper endpoint at the first
excluded integer `170,752,922,588`, but the imported prose called that value
`w*` and asserted exclusion only for `w>w*`.  The checker correctly computes
the complementary endpoint:

```text
last unexcluded = 170,752,922,587;
first excluded  = 170,752,922,588.
```

This rerun changes only the expected endpoint convention, the associated
result field names, and the output filename.  It retains every finite-field,
norm, tower, and tamper check from `AUDIT_PREREG.md`.  The source proof,
report, roadmap, and calculator wording are corrected in the same committed
change.  The first failed JSON remains immutable; the rerun writes
`cs_independent_audit_rerun_result.json`.

## Resource ceiling and decision

One Modal container, one CPU, 1 GiB RAM, 120 seconds, no retry.  A pass
authorizes construction of the PROVED supplier packet, subject to a separate
written proof audit.  Any other failure blocks promotion.
