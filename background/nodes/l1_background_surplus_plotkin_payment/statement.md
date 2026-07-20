# L1 background-surplus Plotkin payment

- **status:** PROVED
- **role:** exploit every agreement above the minimum background threshold
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart, exact petal support, defect degree,
and exact background agreement count

```text
q_bg=u+z,       u=ell-(h-d),       z>=0.                (PS1)
```

Put

```text
V=N+b,       E_z=V-4(ell+z).                            (PS2)
```

The combined defect/background sets of distinct contributors have Hamming
distance at least

```text
2(ell+z).                                               (PS3)
```

If `E_z<=E_0` for a fixed nonnegative cap `E_0`, the exact stratum has at
most

```text
2^(E_0+1)n                                              (PS4)
```

contributors. This includes every `E_z<0` stratum.

For fixed petal-polarity cap `p<=P`, summing all exact background-count
strata satisfying `E_z<=E_0` is polynomial per source chart, with bound

```text
2^(E_0+1)(P+1)n^(1/c_0+P+3).                           (PS5)
```

More generally, for every fixed nonnegative constant `C`, the full class

```text
E_z<=C log_2 n                                           (PS5L)
```

is polynomial per chart, with bound

```text
2(P+1)n^(1/c_0+P+C+3).                                  (PS5B)
```

Consequently a bounded-polarity per-chart counterfamily must satisfy

```text
E_z/log_2 n -> infinity.                                (PS6)
```

Writing `E_P=N+b-4ell`, this is

```text
(E_P-4z)/log_2 n -> infinity.                           (PS7)
```

For an official rate-`1/r` source,

```text
(r-1)E_z
 =(M-3(r-1)+1)ell-r(g+1)-4(r-1)z.                      (PS8)
```

## Scope

This is a per-source-chart exact-count payment. It does not bound unbounded
effective excess, growing petal polarity, or non-intrinsic first-match chart
multiplicity.
