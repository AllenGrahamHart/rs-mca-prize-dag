# Proof

Because `DW=1-y^m` and `D(0)=1`, the coefficients of `W` below degree `m`
are the corresponding coefficients of `D^(-1)`. Since `c<2h`,

```text
D^(-1)=S^(-2) mod y^c.                            (1)
```

The Belyi normal form gives `S=F mod y^c`, where `F=Z^(-1/3)`. Therefore

```text
S^(-2)=F^(-2)=Z^(2/3)=ZF=ZS mod y^c.              (2)
```

Both `W` and `ZS` have degree at most `c`. Equations `(1)--(2)` show that
their difference has no coefficient below degree `c`, so there is a unique
`lambda in K` with

```text
W=ZS+lambda y^c.                                  (3)
```

Now reduce `DW=1-y^m` modulo `S`. Since `2h+c=m`, equation `(3)` gives

```text
D=-a^2y^(2h) mod S,       W=lambda y^c mod S,
1-y^m=-a^2lambda y^m mod S.
```

Consequently

```text
1-(1-a^2lambda)y^m=0 mod S.                       (4)
```

The Belyi theorem proves that `S` has degree `h>0`, is squarefree, and has
nonzero constant term. At any root `r` of `S`, equation `(4)` reads

```text
(1-a^2lambda)r^m=1.
```

Thus `kappa=1-a^2lambda` is nonzero and `(4)` is exactly `(KMP2)`. The two
outside members in `(KMP3)` multiply to `D`, so each divides `1-y^m` as
well.

It remains to prove the finite-field assertion. Suppose `K=F_q` and put
`theta=kappa^(-1)`. Since `mu_m` is contained in `K`, Frobenius fixes every
`m`-th root of unity. For one root `alpha` of `y^m-theta`, define

```text
eta=alpha^(q-1).
```

Then `eta^m=theta^(q-1)=1`, so `eta in mu_m`. Every root has the form
`zeta alpha` with `zeta in mu_m`, and Frobenius acts by

```text
(zeta alpha)^q=zeta eta alpha.
```

All Frobenius orbits therefore have the same length
`d=ord(eta)`. Equivalently, every irreducible factor of `y^m-theta` has
degree `d`, and `d|m`. Since the `K`-polynomial `S` is a product of these
factors, `d|deg S=h`. For dyadic `m`, this gives
`d|gcd(m,h)=2^v_2(h)`. If `h` is odd, then `d=1`, which means all roots of
`S` lie in `K`.

Primitivity removes the apparent even-width extension branch as well. The
root set of `S` is defined over `K`, so it is stable under Frobenius. On the
roots of `y^m-theta`, Frobenius is multiplication by `eta`; hence the root
set of `S` is stable under multiplication by `eta`. Since `S(0)=1`, equality
of normalized root sets gives

```text
S(eta y)=S(y).                                      (5)
```

We already know `d=ord(eta)` divides `h`, so `eta^h=1`. Equations `(5)` and
the definitions of the outside pencil members imply

```text
U(eta y)=S(eta y)-a eta^h y^h=U(y),
V(eta y)=S(eta y)+a eta^h y^h=V(y).                (6)
```

If `d>1`, multiplication by `eta^(-1)` is therefore a nontrivial common
scaling stabilizer of both root supports. The primitive shift-pair orbit
router proves that such a pair is a common quotient pullback, contradicting
primitivity. Thus `d=1`. Frobenius fixes every root of `y^m-theta`, so `S`
splits over `K`; the outside members already split over `K` as divisors of
`1-y^m`. QED.
