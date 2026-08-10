# FPC5 shifted-Johnson GRS shell cap

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one FPC5 source, touched-petal set, and defect degree. Use

```text
N=k-1,       h=t ell,       u=d-(t-1)ell,       a=N-d.
```

For a nonempty chart, define its effective check endpoint `H`, number of
charts `W`, and adjacent base-code dimension `K` by

```text
u<0:          H=h,           W=1,
0<=u<=b:      H=d+ell,       W=binom(b,u),
K=N-H.                                                (SJ1)
```

Assume `K>=2`. For an integer `m>=3`, put

```text
Q_m=floor sqrt((2m+1)^14 N^7
               /(384^2 (K-1)^3)).                    (SJ2)
```

If

```text
(2m a)^2 >= (2m+1)^2 N(K-1),                         (SJ3)
K Q_m<q-N,                                            (SJ4)
```

then the complete fixed cell has at most

```text
W L_m(q),
L_m(q)=ceil(Q_m(q-N)/(q-N-K Q_m)).                    (SJ5)
```

contributors. In particular, the cell's local count is at most the prize
budget `B*=floor(q/2^128)` whenever

```text
W L_m(q)<=B*.                                         (SJ6)
```

This reaches the one-code-dimension strip beyond the ordinary Johnson
boundary of the GRS shell: `(SJ3)` needs `a^2>N(K-1)`, whereas the target
code has Johnson quantity `NK`.

## Smallest-row frontier replay

At `n=8192`, the following `(PF6)` cells lie in genuinely unpaid
shifted-Johnson territory: `u<0`, or `0<=u<=b` with
`J_fix=d^2-N(d-ell)<=0`. The printed powers of two are sufficient field-order
thresholds for `(SJ6)` on every admissible field above them.

```text
R   M   t    d    u     K     m       sufficient q
2   5   4  2264 -193   819  1176      2^226
4  13   3   911  -33   631  1456      2^225
8  29   3   486   -8   282   318      2^208
16 61   3   248   -2   136   376      2^208
16 61   3   286   36   100  1406      none below 2^256
16 61   3   287   37    99   512      none below 2^256
16 61   3   288   38    98   307      2^254
16 61   3   289   39    97   216      2^249
16 61   3   290   40    96   165      2^245
16 61   3   291   41    95   132      2^242
16 61   3   292   42    94   109      2^238
```

Thus the theorem gives a new local cap on one first-scale cell at rates
`1/2`, `1/4`, and `1/8`, and on six of the eight shifted/nonpositive-Johnson
cells in the displayed rate-`1/16`, `M=61` slice. The other two exceed the
budget even at the strict `2^256` envelope. The `M=57,58,59` shifted cells
all have `J_fix>0` and were already covered by the fixed-background Johnson
payment.

## Scope

`(SJ5)` is a complete bound for one fixed source/touched/degree cell, including
the exact `binom(b,u)` background incidence cost. It does not aggregate source
layouts, touched sets, degrees, or first-owner chronology, and `(SJ6)` leaves
no slack for summing other cells. A parameter cell in the replay is not an
assertion that an FPC5 contributor exists. Cells outside the one-dimension
shifted strip remain open to this method.
