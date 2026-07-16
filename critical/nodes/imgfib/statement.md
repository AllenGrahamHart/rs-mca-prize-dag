# imgfib

- **status:** CONDITIONAL (2026-07-14, catch #212; the 2026-07-13 PROVED promotion was an over-claim — mixed-petal bucket uncovered)
- **closure:** proof
- **refs (legacy repo):** ['wp_detail/wp_consolidation_sketch_extracts.md']

## Statement

For ALL received words U: #ImgFib_U(k+sigma) <= n^B once sigma log2(q_D) >= (1+eps) log2 C(n, k+sigma) and the quotient profile is budgeted.

## Attack surface

close the petal escape route (the only open branch of the Thm 21/B11 frontier); monomial instance already proved in quasi-poly range

## Falsifier

a toy word family with super-poly image fibers above the corrected reserve

## Ledger (migrated notes)

PROMOTED red -> amber (Codex flip packet, my replay 8/8; flip_packets/imgfib.md): statement-level assembly over the wired kids.

## SCOPE ADDENDUM (2026-07-16, wave-8 import)

Explicit-hypotheses narrowing accepted (audited): the statement's
count is read with the poly-field + lower-cutoff scoping recorded in
notes/mixed_petal_scope_audit_20260714.md (the Linnik-family
exponential floors sit OUTSIDE the entropy reserve — sigma >= Cn/log n
+ the reserve inequality are load-bearing, catch #213's sigma=1
subsumption note notwithstanding: the floors live at sigma=1 on rows
where the reserve FAILS by ~n bits). Machine check:
verify_scope_repair.py.
