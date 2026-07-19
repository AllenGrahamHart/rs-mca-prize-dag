# Proof

Write `S_i` for the active support in block `A_i`, and put

```text
U=union_i S_i,       R=|U|,
I_0=sum_i |S_i|,
P_0=sum_(i<j)|S_i intersect S_j|.
```

There are

```text
E=tm-I_0
```

additional block incidences beyond the active supports. Let `q` be the
number of coordinates outside `U` used by at least one of these incidences,
so `v_J=R+q`.

Adding one block incidence at a coordinate already in `U` creates at least
one new block pair. At a new coordinate used by `r` blocks, the `r`
incidences save `r-1` coordinates relative to private placement and create
`C(r,2)>=r-1` block pairs. Therefore the total number of new block-pair
incidences is at least `E-q`. Pair cap four gives

```text
P_0+(E-q) <= 4 C(t,2).
```

Hence

```text
v_J=R+q >= R+E-(4C(t,2)-P_0).                         (1)
```

For the five support-atlas profiles, the data in `(1)` are

```text
profile   t  R  I_0  P_0  4C(t,2)   lower bound for v_J
   1      4  6   20   24      24          4m-14
   2      4  7   21   21      24          4m-17
   3      4  8   24   24      24          4m-16
   4      5  6   25   40      40          5m-19
   5      6  6   30   60      60          6m-24.
```

Substituting `c=m-4` into `2v_J-8-ct` gives, by profile,

```text
4m-20,       4m-26,       4m-24,       5m-26,       6m-32.
```

Evaluation at `m=7,8,9,10` is exactly the table in the statement. Its
minimum is two.

These union bounds are sharp as set-system bounds. In profiles 1, 3, 4,
and 5 the support intersections already consume the full pair cap, so every
additional incidence is private and equality in `(1)` follows. In profile
2, the row with one support zero has support intersection four with each
other row, while the other three row pairs have intersection three. Put one
new coordinate on each of those three pairs and place all remaining
incidences privately. This spends exactly the three units of pair slack and
again gives equality in `(1)`.

If `J=G`, the Maxwell identity would give

```text
Delta_J=2|union G|-8-c|G|=-e<=0,
```

contradicting `(MP2)`. Thus every rank-two relation omits at least one
Maxwell block. Rank one is already excluded by the preceding localization,
so a full-block-support relation has rank at least three. This proves all
claims.
