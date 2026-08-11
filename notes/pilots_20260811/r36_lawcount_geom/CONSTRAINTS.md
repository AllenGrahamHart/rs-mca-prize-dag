# Binding constraints (r36_lawcount_geom, round 36)

- COMPUTE LAW (standing): never bare python3 FOR ANY PURPOSE —
  including file patching, string replacement, no-op probes, and
  empty heredocs. Every interpreter invocation is
  tools/ramguard tiny -- python3 ... (256M/60s) or
  tools/ramguard local -- python3 ... (1G/5min), repo root, literal
  --, RAMGUARD_TIMEOUT documented per use. Stdlib only. No Modal,
  no network, no git, no subagents. A bare python3 invocation is a
  breach EVEN IF IT COMPUTES NOTHING.
- WRITE DISCIPLINE (standing): sed -i, awk -i, perl -i, tee, shell
  redirection onto an existing file, and ANY in-place shell stream
  edit of a file are WRITES and must go through the Edit/Write
  tools. Scripts MAY create/overwrite their own results files.
- IMPORTED-SCRIPT RULE (NEW, round-35 breach): before importing or
  executing ANY copied banked script, AUDIT ITS OUTPUT PATHS (grep
  for open(/write/results paths). If any path points outside your
  directory, fix it with the Edit tool BEFORE the first import —
  imports can write at import time.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; every
  recursive grep carries --exclude=dag.json IN ADDITION to the
  --exclude-dir set below; bounded windows on large statements;
  checkpointed batches with results files.
- WRITE SCOPE: ONLY notes/pilots_20260811/r36_lawcount_geom/. No
  dag/, nodes/, critical/, background/, tools/ edits. No git.
  Never touch any path containing prize-codex-. Scratch files go
  in your own dir, never /tmp.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  The sibling round-36 dirs are, BY NAME: r36_lawcount_geom (you),
  r36_sat3_on_l2, r36_hrlow, r36_m4_nonsplit — NEVER read the
  other three; you never need to ls the parent (the names are
  given here). The r35_*, r34_*, rh_* and all earlier pilot dirs
  ARE readable (copy banked scripts into your dir before running —
  see the imported-script rule). Every recursive grep uses, at the
  SEARCH level: --exclude-dir=r36_sat3_on_l2
  --exclude-dir=r36_hrlow --exclude-dir=r36_m4_nonsplit
  --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*'
  --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json.
- BLIND PRIORS: after reading ONLY the two anchors named in
  PREREG.md, append "## Pilot registrations" there with the Edit
  tool BEFORE any other read, any grep, any ls, and any
  interpreter invocation. Include a MISS-2-guard (mean-vs-max)
  registration and zero-power pre-declarations.
- REPORT: the harness refuses a REPORT.md write — in ALL cases
  return the full REPORT text verbatim as your final message.
  MISSES-FIRST; every quantifier claim file:line (CATCH-24C);
  own-repo greps before novelty claims INCLUDING hyphenated and
  infixed variants (CATCH-24A); zero-power declarations on
  max-quantified claims; two-field confirmation for structural
  claims; compliance paragraph (interpreter count + ramguard
  status, quarantine, write scope, imported-script audits).
