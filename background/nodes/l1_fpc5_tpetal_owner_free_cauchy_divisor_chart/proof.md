# Proof: owner-free weighted Cauchy divisor chart

The Chinese remainder theorem gives the unique `chi` in `(CC2)`. If a pair
obeys `(CC4)`, then `B` and `chi G` have the same residue modulo every
pairwise coprime `L_i`, hence modulo `Lambda`. Since `deg B<h`, this forces

```text
B=rem_Lambda(chi G)=B_G.
```

Conversely `(CC3)` has the required residues, so it gives a pair in the
slice exactly when its degree is at most `d`. This proves `(CC3)--(CC4)`.

Because `Lambda` is squarefree and split, Lagrange interpolation gives

```text
B_G(X)/Lambda(X)
 =sum_(z in T) c(z)G(z)/(Lambda'(z)(X-z)).            (1)
```

Expand both sides at infinity. The right side is

```text
sum_(j>=0) M_j(G) X^(-j-1).                           (2)
```

The left side is `O(X^(d-h))` exactly when `deg B_G<=d`. This is equivalent
to the vanishing of the coefficients of
`X^(-1),...,X^(-(h-d-1))`, namely `(CC6)`. The number of equations is
`h-d-1`.

Now let `x` be a root of the squarefree split `G` and write

```text
G(X)=(X-x)G_x(X).
```

Evaluating `(1)` at `X=x` gives

```text
B_G(x)/Lambda(x)
 =sum_(z in T) c(z)(z-x)G_x(z)/((x-z)Lambda'(z))
 =-M_0(G_x).
```

The core and petals are disjoint, so `Lambda(x)` is nonzero. This proves
`(CC8)`, and squarefreeness makes coprimality equivalent to the `d`
nonvanishing tests in `(CC9)`.

For `y` in the disjoint background, direct evaluation of `(1)` gives
`(CC10)--(CC11)` because `Lambda(y)` is nonzero.

Finally, `G A=L_Core`. Every petal root is outside the core, so `A(z)` is
nonzero and

```text
G(z)=L_Core(z)/A(z).
```

Substitution in `(CC6)` proves `(CC12)`. The affine-dimension assertion is
exactly the monic-chart conclusion of the saturated-slice dimension
theorem applied to the equivalent pair slice `(CC4)`. QED.
