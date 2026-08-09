# RULING (2026-08-09, user-ratified): push-on-close for PR #1152

The user ratified Codex's push-on-close behavior for the living K3
export, **scoped to PR #1152 (fork branch k3-433-progress-export)
only**, under two binding conditions:

1. Every pushed certificate's provenance MUST pin the exact worktree
   commit containing the closure (as the cell-9/cell-3 certs did).
   Be aware the pinned commit is NOT publicly reachable until the
   coordinator's next wave merge lands on master — write the README
   so a reader knows replay may need to wait for the next master
   push, or coordinate timing with a wave audit when practical.
2. The coordinator audits every pushed certificate at the next wave
   audit (same-day target) with fix-forward authority: a defective
   certificate is corrected by a follow-up commit on the PR, never
   by history rewrite.

This ruling does NOT extend to any other outward-facing surface: no
pushes to other branches, PRs, upstream przchojecki/rs-mca, or the
public site. Everything else stays coordinator-gated.

Audit record for the two self-pushed certs (cell-9 1b866634, cell-3
e1e7d263): convention-compliant, nonclaims honest, sha256 pins exact
on coordinator spot-checks; pins became publicly reachable with
master push 44b0e88b8. See CAMPAIGN_LEDGER "WAVE 54 INTEGRATED".
