# Codex v10 harvest — 2026-07-27 (awareness only; integration is audit-gated)

Branch `prize-codex-resolution-v10-20260722`, ~75 commits in six hours. Read-only.

## Headline: Codex demotes a node we hold as PROVED, and adds a 24th red

| | ours | codex v10 |
|---|---|---|
| dag nodes | 1224 | 1245 |
| math orbit | **260** | **242** |
| PROVED / CONDITIONAL / TARGET | 201 / 36 / 23 | 180 / 38 / **24** |

**All 23 of our TARGETs are still TARGET in their tree — none closed.** The
difference is one *additional* red:

```text
+ unsafe_crossing_family_instantiation      [TARGET, absent from our dag]
```

wired **req** into `unsafe_at_crossing`, and consequently:

```text
unsafe_at_crossing :   ours = PROVED   |   codex = CONDITIONAL
   our req-parents  : averaged_slope_conversion, qfloor_exact
   their req-parents: averaged_slope_conversion, qfloor_exact,
                      unsafe_crossing_family_instantiation
```

### The new obligation, verbatim

> For every admissible row and its proposed safe agreement `a_safe`, supply an exact
> certificate at `a_safe - 1` of at least one of: **(Q)** a quotient order satisfying
> every `qfloor_exact` hypothesis, endpoint alignment, and `Acl(N',ell') > B*`;
> **(V)** an explicit family of more than `B*` pairwise-distinct bad slopes; or
> **(M)** a deterministic post-paid support family `A` with exact strict-overlap
> profile and occupancy `nu(A) = E[N(A)] - (q/2) C_t(A) > B*`. The certificate must
> use the ambient MCA slope field and account for generated-field transfer and
> first-match ownership.

## Why this matters, and why I have not acted on it

If Codex is right, **our `unsafe_at_crossing` is over-claimed as PROVED**, our board
is 24 reds rather than 23, and a PROVED node sits in our critical orbit without its
adjacent-unsafe witness family. That is a defect in *our* tree, found by comparison
— exactly what a harvest is for.

**Not acted on, deliberately.** Demoting a PROVED node on the critical surface is a
status flip requiring the full artifact chain plus the planner's audit, and the
brief reserves retirements and status flips of critical nodes to Fable/the user.
Codex raw branches are read-for-awareness only. **This is surfaced, not applied.**

## What the planner needs to decide

1. Is `unsafe_at_crossing = PROVED` sound in our tree, or does it silently assume an
   adjacent-unsafe witness family it never supplies? Our two req-parents
   (`averaged_slope_conversion`, `qfloor_exact`) do not obviously deliver the
   `(Q)/(V)/(M)` certificate above.
2. If Codex is right, our census line `260 = 201/36/23` is wrong in the
   **over-claiming** direction — the more dangerous one.

## Also observed (not audited)

Their orbit is 18 nodes *smaller* with 21 fewer PROVED, so v10 has rewired
substantially, not merely added. Any integration is a wave-scale audit, not a
cherry-pick.
