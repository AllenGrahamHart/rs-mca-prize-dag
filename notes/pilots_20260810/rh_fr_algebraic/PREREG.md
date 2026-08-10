# PREREG — rh_fr_algebraic (round 32)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `background/nodes/rate_half_type2_fr_incidence_only_route_fence/statement.md`
2. `notes/pilots_20260810/rh_type2_stratum/REPORT.md` (round 31)

## Mandate

Residual (ii) of the RH-AC budgets stands at a factor 9/4 with ONE
missing inequality, (FR): every non-minimum-weight type-2 slope of a
strict-A=3 pencil at T = rho+2 has |S_gamma ^ W| <= ~2m (the
max-vs-mean upgrade). The wave-57 fence PROVED the incidence route
dead: an explicit m = 64 quartic cyclotomic set system satisfies
EVERY banked incidence constraint (saturation, (OV), (C2) spend,
min pair union = a) yet has max |S_gamma ^ W| = 3m-3 = 189 > 2m.
The fence's own scope line: it is NOT a realizable Hankel-pencil
counterexample. YOUR JOB: the algebraic attack — use the objects
the fence cannot see: the generalized reciprocal-locator polynomials
f_gamma ((GNF): kappa_x = f(x)/sigma'_Z(x), deg f <= j), the common
syndrome pencil, and the apolar Hankel equations.

## Deliverables

**D1 — EXCLUDE THE FENCE SYSTEM.** Is the m = 64 fence system
REALIZABLE as an actual pencil configuration (actual locator sets of
actual type-2 slopes over an admissible field)? Attempt the
realization; if it fails, identify WHICH algebraic constraint kills
it — that constraint is (FR)'s candidate mechanism. If it succeeds,
(FR) as stated is FALSE and the 9/4 is real — that is a
route-deciding result of the first order; verify to the fence's own
standard (two implementations) before claiming.

**D2 — THE ALGEBRAIC (FR).** Derive the max-bound on
|S_gamma ^ W| for REALIZABLE configurations from (GNF) + the
divisibility structure (sigma_{S_gamma} relations through the
common pencil) + the apolar equations. Target: <= 2m + O(1), which
closes residual (ii) to a factor ~1. POSE with falsifiers what you
cannot prove; partial subclass theorems welcome (each with exact
scope).

**D3 — THE SMALL-SCALE REALIZABILITY CENSUS.** At the round-31
census scales (m = 2,3,4, two fields each): measure the TRUE max
|S_gamma ^ W| over realizable configurations vs the incidence bound
3m-3 vs the target 2m. Pre-register the expected separation BEFORE
running. Use the round-31 pilot's decoder machinery (copy scripts
into your dir; its d3_census.py is banked in rh_type2_stratum/).

**D4 — VERDICT.** Either the algebraic (FR) proved/posed with named
gaps, or the honest wall with the exact missing algebra named.
Misses first; zero-power declarations; the (SAT3)-conditionality
and (EQ)-converse caveats from round 31 carry forward — quote them.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  runs, repo root, literal `--`. RAMGUARD_TIMEOUT documented per
  use. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; checkpointed
  batches with results files.
- WRITE SCOPE: ONLY notes/pilots_20260810/rh_fr_algebraic/. No
  dag/, nodes/, tools/ edits. No git. Never touch prize-codex-*.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-32 dirs (rh_farca_upper,
  rh_haboeck_seam, rh_residuals_close). Round-31 and earlier pilot
  dirs are readable.
- BLIND PRIORS: after the two anchors only, append "## Pilot
  registrations" (P(fence system realizable), P(algebraic FR
  provable this round), expected killing constraint) BEFORE any
  further read.
- REPORT: REPORT.md in your dir (if the harness refuses the write,
  return the full text as your final message — and in all cases
  ALSO return it verbatim as your final message); MISSES-FIRST;
  file:line quotes (CATCH-24C); own-repo greps before novelty
  (CATCH-24A); zero-power declarations; banked scripts from scratch
  copies only.
