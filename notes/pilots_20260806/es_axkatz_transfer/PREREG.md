# PRE-REGISTRATION — the Ax-Katz / Chevalley-Warning transfer on (ES)

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. This is the campaign's single
most important open thread: the ONE untested classical transfer on the
four-lane terminal.

## 0. The frontier (verbatim, FABLE_AUDIT of mun_anticoncentration)

> **THE FRONTIER**: the exact zero-count statement (0/1 codewords of
> the [2^41, 2^41-w+1, w] RS codes = periodic only), with four
> proved structural constraints on any solution, and **AX-KATZ /
> CHEVALLEY-WARNING as the untested transfer** — p-divisibility is
> the one classical family sensitive to defining sets.

And the route cut already PROVED (do not re-litigate): identical-
enumerator code pairs with different 0/1 counts — MacWilliams /
Delsarte / Krawtchouk / Sidelnikov / BCH-family CANNOT decide it in
principle; Weil vacuous 13.5-107 bits; L2 loses exactly 2^128.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260804/mun_anticoncentration/PREREG.md` section 0 —
  the object of record: the crossing count is the constant-weight
  count `W_w = { x in {0,1}^n <= F_p^n : wt(x) = r', x in C(n,p,Z_w) }`
  at n = 2^41, w in [2^34, 2^39], r' = 2^40 - w, delta = ord_n(p) in
  {1,2,4}, p >= 2^39+1; the band instance table (strictly finer);
  Newton invertibility at all four rows.
- `notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md` — the
  (ES) statement of record, the four structural constraints, the
  measured early suppression, the above-balance accident witness.
- The five verifiers in that dir — reuse their exact-count machinery
  for calibration rows (they are the banked ground truth).

## 2. Pre-registered claims

- **(A1)** The algebraization: exhibit the count |W_w| as the F_p
  point count of an explicit polynomial system (the 0/1 locus
  x_i^2 = x_i, the vanishing prefix e_1 = ... = e_{w-1} = 0 — or the
  power-sum prefix, Newton-invertible at all rows — plus the weight
  equation), with degrees and variable count stated exactly, in BOTH
  the base-field and delta-extension readings.
- **(A2)** The Ax-Katz divisibility exponent mu computed EXACTLY for
  that system at the four rows of record (both readings), and the
  Chevalley-Warning baseline. State the formula before plugging in.
- **(A3)** THE DECISION: does p^mu-divisibility, combined with the
  four proved structural constraints and the exactly-known periodic
  count, FORCE |W_w| = (periodic count)? Pre-register the three
  possible verdicts and what each requires:
  (i) TRANSFER LIVE — divisibility gap exceeds the accident budget;
  state the remaining obligation as a named lemma.
  (ii) TRANSFER DEAD-VACUOUS — mu too small to separate; prove it
  and state the exact shortfall in bits (as was done for Weil).
  (iii) TRANSFER DEAD-INSENSITIVE — divisibility holds equally for
  periodic-only and accident-bearing counts; exhibit the failure on
  the round-15 identical-enumerator pair or a new witness.
- **(A4)** Calibration: on toy rows where the exact counts are banked
  (reuse the round-15 verifiers), check the Ax-Katz prediction against
  the true counts. `tools/ramguard local -- python3 ...` scale only.
- **(A5)** If the transfer is dead, name what property of the
  defining-set structure a decisive method must see (sharper than
  "not the enumerator"), to steer the Pro brief and the next pilot.

## 3. Pre-registered falsifiers / honesty clauses

- If the algebraization itself is wrong (e.g., the 0/1 slice cannot be
  polynomial-encoded without blowing up degrees past usefulness),
  report that as the finding.
- Any claim of (i) must survive its own adversarial check: verify the
  divisibility bound is NOT satisfied by adding one accident pair to
  the periodic count. If it is, the verdict is (iii), not (i).
- Small-p calibration failures kill the row-level claim, not the
  method; separate the two explicitly.

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  `notes/pilots_20260806/es_axkatz_transfer/`. Never touch dag.json,
  node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.
