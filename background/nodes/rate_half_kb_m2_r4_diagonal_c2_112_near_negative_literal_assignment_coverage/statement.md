# KoalaBear near-negative literal-assignment coverage

- **status:** PROVED
- **scope:** all literal negative near-aligned `c2(1,1,2)` source-line
  cells over characteristic `p=2130706433`
- **dependencies:** aligned-negative literal coverage, negative
  reconstruction factor gate, and q-slice resultant gate
- **consumer:** source-line literal-assignment coverage

Keep the literal frame

```text
J_0={2,1/2,b,1/b},       q(T)=(T-c)(T-d),
Omega={xi,d},             xi in {1/2,2,1/b,b}.     (KBNN-1)
```

The aligned-negative literal theorem proves that the monic residual q-slice
quartic of every reconstructed negative source form has constant term one.
The near target in `(KBNN-1)` has constant term `1/(xi^2 d^2)`. Therefore a
candidate must satisfy

```text
(xi*d)^2=1.                                      (KBNN-2)
```

The branch `xi*d=1` identifies `d` with the reciprocal `J_0` label `1/xi`
and is excluded by the named open. On `xi*d=-1`, substitute

```text
d=-1/xi.                                         (KBNN-3)
```

If `c+d=0` after `(KBNN-3)`, then `c=1/xi`, another `J_0/J_1` label
collision. Thus the generic reconstruction minor covers every admissible
point remaining on the minus branch.

Directly compile the twelve literal source-star assignments and four choices
of `xi`, giving 48 cells. In every cell the specialized consistency
numerator has five irreducible factors. Removing factors shared with the
selected nonzero minor leaves one genuine component in each fixed-moving
cell and two in each moving-moving cell, for 64 component systems.

On each component, the four q-slice coefficient equations generate the unit
ideal after localization by all literal-label collisions, incidence and
reconstruction determinants, degree factors, and rational denominators.
One-step Rabinowitsch localization and independent sequential saturation by
the same irreducible factors agree on all 64 unit classifications.

Hence no literal near-negative assignment passes the necessary q-slice
gate. Together with the aligned-negative literal theorem, the complete
negative-sign literal residual is empty.

## Falsifier

A literal assignment/root pair outside the 48-cell census, a missed
consistency component, a non-named factor in the localizer, or a nonunit
component ideal under either saturation formulation.
