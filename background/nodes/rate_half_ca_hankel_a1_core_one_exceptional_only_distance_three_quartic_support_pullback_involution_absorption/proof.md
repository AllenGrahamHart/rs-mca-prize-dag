# Proof

The deck router gives `(QPIR1)`: for `F(X^4)` use the order-two element of
the cyclic deck group. In every case `tau` preserves `mu_N`, has no fixed
subgroup point in the antipodal case, and has at most two in the
constant-product case.

Let

```text
L={l:P_l=c_lD_l^2}.
```

The internal-slice argument in the tail-rigidity dependency gives `|L|<=2`.
In the ordinary branch every ratio

```text
f_lm=P_lD_m^2/(P_mD_l^2)                            (1)
```

lies in the quartic common field and is therefore `tau`-invariant.

Let `G` be the at least `e-148` pair indices captured by the quartic map,
and fix any `m in G`. Consider a captured pair `D_l` which is not a
nonfixed `tau`-orbit. Pay separately the at most two indices in `L`, the at
most two pairs containing a fixed point, and `l=m`.

For every remaining such `l`, choose a root `x` of `D_l` with
`ord_x(P_l)<=1`. Pair-crossing nonvanishing gives `P_m(x)!=0`, so `(1)` has
a pole at `x`. Its `tau`-invariant divisor has a pole at `tau(x)`. This point
is not the other root of `D_l`. If it is a root of `D_m`, charge it to one
of the two roots of `D_m`; otherwise the only possible denominator zero in
`(1)` is `P_m(tau(x))=0`, which gives one of at most four charges. Distinct
pair supports give distinct charges because `tau` is injective. Hence the
number of captured non-orbits is at most

```text
2+0+1+2+4=9       (antipodal),
2+2+1+2+4=11      (constant product).               (2)
```

The official inequality `e-148>11` provides a captured pair `D_m` which is
an exact nonfixed `tau`-orbit. Fix this new `m`. For any pair `D_l` outside
`L`, containing no fixed point, and not a `tau`-orbit, repeat the pole
argument. Now `tau(x)` cannot be a root of `D_m`: invariance of that pair
would put `x` in the same disjoint support. Thus every such tail charges a
distinct root of the quartic `P_m`. Adding `|L|<=2` and the fixed-point
payment proves `(QPIR2)`.

In the antiweight-derived quartic branch, every `r_l=P_l/D_l^2` with
`l notin L` belongs to the common field and is itself `tau`-invariant. A
nonfixed off-involution root would create a pole with no denominator pole at
its mate. Therefore every tail outside `L` contains a fixed point, giving
the stronger `2` and `4` bounds.

All downstream bounded-tail theorems use only the exact involution-orbit
matching, pair-Lagrange formulas, and tail count; they do not require the
comparison field itself to have degree two. The quartic branch therefore
enters their existing interface. QED.
