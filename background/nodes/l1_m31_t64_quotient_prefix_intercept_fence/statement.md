# M31 `T_64` quotient-prefix intercept fence

- **status:** PROVED
- **closure:** algebraic construction plus exact finite-field replay
- **consumer:** `l1_mixed_petal_amplification` (evidence and route fence)
- **upstream:** `przchojecki/rs-mca` PR `#1048`, exact head
  `6487b234334e4c6d601732b2b587cde2c7bc342d`

Work over `F_p`, `p=2^31-1`, in the pinned `c=2048`, `(u,v)=(0,1)`
quotient profile for upstream's auxiliary Mersenne-31 list row at `2^-100`.
This is not a `2^-128` Prize row. Its complete quotient-label set `Q` has
size `1024`; remove
the two active labels indexed by `1` and `3` and write

```text
Q'=Q\{q_1,q_3},       |Q'|=1022.                    (T64-1)
```

There are seven explicit `479`-subsets

```text
A,B_1,...,B_6 subset Q'                              (T64-2)
```

with one common `415`-point core. Each `B_i` is obtained from `A` by
replacing one complete `T_64` fiber by another, so

```text
|A\B_i|=|B_i\A|=64.                                 (T64-3)
```

The seven monic locators have the same first `63` nonleading coefficients,
and in particular the same depth-`32` target. Hence the rooted deficiency-64
degree at `A` satisfies

```text
d_64(A)>=6.                                         (T64-4)
```

For

```text
H_64=binom(479,64)binom(543,64)
```

exact integer arithmetic gives `4H_64<p^32`. Therefore every pointwise
coefficient-four shell inequality

```text
p^32 (d_64(A)-b)_+ <= 4H_64                         (T64-5)
```

is false for `b=3,4,5`. Intercept `b=6` is only the first value not refuted
by these six listed neighbors; no `(6+4)` theorem is asserted.

This is a support-level counterexample on one pinned quotient profile. It
constructs no received word, codeword, ray, slope, first-match survivor, or
row-global `U_Q` payment, and proves no adjacent-row or proximity-prize
bound.
