# General t-petal joint anchor owner

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Use the explicit anchor Pade chart with squarefree split anchor locator `F`.
Let `Bkg` be the source background, disjoint from the core and petals, and
let

```text
R_0={y in Bkg: W(y)=0},       P_0=F L_(R_0).          (JO1)
```

For a coordinate `H`, write `(G_H,B_H)` for its reconstructed pair and

```text
R_H={y in Bkg: B_H(y)=0}.
```

Then

```text
gcd(H,L_(R_0))=gcd(B_H,L_(R_0)),                     (JO2)
gcd(H,P_0)=gcd(G_H,F) gcd(B_H,L_(R_0)).              (JO3)
```

All gcds are monic. Equivalently, the roots of the single owner in `(JO3)`
are exactly

```text
(Z(G_H) intersect Z(F)) disjoint_union (R_H intersect R_0). (JO4)
```

Thus one gcd of the low-degree determinant coordinate simultaneously
recovers the common defect owner and the common background-agreement owner.
In particular, every distinct exact candidate satisfies

```text
|Z(G_H) intersect Z(F)|+|R_H intersect R_0|<=e-1.    (JO5)
```

For every monic divisor `Q|P_0` of degree `q<=e-1`, the coordinates whose
joint owner contains `Q` are exactly

```text
H=QK,       deg K<=e-1-q,                             (JO6)
```

a linear coordinate space of dimension `e-q`. The exact-owner stratum
`gcd(H,P_0)=Q` is obtained by the additional filter
`gcd(K,P_0/Q)=1`.

The remaining background equations are also explicit. Write

```text
T_H=(Remainder_H W+Lambda H)/F,
Remainder_H=rem_F(-Lambda H W^(-1)).                  (JO7)
```

Then `T_H` depends linearly on `H`, `B_H=W+T_H`, and for every
`y in Bkg\R_0`,

```text
B_H(y)=0 iff T_H(y)=-W(y),                            (JO8)
```

one affine linear equation on the coordinate body.

## Scope

The theorem types all anchor-relative defect and background owners and all
remaining background-root equations. It does not bound the split points in
any owner stratum, sum owner strata, provide a first-owner chronology, or
pay a source cell.
