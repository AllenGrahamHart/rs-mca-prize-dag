# Proof

Put `R=Z[zeta_256]`, `pi=1-zeta_256`, and let
`P_r=(p,zeta_256-r)`. The ten singleton coefficients of `alpha` survive
modulo two. If their exponents form a multiset `E`, then the local expansion
at `zeta_256=1+pi` gives

```text
mu=v_pi(alpha)=v_2(Norm(alpha))
  =ord_(X=1)(sum_(e in E) X^e mod 2).                 (1)
```

Reduce the exponents modulo `16`. Since `X^16=1 mod (X+1)^16`, equal
residues cancel in pairs. The residual parity support has even size at most
ten. If it is empty, `(1)` has order at least `16`. Otherwise the exact
Hasse-derivative test over every even subset of `{0,...,15}` of size at most
ten gives

```text
mu in {1,2,3,4,5,6,7,8,9,10}                        (2)
```

whenever `mu<=10`; every value in `(2)` occurs in the finite local census.

The prize field floor and `S=18` give

```text
m<=floor(18^64/(B_P 2^128))=2013.                   (3)
```

In a conductor-`256` cyclotomic norm, the exponent of every odd prime `q`
is divisible by `ord_256(q)`. Therefore the odd part of any nonzero norm is
`1 mod 256`. Since the row prime also satisfies `p=1 mod 256`,

```text
m=2^mu(1+256t).                                      (4)
```

Intersecting `(2)--(4)` gives fourteen candidates before the same
residue-degree sieve. The only rejected value is

```text
1026=2*3^3*19,
```

because both `3` and `19` have order `64` modulo `256`, while their
exponents are not multiples of `64`. The thirteen values in the statement
remain.

Now factor the collision ideal. Because `Norm(P_r)=p` and `p` occurs to the
first power,

```text
(alpha)=P_r (pi)^mu                                  (5)
```

for a pure cofactor. The three non-pure cofactors are

```text
514=2*257,       1028=4*257,       1538=2*769.       (6)
```

The numbers `257` and `769` are prime and congruent to one modulo `256`, so
each splits into `phi(256)=128` distinct degree-one primes

```text
Q_s=(q,zeta_256-s),
```

indexed by the primitive `256`-th roots `s mod q`. In the corresponding
split branch,

```text
(alpha)=P_r (pi)^mu Q_s.                             (7)
```

Thus two collisions with the same `m` and `Q_s` have equal principal ideals
and differ by a unit.

The entropy-height proofs depend only on square mass `18`, the common ideal,
and the cofactor. They do not use the subdivision `18=4a+b`. For `m=2`, the
cofactor-`2` Smyth comparison makes every such unit ratio torsion. For every
other cofactor, `m>=4`, so the high-cofactor Schinzel comparison does the
same. Hence each fixed ideal family in `(5)` or `(7)` contains at most one
256-vector shift/sign orbit.

There are ten pure families and `3*128` split families, proving

```text
T_210(p,r)<=394.                                     (8)
```

Finally the weighted dictionary gives

```text
E_210<=128 M_33(2,10)*394
     =61906644187645781406222007093836433195008.      (9)
```

QED.

