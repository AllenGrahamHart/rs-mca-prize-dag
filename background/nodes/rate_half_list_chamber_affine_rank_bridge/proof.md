# Proof

The final section of `statement.md` gives the complete argument. This file
separates its logical steps and dependencies.

## 1. Affine rank and mismatch

`rate_half_list_budget_three_affine_rank_rigidity` gives `s=3` for every
four-word predecessor witness. The common-mismatch theorem gives `b=0`.

## 2. First generalized weight

In the slack ledger of
`rate_half_list_budget_three_intersection_reduction`, every one of the six
incidence types has a pair `i,j` whose selected intersection has size
`2d-1`. The nonzero difference `c_i-c_j` has degree below `2d`, hence no
more than `2d-1` domain zeros. Its selected zeros already attain that cap,
so its support is `4d-(2d-1)=2d+1`.

The generalized Singleton bound for a one-dimensional subcode of
`RS[F,D,2d]` gives `d_1>=4d-2d+1=2d+1`. Consequently `d_1=2d+1`.

## 3. A uniform upper bound on the second generalized weight

For three of the affinely independent codewords, their two differences span
a two-dimensional subcode. Every coordinate selected by all three is a
common zero of that subcode. The six-type table has, in the notation of the
split-pencil normal form,

```text
max_l (|F|+|T_l|) >= d-1.
```

Thus at least one two-dimensional subcode has at least `d-1` common zeros,
and the minimum support over all such subcodes satisfies `d_2<=3d+1`.

## 4. Rank-flat arithmetic

Put `x=d_3`. Generalized Singleton and the length bound give

```text
2d+3<=x<=4d.
```

At `t=d+1` and `b=0`, the three denominator factors in the rank-flat
compiler obey

```text
d_1-t=d,
d_2-t<=2d,
d_3-t=x-d-1.
```

Hence its unfloored right side is at least the expression `(RF3)` in the
statement. Let

```text
F_d(x)=x(x-1)(x-2)-8d^2(x-d-1).
```

Direct expansion gives

```text
F_d(2d+3)=8d^2+22d+6>0,
F_d'(2d+3)=4d^2+24d+11>0,
F_d''(x)=6x-6>0.
```

Therefore `F_d` is positive throughout `x>=2d+3`. The rank-flat expression
is strictly greater than four and its floor is at least four. It cannot
exclude a four-word chamber by proving a cap of three. QED.
