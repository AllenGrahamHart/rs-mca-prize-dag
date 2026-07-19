# Audit

Date: 2026-07-18.

## Primary-source read

The proof was checked against Konyagin--Shparlinski--Vyugin,
*Polynomial Equations in Subgroups and Applications*, arXiv:2005.05315,
especially equations (1.8), (1.9), (2.3), Lemmas 2.1 and 2.4, and equations
(4.2), (4.4), and (4.5). For bidegree `(2,1)`, their dimension condition is
exactly `4(A0 D+3D^2)<A0BC`, their singular allowance is `9`, and their
Bezout term is `3(B+C-1)n/D`.

The source theorem prints an unspecified lower-order threshold. This node
does not consume that threshold: it reuses the displayed auxiliary
construction and checks every dimension, coprimality, and degree inequality
on all 29 orders. The subgroup-preserving change `(x,y)->(x,x/y)` is
bijective and repairs the one-monomial lowest-part defect of the original
normalization.

## Forward audit

For `tau!=0,1`, `Q_tau` is irreducible and its lowest homogeneous part has
two terms. The three floor repairs are exactly the rows where the unadjusted
dimension inequality fails. The final constant `33` is strict on every row;
the same parameter family cannot prove `32`, which the verifier checks as a
negative control.

## Consumer-backward audit

The C36 leaf needs a weighted product/quotient correlation. `(PF33)` gives
only a pointwise cap on `P`. At `n=8192` the cap is already above `13,000`,
far above the rich threshold `19`. The theorem is therefore evidence and a
future joint-incidence input, not a discharge of any critical premise. Its
critical-target edge remains `ev`. The only `req` edge is to the proved joint
derivative-ideal node, where `(PF33)` merely replaces the trivial excess cap
`n-19` by `ceil(33n^(2/3))-19` in the separator exponent. The verifier rejects
every other required consumer.

## Replay scope

The verifier checks all finite parameter inequalities using integer
arithmetic, detects the three necessary floor repairs and the failed
constant-32 mutation, proves the normalized equation by exhaustive finite
fixtures, and checks the DAG status and evidence edge. It uses no Modal.
