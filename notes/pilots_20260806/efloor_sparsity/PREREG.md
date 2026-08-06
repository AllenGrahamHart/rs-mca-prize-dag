# PRE-REGISTRATION — E_floor SPARSITY (hybrid): prove the sparsity half of CC, and attack it

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. HYBRID mandate: half the
pilot proves (sparsity of the exceptional floor class), half attacks
(construct the DENSEST floor families you can — the truth is wherever
the two meet). This is the repo's long-named pair-coprimality open
lemma in its round-17 sharpened form.

## 0. The object (round-17 es_coprimality, banked)

```
E_floor = { S : some odd p | N_odd(I_S) has |Z_w^odd(p)|·log2 p <= (n/4)·log2 r' }
```
CC-sparsity: |E_floor|/#orbits -> 0 as w grows (measured: 0.9934+
coprimality rates at w >= 3, exactly 1.00000 at the crossing shape).
THEOREM CS makes E_floor membership REQUIRE a small bad prime
(p below the CS3 floor); the measured residual bad primes at
a = 0, w >= 3, n = 32 are ONLY {3,7,17,47,97,193,257,353,449}.

The lineage (quote both): the pair-coprimality open lemma
(critical/nodes/u1_x4_direct_column_budget/notes/F3_SHALLOW_LADDER.md:200-202,
"ONE open lemma (pair-coprimality / norm-gate sparsity) stands
between the data and the theorem — shared verbatim with F2's
accident story") and CATCH-17B (the u2c empirical credit was never
banked mathematics — this pilot is the debt coming due).

## 1. Source surfaces (read ALL first; quote verbatim)

- notes/pilots_20260806/es_coprimality/{REPORT.md, PROOFS.md,
  cop_lib.py} — THEOREM CS, LEMMA TWO/STRAT, the E_floor
  definition, the rate table, the bad-prime lists, the HNF norm
  machinery (reuse it; it is banked).
- notes/pilots_20260806/es_boundary_adversary/REPORT.md — the
  witnesses (three of five are E_floor members: (47), (23), (463)
  rows) and the census method.
- background/nodes/dli_wcl_weight3_ambient_exclusion/proof.md +
  weight4 sibling — the banked resultant/bad-prime method and its
  PROVED exclusions (subtract; these may already prove small-w
  floor emptiness in their regime).
- critical/nodes/u2c_giant_tnull_dichotomy — the consumer whose
  empirical credit this lemma would convert to mathematics.

## 2. Pre-registered deliverables

- **(S1, generative) SMALL-PRIME EXCLUSION.** For a FIXED small
  prime p (start p = 3, then 7, 17), characterize/bound the S with
  p | N_odd(I_S) at given (n, r', w): this is the F_p-solution count
  of the reduced window system — a fixed-characteristic question the
  banked weight3/weight4 exclusions may already partially cover.
  Target theorem shape: for each fixed p, the density of
  {S : p | N_odd(I_S)} among orbits is <= f(p, w) with
  sum_p f(p, w) -> 0 as w grows (a union bound over the FINITE
  bad-prime range that CS3 leaves alive). If provable even for
  p = 3 alone, it is the first sparsity theorem.
- **(S2, adversarial) DENSEST FLOOR FAMILIES.** Construct S families
  maximizing bad-prime membership: coset-near unions, arithmetic-
  progression supports, LEMMA-STRAT-boundary structures. Measure
  their density contribution exactly. The goal: locate the TRUE
  decay rate of |E_floor|/#orbits in w and n, and find whether any
  family gives a NON-vanishing density (which would refute
  CC-sparsity — report as a catch with witnesses, per the falsifier
  below).
- **(S3) The n-asymptotic.** The round-17 measurement is n <= 32
  only. Extend the exact census to n = 64 at the feasible (r', w)
  corner under ramguard-local (pre-register the reachable grid
  first; if n = 64 is out of reach in 5-minute chunks, say exactly
  what was reached — round 16 left an honest unreached-n = 64 flag;
  close it or re-flag it honestly).
- **(S4) The u2c conversion statement.** State exactly what
  (S1)-form theorem would convert u2c's 1440-trial empirical credit
  into mathematics, and how far this pilot got toward it.

## 3. Pre-registered falsifiers / honesty clauses

- A constructed family with non-vanishing floor density refutes
  CC-sparsity as posed — campaign-relevant catch, report with
  reproduction script; the round-17 conditional (K5) then needs
  re-scoping, not silent repair.
- (S1) bounds must be proved for the stated p, not extrapolated
  across primes; the union bound must use the PROVED CS3 floor for
  its range, cited exactly.
- n = 64 nulls from unreached regimes are not evidence (round-16
  rule).

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/efloor_sparsity/. Never edit dag.json, node
  shards, tools/, or push. Do NOT read
  notes/pilots_20260806/crossing_low_w/ (sibling this round).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. Includes file patching
  and JSON peeking (three round-17 pilots breached exactly there).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.
