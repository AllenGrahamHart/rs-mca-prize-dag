# E1 N=512 trinomial interval-norm exclusion

- **status:** PROVED
- **closure:** proof plus dual exact resultant certificate

At `N=512,s=2`, the folded profile `(a,b,c)=(1,2,0)` can be normalized,
without changing its cyclotomic norm divisibility, to

```text
F(zeta)=2+epsilon zeta^a+delta zeta^b,
1<=a<b<=255,       epsilon,delta in {+1,-1}.
```

There are exactly

```text
4 binom(255,2)=129540
```

normalized signed states. Quotienting by all odd Galois conjugations gives
748 exact orbits. For one representative of each orbit, compute

```text
R(F)=|Res_X(X^256+1,F(X))|=|Norm(F(zeta))|.
```

The 748 representatives give 746 distinct nonzero norms. For each norm `R`
and each of the two exact pair-feasible prime intervals `[L,U]`, any prime
divisor `p` in that interval would have complementary cofactor

```text
ceil(R/U) <= R/p <= floor(R/L).
```

Across all 746 norms and both intervals, those integer windows contain only
four integers and each window has width at most one. Only one of the four
integers divides its norm. The resulting quotient is composite and is
`0 mod 512`, so it is not a pair-feasible row prime. There are no candidate
primes.

Hence profile `(1,2,0)` cannot collide at any named pair-feasible anchor.
Together with `e1_n512_four_singleton_collision_exclusion`, every
`N=512,s=2` profile is impossible, and every surviving `N=512` E1 collision
has raw swap distance `s>=3`.

This theorem does not control `s>=3` or pay the total collision-pair ledger.
