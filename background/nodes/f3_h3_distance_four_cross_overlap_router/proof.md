# Proof

Write the three signed monomial atoms of a generic pair `E={i,j}` as

```text
+zeta^(i+j),       -zeta^i,       -zeta^j.
```

Folding by `zeta^(n/2)=-1` gives the three distinct signed half-basis atoms of
`v_E`. For a selected non-diagonal pair not containing `-1`, the only way its
vector norm can drop below three is cancellation of the two negative atoms,
which occurs exactly when the roots are antipodal. Such a vector has squared
norm one. Two antipodal pairs in the same shifted-product fiber satisfy
`1-x^2=1-u^2`, so their unordered pairs agree; distinctness rules this out.
If `E={x,-x}` and `F={u,v}` is the other pair, equality of shifted products is

```text
1-x^2=(1-u)(1-v),
```

which rearranges to `(D4A)`. This proves the first-lane description and its
two-variable parameterization.

Now assume both vectors have squared norm three. From `(D4R1)`,

```text
<v_E,v_F>=(3+3-4)/2=1.                              (1)
```

The inner product of two signed three-atom vectors is the number of common
atoms with the same sign minus the number with opposite signs. Equation `(1)`
therefore forces at least one common signed atom.

A same-kind common atom is impossible in a common finite-field product fiber.
If two negative atoms agree, the two representations share one root. Their
equal nonzero shifted products then force the other root to agree as well. If
the two positive atoms agree, the ordinary root products satisfy `xy=uv`.
Equality of shifted products then gives `x+y=u+v`, so the two unordered root
pairs are the roots of the same quadratic and again agree. Both conclusions
contradict distinctness.

Hence at least one common atom is cross-kind. In actual monomials this says
that a positive product monomial equals a negative root monomial. Relabel to

```text
uv=-y.                                              (2)
```

The common shifted-product equation is

```text
(1-x)(1-y)=(1-u)(1-v).
```

Substitute `v=-y/u`, multiply by `u`, and cancel common terms. The result is

```text
u x (1-y)=u^2-y,
```

which is `(D4R2)`. Since `u!=0` and `y!=1`, division gives `(D4R3)`. QED.

## Global edge count

Every generic edge has at least one canonical cross-overlap certificate. Given
`(u,y) in H^2`, equations `(D4R2)` and `uv=-y` determine

```text
x=(u^2-y)/(u(1-y)),       v=-y/u.
```

If these values define a valid selected edge, they determine that edge;
otherwise the parameter pair contributes nothing. Thus the number of generic
edges is at most `n^2`.

For an antipodal edge, the non-antipodal unordered pair `{u,v}` determines
`x^2=u+v-uv`, and therefore determines the unordered pair `{x,-x}` whenever it
exists. There are at most `n(n+1)/2` unordered pairs in `H`. The two lanes are
disjoint, so adding their bounds proves `(D4R4)`.

The refined packing theorem gives at least six distance-four-or-six edges in
any selected seven-vector graph of a rich target. If the full eligible fiber
has no distance-six edge, all six are counted by `N_4`. Product fibers
partition the edge ledger, so division of `(D4R4)` by six proves `(D4R5)`.
QED.
