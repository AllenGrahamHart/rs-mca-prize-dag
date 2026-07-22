# L1 decorated shift-pair gcd descent and sharpness

- **status:** PROVED
- **role:** normalize common cofactors and fence support-only compression past `e=w`
- **consumer:** `l1_mixed_petal_amplification`

## Canonical gcd descent

Take a decorated shift-pair record from
`l1_growing_cofactor_decorated_shift_pair_compiler`:

```text
AQ_1-BQ_2=R,       deg Q_i=e,
deg R<=d-w-1,       gcd(Q_1,BN)=gcd(Q_2,AN)=1.         (GD1)
```

Let `D` be the monic gcd of `Q_1,Q_2`, put `c=deg D`, and write

```text
Q_i=D q_i,       R=D r.                               (GD2)
```

Then

```text
gcd(q_1,q_2)=1,
Aq_1-Bq_2=r,
deg q_i=e-c,
deg r<=d-(w+c)-1,                                     (GD3)
gcd(D,ABN)=1.                                         (GD4)
```

Thus every common-cofactor record is a primitive decorated shift pair with
reduced cofactor degree and increased effective cancellation depth

```text
e'=e-c,       w'=w+c.                                 (GD5)
```

In particular, the primitive uniqueness theorem applies after descent
whenever

```text
e<=w+2c.                                              (GD6)
```

Otherwise the canonical residual satisfies `e'>w'`. Also `D|R` implies
`c<=d-w-1`. Every domain root of `D` lies in the common agreement core `G`;
roots outside `G` are off-domain common factors.

## Sharpness beyond `e=w`

The support-only primitive uniqueness cutoff cannot be extended past `e=w`.
Over `F_13`, put

```text
A=(Z-3)(Z-4)=Z^2+6Z+12,
B=(Z-9)(Z-12)=Z^2+5Z+4,
d=2,       w=1,       e=2.
```

For `t in F_13`, define

```text
Q_(1,t)=Z^2+(4t+2)Z+t,
Q_(2,t)=Z^2+(4t+3)Z+5t+5.                             (GD7)
```

Then

```text
A Q_(1,t)-B Q_(2,t)=5t+6,                             (GD8)
gcd(Q_(1,t),Q_(2,t))=1.                               (GD9)
```

For `t` outside `{0,4,12}`, take

```text
H={0,1,3,4,9,12},       G=Z-1,       N=Z,
U_t=G A Q_(1,t),
P_(1,t)=0,       P_(2,t)=G(5t+6).                    (GD10)
```

Both codewords have degree below `k=2`, `deg U_t=5<n=6`, and their exact
agreement sets are respectively `{1,3,4}` and `{1,9,12}`. Hence the same
ordered `(A,B)` supports ten primitive cross-coprime decorations at
`e=w+1`, realized by ten received words.

## Consequence

After gcd descent, the `e'<=w'` branch may forget the cofactor decoration
once the ordered support pair and received-word owner are fixed. The
`e'>w'` branch must retain the received-word/Toeplitz owner; no uniform
support-only one-decoration compiler exists there. This sharpness witness is
not a counterexample to L1 and does not show multiple decorations for one
fixed received word.
