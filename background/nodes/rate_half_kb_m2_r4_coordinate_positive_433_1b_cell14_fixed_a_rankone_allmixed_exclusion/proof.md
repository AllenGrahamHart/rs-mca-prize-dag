# Proof

Use target products

```text
a=de,  u=df,  v=ef,  f=f,             a f^2 = u v.       (1)
```

The parent cell-14 theorem supplies a quadratic common curve

```text
F(r,b)=F_2(r)b^2+F_1(r)b+F_0(r)=0
```

and a normalized common kernel. The missing record is one of `de,de,-de`, so
its equation fixes `a` as a linear element of `F_p(r)[b]/(F)`. The preceding
rank-one boundary theorem excludes the chart where this division fails.
Target guards give `a,u,v,f != 0`; put `u=z` and `v=a f^2/z`.

Build the three residual-pair Vieta determinants and the missing squared-sum
equation first as ordinary polynomials in `(u,v,f)`. Apply the torus map
termwise:

```text
u^i v^j f^k  ->  a^j z^(i-j) f^(k+2j).                  (2)
```

After reduction modulo `F`, each equation is `C_i(z,f,r)+bL_i(z,f,r)`.
Choose a nonzero cutter `C+bL`; every solution annihilates the equation-pair
crosses and the common-curve norm

```text
C_i L-L_i C,                         (3)
F_2 C^2-F_1 C L+F_0 L^2.             (4)
```

For matchings `6,7,8`, all four normalized projected components are mixed in
`z,f`. The compiler forms all six pair resultants in each elimination
direction, ranks the six complete double-resultant routes by an exact degree
bound, and selects the first nonzero outer eliminant `H(r)`. Exact FLINT
arithmetic gives a nonzero eliminant in every one of the 144 cases.

The exact field-root calculation

```text
gcd(H(r), r^2130706433-r)
```

has 2,992 case-root incidences. Established route and inverse guards account
for 1,808. At 224 of the remaining roots, the specialized resultant cuts have
no target-field outer root.

At the other 960 roots, all pair resultants vanish because the four projected
components share a weighted-homogeneous factor `G(z,f)`. This is a projection
base component, so the compiler checks both pieces of the exact decomposition

```text
V(G Q_1,...,G Q_4) = V(G) union V(Q_1,...,Q_4).          (5)
```

On `V(G)`, target nonvanishing permits `w=z/f^2`. Dehomogenizing `G` at `f=1`
has no field root in 192 cases. The other 768 roots give 960 field-valued
`w` branches. On each branch, substitute `z=w f^2` into the original cleared
equation pairs, form every common-`b` cross and curve norm as a polynomial in
`f`, and take their gcd. None of the 960 branch gcds has a field root. Thus
the factor branch is empty before any pairwise-distinctness guard is needed.

For the residual branch, divide `G` exactly from every projected component
and recompute all pair resultants. Their common outer cut has no field root in
all 960 cases. Hence every live parameter root is excluded. No live
coefficient-clearing boundary, direct target fiber, guarded witness, or target
boundary remains.

Every eliminant is compressed and hash-pinned in the ledger. An independently
written 24-shard FLINT replay reparses all 144 eliminants, checks 230,008,092
decompressed bytes, and reproduces all 2,992 root sets. The aggregate census
checks the full Cartesian ledger and every root disposition. Therefore all
144 guarded systems are empty. QED.
