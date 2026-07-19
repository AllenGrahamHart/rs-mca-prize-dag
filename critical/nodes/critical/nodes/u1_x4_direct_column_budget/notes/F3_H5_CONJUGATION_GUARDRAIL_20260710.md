# SPLIT-PRIME CONJUGATION GUARDRAIL (2026-07-10, coverage-audit banking)

## The defect

The h=5 (and h=8) reciprocal-system machinery consumes rows derived from
"formal transpose", "Hermitian", and "unit" relations that treat cyclotomic
conjugation (zeta -> zeta^{-1}) as if it acted as a SAME-PRIME automorphism
of the residue field F_p. It does not: Aut(F_p) is trivial, and at split
primes (p = 1 mod n, the official corridor — where p splits completely in
Q(zeta_n)) conjugation PERMUTES the two primes above p rather than fixing
either. Any row of a reciprocal system justified by "apply conjugation and
reduce mod the same prime" is unjustified at official rows.

## Consequence

The h=5 central fixed-scheme payment (F3_H5_CENTRAL_FINITE_SCHEME_PAYMENT.md:
Bezout K = 81*72*63*54 = 19,840,464, Kn < n^3) is arithmetically correct AS
ARITHMETIC but its fixed-scheme premise is unsupported at official rows —
the payment is RETRACTED there. Likewise the h=8 worktree
mixed-volume/odd-chart payments (never banked on master; self-revoked in the
worktree). The honest official-row T4 frontier is h = 4, 5, 6, 7,
8(non-antipodal), plus the h > 8 band up to the (unpinned — catch #38) band
ceiling.

## The witness (independently replayed from master state alone)

n = 8192, p = 67,239,937 (p = 1 mod n, p > n^2), z = 5^((p-1)/8192):
P = {z^86, z^1410, z^6696}, Q = {z^1513, z^2110, z^2368} — disjoint,
equal e1 and e2, NON-TORAL; hit at dilation u = 1 under the canonical
convention. Replay: audit_witness_check_20260710.py (this directory).
This is the exact object on which the transpose/Hermitian rows fail. (It is
an h=3 activation event — consistent with H3-ACT, NOT a floor falsifier —
but it kills the conjugation-based h=5/h=8 payment chains.)

## Affected packets (consume ONLY with the guardrail; sampled-row
## certificates remain valid evidence at their stated rows)

- F3_H5_CENTRAL_FINITE_SCHEME_PAYMENT.md (the retracted payment)
- F3_H5_BASEFREE_RECIPROCAL_SYSTEM.md
- F3_H5_UNIT_NORM_RECIPROCAL_GATE.md
- F3_H5_RECIPROCAL_COMPATIBILITY_COMPILER.md
- F3_H5_RECIPROCAL_OPEN_COVER.md
- F3_H5_X83_TRIANGULAR_NORM_GATE.md (triangularization rows)
- the h=8 reciprocal/mixed-volume worktree packets (never banked; listed for
  the merge reconciliation)
- F3_H5_STRUCTURAL_REDUCTION.md (payment line; added catch #59 — the label sweep
  found it missed by the original retrofit)
- F3_H4_H5_BONUS_REDUCTION.md (h=5 classification premise, same chain; added
  catch #59)

Unaffected: the h=5/h=6/h=7 finite certificate banks at n=32/64/96/128 (pure
enumeration, no conjugation rows) — valid at their sampled rows; the h=2
chain; the entire h=3 ACT chain; the shift-pair weld.

## Provenance

Author's own scope revocation in worktree codex/f3-flip-20260708 (frozen
d670b7c) found the witness first; this banking re-derives it independently
on master state (audit agent, 2026-07-10) per the "re-derive, don't copy"
rule. Codex: reconcile on merge; the master-side edits are the two ledger
banners + label strings, this file, and the payment-packet annotation.
