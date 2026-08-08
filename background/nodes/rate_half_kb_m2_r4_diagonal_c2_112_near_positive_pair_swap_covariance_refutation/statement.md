# KoalaBear near-positive reciprocal-pair-swap covariance refutation

- **status:** PROVED
- **scope:** the natural reciprocal-pair-swap centralizer map on affine
  positive near-aligned q-slice systems
- **dependencies:** source-line internal-star reconstruction and q-slice gate
- **consumer:** source-line literal-assignment coverage

Put

```text
u=(2b-1)/(b-2),       phi_b(x)=(u x+1)/(x+u),
b'=phi_b(2)=(5b-4)/(4b-5).                       (KBPS-1)
```

Then `phi_b` commutes with inversion and sends

```text
b -> 2,       1/b -> 1/2,       2 -> b',       1/2 -> 1/b'.
```

It therefore exchanges the fixed and moving reciprocal pairs. Its induced
action on source assignments is

```text
F00<->F04  F01<->F06  F02<->F05  F03<->F07
M00<->M01  M02<->M03.                            (KBPS-2)
```

When `c,d,W` are transformed by the same map, all twelve target quadratics
transform exactly, with target-root action

```text
A->OB,       TA->OI,       OB->A,       OI->TA.  (KBPS-3)
```

However, the reconstructed source residuals are not covariant. For every
one of the twelve source assignments, both endpoint residuals fail
projective equality with the destination in `(KBPS-2)`. An exhaustive exact
rational search over all twelve possible destination assignments and both
root orders finds no destination for any source assignment.

Consequently the missing reciprocal-pair-swap centralizer element cannot be
added to the proved inversion transport group. The combinatorial orbit count
it would produce is not an algebraic q-slice coverage theorem.

This statement does not prove that any literal cell is nonempty or empty. It
does not rule out a different, explicitly proved nonlinear transport, and it
does not concern full quotient identities or projective boundary charts.

## Falsifier

An exact destination assignment and root order for which the pulled-back
residual pair is projectively equal under `(KBPS-1)`, or a failure of one of
the reported target identities.
