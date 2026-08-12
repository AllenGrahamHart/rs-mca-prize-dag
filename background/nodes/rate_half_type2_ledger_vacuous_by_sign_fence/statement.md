# The type-2 ledger is vacuous BY SIGN on the whole open bracket

- **status:** PROVED (exact arithmetic; a scope fence of record)
- **closure:** sign computation on the (C2) per-slope floor
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/type2_ledger_scope_fence/`,
  coordinator line-audited.

## The statement

`(C2)`'s per-slope floor is

```text
floor(W) = (R + 1) - w*,        w* = |W| = |S_g u S_h| in [r, 2r].
```

It is positive **for every admissible `W`** iff

```text
2r <= R      <=>      a >= 3n/4,
```

i.e. exactly at the top of the open bracket — the unique-decoding radius.
At rate one half (`k = R = n/2`, `r = n-a`) the two conditions are
*identical*, not merely related; the verifier checks the equivalence for
every `(n, a)` with `n <= 398` even, and at razor.

## At razor shape it is vacuous BY SIGN, not by slack

```text
n = 2^41,  k = R = 2^40,  rho = 2^34,  a = k + 2^34 = 1116691496960,
r = n - a = R - rho = 63*rho = 1082331758592.
```

The adversary takes `w* = 2r`, giving

```text
floor = (R+1) - 2r = -1,065,151,889,407.
```

The floor is positive only if

```text
|S_g ^ S_h| >= 2r - R = 62*rho = 62r/63 = 98.412698% of r,
```

which is **adversary-free**: nothing forces two supports to overlap in
`98.4%` of their points.

## The consequence — a SCOPE FENCE of record

> **No transport of `(C2)`/`(C3)`/`(C4)`/`X_gamma`/layer-A instruments into
> `[k+2^34, 3n/4)` can bind.**

The bracket is **vacuous by sign before it is vacuous by counting**. The
verifier confirms the whole half-open bracket lies on the vacuous side and
that the sign flips **exactly** at the excluded top `a = 3n/4 = k + 2^39`,
where the floor is precisely `+1`.

No banked text connected the type-2 ledger to far-CA (zero grep hits) — and
now there is a **proved reason** not to.

## Worked small cell

`n = 22`, `k = 11`, `R = 11`, `rho = 2`, `r = 9`, `a = 13`: the adversary's
`w* = 18` gives floor `12 - 18 = -6`; the threshold is `2r - R = 7` out of
`r = 9`; and `a/n = 13/22 < 3/4`, so the cell sits on the vacuous side —
the same three facts as at razor, at a scale one can read.

## Relation to the sibling fences

`2r > R` at razor is the SAME inequality that puts the razor row at
`r > R/2`, which is why the proved bound `B_ca^far(n-r) <= r+1` does not
cover the crossing offset either (sibling node
`rate_half_far_ca_negation_closure_excess_fence`). **One inequality, two
fences.** It is also why the crossing-offset value question's cap must come
from the fibre pigeonhole rather than from any ledger import — the (FIB)
cap in `rate_half_far_ca_crossing_offset_value_ledger` is explicitly a
from-scratch pigeonhole for this reason. [WIRING NOTE 2026-08-11: the
value question was posed as STATEMENT U at drafting time; U was REFUTED in
round 37 (the far-CA count is `r+1 + Theta(n/rho)`, see the successor node
and A1's Round-37 U-rand addendum). The refutation changes the ANSWER, not
this fence: the ledger-import route stays closed either way, and the
pigeonhole cap remains the only cap instrument on the bracket.]

## Scope

- Exact integer arithmetic; **no measurement, no field dependence, nothing
  asymptotic.**
- The fence says the ledger cannot BIND on the bracket. It says nothing
  about whether the bracket's true `B_ca^far` is large or small — that is
  the value ledger's question, now priced `r+1 + Theta(n/rho)`.
- `w*` is reported in the source under a `24`-locator cap; the direction of
  that cap FAVOURS the vacuity conclusion, so it does not weaken the fence.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:3613-3625`
  (Round-35 R-FG-RAZOR addendum, 2026-08-11, coordinator-audited; round 35
  bank 2, pilot `r35_fg_razor`; every committed razor integer E1-E22 replayed
  exact, ibid. :3608-3611).
- The `24`-locator cap and its direction: ibid. :3672-3677.
- Razor constants independently banked at
  `notes/pilots_20260811/r36_hrlow/f4_results.txt:30`.

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_type2_ledger_vacuous_by_sign_fence/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_type2_ledger_vacuous_by_sign_fence/verify_audit.py
```
