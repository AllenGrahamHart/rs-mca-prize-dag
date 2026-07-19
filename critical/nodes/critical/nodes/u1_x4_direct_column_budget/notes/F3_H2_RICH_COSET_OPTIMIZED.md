# F3 h=2 rich-coset constant optimization

Status: PROVED ARITHMETIC SHARPENING for the Terminal-B h=2 chain.

This is the first T3 constant-campaign packet from
`notes/codex_briefs/F3_FLIP_20260708.md`.  It keeps the existing
`F3_H2_RICH_COSET_STEPANOV.md` proof intact and sharpens only the explicit
parameter bookkeeping in its Step 5.

## Pre-registration

Question:

```text
Can the in-house rich-coset Stepanov constant K=129 be lowered by replacing the
coarse floor-loss inequalities in the existing proof with exact optimized
floor bookkeeping?
```

Success criterion:

- prove, using the same auxiliary polynomial and nonvanishing lemma, a smaller
  explicit constant `K`;
- verify the active/trivial branch inequalities by exact integer arithmetic on
  stress rows covering small, transition, and large parameter ranges;
- print the new h=2 crossover table for official-row sizes.

Failure criterion:

- any floor-loss inequality fails in the exact verifier;
- the improvement is only empirical and cannot be stated as a proof-level
  replacement for `K=129`.

## Optimized Rich-Coset Lemma

Let `H = mu_h <= F_p^*`.  For a set `U` of `T >= 1` nonzero shifts in distinct
`H`-cosets, let

```text
R(U) = sum_{u in U} |{x in H : x-u in H}|.
```

Under the same hypothesis as the existing note,

```text
h^4 T < p^3,
```

one has

```text
R(U) <= 66 * (hT)^(2/3).
```

### Proof

Use the same auxiliary polynomial

```text
Phi(X, X^h, (X-1)^h)
```

and the same nonvanishing lemma as `F3_H2_RICH_COSET_STEPANOV.md`.  Put

```text
X = h^(2/3) T^(-1/3),       Y = h^(1/3) T^(1/3),
```

so `XY = h` and

```text
hY/X = (hT)^(2/3).
```

If `X <= 4225 = 65^2`, the trivial bound `R(U) <= h` gives

```text
R(U)/(hT)^(2/3) = X^2/h <= sqrt(X) <= 65 < 66,
```

using `T >= 1`, hence `h >= X^(3/2)`.

Assume now `X > 4225` and choose

```text
A = floor(X/4),       B = floor(Y/2),       D = floor(X/64).
```

Since `X > 4225` and `T >= 1`, we have `Y = h/X >= sqrt(X) > 65`.  Hence

```text
A >= X/5,        B >= Y/3,        D >= X/65.
```

The linear-system inequality holds because

```text
A B^2 >= X Y^2 / 45 = X^2 T / 45
```

while

```text
D(A+D)T <= (X/64)(X/4 + X/64)T
        = 17 X^2 T / 4096
        < X^2 T / 45.
```

The nonvanishing conditions hold exactly as before:

```text
AB <= h/8 <= h,
```

and `h^4 T < p^3` implies `hY < p`; also `X < p`, so

```text
A + hB < X/4 + hY/2 < p.
```

Therefore the auxiliary polynomial is nonzero and the degree/multiplicity
argument gives

```text
R(U) < (A + 2hB)/D
     <= (X/4 + hY)/(X/65)
     = 65/4 + 65 (hT)^(2/3).
```

In the active branch `(hT)^(2/3) = hY/X >= X > 4225`, so

```text
65/4 + 65 (hT)^(2/3) < 66 (hT)^(2/3).
```

This proves the optimized rich-coset lemma with `K = 66`.

## h=2 Energy Consequence

The existing compiler gives

```text
E(H) <= (1 + 5(K^2 + K)) h^(5/2).
```

With `K = 66`,

```text
E(H) <= 22111 h^(5/2),
T_2 <= (22111/8) h^(5/2).
```

Thus the in-house h=2 theorem implies `T_2 < h^3` once

```text
h > (22111/8)^2 = 488896321/64 = 7,639,005.015625.
```

So integer `h >= 7,639,006` is covered by the optimized in-house chain.  In the
official range `[2^13, 2^41]`, this covers every row with `h >= 2^23`; rows
`2^13` through `2^22` remain a finite midrange for exact certificates or the
external Cochrane--Pinner import.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_optimized.py
```

Expected digest:

```text
H2_RICH_COSET_OPTIMIZED_PASS
```
