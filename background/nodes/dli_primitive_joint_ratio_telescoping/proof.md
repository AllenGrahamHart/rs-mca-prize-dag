# Proof

At level zero the alphabet is `{0,1}` with unit weights, so `Z_0` is the
number of all-weight `t`-null supports. The first saturated column consists
of pair sums in `{0,2}`. Dividing those sums by two identifies it with the
`(n/2,t/2)` subset census. Hence

```text
C_1=Z_0(q,n/2,t/2).
```

The dyadic first-owner theorem says that a support in a cyclic `2`-group is
nonprimitive exactly when it is invariant under the antipodal shift. Those
are exactly the first saturated-column supports, so the primitive numerator
is `Z_0-C_1`.

The proved unreduced telescoping lemma gives the all-weight joint-to-marginal
ratio

```text
J_all = 2^(nm) Z_0/(Z_m product_(j=0)^(m-1) B_j).
```

Primitive deletion changes only the joint numerator. The unconditional
block marginals and the terminal marginal are properties of the base
`U`-measure and remain unchanged. Replacing `Z_0` by `Z_0-C_1` proves
`(PRIM-TEL)`. Dividing the primitive and unreduced formulas gives the
logarithmic correction whenever the primitive numerator is positive.

Finally, the C2'' numerator restricts to the central half-band. Every term
has nonnegative weight, so its primitive numerator is at most the all-weight
primitive numerator. Division by the same positive marginal product proves
that `(C2-INT)` is sufficient for C2''. No estimate of `(C2-INT)` is used in
this identity proof.
