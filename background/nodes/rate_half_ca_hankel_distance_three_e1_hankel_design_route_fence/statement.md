# Rate-half distance-three `e=1` Hankel-design route fence

- **status:** PROVED
- **closure:** exact verification
- **consumer:** `rate_half_band_closure`
- **dependency:** `rate_half_ca_hankel_split_pencil_equivalence`

There is an exact smallest-order analogue over `F_17` in which the
distance-three normal form, split-design saturation, column-far condition,
affine Hankel kernel, exceptional transversality, and pinned adjugate all
hold simultaneously.

Take the rate-half domain and fixed core

```text
D=F_17^*,       H(X)=X-1,       D_res=D\{1},
e=1,       r=3.                                          (E1F1)
```

Put

```text
A(X)=(X-2)(X-5)=X^2+10X+10,
B(X)=(X-3)(X-13)(X-15)=X^3+3X^2+7X+10,
Q(z;X)=A(X)+z(B(X)-A(X)).                              (E1F2)
```

The contracted moment pencil `h(z)=h_0+z h_1` is

```text
h_0=(0,10,2,16,7,8,3),
h_1=(15,16,6,2,14,12,1).                              (E1F3)
```

Its `4 x 4` Hankel matrix has rank two at `z=0`, rank three at every
nonzero finite `z`, and kernel vector equal to the coefficient vector of
`Q(z;X)`. At the exceptional slope the kernel is the two-shift plane of
`A`, and the first-order pairings have shape

```text
u^T M_1u=0,       v^T M_1u=0,       v^T M_1v!=0.      (E1F4)
```

Moreover its adjugate has the exact pinned form

```text
adj M(z)=c_H z q(z)q(z)^T,       c_H!=0.              (E1F5)
```

Lifting by `H=X-1` gives the full eight-moment endpoint syndromes

```text
y_0=(0,0,10,12,11,1,9,12),
y_1=(0,15,14,3,5,2,14,15).                            (E1F6)
```

Their degree-four split-locator pencil is column-far. Its finite supported
slopes and residual root sets are exactly

```text
z=0:   {2,5}                       exceptional,
z=1:   {3,13,15}                   internal,
z=15:  {4,9,11},
z=2:   {6,7,10},
z=4:   {8,12,16}.                                   (E1F7)
```

There is no supported slope at infinity. The three external triples
partition the nine points outside the canonical support except for the
unique omitted row `14`, and their monic product is the complement-domain
polynomial, the `e=1` instance of the exact power identity.

The quotient support distance of `h_1` modulo the two `A`-root columns is
three, but there are four supporting triples: the internal triple and all
three external triples. This is precisely where the fixture lies below the
official theorem's `r>=4` uniqueness threshold. It is not a prize
counterexample and does not satisfy or test the complete corrected
reciprocal square. It proves that an exclusion using only the split census,
pair-Lagrange form, incidence power, Hankel ranks, transversality, or
adjugate pin cannot be valid without an additional official-scale input.
