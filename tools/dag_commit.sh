#!/bin/bash
set -e
cd "$(dirname "$0")/.."
ERRS=$(python3 tools/verify_prize_dag.py 2>&1 | grep -c "declared\|ERROR" || true)
[ "$ERRS" != "0" ] && { echo "BLOCKED: validator errors"; exit 1; }
python3 tools/build_critical_orbit.py
git add -A
git commit -q -m "$1

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
echo "committed"
