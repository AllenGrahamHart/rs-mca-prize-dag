# The content audit protocol (Codex's job; flags only, one-writer rule)

GOAL: every node's status independently re-derived from its artifacts.
The machine layer (wiring, artifact existence, pins, verifier replay:
tools/replay_all.py) is already enforced — do NOT re-check it. Your layer
is CONTENT: does the artifact actually establish the full statement?

SCOPE + ORDER: all nodes, batches of ~15 per turn, alphabetical within
priority class: (1) PROVED first — highest stakes; (2) CONDITIONAL packets;
(3) PROVABLE sketches; (4) reds last (statement quality only).

PER NODE, ANSWER FIVE QUESTIONS:
1. Is the statement truth-apt, self-contained, unambiguous? (Every symbol
   defined or pinned; no tool-description phrasing.)
2. Does the artifact prove THE statement — not a weaker cousin? Name the
   exact gap if any (toy-row-only, one-direction-only, missing uniformity,
   asserted-not-proved step). Quote the weakest step of the proof.
3. Are the wired predicates SUFFICIENT for the implication as written —
   no silent extra hypotheses used in the packet body?
4. Does the verifier test the STATEMENT (not a tautology or a fixture)?
5. Is a stronger status warranted (under-claiming is also an error)?

OUTPUT: append findings to nodes/CONTENT_AUDIT.md, one line per node:
  | node | verdict OK/MINOR/MAJOR/BLOCKER | the specific defect, with quote |
BLOCKER = status is wrong (proof does not establish statement).
MAJOR = gap that a referee would bounce (fixable without status change).
MINOR = hygiene. NO status flips, NO dag.json edits, NO deletions — the
maintainer adjudicates every flag and performs any flips on replay.

Commit per batch with the audit ledger diff only.
