# Proof

We first prove the quadratic staircase. Write `a=n-r`. For a received line,
choose one exact noncommon witness support `S_z` of size `a` for every bad
slope `z`. A fixed noncommon support cannot witness two distinct slopes, so
these supports are distinct.

## Large-overlap collapse

Suppose two selected supports satisfy

```text
|S_z intersect S_w|>=k+r.
```

The two explaining codewords interpolate a codeword pair `(c_0,c_1)` which
agrees with the received pair on their intersection. Let `C_0` be the full
common support and put `c=|C_0|>=k+r`. Every other witness support meets
`C_0` in at least

```text
a+c-n>=k
```

coordinates. The MDS information-set property therefore forces its explaining
codeword to be `c_0+z c_1`.

After subtracting `(c_0,c_1)`, every coordinate outside `C_0` is a nonzero
affine function of the slope and can cancel at most once. A noncommon witness
needs at least `max(1,a-c)` such cancellations. Hence

```text
#bad slopes <= floor((n-c)/max(1,a-c)) <= r+1.      (1)
```

The final inequality is immediate for `c>=a` and `c=a-1`; if
`x=a-c>=2`, its left side is at most `(r+x)/x<=r+1`.

## Mean-overlap forcing

Assume for contradiction that there are `N=r+2` bad slopes and that no pair
of their supports has the large overlap above. If `d_x` is the number of
selected supports containing coordinate `x`, then

```text
sum_x C(d_x,2) <= C(N,2)(k+r-1).                  (2)
```

On the other hand, Cauchy-Schwarz and the quadratic hypothesis give

```text
sum_x C(d_x,2)
 >= (N^2 a^2/n-Na)/2
 >= (N^2(k+r)-Na)/2.                              (3)
```

The last expression exceeds the right side of `(2)` by

```text
N(k+3r-n+1)/2.
```

When `3r>R=n-k` this is positive, a contradiction. It remains to supply the
deep branch `3r<=R`. Choose two bad slopes, explaining codewords, and error
sets `E_1,E_2` of size at most `r`. Solving the two affine equations produces
a codeword pair `(c_0,c_1)` such that the residual pair
`(e_0,e_1)=(u_0-c_0,u_1-c_1)` is supported on
`T=E_1 union E_2`, with `|T|<=2r`.

At any further bad slope, subtract `c_0+z c_1` from its explaining codeword.
The resulting codeword is supported on the union of `T` and one more
radius-`r` error set. Its weight is at most `3r<=R`, below the MDS minimum
distance `R+1`, so it is zero. Consequently every bad slope makes
`e_0+z e_1` have weight at most `r`. If `T'` is the support of the residual
pair and `|T'|>=r+1`, each bad slope must cancel at least `|T'|-r`
nonzero affine coordinate functions. Each coordinate function has at most
one finite root, whence

```text
#bad slopes * (|T'|-r) <= |T'|,
```

and therefore there are at most `r+1` bad slopes. If instead `|T'|<=r`,
the explaining codeword on a bad support must again equal `c_0+z c_1`, now
because their difference has weight at most `2r<=R`. Noncommonness forces
the support to contain a coordinate of `T'` at which
`e_0+z e_1=0`. That coordinate determines `z`, so there are at most
`|T'|<=r` bad slopes. This proves the upper bound in the deep branch as
well.

For the lower bound, use an MDS parity-check matrix. A syndrome lies in the
span of columns indexed by `E` exactly when its word is within an error
supported on `E` of the code. Choose `r+1` independent parity-check columns
`h_i` and distinct slopes `gamma_i`. Put

```text
s_1=sum_i h_i,             s_0=-sum_i gamma_i h_i.
```

At slope `gamma_i`, the syndrome `s_0+gamma_i s_1` lies in the span of all
chosen columns except `h_i`, while `s_1` does not. Lift `(s_0,s_1)` to a
received pair. The complement of those `r` columns is then an agreement
support, and the failure of `s_1` to lie in their span makes it noncommon.
This gives a witness at each of the `r+1` slopes. Hence
`B_C(n-r)=r+1`, proving `(QMS)`.

## The four rows

For every printed prime, the verifier checks a Proth certificate

```text
p=u 2^s+1,       u odd,       u<2^s,
a_0^((p-1)/2)=-1 mod p.
```

It follows that `p` is prime. The same exact replay checks `n | p-1`,
`p<2^256`, and the quotient and remainder in division by `2^128`, so the
printed `B` is exact and the order-`n` multiplicative subgroup exists.

Finally put

```text
F_(n,k)(r)=r^2-n(3r-(n-k)).
```

For all four rows the verifier checks

```text
F_(n,k)(B-1)>=0>F_(n,k)(B).
```

Thus `(QMS)` gives exactly `B` bad slopes at radius `B-1`, while the tangent
construction gives at least `B+1` at radius `B`. Monotonicity gives `(ADJ)`.
Because a closed real Hamming ball uses `floor(delta n)` errors, the safe set
is exactly `[0,B/n)`.

## Source audit

The argument above was reconstructed and checked consumer-backward from the
proof at upstream commit `9262f63c`; it does not import the status label of
that draft. The local proof uses neither the near-capacity profile envelope
nor any of its five open hard inputs.
