# PRE-REGISTRATION — ROUTE (b): character sums for ternary relations over 2-power subgroups (round 19, GENERATIVE)

Round 19, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. MANDATE: the one route left
open by round-18's THEOREM Z-NOGO — make it precise, machine-checked,
and either advance it or kill it. If the ternary unification is real,
this is its shared attack; if route (b) dies too, the F2 knife edge
has NO known route and that changes the board.

## 0. The state (quote the minted nodes verbatim first)

- background/nodes/f2_z1_mass_knife_edge: THEOREM Z-NOGO (the
  distance+counting family needs p <= 8 — dead); route (b) = "Weil-
  type / square-root cancellation for products over the
  2^{e_p}-subgroup inside F_p (sizing: sqrt(p)·log p = 2^38 vs
  subgroup 2^39 — a factor-2 headroom; back-of-envelope, NOT a
  theorem)". The object: Z_1 = sum over ternary eps of
  2^{-wt(eps)} [eps in the GRS dual], on the half-system of
  mu_{2^{e_p}}, R/S = 1/log2 p.
- The round-15 measured barrier (mun REPORT §3): the L2/sqrt method
  loses 1-2 orders at every fixture because sqrt-cancellation is
  exactly what fails on structured sets — route (b) must beat THAT
  precedent, not just the envelope.

## 1. Pre-registered deliverables

- **(R1) THE EXACT CHARACTER-SUM FORM.** Express Z_1 (and its
  unweighted sibling |T|) as an exact character/exponential sum:
  the syndrome indicator over the R conditions gives
  Z_1 = p^{-R} sum over multiplicative-character tuples of a
  PRODUCT over the S evaluation points of local factors
  (1 + 2·2^{-1}·cos-type terms — derive the exact local factor for
  the {0,±1} alphabet with the 2^{-wt} weighting; note the
  weighting makes each local factor (1 + 2^{-1}(chi(x) +
  chi(x)^{-1}))-shaped — write it exactly). Machine-verify the
  identity exactly at toy scale (2-power lengths only, CATCH-Z6).
- **(R2) THE CANCELLATION LEDGER.** The main term (trivial
  characters) gives the random-baseline 2^{m - R log2 p} — the
  knife edge. The error is a sum over nontrivial character tuples
  of products over the half-system. State EXACTLY what bound per
  tuple is needed for the total error to stay below the main term
  at k = e, and what Weil/Deligne-type bounds give: complete-sum
  bounds over subgroups (Gauss-sum / Katz), the subgroup structure
  (the half-system is a coset-like half of mu_{2^{e_p}} — is the
  relevant complete sum over the FULL subgroup, recovering exact
  Gauss sums, or genuinely over the half, where partial-sum losses
  bite?). The factor-2 headroom claim must come out of this ledger
  as a theorem-grade statement or die.
- **(R3) THE STRUCTURED-SET PRECEDENT TEST.** The round-15 barrier:
  L2 loses 1-2 orders on structured sets. Determine whether route
  (b)'s sums are the SAME sums that failed there (in which case the
  headroom is illusory — report the kill) or genuinely different
  (independence across the R conditions / the product structure —
  in which case say exactly what is new).
- **(R4) TOY VALIDATION.** At reachable (p, S) with the exact shape
  (p = c·2^{e_p}+1, half-system evaluation, R = S/log2 p rounded):
  compute Z_1 exactly AND via the character-sum decomposition;
  measure the actual per-tuple cancellation against the Weil
  prediction. Pre-register the grid (2-power only). The measured
  constants calibrate (R2)'s ledger.
- **(R5) THE VERDICT.** One of: (i) ROUTE LIVE — a theorem-grade
  conditional ("if [named character-sum bound] then Z_1 <= ...")
  with the named bound's status in the literature stated honestly;
  (ii) ROUTE DEAD — the ledger shows the needed cancellation
  exceeds what any square-root-type bound can give (state the gap
  in bits); (iii) ROUTE TRANSFORMED — the analysis reveals a
  different decomposition (e.g. Gauss-sum exact evaluation at
  2-power conductors — these are classically computable!) that
  changes the question. Chase (iii) hard: at 2-power conductor the
  relevant Gauss/Jacobi sums have KNOWN exact evaluations
  (quadratic + quartic residue symbols) — this may make parts of
  the error term EXACT rather than bounded.

## 2. Pre-registered falsifiers / honesty clauses

- The (R1) identity failing at any toy point kills everything
  downstream — it is the gate.
- No congruence conclusions about counts (AK-UNIT); character sums
  bound archimedean size, which is the admissible shape.
- If the honest ledger says DEAD, say DEAD — the board needs to
  know the knife edge has no route more than it needs optimism.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/tern_route_b/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tern_small_scale_laws/ (sibling
  independence).
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.
