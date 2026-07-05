# proof: m720_overceiling_complete_window_certificates

Consider either over-ceiling cell. Here `n=32`, `h=16`, and the anchored MITM
complete window has `W=n`.

Let `P` be the anchored half, so `0 in P`, and let `Q` be the other half. Both
have size 16 and are disjoint subsets of the 32 roots. Since `|P|+|Q|=32`,
disjointness forces

```text
Q = mu_32 \ P.
```

Let

```text
A(X) = prod_{x in P} (X-x)
B(X) = prod_{x in Q} (X-x).
```

Then

```text
A(X) B(X) = X^32 - 1.
```

The h=16 trade condition requires the lower elementary signatures
`e_1,...,e_15` of `P` and `Q` to agree. Equivalently, the monic degree-16
polynomials `A` and `B` have the same top 15 subleading coefficients:

```text
A = X^16 + a_1 X^15 + ... + a_15 X + c,
B = X^16 + a_1 X^15 + ... + a_15 X + d.
```

Compare coefficients in `AB = X^32 - 1`. Since the characteristic is odd,
the coefficient of `X^31` gives `2a_1=0`, hence `a_1=0`. Descending
inductively, the coefficient of `X^(32-r)` gives `2a_r` plus terms already
known to be zero, so `a_r=0` for every `1 <= r <= 15`.

Therefore

```text
A = X^16 + c,
B = X^16 + d.
```

The product identity gives `c+d=0` and `cd=-1`, hence `c^2=1` and
`d=-c`. Thus the two factors are exactly

```text
X^16 - 1
X^16 + 1.
```

Their root sets are the even and odd exponent cosets of `mu_32`. Since the
anchored half contains exponent `0`, it is the even coset; the other half is
the odd coset. Both halves are full `mu_16` cosets, so the pair is toral and
paid. The top coefficient differs (`c=-d`), so this toral pair is indeed the
single anchored trade, but it is not unpaid non-toral.

Hence both over-ceiling complete-window cells have zero unpaid non-toral
anchored active cores.
