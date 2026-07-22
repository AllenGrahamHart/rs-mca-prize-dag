# Proof

Let `psi` be the map supplied by the low-degree fiber reduction and put
`N=2^41`, `e=2^38-1`, and `G=mu_N`.

## Degree two

If `deg psi=2`, separability and odd characteristic give a unique
nonidentity deck involution `tau` over the base field. The dependency
supplies at least

```text
M_2=e-4-9*2^2=e-40                                  (1)
```

pairs in fibers of `psi`. Each is a two-cycle of `tau`, so the graph of
`tau` contains at least `2M_2` ordered points of `G x G`.

The Mobius-graph case split proved in the trigonal dependency has only two
subgroup-heavy forms:

```text
y=kx,       xy=k.                                    (2)
```

Every other graph has at most `32N^(2/3)` subgroup points by the published
bound. The exact official inequality

```text
32N^(2/3)<2M_2                                       (3)
```

therefore forces one of `(2)`. A graph point puts `k` in `G`. In the first
case the nonidentity involution condition gives `k^2=1` and `k!=1`, hence
`k=-1`. The second case is the involution `x |-> k/x`; write `k=c`.
This proves `(Q23-1)--(Q23-2)` and the tail count.

## Degree three

Assume now that `deg psi=3`. Any degree-three rational map can be
postcomposed by a Mobius map so that

```text
psi=S/R,       deg S=3,       S(0)!=0,       deg R<=2.   (4)
```

Indeed, in the two-dimensional span of a coprime numerator and denominator,
the kernel of the leading-coefficient functional supplies `R`; outside the
union of that line and the kernel of evaluation at zero, choose `S`.
The official field has more than two elements. Scale `S` to be monic.

Form the off-diagonal coincidence polynomial

```text
C(x,y)=[S(x)R(y)-S(y)R(x)]/(x-y).                   (5)
```

It has bidegree at most `(2,2)`. The dependency's coefficient/corner proof
uses only the normal form `(4)`: with

```text
S=x^3+s_2x^2+s_1x+s_0,       R=r_2x^2+r_1x+r_0,
```

its symmetric coefficient array is

```text
       y^0                    y^1                       y^2
x^0   s_1r_0-s_0r_1          s_2r_0-s_0r_2            r_0
x^1   s_2r_0-s_0r_2          r_0+s_2r_1-s_1r_2        r_1
x^2   r_0                    r_1                       r_2.       (6)
```

If `C` is absolutely irreducible, inversion of subgroup coordinates or one
of the two printed determinant-one torus changes from that dependency puts
it under the published estimate with worst bidegree `(2,3)`. Hence

```text
#C(G x G)<=1440N^(2/3).                              (7)
```

But the fiber reduction supplies

```text
M_3=e-4-9*3^2=e-85                                  (8)
```

pairs and therefore `2M_3` ordered points on `C`, while

```text
1440N^(2/3)<2M_3.                                   (9)
```

This is impossible.

If `C` is geometrically reducible, coprimality of `S,R` makes the
degree-three extension cyclic. The two components of `C` are the graphs of
an order-three Mobius deck map `tau` and `tau^2`. They cannot be exchanged
by Frobenius: base-field points on exchanged components lie in their
intersection, which has at most two points, whereas `(8)` supplies many
more. Each component is therefore base-field defined, and each captured
unordered pair contributes one orientation to each graph. Each graph has at
least `M_3` points of `G x G`.

A nonspecial Mobius graph has at most `32N^(2/3)<M_3` such points. The
special graph `xy=k` has order two. For `y=kx`, one graph point puts `k` in
the power-of-two group `G`, while order three gives `k^3=1`; hence `k=1`
and the graph is diagonal. No nonidentity order-three deck map remains.
This excludes the degree-three branch and proves the theorem. QED.
