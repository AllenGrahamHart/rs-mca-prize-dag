#!/bin/bash
set -e
cd "$(dirname "$0")/.."
python3 tools/auto_discharge.py
# GATE (fixed 2026-07-06): use exit codes, not output greps -- the old grep pattern
# silently ignored reachability failures and every invariant added after it was written.
if ! python3 tools/verify_prize_dag.py > /tmp/dag_validate.out 2>&1; then
  echo "BLOCKED: validator errors:"; grep -A100 "^FAIL:" /tmp/dag_validate.out | head -30; exit 1
fi
if [ -f tools/verify_assembly_implications.py ]; then
  if ! python3 tools/verify_assembly_implications.py > /tmp/dag_assembly.out 2>&1; then
    echo "BLOCKED: assembly implication drift:"; tail -5 /tmp/dag_assembly.out; exit 1
  fi
fi
python3 tools/build_critical_orbit.py
git add -A
git commit -q -m "$1

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
echo "committed"
