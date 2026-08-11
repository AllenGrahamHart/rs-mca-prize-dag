# Binding constraints (r38_sporadic_det, round 38)

- COMPUTE LAW + THE PRE-BASH CHECKLIST (NEW, after two identical
  breaches in two rounds): before EVERY Bash call, scan the
  command string — if it contains "python3" it MUST match
  "tools/ramguard (tiny|local) -- python3". There is NO
  legitimate bare python3, EVER — not for patching, not for
  probes, not as an empty-heredoc no-op between edits. If you
  feel the urge to run a no-op interpreter, DON'T. Every
  invocation: tools/ramguard tiny -- python3 ... (256M/60s) or
  tools/ramguard local -- python3 ... (1G/5min), repo root,
  literal --, RAMGUARD_TIMEOUT documented. Stdlib only. No
  Modal, no network, no git, no subagents.
- WRITE DISCIPLINE: sed -i, awk -i, perl -i, tee, shell
  redirection onto an existing file, and ANY in-place shell
  stream edit are WRITES — use the Edit/Write tools. Scripts MAY
  create/overwrite their own results files subject to:
- RESULTS-FILE RULES: results files open in APPEND mode or are
  versioned per run (never a blind "w"); results-producing runs
  are NEVER piped through head.
- IMPORTED-SCRIPT RULE: before importing or executing ANY copied
  banked script, AUDIT ITS OUTPUT PATHS (grep for open(/write);
  fix with Edit BEFORE first import — imports can write at
  import time (biv_core.py and share3_pencil.py both have
  module-level writes; both prior incidents are on record).
  Preferred: duplicate helpers per file so no import exists.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; every
  recursive grep carries --exclude=dag.json plus the exclude-dir
  set below; bounded windows on large statements (the crossing
  statement is >5000 lines — grep headers, window sections).
- WRITE SCOPE: ONLY notes/pilots_20260811/r38_sporadic_det/. No
  dag/, nodes/, critical/, background/, tools/ edits. No git.
  Never touch any path containing prize-codex-. Scratch in your
  own dir, never /tmp.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Sibling round-38 dirs BY NAME: r38_sporadic_det (you),
  r38_side_door, r38_urate_genericity, r38_cauchy_lattice —
  NEVER read the other three; never ls the parent. r37_*, r36_*,
  r35_*, r34_*, rh_* ARE readable (copy scripts in first; audit
  paths). Every recursive grep, at the SEARCH level:
  --exclude-dir=r38_side_door
  --exclude-dir=r38_urate_genericity --exclude-dir=r38_cauchy_lattice
  --exclude-dir=pilots_20260802 --exclude-dir='prize-codex-*'
  --exclude-dir=.git --exclude-dir=__pycache__ --exclude=dag.json.
- BLIND PRIORS: after reading ONLY the two anchors named in
  PREREG.md, append "## Pilot registrations" with the Edit tool
  (in 2-3 parts if large — the harness output cap is real) BEFORE
  any other read, any grep, any ls, and any interpreter
  invocation. Include a MISS-2 guard and zero-power declarations.
- REPORT: the harness refuses a REPORT.md write — return the full
  REPORT verbatim as your final message, UNDER ~40,000 characters
  (compress deliverables, never misses/compliance). MISSES-FIRST;
  file:line on every quantifier claim (CATCH-24C); own-repo greps
  incl. hyphenated/infixed variants before novelty claims
  (CATCH-24A); zero-power declarations; two-field confirmation;
  full compliance paragraph.
