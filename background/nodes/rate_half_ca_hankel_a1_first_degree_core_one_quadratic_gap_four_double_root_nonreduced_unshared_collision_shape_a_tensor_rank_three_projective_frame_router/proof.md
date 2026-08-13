# Proof

Choose a minimal representation

```text
G(t,X)=A_0(t)B_0(X)+A_1(t)B_1(X)+A_2(t)B_2(X),    (1)
```

where both triples are linearly independent and `deg B_j<=n`. Exact row
nonvanishing defines

```text
b(x)=[B_0(x):B_1(x):B_2(x)] in P^2                (2)
```

at every one of the `R` domain rows.

The preimage of a projective line `ell=0` is cut out by the polynomial

```text
ell(B_0(X),B_1(X),B_2(X)),                          (3)
```

of degree at most `n`. It is not the zero polynomial, since that would be a
linear dependence among the `B_j` and lower the tensor rank. Therefore any
projective line contains the images of at most `n` domain rows.

Select two distinct images and then a third outside their line; such choices
exist by the same line bound. The three pair-lines determined by these
noncollinear points contain at most `3n` domain rows in total. Since
`R=3n+7`, at least seven rows lie outside their union. Choose one as `x_4`.
The four coefficient vectors are in general position, so every three are
linearly independent.

Put `P_i(t)=G(t,x_i)`. The four polynomials lie in the three-dimensional
span of the `A_j`, while every three are independent. They therefore have a
unique projective circuit

```text
c_1P_1+c_2P_2+c_3P_3+c_4P_4=0,                    (4)
```

with every `c_i` nonzero.

Suppose a slope `delta` roots three of the `P_i`. Equation `(4)` then makes
it a root of the fourth. Three of the corresponding coefficient vectors
are independent, so their three equations

```text
b(x_i) dot (A_0(delta),A_1(delta),A_2(delta))=0
```

force every `A_j(delta)=0`. Equation `(1)` would make
`G(delta,X)` the zero polynomial, contradicting the all-excess nonzero-fiber
condition. Thus no slope belongs to three or four row root sets.

Let `u` be the size of their root-set union and let `d_2` be the number of
slopes occurring twice. Since every occurrence multiplicity is one or two,

```text
4m=u+d_2.                                           (5)
```

The union lies in `Gamma`, so `u<=3e`. Substituting `m=e-2` gives

```text
d_2=4m-u>=4(e-2)-3e=e-8.                           (6)
```

No triple overlap occurs, so each repeated slope contributes to exactly one
of the six pair intersections. Hence their sum is `d_2`, proving `(TRF2)`.
Pigeonhole proves `(TRF3)`, and exact substitution gives `(TRF4)`. QED.
