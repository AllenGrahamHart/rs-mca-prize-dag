# Proof

Let `F=F_(p^d)`. Pair feasibility implies `F=F_p(Q)` by
`e1_pair_feasible_ambient_generation`. By the canonical quotient definition,
`Q=D^(n/N)` is cyclic of order `N`, so it contains a primitive `N`-th root and
generates the same field as that root. Finite-field theory therefore gives

```text
d=ord_N(p).
```

The characteristic is odd because `N` divides `p^d-1` and `N>=256`. The
group `(Z/2^r Z)^x` is a two-group, so `d` is one of

```text
1,2,4,...,64       for N=256,
1,2,4,...,128      for N=512.
```

The RowC budget interval is

```text
I_C=[2^250, 2^250+2^128-1].
```

For `d=2`, its exact integer square-root interval consists of

```text
p in {2^125,2^125+1,2^125+2,2^125+3}.
```

The even candidates are not characteristics of the required row.
`2^125+1` is `1 mod N`, so has order one. `2^125+3` is `3 mod N`, whose
orders are `64` modulo `256` and `128` modulo `512`, not two. For every
allowable `d>=4`, the least integer with `p^d>=min(I_C)` already has
`p^d>max(I_C)`; the verifier prints the exact adjacent root endpoints.

For the prize budget interval

```text
I_P=[B_P 2^128,(B_P+1)2^128-1],
B_P=317494674775468773183020924238786383963,
```

the exact root interval is empty for every allowable `d>=2`, including
`d=128` at `N=512`.

Thus neither budget interval admits `d>1` with `d=ord_N(p)`. Hence `d=1`,
so `q=p`; containing a primitive `N`-th root then gives `p=1 mod N`.
