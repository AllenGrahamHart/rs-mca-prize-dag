# Claim contract - L1 quotient-chart bipolar entropy closure

## Inputs

- one source chart whose petal and core blocks are complete fibers of the same
  degree-`ell` quotient polynomial;
- fixed petal-polarity and core-polarity caps `P_0,B_0`;
- `ell>=c_0 n/log_2 n`, `ell>2P_0`, and `q<=n^gamma`;
- the strict-window and thin-edge numerator theorems.

## Output

The complete common-pencil class in the fixed bipolar box is polynomial per
source chart with explicit bound `(BE4)`.

## Consumer rule

Consumers may replace the one-sided bounded-boundary residual by the stronger
condition that petal polarity or symmetric core polarity is unbounded. They
must retain cross-chart aggregation, non-quotient cores, and arbitrary petal
locators.

## Falsifier

A petal support or defect set missing from its orientation-plus-exceptions
encoding, or a fixed support/locator pair exceeding the applicable CRT bound.

