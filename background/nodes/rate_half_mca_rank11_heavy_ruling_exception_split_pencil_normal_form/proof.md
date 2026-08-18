# Proof

Fix the anchor pair `p_0=(a_0',b_0')` in the shortened triple-owner packet.
Its residual core `H_0` has size at least `m'-11`. Pair noncontainment gives
`|H_0|<m'`, so

```text
1<=e=m'-|H_0|<=11.                                   (1)
```

Every anchor support was chosen core-saturated and has exact size `m'`.
Therefore it is `H_0 disjoint_union E_gamma` with `|E_gamma|=e`. Two
distinct agreement supports from the same pair intersect exactly in `H_0`,
so their exception sets are disjoint. Their monic locators factor as

```text
Lambda_gamma'=L_0 L_(E_gamma).                       (2)
```

Each exception locator is squarefree, split on the residual evaluation
domain, and divides its squarefree domain locator.

Write the nontrivial rational certificate as

```text
Qh_gamma'+s_gamma Lambda_gamma'=A'+gamma B',
s_gamma=c_0+c_1 gamma.                               (3)
```

On `H_0`, the anchor explanation is `a_0'+gamma b_0'` and the locator
vanishes. Apply (3) at two anchor slopes. Subtraction shows that both

```text
U=A'-Q a_0',       V=B'-Q b_0'
```

vanish on `H_0`. Their degrees are at most `m'`: the products with `Q`
have degree below `67472+K'=m'`, and `A',B'` have degree at most `m'`.
Since `L_0` is squarefree, there are unique polynomials `u,v` such that

```text
U=L_0u,       V=L_0v,       deg u,deg v<=m'-|H_0|=e. (4)
```

Substitute (2)--(4) into (3), use
`h_gamma'=a_0'+gamma b_0'`, and cancel the nonzero polynomial `L_0`:

```text
u+gamma v=s_gamma L_(E_gamma).                       (5)
```

The scalar cannot vanish at an anchor slope `gamma_0`. If it did, (5)
would give `u=-gamma_0v`. For every other anchor slope, its monic exception
locator would then be proportional to the same polynomial `v`. Two such
locators would coincide, contradicting their disjoint nonempty root sets.
There are at least 20 anchor slopes, so two alternatives are available.

Equation (5) now has degree exactly `e` at every anchor slope. Hence
`max(deg u,deg v)=e`. If a nonconstant polynomial divided both `u` and `v`,
it would divide two distinct exception locators in (5). Those locators are
pairwise coprime, so `gcd(u,v)=1`.

Finally, `Q` has no residual domain root on `H_0`. Such a point belongs to
all anchor supports, hence to at least two selected supports. The pole-simple
parent proves that a denominator root can belong to at most one selected
support; equivalently it would force the forbidden common pole
`Q=A'=B'=0`. Thus `gcd(Q,L_0)=1`.

All assertions in `(SPI11)` follow. QED.
