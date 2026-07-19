# Proof

The leading-coefficient functional on the two-dimensional pencil is nonzero.
Its kernel is therefore one-dimensional; choose a nonzero generator `V`.
Choose a monic `U` in the pencil. Since every `G_i` is monic, it has a unique
expression `(APD1)`. Distinctness of the `G_i` makes the `c_i` distinct.

Put `cbar=(sum_i c_i)/4`, replace `U` by `U+cbar V`, and replace `c_i` by
`c_i-cbar`. This is valid because four is invertible under either
characteristic hypothesis. It preserves every `G_i` and gives
`sum_i c_i=0`. Hence

```text
product_i(U+c_iV)=U^4+e_2 U^2V^2+e_3 UV^3+e_4V^4.     (1)
```

Let `D(Y)=product_i(Y-a_i^2)`. The descended product identity `(APD0)` is

```text
D(Y) product_i G_i(Y)=Y^d-1.                           (2)
```

Set `h=r-v>=1` and reverse the three polynomials at infinity:

```text
B(z)=z^r U(z^-1),
C(z)=z^v V(z^-1),
E(z)=z^4 D(z^-1).                                      (3)
```

The polynomials `B,E` have constant term one. Substituting `(1)` into `(2)`,
then replacing `Y` by `z^-1` and multiplying by `z^d`, gives

```text
E(B^4+e_2 z^(2h)B^2C^2+e_3 z^(3h)BC^3+e_4 z^(4h)C^4)
 =1-z^d.                                               (4)
```

Therefore

```text
H(z):=E(z)B(z)^4-1
```

is divisible by `z^(2h)`, and `H'` is divisible by `z^(2h-1)`. Direct
differentiation gives

```text
H'=B^3 K,       K=E'B+4EB'.                            (5)
```

Since `B(0)=1`, equation `(5)` implies `z^(2h-1)|K`. But

```text
deg K<=r+3.                                             (6)
```

If `2h-1>r+3`, then `(5),(6)` force `K=0` and hence `H'=0`. Also
`deg H<=d`. In characteristic zero, or in positive characteristic greater
than `d`, a polynomial of that degree with zero derivative is constant. As
`H(0)=0`, this would give `EB^4=1`. This is impossible because `D(0)!=0`,
so the reverse polynomial `E` has degree exactly four.

Consequently `2h-1<=r+3`. Substituting `h=r-v` gives

```text
2v>=r-4,
```

which is `(APD2)`.

If `e_2=0`, equation `(4)` instead shows that `H` is divisible by `z^(3h)`:
the first remaining correction is the `e_3` term, while `3h<d`. Repeating
`(5),(6)` gives

```text
3h-1<=r+3,
```

and hence `3v>=2r-4`. This proves `(APD2')`; it remains valid when `e_3=0`,
although the separate pure-quartic Wronskian theorem is much stronger there.

It remains to verify the characteristic hypothesis on the official row. The
maximal-field collapse gives either `q=p` with `p>=3*2^128`, or `q=p^2`
with `p^2>=3*2^128`, which forces `p>2^64`. In both cases `p>d=2^39`.
Finally,

```text
ceil((2^37-1-4)/2)=2^36-2,
ceil((2(2^37-1)-4)/3)=(2^38-4)/3,
```

proving `(APD3)` and `(APD3')`. QED.
