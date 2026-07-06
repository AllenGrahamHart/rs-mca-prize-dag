# xr_target_budget_audit

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Compute, per clean-rate decision row (from the census/#213 pipeline + the E14 gate-margin conventions reconciled): the exact integer slack s = B* - B_quot(A) - B_tan(A) at the safe-side candidate A. TWO WORLDS: s = 0 => the exclusion is true rigidity (no unpaid support at all — the emptiness form, the hard band problem); s >= 1 => the singleton obstruction DISSOLVES and the requirement becomes bounded-multiplicity forcing (no pair has s+1 unpaid deep slopes) — attackable by the proved multi-slope machinery (two-slope intersection, deep-mca Case (a), eliminant dichotomies: overlapping deep supports force structure). Mechanical arithmetic; the problem's CLASS depends on the answer.

## Attack surface

read s off the exact quotient counts at the candidates (census_exact_counts) minus the tangent staircase; reconcile E14's gate-margin (GM) conventions; note a trivial construction gives SOME pair one deep bad slope, so s = 0 would make the target tight against trivially-existing objects — suspicious, and worth double-checking the decision point's location before concluding rigidity is needed

## Falsifier

n/a (an audit)

## Ledger (migrated notes)

DONE (verifier 49/49): s >= 1 ASTRONOMICALLY at every clean-rate candidate — log2 s ~ 122.0 (Row C) to 127.9 (prize-max): B_quot is STRICTLY ZERO at the candidates (j odd — parity kills the deciding dyadic scales), so essentially the whole B* budget is the aperiodic allowance. Only the pinned calibration row (rate 1/2) gives s = 0 exactly at A=507 (reproducing the proved tangent pin — rate 1/2's knife-edge nature confirmed at calibration). No verdict depends on the B_tan ambiguity or collision direction. FLAG: dihedral-stratum mass excluded from the formula — if E25 finds it real AND it populates odd-j candidates (odd supports = pairs + one of {1,-1}, so not parity-excluded), the budget shrinks; re-run with the dihedral column then. | E30 SHARPENS THE FLAG: the clean-rate candidates sit at ODD j, and dihedral-type words DO exist there in the anti-reciprocal form — the dihedral budget column, when E25 lands, must use the corrected -+a^{-j+2m} clause, not the even-j form. | MANDATORY FOLLOW-UP (QA.21): re-run the budget with the DIHEDRAL COLUMN — E25 says the mass is real, E30 gives the odd-j anti-reciprocal clause for the candidates. The clean-rate s = 2^122+ could shrink; compute B_dih at each candidate exactly. | QA.21 NEGATIVE (76/76 green, GAP QA21-G1): the crude dihedral column exceeds B* at EVERY clean-rate candidate (+292/+158/+52 bits at Row C; ~1e11-bit scale at prize-max); the E26 window model gives 0 at odd j but provably omits the fixed-point branch (E30). NO in-repo lemma bounds per-pair dihedral simultaneity. The s >= 2^122 verdict is now CONDITIONAL on dihedral_staircase; the audit's status reverts to TARGET pending that lemma. Honest arc: the requirement computation giveth (the poly allowance) and taketh away (the dihedral column). | CLOSED by the poly-forcing compiler (52/52, exact integers): 16 n^3 <= s_lo(A) at all six candidates (prize rows tight at 29 n^3); QA21-G1 DISSOLVES — the dihedral/extension columns fold into R_post, so no separate B_dih subtraction exists; the staircase req edge removed accordingly. | QA.22 REQUIRED (X-4): re-run the candidate budget with the staircase column — staircase supports inflate SUPPORT counts not slope counts, but the census/dossier B_quot documentation and the list-side budgets need the exact staircase binomials per candidate (~2^105-115 at prize rows vs B* ~ 2^128: expected to fit with 13-23 bits of room; verify exactly). | QA.22 GATE PASSED (27/27, exact big integers): the four-column split fits under B* at ALL SIX candidates — Row C staircase margins 22.2/55.9/39.0 bits; prize rows have 27.0/60.6+ bits of staircase room after the 16n^3 + B_tan reserve (the headline 0.9-bit 'total margin' at prize rows is the aggregate-vs-B* line under QA.22's conservative convention — read the note's conventions before quoting). The transported quotient-row staircase table emitted for TR.
