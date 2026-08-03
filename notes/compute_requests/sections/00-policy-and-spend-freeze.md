# Proximity Prize deferred compute requests

> **OPERATING PROTOCOL:** Authorization, RAM discipline, and upstream handoff
> rules are summarized in `notes/JOINT_PRIZE_RESOLUTION_PROTOCOL.md` section
> 10. This file remains the authoritative request ledger and run log.

> **PLAN-OF-RECORD POINTER (2026-07-22).** The resolution roadmap was
> rewritten as the date-free r3 gates-not-dates form and installed at
> `notes/PRIZE_RESOLUTION_ROADMAP.md` (maintainer-directed; supersedes every
> prior copy including branch-local ones — KB #120). Before posing a new
> campaign or large compute request, re-read it: sequencing is by the gates
> D0/D1/U3/D3, the dli lane carries a standing one-third effort cap (D2),
> and new poses should name their track (N/A/B/C/H) and pre-registered
> falsifier.

This ledger records computations whose outputs could close or decisively
reshape a named proof branch but whose conservative cost exceeds the current
sub-`$1` Modal policy. It is suitable for contributor requests and upstream
PR notes. Entries are not theorem claims, and partial runs are evidence only.

Every request must specify the mathematical decision, completeness boundary,
certificate format, deterministic checker, resource estimate, and effect of
both outcomes on the critical DAG. Shallow sweeps without a named decision do
not belong here.

> **MAINTAINER GOVERNANCE NOTE (2026-07-20, wave-17 integration — UNRATIFIED;
> carried forward 2026-07-21 across the w18-C1 ledger adoption).**
> The sub-`$1` Modal self-authorization clause remains maintainer-unratified
> (standing item w16-C5). Wave-17 was the **first wave to actually exercise
> it**: three in-tree Modal launches, each a no-hit exclusion screen whose
> `result.json` is **load-bearing for a PROVED node's `verify.py`** (via a
> local coverage/hash certificate checker; no local re-execution):
>
> | app_id | screen | ceiling | candidates/shards | hits | consuming PROVED node |
> |---|---|---|---|---|---|
> | `ap-6KQ2mJjoE3Qkq7VaKqnxlZ` | c1-parity-antiinvariant | `$0.25` | 2,247,721 / 16 | 0 | `…c1_parity_frobenius_router` |
> | `ap-Js6Im9DeoBlc0di05YG2WE` | c1-parity-harmonic-characteristic | `$0.50` | 4,495,441 / 32 | 0 | `…c1_parity_harmonic_exclusion` |
> | `ap-PVTrzkKlh4j1B6qDmGU1Wf` | harmonic-top (order 2^41) | (none stated) | 2,247,720 / 16 | 0 | `…matched_post_field_compiler` |
>
> The three nodes are wired **ev-only** into `rate_half_list_adjacent_crossing`
> (still TARGET); no red flipped on their account. Wave-18 launched zero jobs
> and TIGHTENED the policy (the >= `$1` / unknown / could-exceed-balance
> do-not-launch rule below).
>
> **RESOLVED 2026-07-21 (maintainer ruling, w17-C1).** (a) Remote no-hit
> screens carrying a local coverage/hash certificate ARE accepted as PROVED
> evidence; the three screens' launchers and checkers are now registered in
> the verifier manifest via per-node `verify_screen_certificate.py` (hash
> pins) and `verify_screen_remote.py` (remote launcher). (b) The sub-`$1`
> self-authorization clause is SUPERSEDED by the **time-based rule** in the
> maintainer-ruling section below: self-authorized launches must keep total
> wall-time under 5 minutes. This also settles standing item #260 in
> principle (queued jobs re-screen under the time rule).

## Current spend freeze

As of 2026-07-21, the local Modal account has about `$3` of credit remaining.
No large run in this ledger is authorized against that balance. Preserve it
for an explicitly approved, route-deciding pilot with a conservative total
cost below `$1`; otherwise treat every entry as an outbound contributor
request for an upstream PR.

Record newly identified valuable computations here even when they are not yet
executable. Use a **pre-request** while a finite completeness router, measured
pilot, checker, or cost ceiling is missing. Promote it to a numbered request
only when another contributor can run a bounded campaign and know exactly what
PASS, FAIL, and incomplete output mean. This distinction prevents an
open-ended search from being presented as useful donated compute.

The default disposition for any newly identified run whose conservative cost
is at least `$1`, is unknown, or could exceed the local balance is: do not
launch it; record it here with its proof purpose and readiness gaps. When the
related mathematics is vendored to Przemek's repository, include the record
as an upstream compute request so a contributor with suitable resources can
accept a declared budget and run it independently.

## Maintainer ruling (2026-07-21): time-based self-authorization

The self-authorization criterion above ("explicitly approved ... conservative
total cost below `$1`") is **superseded**. A Modal launch is self-authorized
if and only if ALL of:

1. it is **route-deciding** for a named node or pre-registered falsifier;
2. its conservative estimate of **total wall-time is under 5 minutes**
   (per-shard timings must be banked in the certificate so the bound is
   auditable after the fact);
3. a **result certificate + deterministic local checker** are banked with the
   launch (coverage accounting, per-shard hashes, hit list), and the checker
   is registered in the verifier manifest when the result becomes
   load-bearing for a node's verifier;
4. the launch is **logged in this ledger** (app id, purpose, wall-time).

Anything failing any clause is an outbound contributor request. The dollar
phrasing elsewhere in this file is retained for historical continuity; the
time rule governs. (Ruling recorded in notes/MAINTAINER_DECISIONS_20260713.md;
standing item #260's queued jobs re-screen under this rule.)

### Current operational cap (2026-07-22)

The monthly Modal allowance has refreshed to about `$30`. A self-authorized
launch must still satisfy every rule above **and** have a conservative total
cost below `$1` unless the maintainer explicitly approves more. Thus the
operative test remains the intersection of the five-minute and sub-`$1`
ceilings, not either ceiling alone. Runs costing tens or hundreds of dollars
are out of scope.
Valuable runs exceeding either ceiling, or lacking a reliable cost estimate,
must be recorded here and copied into the corresponding upstream PR as
requests for contributors with available compute.
