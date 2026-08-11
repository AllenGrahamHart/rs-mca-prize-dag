# Binding constraints (r35_bivcurve_m4, round 35)

- COMPUTE LAW (UPGRADED, round-33 censure): never bare python3 FOR
  ANY PURPOSE — including file patching, string replacement, no-op
  probes, and empty heredocs. File edits use the Edit/Write tools;
  if a script must patch a file, run the patcher under
  tools/ramguard tiny. Every interpreter invocation is
  tools/ramguard tiny -- python3 ... (256M/60s) or
  tools/ramguard local -- python3 ... (1G/5min), repo root, literal
  --, RAMGUARD_TIMEOUT documented per use. Stdlib only. No Modal,
  no network, no git, no subagents. A bare python3 invocation is a
  breach EVEN IF IT COMPUTES NOTHING.
- WRITE DISCIPLINE (UPGRADED, round-34 censures): sed -i, awk -i,
  perl -i, tee, shell redirection onto an existing file, and ANY
  in-place shell stream edit of a file are WRITES and must go
  through the Edit/Write tools instead. A shell text edit of any
  file is a breach of write discipline even when it computes
  nothing (banks 3 and 4 were censured for exactly this). Scripts
  MAY create/overwrite their own results files.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json (node.json
  shards + grep); bounded windows on large statements; checkpointed
  batches with results files.
- WRITE SCOPE: ONLY notes/pilots_20260811/r35_bivcurve_m4/. No dag/,
  nodes/, tools/ edits. No git. Never touch any path containing
  prize-codex-. Scratch files go in your own dir, never /tmp.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the OTHER r35_* dirs under notes/pilots_20260811/.
  The round-33/34 dirs (notes/pilots_20260811/rh_*, r34_*) and all
  earlier pilot dirs ARE readable (copy banked scripts into your
  dir before running). Use --exclude-dir at the SEARCH level on
  every recursive grep (output filtering after traversal is a
  disclosed deviation).
- BLIND PRIORS: after reading ONLY the two anchors named in
  PREREG.md, append "## Pilot registrations" there BEFORE any
  further read. Include a MISS-2-guard-style registration for any
  mean-vs-max reasoning you anticipate (the proven guard pattern).
- REPORT: REPORT.md in your dir; the harness will refuse the
  write — in ALL cases return the full REPORT text verbatim as your
  final message. MISSES-FIRST; every quantifier claim file:line
  (CATCH-24C); own-repo greps before novelty claims (CATCH-24A,
  INCLUDING hyphenated/infixed variants of key phrases — a
  round-34 catch); zero-power declarations on max-quantified
  claims; two-field confirmation for structural claims; compliance
  paragraph (interpreter count + ramguard status, quarantine,
  write scope).
