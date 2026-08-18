# Rank-eleven chronology-safe subspace-cover payment

- **status:** PROVED
- **row:** KoalaBear MCA, post-near affine error rank eleven
- **scope:** the first-match nontransverse row-space partition at
  `tau=1679`, `h=38384`

Let the represented nontransverse row spaces be partitioned into classes
`C_alpha`. Suppose each class has a correction subspace
`V_alpha <= C'` of dimension `d_alpha<=9` such that

```text
U_e <= V_alpha for every represented row space U_e in C_alpha.    (SC1)
```

Put

```text
M_d = floor(C(n-K+d,d)/C(A-K+d,d)),
R_d = (n-A) M_d,
L   = B_* - E_transverse = 65167969673715470.
```

Then the complete nontransverse slope contribution is at most

```text
sum_alpha R_(d_alpha).                                      (SC2)
```

Consequently the rank-eleven row is paid whenever that sum is at most `L`.
Every unsafe survivor therefore satisfies the strict weighted cover bound

```text
sum_alpha R_(d_alpha) > 65167969673715470.                 (SC3)
```

For a cover using only `d`-dimensional subspaces, the first possible unsafe
cover sizes are

```text
d                 1          2         3        4      5     6    7   8  9
classes   4420641497  262093370  16384884  1027929  64502  4048  254  16  2
```

In particular, any cover by two five-dimensional blocks is paid. More
generally, a `2 x 5` factor presentation whose represented row spaces use at
most `64501` distinct slices `gB` is paid; an unsafe such presentation needs
at least `64502` projectively distinct used factor slices.

## Nonclaim

This theorem does not produce a subspace cover, synchronize locators, or
bound the number of factor slices. It gives the exact chronology-safe price
of a cover once one is proved from the actual unsafe-line structure.
