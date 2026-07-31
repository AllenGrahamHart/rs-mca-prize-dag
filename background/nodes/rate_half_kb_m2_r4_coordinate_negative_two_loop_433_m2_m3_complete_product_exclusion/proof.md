# Proof

The parent classifier presents every geometric common-`K` candidate by the
two equations in `(KB43V-1)`, with `c` linear and the forced product `p`
protected.  Since the quadratic in `b` is monic after dividing by four,
`R_epsilon` is free of rank twelve over the deployed prime field.

Let `X,Y,Z,U,V` be as in `(KB43V-2)`.  The two multiplicative identities in
that display follow directly from `D=X/b`, `E=Y/c`, and `U=DF`.  Solving in
turn for the member forced to equal `p` gives all five residual lists in
`(KB43V-3)`.  Every denominator is nonzero under the parent product and
leading-support guards.

An actual paired-product lift partitions the residual sextic into three
orbits of the nonsingular parent involution, so one of the fifteen matchings
must satisfy three copies of `(KB43V-4)`.  For a fixed universal residual
form, clear denominators, eliminate its `x` or `q` variable between one pair
equation and each of the other two, then eliminate `a`.  A solution forces
the resulting obstruction to vanish.  The first projection is nonzero in
60 templates; the second is nonzero in the other 15.

It remains to test these 75 necessary conditions on the exact base ledger.
In `R_epsilon`, write an element as `u+vb`.  From `(KB43V-1)`,

```text
b^2=s_epsilon b-1,       s_epsilon=-epsilon A/4.
```

Its quadratic norm down to `F_p[M]/(P_6)` is

```text
Norm(u+vb)=u^2+s_epsilon uv+v^2.                  (1)
```

The element is a unit exactly when the gcd of `(1)` with `P_6` is one.
Custom six-coefficient arithmetic reduces every operation modulo `P_6` and
the quadratic relation without constructing a generic four-variable ideal.
The primary verifier obtains gcd one in all 300 cases.

For an independent replay, share the second pair equation in every
resultant chain, including the 60 cases where the primary shared the first.
Instead of `(1)`, form the multiplication map of each obstruction on the
twelve-element basis

```text
1,M,...,M^5,b,bM,...,bM^5.
```

Every matrix has rank twelve over the deployed field.  The audit is split
by forced type and matching range only to keep each deterministic process
below the local 60-second budget.  Thus no matching exists in any cell, and
the 20-cell frontier is empty. QED.
