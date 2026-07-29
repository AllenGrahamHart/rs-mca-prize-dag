# Conditional proof

Put

```text
L = Q(zeta_256),
K = Q(zeta_128),
zeta_128 = zeta_256^2.
```

Then `[L:K]=2`. The rational prime 257 is `1 mod 256`, so it splits
completely in both fields. For a primitive 256-th root `s mod 257`, write

```text
Q_s = (257,zeta_256-s) in O_L.
```

Its restriction to `O_K`, and equivalently its relative ideal norm, is

```text
q_(s^2) = (257,zeta_128-s^2) in O_K.              (1)
```

Each degree-one prime of `K` above 257 has exactly two extensions to `L`:
`Q_s` and `Q_(-s)`. This is also immediate from the two square roots of a
nonzero residue modulo 257.

Now fix the row prime ideal `P_r`. If `Q_s` is occupied, the proved
Galois/norm dictionary gives

```text
(alpha_s) = P_r (1-zeta_256) Q_s.                 (2)
```

Both `(alpha_s)` and `(1-zeta_256)` are principal. Hence every occupied
prime has the same class in `Cl(L)`:

```text
[Q_s] = [P_r]^-1.                                 (3)
```

The relative ideal norm induces a homomorphism `Cl(L)->Cl(K)`. Therefore two
occupied primes `Q_s,Q_t` have

```text
[q_(s^2)] = [N_(L/K)(Q_s)]
           = [N_(L/K)(Q_t)] = [q_(t^2)].          (4)
```

Under `e1_qzeta128_p257_class_orbit_certificate`, distinct primes above 257
in `K` have distinct classes. Equation (4) thus forces
`q_(s^2)=q_(t^2)`, so `s^2=t^2 mod 257` and `t=+/-s`. By (1), only the two
extensions above one `K`-prime can be occupied. Thus the occupancy is at most
two. QED conditional on the named certificate.

The proof never uses the coefficient profile, autocorrelation energy, or the
ten-profile ledger. Those filters become unnecessary once the certificate is
proved.
