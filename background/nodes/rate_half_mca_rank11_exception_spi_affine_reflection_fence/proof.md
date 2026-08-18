# Proof

Every ordered pair `(x,y) in H^2` contributes once to `R_(x+y)`, so

```text
sum_(c in F_p) R_c=N^2.                              (1)
```

Since `N` is even, `-1 in H`; hence `R_0=N`. Therefore

```text
sum_(c!=0) R_c=N^2-N.
```

The exact average over the `p-1` nonzero constants is

```text
(N^2-N)/(p-1)
 =(2^21-1)/(127*8)
 =2064+127/1016.                                    (2)
```

Some nonzero `c` consequently has `R_c>=2065`.

The set counted by `R_c` is invariant under the involution
`tau_c(x)=c-x`. It has at most one fixed point, namely `c/2`. If that point
is present, at least `(2065-1)/2=1032` two-element orbits remain. If it is
absent, the invariant set has even size and hence at least `2066/2=1033`
two-element orbits. Thus `1032` is a uniform lower bound.

For each two-element orbit, direct multiplication proves `(AR1)`. If two
orbits give the same `gamma`, their elements have the same sum `c` and
product `gamma`; they are the same unordered root pair of the same monic
quadratic. Distinct orbit locators are therefore coprime and have distinct
slopes. They are squarefree because the fixed orbit was removed. Also
`gcd(X^2-cX,1)=1` and every locator is monic.

Finally `tau_c` cannot stabilize all of `H` when `c!=0`. Otherwise the finite
set `H` would be invariant under the nonzero translation obtained by
composing `x -> -x` (which stabilizes `H`) with `tau_c`. A nonzero
translation in characteristic `p` has orbits of size `p`, whereas
`0<N<p`. This is impossible. Hence the construction is a partial affine
reflection on the domain, not a global multiplicative quotient. QED.
