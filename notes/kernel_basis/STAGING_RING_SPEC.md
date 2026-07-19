# Staging-ring spec for the critical orbit map (maintainer-approved
# 2026-07-19; implement next cycle)

GOAL: end the invisibility of parked (ev-lane) structure without
corrupting the req-surface semantics. The board should SHOW the state
of play: ambers and their leaves that are wired ev-only pending a
ceremony (e.g. the WCL amber + its four slot reds under dli, the dli
decomposition trio) appear DIMMED around their consumer.

DERIVATION (tools/build_critical_orbit.py::derive, after `crit`):
staging = { u : (u --ev--> v) in edges, v in crit,
            status[v] in (TARGET, CONJECTURE, CONDITIONAL),
            status[u] in (CONDITIONAL, TARGET),
            u not in crit }
plus one tier of req-ancestry of staging ambers (their own leaves).
Emit them in critical_dag.json with "staging": true.

RENDER (tools/render_prize_dag_svg.py): staging nodes on an outer
dashed ring segment adjacent to their consumer's sector; opacity 0.45;
dashed arcs for their edges; colors keep the status scheme. Stats line
gains "N staged". The app HTML needs no data-flow change (same json).

ACCEPTANCE: non-staging output byte-stable modulo the new elements;
counts line unchanged for the existing classes; the WCL amber + 4
slots + c2pp/baseline visible dimmed under dli after rebuild.
