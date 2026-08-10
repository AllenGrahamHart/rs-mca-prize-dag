# Proof: general t-petal joint anchor owner

Let `y in R_0`. The core, background, and petals are disjoint, so

```text
F(y)!=0,       Lambda(y)!=0.
```

Since `W(y)=0`, evaluating the determinant identity

```text
F B_H-G_H W=Lambda H
```

at `y` gives

```text
F(y)B_H(y)=Lambda(y)H(y).
```

Therefore `B_H(y)=0` if and only if `H(y)=0`. The background locator is
squarefree, so this root-by-root equivalence proves `(JO2)`.

The anchor-coordinate theorem already gives

```text
gcd(H,F)=gcd(G_H,F).
```

The core and background are disjoint, hence `gcd(F,L_(R_0))=1`. Taking the
product of the two gcd identities proves `(JO3)` and `(JO4)`. Since a
distinct candidate has `H!=0` and `deg H<=e-1`, `(JO5)` follows.

Now fix a squarefree divisor `Q|P_0`. Its owner is divisible by `Q` exactly
when `Q|H`. Polynomial division gives `H=QK`, and the coordinate degree
bound is exactly `deg K<=e-1-q`. This space has dimension `e-q`. Since
`P_0` is squarefree, equality `gcd(H,P_0)=Q` is equivalent to
`gcd(K,P_0/Q)=1`, proving `(JO6)`.

Finally, the explicit inverse gives

```text
B_H=(G_HW+Lambda H)/F
   =W+(Remainder_H W+Lambda H)/F
   =W+T_H.
```

The remainder map and exact division are linear in `H`, so `T_H` is linear.
For `y` outside the complete anchor zero set `R_0`, evaluating the last
identity proves `(JO8)`. QED.
