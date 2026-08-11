# Binding constraints (r37_share3_gap, round 37)

- COMPUTE LAW (standing; a breach ended the clean streak last
  round — it is enforced): never bare python3 FOR ANY PURPOSE —
  including file patching, string replacement, no-op probes, and
  empty heredocs. Every interpreter invocation is
  tools/ramguard tiny -- python3 ... (256M/60s) or
  tools/ramguard local -- python3 ... (1G/5min), repo root,
  literal --, RAMGUARD_TIMEOUT documented per use. Stdlib only.
  No Modal, no network, no git, no subagents. A bare python3
  invocation is a breach EVEN IF IT COMPUTES NOTHING.
- WRITE DISCIPLINE (standing): sed -i, awk -i, perl -i, tee,
  shell redirection onto an existing file, and ANY in-place shell
  stream edit of a file are WRITES and must go through the
  Edit/Write tools. Scripts MAY create/overwrite their own
  results files — but see the next rule.
- RESULTS-FILE RULES (NEW, round-36 losses): results files are
  opened in APPEND mode or versioned per run (never a blind "w"
  that a rerun erases); a results-producing run is NEVER piped
  through head (SIGPIPE killed a run's output last round) —
  scripts write their own files and stdout is inspected
  afterwards.
- IMPORTED-SCRIPT RULE (standing): before importing or executing
  ANY copied banked script, AUDIT ITS OUTPUT PATHS (grep for
  open(/write/results paths); fix with Edit BEFORE first import —
  imports can write at import time. Preferred pattern: duplicate
  helpers into each file so no import exists at all.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; every
  recursive grep carries --exclude=dag.json IN ADDITION to the
  --exclude-dir set below; bounded windows on large statements;
  checkpointed batches (append-mode) with results files.
- WRITE SCOPE: ONLY notes/pilots_20260811/r37_share3_gap/. No
  dag/, nodes/, critical/, background/, tools/ edits. No git.
  Never touch any path containing prize-codex-. Scratch files go
  in your own dir, never /tmp.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  The sibling round-37 dirs are, BY NAME: r37_share3_gap (you),
  r37_third_solve, r37_urand, r37_mint_drafts — NEVER read the
  other three; you never need to ls the parent. The r36_*, r35_*,
  r34_*, rh_* and all earlier pilot dirs ARE readable (copy
  banked scripts into your dir before running — see the
  imported-script rule). Every recursive grep uses, at the SEARCH
  level: --exclude-dir=r37_third_solve --exclude-dir=r37_urand
  --exclude-dir=r37_mint_drafts --exclude-dir=pilots_20260802
  --exclude-dir='prize-codex-*' --exclude-dir=.git
  --exclude-dir=__pycache__ --exclude=dag.json.
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
