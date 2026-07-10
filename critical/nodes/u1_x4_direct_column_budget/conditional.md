# u1_x4_direct_column_budget — CONDITIONAL packet (U16 amber, 2026-07-10)

- **status:** CONDITIONAL (amber; the FIFTH route commitment)
- **provenance:** Codex worktree proposal (codex/f3-flip-20260708 @ ecf84fc),
  audited fresh-context same night — verdict AMBER-READY with amendments
  A1-A5, all applied at import; catch #71 (false trace-zero envelope)
  REPAIRED before minting. One-writer banking; Codex's branch untouched.
- **route of record (U-PART):** over the proved band 2 <= h <= H_max =
  min(k+t, floor(n/2)) (KB #27):
  R_post = R_1 + R_2 + R_3 + Sigma_{h=4}^{H_max} R_h
         =  0  + <n^3 + <n^3 +        <=14n^3        < 16n^3 strictly.
  R_1: f3_h1_singleton_injectivity [PROVED, one-line]. R_2:
  f3_h2_stratum_theorem [PROVED; CP import + the imported in-house K6 chain
  (211/8)n^(5/2), dissolving the import caveat — catch #72]. R_3:
  f3_h3_direct_floor_conditional_close [CONDITIONAL on C36-prime]. Tail:
  f3_hge4_aggregate_budget [TARGET, the forced uniform-in-h gate].
- **open leaves:** f3_h3_three_to_one_c36 (C36', pre-stressed: 12-prime
  exhaustive sweep at 2.774% of threshold) and f3_hge4_aggregate_budget.
- **alternates kept (ev):** the ACT(4096) h=3 route
  (f3_h3_officialrow_conditional_close + conic/rankcap gates);
  f3_active_core_width_cap (route-1 evidence for HGE4).
- **pins:** A1 row-set pin (six proved candidates; 29-row table owed);
  A5 five-strips convention + F-4 minimal-trade scope; strict totals from
  the two strict links; the {P,-P}-class tightening option (would restore
  the 8n^(4/3) threshold).
- **verification record:** assembly compiler (rows=29 total=16 tail=14,
  exit 0) + fresh-context audit (32 exact checks; mutation controls
  14->15 and 8/36->9/36 both exit 1; the #71 counterexample) — banked at
  notes/cx_amber_audit_20260710.py and notes/f3_u1_x4_amber_assembly.py.
- **re-surgery criteria:** in dag.json statement (C36' falsified; HGE4
  falsified under slice semantics; band-pin change; consumer allowance
  moves via QA.22/#493; A1 table failure; F-4 convention re-opens).
