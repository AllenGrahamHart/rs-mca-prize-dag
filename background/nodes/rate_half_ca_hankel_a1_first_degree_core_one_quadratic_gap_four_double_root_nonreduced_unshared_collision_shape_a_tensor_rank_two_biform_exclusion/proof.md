# Proof

Assume `(TRE2)`. First remove the greatest common divisor of `A_0,A_1`.
If that divisor has degree `d>0`, each row gets at most `m-d` roots from the
primitive pencil. Since every row has `m` distinct roots in `Gamma`, all
`d` roots of the common divisor must also lie in `Gamma`. At each such
parameter the complete fiber `G(delta,X)` vanishes identically, contrary to
hypothesis 2. Hence the parameter pair is coprime.

For a domain row `x`, the coefficient pair

```text
b(x)=[B_0(x):B_1(x)] in P^1                         (1)
```

is defined: simultaneous vanishing would make the row zero. Its row roots
are the roots in `Gamma` of the corresponding pencil member

```text
B_0(x)A_0(t)+B_1(x)A_1(t).                         (2)
```

Two distinct projective coefficient types have disjoint root sets. Indeed,
if their two pencil members vanished at the same `delta`, invertibility of
the two coefficient rows would give

```text
A_0(delta)=A_1(delta)=0,
```

contradicting coprimality. Every type owns exactly `m` roots in `Gamma`, so
if `s` types occur then

```text
s m<=|Gamma|=3e.                                   (3)
```

For `e>=9`, `4m=4e-8>3e`; hence

```text
s<=3.                                              (4)
```

It remains to bound the number of rows of one type. Remove any common
factor of `B_0,B_1`; it is nonzero at every retained domain row and does not
change the projective type. For a fixed `[u:v]`, the condition

```text
[B_0(x):B_1(x)]=[u:v]
```

is one nonzero polynomial equation

```text
vB_0(X)-uB_1(X)=0                                  (5)
```

of degree at most `n`, unless the projective ratio is globally constant.
In the latter case `(TRE2)` has tensor rank one. Then every row has the same
`m` roots in `Gamma`, and every one of those parameter fibers is identically
zero, again contradicting hypothesis 2. Thus `(5)` is nonzero for every
type and each type occurs on at most `n` domain rows.

Combining this with `(4)` gives

```text
R<=s n<=3n,                                        (6)
```

whereas `(TRE1)` says `R=3n+7`. This contradiction proves that `(TRE2)` is
impossible. QED.
