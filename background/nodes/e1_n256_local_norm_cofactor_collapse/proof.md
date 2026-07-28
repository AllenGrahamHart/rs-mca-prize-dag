# Proof

Complete `K=Q(zeta)` at its unique prime above two. Local reciprocity
identifies

```text
Q_2^* / Norm_(Q_2(zeta)/Q_2)(Q_2(zeta)^*)
    with Gal(Q_2(zeta)/Q_2).
```

For the cyclotomic tower over `Q_2`, the reciprocity map sends a
2-adic unit `a` to the inverse cyclotomic automorphism
`zeta -> zeta^(a^-1)`. Projecting to the level of conductor 256
therefore gives

```text
Norm_(Q_2(zeta)/Q_2)(O_K^*)=1+256 Z_2.                (3)
```

This is the standard explicit cyclotomic case of local reciprocity. A source
pin is recorded in `audit.md`.

Let `pi=1-zeta`. Its norm is `2`. If
`mu=v_pi(alpha)=v_2(R)`, write `alpha=pi^mu u` with
`u` a local unit. Taking norms and using (3) yields

```text
R/2^mu = Norm(u) = 1 mod 256,
```

where the global norm is positive because its conjugates pair into complex
absolute-value squares. This proves (1).

On the pair-feasible branch, the prime-field reduction proves
`p=1 mod 256`. If `R=p m`, then
`v_2(m)=v_2(R)=mu` because `p` is odd. Divide by
`2^mu` in the equality `R=p m` and reduce modulo 256:

```text
1 = R/2^mu = p (m/2^mu) = m/2^mu mod 256.
```

This proves (2).

For profile `(3,4,0)`, the 2-adic cofactor theorem gives
`1<=mu<=5` and `m<64`. The positive odd integer
`m/2^mu` is less than 32 and congruent to one modulo 256, so it is
one. Hence `m=2^mu`.

For profile `(4,2,0)`, the two-singleton formula gives
`mu in {1,2,4,8,16}`, while `m<2^17`. Equation (2) writes

```text
m=2^mu(1+256t),       t>=0.
```

The strict bound gives respectively

```text
mu=1:  0<=t<=255,       mu=2: 0<=t<=127,
mu=4:  0<=t<=31,        mu=8: 0<=t<=1,
mu=16: t=0.
```

The number of candidate cofactors is `256+128+32+2+1=419`.

For a prize-envelope row, `p>=B_P 2^128` and the L2 norm bound gives
`R<=18^64` in profile `(4,2,0)`. Hence

```text
m=R/p <= floor(18^64/(B_P 2^128))=2013.              (4)
```

Intersecting (4) with `m=2^mu(1+256t)` gives

```text
mu=1: 0<=t<=3,        mu=2: 0<=t<=1,
mu=4: t=0,            mu=8: t=0,
mu=16: no value.
```

Substitution gives exactly the eight values in `statement.md`.
