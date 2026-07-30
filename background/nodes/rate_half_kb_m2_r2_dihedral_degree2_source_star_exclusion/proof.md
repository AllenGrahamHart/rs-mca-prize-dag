# Proof

Fix one generic order-five pole `p` of `G`. For the degree-two reflection
quotients, write

```text
q_u^(-1)(p)={y_0,y_1},       q_v^(-1)(p)={z_0,z_1}.
```

All four values are unramified in their quotient maps. The group generated
by the two distinct reflection involutions is `D_2=V4`. On a generic regular
V4 orbit, quotienting by the two reflection subgroups gives two two-element
partitions with trivial subgroup intersection. The map from the four orbit
points to the product of the two quotient sets is therefore bijective.
Equivalently, the incidence of the two `Y` and two `Z` values on `C` is

```text
K_(2,2).                                            (KBM2D-2)
```

Fix `z` in `{z_0,z_1}` and an endpoint source label
`w in h^(-1)(z)`. The endpoint map `h` is unramified over every source pole.
Above each of the two points of `C` over `Z=z`, full endpoint V4 stability
puts both points of `h^(-1)(y_i)` over the fixed value `W=w` on `Gamma`.
Thus the normalized `W=w` fiber of `Gamma` consists of four distinct points,
two over each `y_i`.

The normalization of the actual source component is isomorphic to the
normalization of `Gamma`, with `W=psi(X)`. Hence the complete source divisor

```text
D_w=psi^*[w]
```

is reduced of degree two here: ramification would ramify the normalized map
to `W`, contrary to the four distinct points above. Write its points as
`x,bx`. The preserving source lift is `(T,X)->(tau(T),b(X))`, so the two
roots over `bx` are the `tau` images of the two roots over `x`. In particular,
the two source-parameter fibers have the same number of roots over each
`y_i`. Their combined fiber has exactly two roots over each `y_i`, so each
one has one. Every star arising from `D_w` is therefore one of the four cross
edges

```text
h^(-1)(y_0) times h^(-1)(y_1).                     (KBM2D-3)
```

There are two endpoint labels `w` above each `z`, and every `D_w` has degree
two. Hence each `z` contributes four star units. By `(KBM2D-2)`, both
`z_0,z_1` use the same four possible vertices in `(KBM2D-3)`, so one pole of
`G` already contributes eight units on at most four vertices.

Let their weights be `w_1,...,w_4`, adding zero-weight vertices if needed.
Then `sum_i w_i=8`, and Cauchy--Schwarz gives

```text
sum_i binom(w_i,2)
 = (sum_i w_i^2-8)/2
 >= ((8^2/4)-8)/2
 = 4.                                               (KBM2D-4)
```

The proved complete-source quartic defect budget is at most three. This
contradicts `(KBM2D-4)`, so `n=2` is empty. The preceding degree-five child
then leaves exactly `(KBM2D-1)`. QED.
