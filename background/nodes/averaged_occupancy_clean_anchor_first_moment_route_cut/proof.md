# Proof

For supports of size `m=k+r`, `fm1` gives

```text
E[N_m] = binom(n,m)(1-q^-r)q^(1-r)
       < U_m := binom(n,m)q^(1-r).
```

Every subfamily has no larger expectation. Moreover

```text
U_(m+1)/U_m = (n-m)/((m+1)q) < n/q.
```

At all six named envelopes, `q>=q_0=B*2^128>2n`. Therefore, for every family
of supports of sizes at least `a`, writing `t=a-k`,

```text
E[N(A)] < sum_(m=a)^n U_m
        < 2 U_a
        = 2 binom(n,a) q^(1-t)
        <= 2 binom(n,a) q_0^(1-t).
```

It remains to prove the last quantity is below `B*`.

For the three RowC anchors this is the exact integer comparison

```text
2 binom(n,a) < B* q_0^(t-1),
```

with bit-length slack `40,309,23` at rates `1/4,1/8,1/16`.

For the prize anchors, use the standard bound

```text
binom(n,a) <= (e n/a)^a < (3n/a)^a.
```

The exact rational certificates

```text
(3n)^5 < 2^c a^5
```

hold with `c=18,23,28` at rates `1/4,1/8,1/16`. Since the printed prize
budget has 128 bits, `B*>=2^127`, and hence

```text
B* q_0^(t-1) = (B*)^t 2^(128(t-1)) >= 2^(255t-128).
```

The exact exponent comparisons

```text
5 + ca < 5(255t-128)
```

hold on all three rows, proving `2 binom(n,a)<B*q_0^(t-1)` without constructing
any prize-scale integer.

Thus `E[N(A)]<B*`. Finally, `C_t(A)>=0` because it is a second factorial
moment, so `nu(A)<=E[N(A)]<B*`. The strict occupancy premise cannot fire.
