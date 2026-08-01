# Proof

For template A write

```text
x=ef,       y=de,       z=-df.
```

The three product pairs in `(KBTEC-2A)` immediately give the first two
equalities in `(KBTEC-3A)`.  Their two remaining products give

```text
F(-v)F(-w)=(cf)(be)=bc(ef)=bc F(xi),
```

which proves the third.  Since all representatives are nonzero,

```text
d^2=-yz/x,       e^2=-xy/z.
```

Therefore the target squared sum at `u` is

```text
(d+e)^2=2y-yz/x-xy/z=-y(z-x)^2/(xz).
```

The source Vieta row says that the same squared sum is `H(u)`.  Multiplying
by `xz` and substituting `x=F(xi)`, `y=F(u)`, `z=F(-u)` gives
`(KBTEC-4A)`.

For template B put

```text
x=ef,       y=de,       z=cf.
```

The three oriented product pairs give the first two identities in
`(KBTEC-3B)`, while

```text
F(-u)F(-w)=(cf)(be)=bc F(xi).
```

Now `f=z/c`, `e=cx/z`, and `d=yz/(cx)`.  Hence

```text
(d+e)^2=(y z^2+c^2 x^2)^2/(c^2 x^2 z^2).
```

Equating this to `H(u)` and clearing the nonzero denominator gives
`(KBTEC-4B)`.  Substitution of `F=A_0/A_2` and
`H=W B_1^2/A_2^2` makes both cuts polynomial after multiplication by the
supported denominator product. QED.
