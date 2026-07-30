# Proof

Let

```text
G=(Z/256Z)^x=Gal(Q(zeta_256)/Q).
```

Work with shift/sign orbits of profile-`(0,18)` collision polynomials of
exact norm `514p`. Their principal ideals have the form

```text
P_t (1-zeta_256) Q_s,                              (1)
```

where `t` is a primitive 256-th root modulo `p` and `s` is one modulo 257.
Both rational primes split completely. Galois conjugation preserves the
coefficient profile, exact norm, and the shift/sign equivalence relation, and
acts diagonally on `(1)`:

```text
u:(P_t,Q_s) -> (P_(t^u),Q_(s^u)).                  (2)
```

The action of `G` on the 128 primitive roots modulo `p` is regular. Hence
every diagonal Galois orbit in the norm-`514p` collision set meets the fiber
`P_r` exactly once: existence follows from transitivity, and uniqueness from
the trivial stabilizer of `r`.

Inside the `P_r` fiber, send a collision orbit to its extra ideal `Q_s`.
This map is surjective onto occupied ideals by definition. It is injective
because two collisions with the same `P_r` and `Q_s` have the same principal
ideal; the proved common-ideal height theorem then makes their quotient
torsion, so they belong to the same shift/sign orbit.

Thus

```text
O_514(p,r)
 =#(collision orbits in the P_r fiber)
 =#(diagonal Galois orbits of exact norm 514p).     (3)
```

The right side of `(3)` does not involve `r`, proving root independence and
the stated equivalence. QED.
