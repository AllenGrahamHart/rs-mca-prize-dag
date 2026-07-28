# Proof

Write the positive-half negacyclic autocorrelation coefficients as
`A_1,...,A_63` and put

```text
E=sum_d A_d^2=V/2,       L=sum_d |A_d|.
```

The fifteen raw chord products have magnitudes six `4`s, eight `2`s, and one
`1`, with total mass `W=41` and square mass `Q=129`. The signed-chord ledger
therefore gives

```text
4L<=E+35,       L=E mod 2.                              (1)
```

For `y_u=|F(zeta^u)|^2`, autocorrelation antisymmetry gives

```text
0<y_u<=18+2L,                                           (2)
```

unless `R=0`, which cannot be a collision.

## Exact third-moment rows

Normalize the two singleton positions to `0,1`, as permitted by the odd
singleton separation on the `v_2(m)=1` branch. The complete normalized
universe has `32 binom(126,4)=320292000` signed vectors.

Two independent enumerators compute

```text
M_3=mean_u (y_u-18)^3=(c*c*c)_0.
```

The primary uses a direct full 128-slot convolution, lexicographic shards,
and a sparse ordered-pair moment identity. The audit uses folded pairs,
balanced shards, and an independent negacyclic-square identity. They agree on
every population, minimum, and maximum through `V=194`. The load-bearing
maxima are

| `V` | 106 | 114 | 122 | 130 | 138 | 146 | 154 | 162 | 170 | 178 | 186 | 194 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `max M_3` | 1452 | 1608 | 2256 | 3264 | 2748 | 3528 | 3264 | 4248 | 4164 | 4560 | 5280 | 5904 |

For contacts `a<b`, let `p_(a,b)` be the cubic Hermite interpolant to `log x`
at `a,b`, matching values and derivatives. Its remainder is

```text
log x-p_(a,b)(x)=-((x-a)^2 (x-b)^2)/(4 xi^4)<=0.
```

Exact rational atanh intervals certify that its cubic coefficient is positive
and that substituting

```text
mean y=18,
mean y^2=324+V,
mean y^3=5832+54V+max M_3
```

is below `(1284/320) log 2` in all twelve rows. The contacts are

```text
(12,37), (12,38), (13,42), (14,47), (13,43), (13,47),
(12,45), (13,49), (12,48), (12,49), (13,52), (13,54).
```

## Universal-layer rows

Let `n_j` count positive-half coefficients with `|A_d|=j`. There are at most
fifteen nonzero classes and

```text
sum_j j^2 n_j=E,       sum_j j n_j<=L,
sum_j n_j<=15.                                           (3)
```

For the nested symmetric layers `S_r={d:|c_d|>=r}`, put `s_r=|S_r|`.
Expanding `|c|` into layers gives the universal bound

```text
|M_3|<=Phi(n)
 =sum_(r,s,t) min{s_r s_s-min(s_r,s_s),
                   s_r s_t-min(s_r,s_t),
                   s_s s_t-min(s_s,s_t)}.               (4)
```

Exact enumeration of (3), using (1) and parity, gives

| `V` | `E` | `L` cap | profiles | `Phi` cap | contacts |
|---:|---:|---:|---:|---:|:---|
| 202 | 101 | 33 | 236 | 12490 | `(15,83)` |
| 210 | 105 | 35 | 266 | 13738 | `(15,86)` |
| 218 | 109 | 35 | 292 | 14030 | `(15,86)` |
| 226 | 113 | 37 | 335 | 15346 | `(15,89)` |
| 234 | 117 | 37 | 365 | 16206 | `(15,90)` |
| 242 | 121 | 39 | 397 | 17614 | `(15,94)` |
| 250 | 125 | 39 | 448 | 17978 | `(15,93)` |

The same exact Hermite verification excludes all seven rows.

Finally, with

```text
p_min=B_P 2^128,
B_P=317494674775468773183020924238786383963,
```

exact integer arithmetic gives `(2p_min)^5>2^1284`. Thus every listed
chamber has `R<2^(1284/5)<2p_min`, contradicting `R=2p` with `p>=p_min`.
The parent congruence leaves exactly `10<=V<=98`, `V=2 mod 8`.
