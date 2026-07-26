# Claim contract

## Inputs

- `fm1` for each exact support size;
- the nonnegative correction in `averaged_slope_conversion`;
- the six named clean predecessor agreements and numerator budgets.

## Output

- an exact impossibility result for the current averaged-occupancy `M`
  supplier at all six named envelopes;
- coverage of arbitrary support subfamilies and mixed support sizes `>=a`.

## Guards

1. The statement concerns the named high-budget envelope checks, not every
   admissible row.
2. The unsafe point is `a=a_safe-1`.
3. Larger support sizes are included through a geometric tail bound.
4. The proof uses only `nu(A)<=E[N(A)]`; no overlap profile is assumed.
5. Failure of this supplier is not an upper bound on `B_C(a)`.

## Falsifier

A support family at one named envelope with `E[N(A)]>=B*`, or a failure of one
of the exact row comparisons, refutes the node.
