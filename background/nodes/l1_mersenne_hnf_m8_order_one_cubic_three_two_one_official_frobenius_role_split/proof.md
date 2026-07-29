# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one official Frobenius-role split

The official row supplier lists four Mersenne characteristics

```text
p in {8191,131071,524287,2147483647}.
```

Each is `7 mod 8`. The quadratic-character formula therefore gives
`(2/p)=1`, so choose `s in F_p` with `s^2=2`. If `zeta` is a primitive
eighth root, replacing `s` by its negative only exchanges the two factors
below; one may take `s=zeta+zeta^-1`.

The first three packets in (GRW1) are already quadratic. Substituting
`X=1+T` gives (FRS1) after homogenizing by `S^2`.

For the nine quartics, multiply each conjugate pair in (FRS2), using only
`s^2=2`. The products are

```text
T^4+1,
T^4+2T^2+4T+2,
T^4+6T^2+1,
T^4+4T^3+12T^2+16T+8,
T^4+4T^3+8T^2+4T+1,
T^4+4T^3+6T^2+4T+2,
2(2T^4+4T^3+6T^2+4T+1),
2(2T^4+4T^3+2T^2+1),
2(8T^4+16T^3+12T^2+4T+1).                         (1)
```

Direct substitution `X=1+T` in `P_4,...,P_12` identifies (1) with
(FRS3). The three rational quadratics and the eighteen signed quadratics
therefore have total degree

```text
3*2+18*2=42.                                        (2)
```

By the Galois-role weld they exhaust the degree-42 ordered role polynomial.
Homogenization is reversible on `S!=0`, and the scalar two in the last three
products is invertible because every official characteristic is odd. This
proves the exact disjunction (FRS4).

It remains to show that these are Frobenius packets rather than quadratics
which split further. Write a normalized role as

```text
lambda=(gamma-1)/(beta-1),
beta,gamma in mu_8 minus {1},       beta!=gamma.     (3)
```

Since `p=-1 mod 8`, Frobenius inverts every eighth root. Thus

```text
lambda^p=(gamma^-1-1)/(beta^-1-1)
        =(beta/gamma)lambda.                         (4)
```

The role is nonzero. If it belonged to `F_p`, (4) would force
`beta=gamma`, contradicting (3). Every role therefore has Frobenius orbit
of size two. The 21 degree-two factors in (2) are consequently irreducible
and are exactly those orbits. QED.
