# Rank-eleven kernel rank-stratified capacity cut

- **status:** PROVED
- **scope:** every residual shortening `10<=K'<=4598`
- **units:** dominant-lane `(record, eleven-subset)` incidences

Put `n'=1048576+K'`, `m'=67472+K'`, and

```text
D(K')=(495405467/10^9) N_min C(m',11).
```

For `d=1,...,9`, put `r=10-d`, let `M_d(K')` be the fixed-basis record
cap after cancelling `r` coordinates, and define

```text
Cap(K') = sum_(d=1)^9 C(n',10-d) M_d(K') C(K'-10,d+1).
```

Canonical basis assignment and the kernel globalizer prove that `Cap(K')`
is an upper bound for the complete rank-deficient lane. Exact integer replay
gives

```text
D(K') > Cap(K')       for every 10<=K'<=4598.
```

At the endpoint,

```text
ceil(D(4598)) =
929128176313956503149540905404647183686331231003203243640927369,

Cap(4598) =
928908903983455301405411728138488194978633914765154364813729684,

gap =
219272330501201744129177266158988707697316238048878827197685.
```

Therefore the kernel lane cannot be the dominant component lane on this
complete shortening interval. At `K'=4599` the inequality reverses, so no
larger interval is claimed.

## Falsifier

A missed rank-zero stratum; tuple overcounting under canonical basis
assignment; a fixed-basis capacity above its globalizer bound; failure at
any integer `K'` in the printed interval; or a positive gap at `K'=4599`.
