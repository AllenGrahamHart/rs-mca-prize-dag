#!/bin/bash
set -e
cd "$(dirname "$0")/.."
python3 tools/auto_discharge.py
ERRS=$(python3 tools/verify_prize_dag.py 2>&1 | grep -c "declared\|ERROR\|AMBER LEAF\|not wired\|does not resolve" || true)
PINS=$(python3 tools/verify_assembly_implications.py 2>&1 | grep -c "FAILED\|drift" || true)
ERRS=$((ERRS + PINS))
[ "$ERRS" != "0" ] && { echo "BLOCKED: validator errors"; exit 1; }
python3 tools/build_critical_orbit.py
git add -A
git commit -q -m "$1

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
echo "committed"
