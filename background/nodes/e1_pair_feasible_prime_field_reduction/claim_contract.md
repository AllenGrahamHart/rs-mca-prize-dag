# Claim contract

## Inputs

- the exact two numerator budgets and target denominator `2^128`;
- quotient orders `N in {256,512}`;
- the canonical quotient definition `Q=D^(n/N)`, hence `Q` has order `N`;
- `e1_pair_feasible_ambient_generation`;
- finite-field root-degree identity `d=ord_N(p)`.

## Output

- prime-field reduction of the pair-feasible E1 target at all six named
  anchors.

## Guards

1. Ambient generation is required before identifying the extension degree
   with `ord_N(p)`.
2. Perfect-power roots use exact integer arithmetic.
3. The RowC square candidates are rejected by parity or order, not a probable-
   primality test.
4. The conclusion concerns the two named budget intervals.

## Nonclaims

- No prime in either interval is enumerated or certified.
- No E1 collision is excluded.
- No safe or unsafe endpoint moves.
