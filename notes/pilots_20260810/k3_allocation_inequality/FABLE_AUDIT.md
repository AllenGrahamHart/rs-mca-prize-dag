# FABLE_AUDIT — k3_allocation_inequality (round 30)

Coordinator: Fable. Date: 2026-08-10. Pilot: Opus (~23 min, 100 tool
uses, 5 interpreter invocations, all ramguard). REPORT.md persisted
verbatim by the coordinator (harness blocked the pilot's write).
Disclosed: two early greps streamed dag.json lines before the
exclusion was added (no Read, no parse) — accepted.

## Verdict

**BANKED. The dry run is BLOCKED THREE WAYS and the fourth integer is
UNDEFINED: U_positive blocked on the eleven-route TARGET (0 of 11
routes has a printed integer), U_sourcecover blocked on the open
orientation TARGET (no census, no cap — cannot even be bounded),
and U_K3_allocation is DEFINED NOWHERE IN THE REPO (the only 4
occurrences are the two K3 nodes that demand it). The strongest
exact statement available is the interval 0 <= U_K3_allocation <=
274980728110413983 (the joint three-cell reserve, attained by K3
only under the unproved side condition U_Q = U_new = 0). Plus a
DERIVED floor: U_Q + U_BC + U_new >= 57197049262 (from the banked
identity-prefix lower attack minus the U_paid cap), which kills the
ledger's "record U_K3=0" fallback as a free move. Five findings new
to the repo (M1 allocation undefined, M2 allocation node unwired,
M6 the B_star row-key collision kb_mca/kb_list, M7 the "allocation"
homonym, M8 the floor). The binding schema draft (9 blocks,
refuse-to-substitute) is the right design.**

## Coordinator verifications (mine)

| what | result |
|---|---|
| compute_arith.py full replay | 56/56 PASS (row constants incl. B_star = floor(p^6/2^128) = 274980728111395087, reserve, the 13-route re-derivation, the 42,840 partition, the floor arithmetic, 15 file digests) |
| verify_partition_digest.py replay | MATCH True; same_partition True; U_BC stage confirmed (scratch copy of the banked verifier with the dag.json read removed — compliant) |
| M1 grep | independently re-run: exactly 4 in-repo files + compiled dag.json — confirmed |
| atom's "No value is proved here" | verbatim at tangent_source_atom/statement.md:69 |
| M6 B_star collision | confirmed: the literal appears exactly twice in deployed_rows.json (kb_mca + kb_list) |
| U_positive = U_remaining | confirmed from complete_payment/node.json statement |

## Audit judgements

- **M1 + M2 together are the round's ledger-level finding**: the
  allocation node demands an inequality against a number that
  nothing defines, and has requires=[] so the binding it demands is
  not even representable in the DAG. This does not flip any status
  (TARGET stays TARGET) but it re-prices the leaf: closing it needs
  a DEFINITION first, not a computation. Repair options (prove
  U_Q=U_new=0 and promote the reserve, or an explicit three-way
  split with its own certificate) are Codex-lane choices: SURFACED.
- **M3 (the unit seam) confirms the sibling pilot's O5
  independently** — two blind pilots converged on labels-vs-slopes
  as the binding blocker. It is the top item of the unblock chain
  and has NO owner.
- **The derived floor (section E) is properly labelled DERIVED with
  its one missing owner ruling** — not imported, not banked as fact.
  Its firm consequence (some unpaid cell is nonzero) stands.
- **M10 (the "saturated" scope carry) is a word-level seam** between
  the ledger's zero-contribution clause and the source-line
  certificate — cheap to fix in Codex's lane, easy to lose:
  surfaced in the wave-57 brief.
- Priors honestly scored: P1c (15% branch) was the outcome; P2c
  (15%) the outcome; P3 declared not-evaluable rather than guessed.
  Two zero-power declarations properly scoped (Z2, Z3).

## Corrections applied

None to nodes (K3 lane = Codex's write lane). Pilot dir banked
as-is: REPORT.md, compute_arith.py, verify_partition_digest.py,
binding_schema_draft.json, PREREG.md.

## Follow-ups filed (not executed)

- The unblock chain in dependency order (labels-to-slopes conversion
  -> allocation definition -> route integers -> U_sourcecover ->
  wiring) is the spine of the wave-57 Codex brief.
- The binding schema draft should ship with that brief as the
  checkable contract for the eventual allocation run.
- The B_star row-key hazard (M6): any future row binding must key on
  (n,k,p,K), never on the budget. Candidate one-line addition to
  the K3 nodes' attack text — Codex's lane.
