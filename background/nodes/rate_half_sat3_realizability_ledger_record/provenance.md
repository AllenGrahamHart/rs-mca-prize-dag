# Provenance

The ledger spans rounds 33-36: the round-33 cell values, round 34 bank 4's
automorphism quotient and TCAP re-pose, round 35 bank 4's gate and m=1
double calibration, and round 36 bank 2's (ERC2)-forced dim-18 correction
and stacking. Drafted as a standalone package by pilot `r37_mint_drafts`
(round 37, bank 2, package 10 of 10), which raised the BLOCKING D9 flag
(the gate's expression never printed) and the sign-convention flag.

D9 was resolved by the coordinator at round-37 triage: the formula was
found banked at `notes/pilots_20260811/r35_rout_layer_a/REPORT.md`
(section D3.3) and the +13.75 calibration re-verified by hand. Wired
2026-08-11 in the task-#41 mint session with the formula printed in the
statement and computed at both calibration points by the audit; the
round-38 inhabitation of the +62.5-bit T = 3 cell is recorded as a wiring
note. Requires edge: the (ERC2) node. No proof.md (HEURISTIC — there is
nothing to prove; the arithmetic is machine-checked inline). No Modal
computation or external library was used.
