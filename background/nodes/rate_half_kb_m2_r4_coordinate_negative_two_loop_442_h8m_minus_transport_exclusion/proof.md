# Proof

Write `s=l^3-l+1`.  Both negative-sign eighth-root rows have

```text
l^4+1=0,       b^2-bs+1=0.                        (1)
```

If `b'=1/b`, dividing `(1)` by `b^2` proves the same equation for `b'`.
On `H8-L`, `c=(b-2)s`; hence

```text
-c/b=(2/b-1)s=(2b'-1)s,
```

which is the `H8-M` locator.  Swapping `A,B` also swaps `AC,BC`, giving the
label identity `(KB44M-2)`.

Before renormalization, swapping `A,B` sends the common product vector to

```text
(-b^2,-1,b,-bc,c).
```

Dividing by `b^2` gives `(KB44M-3)` with `(KB44M-1)`.  This is one global
postcomposition scaling, so it preserves Mobius interpolation and the
product involution.

For the `H8-M` forced-product formula `(KB44O-4)`, direct reduction gives

```text
N-b^2 H=0                                         (2)
```

modulo `(1)`.  Its denominator is protected by the outside compiler, so
`p_xi=b^2`.  At `b'=1/b`, this equals `1/b^2`, exactly the scaled image of
the `H8-L` forced value.

Finally substitute `(KB44M-1)` and `(KB44M-4)` into the seven outside
products.  Each equals its old value divided by `b^2`; the internal sign
`sigma` is unchanged.  Hence the map preserves each of the three forced-
type orbits and all residual matching equations.  Applying the map twice
returns `(b,c,D,E,F)`, so no packet is lost at a chart boundary.

An `H8-M,tau=-1` completion would therefore give an
`H8-L,tau=-1` completion, contradicting the parent complete-product
exclusion.  The row and cell counts follow by removing its six cells and
their post-template cap `78`. QED.
