# Proof

Suppose `q=-1`. Substitution in the three Möbius-ratio equations gives the
three alternatives

```text
r^2-r+1=0,       r=-1,       r^2-4r+1=0.              (1)
```

The middle alternative contradicts `r^4!=1`. In the first alternative,

```text
(r+1)(r^2-r+1)=r^3+1=0.                               (2)
```

The official characteristic is greater than three, so `r!=-1`; hence `(2)`
makes `r` have order six. But `(MRR2)` says the order of `r` divides
`2^40`. This is impossible.

It remains to exclude the third alternative. It gives

```text
r+r^(-1)=4.                                           (3)
```

Define the trace recurrence in `F_p` by

```text
c_0=4,       c_(j+1)=c_j^2-2.                         (4)
```

Induction from `(3)` gives

```text
c_j=r^(2^j)+r^(-2^j).                                 (5)
```

The order of `r` is a power `2^s`. Since `r^4!=1` and its order divides
`2^40`, one has `3<=s<=40`. Then `r^(2^(s-2))` is a primitive fourth root,
so `(5)` gives

```text
c_(s-2)=0       for some 1<=s-2<=38.                  (6)
```

The field-degree dependency and `(HDE1)` write every possible characteristic
uniquely as

```text
p=1+k*2^40,
29058991<=k<33554432.                                 (7)
```

The pre-registered Modal computation evaluated `(4)` through `c_38` for every
one of the `4,495,441` integers in `(7)`. It found no zero for any modulus,
before imposing primality. All 32 shards completed, their ranges are disjoint
and contiguous, and their hashes replay under the independent checker

```text
tools/ramguard tiny -- python3
  experiments/prize_resolution/
    rate_half_list_deleted_pair_harmonic_characteristic_check.py
```

Thus `(6)` is impossible for every official `p`. All three alternatives in
`(1)` are excluded, proving `(HDE2)`. QED.
