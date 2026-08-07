# PRE-REGISTRATION — RED CLOSABILITY PROBES: two reds vs two recent theorems (round 21)

Round 21, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: two cheap decisive
probes — recent theorems may have quietly made two mystery-lane reds
closable by known methods. Decide each, honestly.

## PROBE 1 — integer_code_distance_cert vs the transported distance law
- Source: critical/nodes/integer_code_distance_cert (the RESIDUE:
  certify min ternary distance > 2l' for the explicit k x N'
  system) — quote the exact system and the exact threshold.
- The instrument: THEOREM Z-1/D1 (round 18, banked in
  f2_z1_mass_knife_edge + the o1/z1 pilot dirs): the DLI
  short-window exclusion gives min ternary weight >= 2R+1 whenever
  char > w, omega of exact 2-power order, distinct exponents, and
  the window starts at l = 1 (shift-0 ONLY — 43 shifted
  counterexamples are banked; THE SCOPE CHECK IS THE WHOLE PROBE).
  Plus THEOREM Z-2 (the l1-weight integer-coefficient extension —
  possibly exactly the "integer code" form this node needs).
- Deliverable: hypothesis-match the node's explicit system against
  Z-1/Z-2 term by term. If it matches: the certificate, written out,
  with a verifier — the red is CLOSABLE (no status flip — the
  coordinator flips on replay). If it mismatches: the exact gap,
  and whether a bounded amount of new work closes it.

## PROBE 2 — unsafe_crossing_family_instantiation vs THEOREM BB
- Source: critical/nodes/unsafe_crossing_family_instantiation
  (universal adjacent-unsafe witness-family instantiation) — quote
  the exact universality/instantiation requirement (which rows must
  the family cover? "universal" is the load-bearing word).
- The instrument: THEOREM BB + LEMMA SL/THEOREM SM/THEOREM AC
  (notes/pilots_20260806/gamma_shell/, banked): a PROVED unsafe
  witness family at break-region tower rows (e >= 3 fully at
  delta_a = 1; partial e = 2/(4,2)); e = 1 prime rows NOT covered
  and provably unreachable by that method.
- Deliverable: does the node's universality quantifier need the
  prime rows? If the node's family may be row-class-restricted (or
  if the node's consumers only need tower-row witnesses), BB may
  close it or close a named part; if it needs e = 1 rows, state
  exactly what remains and whether the (RHL-B12)-style exact
  closures cover any of it. Write the closable part's certificate.

## Rules
- DRAFT ONLY in notes/pilots_20260807/red_closability_probes/.
  Never edit dag.json/nodes/tools; no git. COMPUTE LAW:
  tools/ramguard tiny|local -- python3 (including file patching).
  Verbatim quotes with file:line. No status flips — closability
  verdicts + certificates only; the coordinator flips on replay.
  No REPORT.md — your final message IS the report. Do not read
  CAMPAIGN_LEDGER entries after the "ROUND 21 LAUNCHED" marker;
  pass the quarantine clause to any subagent you dispatch.

---

# PILOT REGISTRATIONS (appended BEFORE any computation, 2026-08-07)

Opus pilot, round 21. Everything below is registered before a single
line of arithmetic is run. Sources were READ first (reading is not
computing); no script had been executed at the time of this append.

## P0 — scope and rules I bind myself to
- DRAFT ONLY in `notes/pilots_20260807/red_closability_probes/`.
- No status flip in either probe. Closability verdict + certificate only.
- Every load-bearing quote carries `file:line`.
- Every computation runs under `tools/ramguard tiny|local -- python3`,
  including any patching of my own draft files.
- I will not read `notes/pilots_20260802/CAMPAIGN_LEDGER.md` at all, and
  any subagent I dispatch is given the same quarantine clause verbatim.
- If a probe's answer is "no", I report the exact gap rather than
  manufacturing a partial closure.

## P1 — PROBE 1, the object I will hypothesis-match
The node's explicit system, as I will quote it, is the kernel
`K_p = {v in Z^{N'} : sum_j v_j zeta^j = 0 mod p}` with `zeta` of exact
order `N'` (2-power), `p = 1 mod N'`, ternary `v`, support `<= 2l'`,
modulo the antipodal cyclotomic relations. I register FOUR hypothesis
slots to be filled term by term against THEOREM Z-1 / THEOREM Z-2:
  (H1) `char F = 0` or `char F > w`;
  (H2) `omega` of EXACT order `2N`;
  (H3) exponents distinct in `{0,...,N-1}` (a HALF system);
  (H4) vanishing at the FIRST `ell` odd powers, `omega^{2j-1}`,
       `j = 1..ell`, with `w <= 2ell`  (shift 0).
`ell` = the number of independent odd-power vanishing conditions the
node's system actually supplies. This is the slot I expect to decide the
probe, not the shift.

