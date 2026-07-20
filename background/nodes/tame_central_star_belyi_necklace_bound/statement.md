# Tame central-star Belyi necklace bound

- **status:** PROVED
- **consumer:** `f3_hge4_near_third_belyi_necklace_bound`

Let `k` be algebraically closed of characteristic zero or characteristic `p>m`.
Suppose a degree-`m` polynomial `A` has factorizations

```text
A=ZS^3,       A-1=y^cT,
m=3h+e,       c=h+e,
```

where `Z,S,T` are squarefree of degrees `e,h,2h`, respectively, `Z` and `S`
are coprime, and the displayed factors across `A` and `A-1` are coprime.
Assume `y=0` is the distinguished multiplicity-`c` point above `1`.

Put

```text
N(c,e)=(1/c) sum_(d|gcd(c,e)) phi(d) binom(c/d,e/d).       (CSN1)
```

Then, up to source scalings `y -> alpha y`, there are at most `N(c,e)` such
labelled polynomial covers. Equivalently, their tame branch-cycle classes
inject into the binary necklaces of length `c` and weight `e`.

This is an upper bound: not every necklace need be realizable over a given
field or satisfy any additional cyclotomic divisor condition.
