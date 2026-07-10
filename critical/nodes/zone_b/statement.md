# zone_b

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONJECTURE]
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

Determine |{e_1(B) mod p : B in binom(Q, l')}| for quotient orders 80 < N' < 512 at prize-scale p: (1-o(1))-full vs collided (= prob:perfiber at sigma = 1). SHARPENED (E1 compatibility): on 2-power rows the open cells are the 2-power divisors in (80, 512) — for Row C exactly N' in {128, 256}: the corridor question is TWO value sets per row.

## Attack surface

extend the split-prime transfer range, or the norm threshold, or prove e1-fullness directly

## Falsifier

Row-C birthday sampling showing collision rates far from either the full or the heavily-collided prediction

## Ledger (migrated notes)

PREFERRED ROUTE (evidence-backed): collision-free branch via norm criterion -> density -> typicality (e1_random_prime_model); collided-branch machinery (averaged_slope_conversion) is INSURANCE, not the plan.
