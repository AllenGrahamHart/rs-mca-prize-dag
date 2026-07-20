# Proof

Write a quotient representation as

```text
t=(1-w)/(1-z),       z,w in H\{1}.                  (1)
```

Since `t notin {0,1}`, the three elements `1,z,w` are distinct. Exchanging
`z,w` in `(1)` replaces `t` by `1/t`. The bijection

```text
(z,w) -> (w/z,1/z)                                 (2)
```

preserves `H^2`, avoids the identity in both coordinates, and replaces the
ratio by

```text
(1-1/z)/(1-w/z)=(z-1)/(z-w)=1/(1-t).               (3)
```

Its inverse is `(z',w')->(1/w',z'/w')`. Hence `R` is invariant under the
two transformations `t->1/t` and `t->1/(1-t)`. These generate exactly the
six values in `(AAT1)`, proving that `R` is constant on the orbit. Equivalently,
this permutes the ordered triple `(1,z,w)` and renormalizes its first entry
to one.

Now suppose `t=1-a^2`, with `a in H\{1,-1}`. Then

```text
tau(t)=t/(t-1)=1-a^(-2).                            (4)
```

An ordered product representation of `t` is

```text
(1-X)(1-Y)=1-a^2,       X,Y in H\{1}.              (5)
```

Equation `(5)` gives `a^2-Y=X(1-Y)`. Therefore

```text
(1-X^(-1))(1-Y/a^2)
 =(X-1)(a^2-Y)/(Xa^2)
 =-(1-X)(1-Y)/a^2
 =1-a^(-2).                                         (6)
```

Both transformed roots lie in `H`. The first is not one because `X!=1`.
If `Y/a^2=1`, equation `(5)` would give `X=0`, impossible in `H`; hence the
second is also not one. Applying the same map with `a` replaced by `a^(-1)`
recovers `(X,Y)`. Thus

```text
(X,Y)->(X^(-1),Y/a^2)                               (7)
```

is a bijection between the ordered product fibers at `t` and `tau(t)`, so
their `P` values agree. Their `R` values agree by `(AAT1)`, proving `(AAT2)`.

Finally, `tau(t)=t` is equivalent to `t(t-2)=0`. Since retained targets are
nonzero, only `t=2` can be fixed. The bijection `(7)` is endpoint-dependent
and need not preserve signed-support intersections between two different
representations, so no edge-count conclusion follows.

For the parity assertion, diagonal product representations have `X=Y` and

```text
(1-X)^2=1-a^2,
```

or equivalently

```text
X^2-2X+a^2=0.                                      (8)
```

The two roots of `(8)` are distinct because its discriminant is
`4(1-a^2)=4t!=0`, and their product is `a^2`. If one root belongs to `H`,
the other is `a^2/X` and also belongs to `H`. Neither is one because `t` is
nonzero. Thus the number of diagonal representations is zero or two. Every
off-diagonal ordered representation is paired with its coordinate exchange,
so `P(t)` is even. The antipodal Cayley-product identity gives `P(t)=2+M_a`,
hence `M_a` is even as well. This proves `(AAT3)`. QED.
