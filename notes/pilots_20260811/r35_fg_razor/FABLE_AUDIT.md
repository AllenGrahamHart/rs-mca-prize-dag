# FABLE_AUDIT — r35_fg_razor (round 35, bank 2/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — R-FG-RAZOR walled AND downgraded; the type-2
ledger's vacuity on the open bracket accepted as a scope fence;
R-HRLOW adopted as the new load-bearing far-CA residual; two
forced scope corrections applied to banked text (both flagged by
the pilot, verified by me).** Node work: the round-35 R-FG-RAZOR
addendum + two inline SCOPE-CORRECTED markers on the round-34
text (LB1-generic; q_crit). No status flips; census unchanged.

## Replay + verification

- **e3_razor.py replayed** (tiny, RAMGUARD_TIMEOUT=55, EXIT=0):
  deterministic exact-integer arithmetic; the regenerated
  e3_results.txt carries every constant the REPORT quotes —
  E1-E22 exact, theta_2 = 63.988728, theta_1 = 127.977457, the
  vacuous floor -1,065,151,889,407, p*(LB1) = 549,755,813,889,
  and the internal banked-constant check (LB1-C margin at
  q=2^167 -> 670,014,898,009, match: True). NOTE: my replay ran
  before I copied the pilot's original (overwrote it); since the
  script is deterministic and the regenerated file matches every
  REPORT quote, content identity is established; byte-provenance
  of the pre-replay file is not (disclosed).
- **Coordinator hand-checks:** 2r-R = R-2rho = 62r/63 =
  1,065,151,889,408 (r = 63*2^34) — CHECK; theta_2 = 64*H2(63/128)
  from n/(2rho) = 64, r/n = 63/128 — CHECK; the LB1-C margin
  (2^34-1)*167 - 2^41 = 670,014,898,009 — CHECK by hand,
  exact match with crossing_location:640-641; floor((R+2)/2) =
  2^39+1 = 16*(2rho)+1 — CHECK; the (C2) sign mechanism (floor
  positive for all W iff 2r <= R iff a >= 3n/4) — CHECK against
  the banked unique-decoding radius line.
- REPORT.md persisted (WROTE verified, 47,918 chars).

## The two forced corrections (verified before applying)

1. **q_crit is a razor-row constant.** theta_2 = n*H2(r/n)/(2rho)
   is shape-dependent; at the official row's own shape
   (r/n ~ 1/4) it evaluates to 1.6226, not ~64. The banked
   sentence was correct only at a = k+2^34. Inline
   SCOPE-CORRECTED marker applied; the key-equation threshold
   theta_1 = 2*theta_2 added.
2. **"LB1 is GENERIC" does not transfer.** The 3591/3591
   measurement is at LB1's own k=2 small cell (a-1 < r regime);
   at razor-faithful shape (a > R+1, a-1 > r) the law is
   p*(LB1) = max(rho+1, floor((R+2)/2)), confirmed 5/5 rate-half
   + 3/3 k=1 cells. Inline SCOPE-CORRECTED marker applied. The
   pilot's own MISS 1 (its first k=1 design would have banked the
   OPPOSITE conclusion) is the strongest argument for the
   faithfulness conditions it names — recorded in the addendum.
3. (Recorded, not an edit:) the r34_pstar REPORT's D1.2 "FG"
   label on the h_r = p* row is wrong as a criterion (h_r = p*
   necessary, not sufficient; d* < p* counterexamples 3/3).
   Banked artifact stays byte-original; the correction lives in
   the addendum. Witness B unaffected (deg P = p, 10/10).

## Assessment of the restructuring

The R-HRLOW promotion is evidence-based and I adopt it: the
extremal object (LB1) sits at h_r = rho+1 with a field-size-
independent structural floor T_1 = r+1 attaining (C3) at 0 bits,
while FG shows no floor and tracks its (deeply subcritical at
official rows) first moment. The nesting R-FG < R-KER is
structurally verified. The "first moment wrong by 6.70e11 bits"
exhibit (proved floor vs mu_1) is the sharpest anti-random-model
statement in the lane and correctly grounds the priority
inversion. The type-2-ledger scope fence closes a whole class of
future wasted transports (and retroactively explains the zero
grep hits connecting the ledgers).

## Honesty audit

Strong: MISS 1 (the near-inversion of the headline by a
non-faithful cell) reported first; the wrong principality test
(MISS 2) re-run rather than patched over; the E20 interpretive
miss conceded with its hedge; the 2^128 numerology explicitly
defused; the killed run (MISS 9) and the widened q-range (MISS 7)
disclosed; the column-close LB1 row and the T=0 FG instance
reported rather than dropped.

## Compliance

Compute law CLEAN 6/6 (zero bare python3 — sixth consecutive
clean pilot). Upgraded write discipline CLEAN (the one redirection
created a NEW file, permitted). Quarantine clean — and the pilot's
find-names-only maneuver to build a certifiable exclude list is
the right fix for the round-34 gap; round-36 CONSTRAINTS will
pre-list sibling names instead. Registrations honest (the
semi-blind markings are the standard the honesty-note precedent
set in r34_pstar).

## Mint queue additions

1. The type-2-ledger scope fence node ((C2) sign law; the
   62r/63 threshold; "vacuous by sign before vacuous by
   counting").
2. R-HRLOW as target of record + the h_r-indexed residual family
   (LB1 coordinates: h_r = rho+1, p* = floor(R/2)+1,
   dim K_0 = r-rho, T_1 = r+1).
3. The p*(LB1) shape law + faithfulness conditions (a > R+1,
   a-1 > r).
4. The theta_1/theta_2 pair + the first-moment-vs-LB1 exhibit.

## Round-36 anchors fed by this bank

R-HRLOW (above R-FG-RAZOR); the h_r = rho+2..O(1) band between
LB1 and FG; whether any FG pencil beats its first moment (the
named gap — now secondary).
