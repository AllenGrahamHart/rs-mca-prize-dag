# Binding constraints (rh_sat3_realizability, round 33)

- COMPUTE LAW: never bare python3. tools/ramguard tiny -- python3 ...
  (256M/60s) peeks; tools/ramguard local -- python3 ... (1G/5min)
  runs; repo root; literal --; RAMGUARD_TIMEOUT documented per use.
  Stdlib only. No Modal, no network, no git, no subagents.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json (node.json
  shards + grep); bounded windows on large statements; checkpointed
  batches with results files.
- WRITE SCOPE: ONLY notes/pilots_20260811/rh_sat3_realizability/. No dag/, nodes/,
  tools/ edits. No git. Never touch any path containing
  prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the OTHER round-33 dirs under notes/pilots_20260811/.
  notes/pilots_20260810/ and earlier ARE readable (copy banked
  scripts into your dir before running).
- BLIND PRIORS: after reading ONLY the two anchors named in
  PREREG.md, append "## Pilot registrations" there BEFORE any
  further read.
- REPORT: REPORT.md in your dir; the harness may refuse the write —
  in ALL cases return the full REPORT text verbatim as your final
  message. MISSES-FIRST; every quantifier claim file:line
  (CATCH-24C); own-repo greps before novelty claims (CATCH-24A);
  zero-power declarations on max-quantified claims; two-field
  confirmation for structural claims; compliance paragraph
  (interpreter count + ramguard status, quarantine, write scope).
