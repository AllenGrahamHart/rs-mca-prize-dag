# Proof

Expanding the normalized denominator reversal gives `(C2G1)--(C2G2)`. Since
`A=E^(-1/4)`, logarithmic differentiation yields

```text
4EA'+E'A=0.                                           (1)
```

The coefficient of `z^(n-1)` in `(1)` is

```text
4n a_n+sum_(j=1)^min(4,n)(4(n-j)+j)E_j a_(n-j)=0.
```

Since `4(n-j)+j=4n-3j`, this is `(C2G3)`. On the maximal
row the field-degree collapse gives either a prime field with
`p=1 mod 2^41` or a quadratic field with `p=+/-1 mod 2^40` and the official
budget lower bound. In both cases `p>N`, so every `4n` used through degree
`N` is invertible.

The boundary transfer gives `r=2H-3` and the primary fourth-root gap
`(C2G4)`. Its two-window square theorem gives `(C2G5)--(C2G6)`, including
existence and uniqueness of `C` under `C(0)=1` and the degree bound. Thus the
primary and secondary conditions depend only on the recurrence inputs
`(t,S,P)`.

For degrees below `N`, one has `Q=E^(-1)=A^4`. Since

```text
A-B=c z^(2H)+higher terms,                            (2)
```

the factorization

```text
A^4-B^4=(A-B)(A+B)(A^2+B^2)                          (3)
```

shows that the coefficient of `z^(2H)` in `R` is `4c`. This proves the
formula for `alpha` in `(C2G7)`. The remaining definitions in `(C2G7)` and
the span identity `(C2G8)` are exactly the canonical-span certifier after the
doubled-order boundary transfer. Its uniqueness formulas prove that `beta`
and `gamma` are outputs, not search variables.

The binary-quartic invariants of the resulting canonical outer quartic are
those in `(C2G9)`. The normalized selected denominator pair is `{1,t}`, so
its pair trace is `z_t=(1+t)^2/t`. The joint pair-torsion selector and the
mismatch invariant converse say that its completion-root PGL coupling holds
if and only if the outer invariant cubic vanishes at `z_t`; expanding that
cubic is `(C2G10)`.

All transformations used above are equivalences within the retained generic,
split, squarefree chamber. The normalized-pair dependency supplies the exact
torsion, distinctness, split, square-class, and orientation conditions. The
canonical-span and mismatch-invariant dependencies supply the two converse
reconstructions. Therefore the displayed interface loses and adds no
normalized packet. QED.