## P2 — PROBE 1 decision rule (registered, binding)
- CLOSABLE iff the node's system supplies `ell >= l'` odd-power
  conditions at shift 0 with `char p > w`, since Z-1/Z-2 then give
  min (l1) weight `>= 2ell+1 >= 2l'+1 > 2l'`, which is EXACTLY the
  node's threshold.
- NOT CLOSABLE if `ell < l'`; in that case I report the exact deficit
  `l' - ell` and whether any banked object supplies the missing
  conditions.
- A match on (H1)-(H3) plus a failure on (H4)'s `ell` is a MISMATCH,
  not a partial closure. I will not report it as "nearly closes".

## P3 — PROBE 1 prediction (pre-registered, falsifiable)
I predict `ell = 1`: the node's collision condition is a SINGLE
`F_p`-linear functional `v -> sum_j v_j zeta^j`, because `zeta` lies in
`F_p` and therefore the Galois conjugations `zeta -> zeta^a` are NOT
induced by field automorphisms of `F_p`, so no further vanishing
conditions come for free. Consequently Z-2 would yield only
`min l1 weight >= 3`, against a required `> 2l'`.
FALSIFIER of this prediction: exhibiting, in the node's own row payload
or in a PROVED supplier, `k >= 2` genuinely independent odd-power
conditions on the same ternary vector. `multi_multiplier_reduction` is
REFUTED, so I expect none; if I find one I will say so.
I also predict the SHIFT check PASSES (the single exponent is the first
odd power `j = 1`), i.e. the 43 banked shifted counterexamples are NOT
what blocks this node.

## P4 — PROBE 1 verifier (registered before it is written)
`probe1_verify.py`, stdlib only, under ramguard tiny:
 (V1) at small 2-power cells `N'` with `p = 1 mod N'`, enumerate the
      folded box exhaustively and report the exact minimum `l1` weight
      of a NON-cyclotomic kernel vector;
 (V2) check Z-2 at `ell = 1` (no nonzero kernel vector of `l1` weight
      `<= 2`) — must PASS at every cell;
 (V3) check whether the `ell = 1` floor `2*1+1 = 3` reaches the node's
      threshold `2l'` — must FAIL wherever `l' >= 2`, quantifying the
      gap;
 (V4) POSITIVE CONTROL: build the genuine `ell`-condition system
      (vanishing at `omega^1, omega^3, ..., omega^{2ell-1}`) and verify
      that there Z-2's `2ell+1` floor is attained/respected — showing
      the theorem is fine and it is the node's system that is short;
 (V5) FAIL-CLOSED control that must exit non-zero.

## P5 — PROBE 2, the quantifier I will decide
I will quote `unsafe_crossing_family_instantiation`'s universality
requirement verbatim from `statement.md`, `node.json`, and
`claim_contract.md`, then decide closability against THEOREM BB under
this binding rule. BB closes the node, or a NAMED part of it, only if
ALL FOUR hold:
  (C1) SAME FUNCTIONAL: BB's counted quantity is the node's counted
       quantity (`B_C`, ambient-MCA bad slopes), or a PROVED transfer
       between them is banked;
  (C2) ROW ADMISSIBILITY: BB's row region consists of rows admissible
       for this node;
  (C3) FORM: BB's output is expressible as one of the node's `Q`, `V`,
       or `M` payloads, meeting the claim-contract's load-bearing
       checks 1-8;
  (C4) ENDPOINT: BB's agreement is exactly the node's `a_safe - 1`.
Any of (C1)-(C4) failing => I state the exact remainder rather than
claiming a partial closure.

## P6 — PROBE 2 prediction (pre-registered, falsifiable)
I predict (C1) FAILS as the FIRST obstruction, ahead of the `e = 1`
row gap: THEOREM BB bounds `L_1(k+2^34)`, the LIST-side maximal
codeword count of `rate_half_list_adjacent_crossing`, whereas this node
counts `B_C(a_safe-1)`, ambient-MCA bad slopes for `mca_grand`. I
predict no banked PROVED `L_1 -> B_C` transfer exists.
FALSIFIER: a banked PROVED node stating `B_C(a) >= L_1(a)` (or an
equality of the two counts) on the relevant rows; or a demonstration
that the node's `B_C` is definitionally the same count as `L_1`. I will
search for exactly this before ruling.
I further predict that even granting (C1), the `e = 1` prime rows are a
non-empty part of the node's universal quantifier, so BB cannot close
the node outright.

## P7 — PROBE 2 deliverable rule
If a named part is closable I write its certificate in the node's own
`Q`/`V`/`M` grammar with the row region printed as inequalities. If no
part is closable in that grammar, I say so plainly and print the
exact remainder, including whether the `(RHL-B12)`-style exact closures
cover any of the `e = 1` rows. No status flip either way.

## P8 — what would make me report a NEGATIVE result
Both probes are permitted to return "no". A "no" with an exact gap is
the successful outcome of a cheap decisive probe; I will not upgrade a
structural mismatch into a conditional closure to manufacture a
positive.
