# L1 Mersenne next-to-maximal Belyi shifted-value gate

- **status:** PROVED
- **dependency:** `l1_mersenne_next_to_maximal_exceptional_reduction`
- **consumer:** `l1_mixed_petal_amplification`

Use the exactly saturated Belyi residue, and write

```text
r_0=R(0),       z=the other quadratic quotient root,
a=[Y^(h-2)]G,   n=m(p+1),       h=m-1.                (BSG1)
```

For every root `beta_i` of the squarefree split-value polynomial `G`, put

```text
x_i=(beta_i-r_0)/(z-r_0),
P(W)=(z-r_0)^(-h)G(r_0+(z-r_0)W).
```

Then every `x_i` lies in `mu_n`, and therefore

```text
P(W) divides W^n-1.                                   (BSG2)
```

Put `Delta=z-r_0` and `K=2a lambda/Delta^(h+1)`. For every nonzero split
value, its normalized root `x_i` satisfies

```text
x_i(x_i-1)P'(x_i)=K.                                 (BSG2a)
```

Hence, when `ord_0(T)=0`,

```text
W(W-1)P'(W)-K=(hW+b)P(W)                             (BSG2b)
```

for one scalar `b`. When `ord_0(T)=1`, the same left side is divisible by
`P(W)/(W+1/(c-1))`; the removed root is the normalized split value zero.

In fact `z!=0`: the `z=0` chamber would make zero both a complete simple
split value and a second quadratic-quotient root, giving incompatible local
orders one and two in the Euler identity. Define the two projective invariants

```text
c=z/r_0,       theta=2a/(r_0 z).                      (BSG3)
```

No survivor can have both `c` and `theta` in the prime field `F_p`.
More precisely, under that hypothesis the rational logarithmic-derivative
identity forces

```text
theta=h,       c=m,                                   (BSG4)
ord_0(R-r_0)=1,
ord_x(R-r_0)=((m-1)p-1)/m
```

at every nonzero root `x` of `R-r_0`. The remaining degree `p-1` lies
strictly between one and two copies of the displayed multiplicity, a
contradiction.

For the `ord_0(T)=0` chamber, `theta=h` holds before this argument, so merely
`c in F_p` is impossible. Thus every remaining endpoint passport satisfies

```text
z!=0,       {c,theta} is not contained in F_p.          (BSG5)
```

This is a strict exclusion and divisibility gate, not a closure of the
quadratic-field-normalized residue or of lower `h`.
