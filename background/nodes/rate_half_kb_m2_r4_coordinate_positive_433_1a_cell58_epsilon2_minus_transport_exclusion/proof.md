# Proof

The common compiler enumerates cells `5` and `8` exactly as in `(KBC58-1)`.
Transposing `AB+1` and `AB+2` sends one assignment to the other.  Those two
roles have the same product `b` and sum `1+b`; hence the transposition fixes
their target data.  It merely relabels the occupied common source quotient
and its complementary outside source slots.  The universal target
elimination theorem is equivariant under this source-record relabeling, so
`rho` preserves the complete packet equations and guards.

Fix one of the two cells.  Its common roots are

```text
LC=1,  AC=epsilon_1*i,  AB+=r,
AB-=epsilon_2*i*r,      singleton=t,
```

with `i^2=-1`; the displayed `AB+` is the nonsingleton copy.  Under
`(KBC58-3)`, each root square is fixed.  Therefore every quotient label and
product row is fixed.  The `LC` sum is zero.  Direct substitution shows that
all four nonloop values `q=z*s` are negated.  Multiplying Vieta rows by
nonzero scalars alone is not the asserted transport: a sum row also contains
the `B_1` coefficients.  Instead send the coefficient polynomial `B_1` to
`-B_1`.  For every nonloop record,

```text
q A_2 + lambda B_1 = 0
    -> (-q) A_2 + lambda(-B_1)
     = -(q A_2 + lambda B_1)=0.
```

For the loop, `q=0`, so the same coefficient involution simply negates its
sum equation.  Product equations do not use `B_1` and remain fixed.  This
gives an invertible correspondence of complete common coefficient kernels.

For every outside record, replace its source lift `z` by `-z`.  Its quotient
label `z^2`, target product, and product row stay fixed, while `z*s` and the
`q` part of its sum row are negated.  The same `B_1 -> -B_1` involution
carries that transformed equation to the negative original equation.
Source distinctness depends only on quotient labels; target distinctness
and all target equations are unchanged.  Hence this is an exact bijection
of admissible complete packets between the two `epsilon_1` rows at fixed
`epsilon_2`.

The complete-sign-row theorem excludes cell `5`, signs `(-1,-1)`, for every
deployed value of `t`.  The sign transport excludes cell `5`, signs
`(+1,-1)` (sending `t` to `-t`), and `rho` transports both exclusions to
cell `8`.  This is exactly `(KBC58-4)`. QED.
