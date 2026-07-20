# Claim contract - L1 quotient-chart bounded core-boundary closure

## Inputs

- one fixed source chart whose petals and core are complete fibers of one
  degree-`ell` quotient polynomial;
- the L1 cutoff `ell>=c_0 n/log_2 n`, `ell>2P_0`, and generated field
  `q<=n^gamma`;
- fixed bounds `p<=P_0`, `beta(D)<=B_0`;
- one arbitrary degree strip `m ell<d<(m+1)ell`.

## Output

The complete fixed-chart class is polynomial with the explicit bound `(BC4)`.

## Consumer rule

Consumers may delete this bounded box from the fixed-chart common-pencil
frontier. They must retain cross-chart aggregation, unbounded `p` or `beta`,
non-quotient cores, and arbitrary petal locators.

## Falsifier

A support pattern missing from the dense/sparse exception encoding, a defect
locator missing from the quotient-boundary encoding, violation of `(BC1)`, or
a fixed locator with more than the applicable strict-window or thin-edge CRT
bound.
