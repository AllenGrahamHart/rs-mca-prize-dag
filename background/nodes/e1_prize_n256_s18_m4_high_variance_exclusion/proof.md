# Proof

Write the positive-half negacyclic autocorrelation coefficients as
`A_1,...,A_63` and put

```text
E=sum_d A_d^2=V/2,       L=sum_d |A_d|.
```

The six support coefficients have magnitudes `2,2,2,2,1,1`. Their fifteen
raw chord products comprise six `4`s, eight `2`s, and one `1`, so their total
mass and square mass are `W=41` and `Q=129`. The signed-chord argument proved
in the cofactor-16 sibling applies without reference to the cofactor and gives

```text
4L<=E+35.                                                (1)
```

Also `L=E mod 2`. If `y_u=|F(zeta^u)|^2`, autocorrelation antisymmetry gives

```text
0<y_u<=18+2L,                                           (2)
```

unless a conjugate vanishes, in which case `R=0` and there is no collision.

## Exact third-moment rows

Extend the positive-half autocorrelation by

```text
c_0=c_64=0,       c_d=A_d,       c_(128-d)=-A_d.
```

Then the third central moment is

```text
M_3=mean_u (y_u-18)^3=(c*c*c)_0.
```

Two independent complete normalized enumerators cover all
`32 binom(126,4)=320292000` signed vectors after placing the singleton
positions at `0,2`. One uses a direct full 128-slot convolution with
lexicographic shards and computes the moment from sparse ordered pairs. The
audit uses folded pair data with balanced shards and an independent
negacyclic-square identity. They agree on every population, minimum, and
maximum through `V=162`. The load-bearing maxima are

| `V` | 82 | 90 | 98 | 106 | 114 | 122 | 130 | 138 | 146 | 154 | 162 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `max M_3` | 912 | 1104 | 1548 | 1728 | 1968 | 2256 | 3264 | 3132 | 3888 | 3264 | 4248 |

For contacts `a<b`, let `p_(a,b)` be the cubic Hermite interpolant to `log x`
which matches the value and derivative at both contacts. Its remainder is

```text
log x-p_(a,b)(x)=-((x-a)^2 (x-b)^2)/(4 xi^4)<=0,
```

so it is a global majorant on `x>0`. Exact atanh-series intervals verify that
the cubic coefficient is positive and that substitution of

```text
mean y=18,
mean y^2=324+V,
mean y^3=5832+54V+max M_3
```

is below `(1289/320) log 2` in every row, using contacts

```text
(13,34), (13,35), (13,39), (13,39), (13,40), (13,42),
(14,48), (13,46), (13,49), (12,45), (13,49).
```

## Universal-layer rows

Let `n_j` count positive-half coefficients with `|A_d|=j`. There are at most
fifteen nonzero classes and

```text
sum_j j^2 n_j=E,       sum_j j n_j<=L,
sum_j n_j<=15.                                           (3)
```

For nested symmetric layers `S_r={d:|c_d|>=r}`, put `s_r=|S_r|`. Expanding
`|c|` into layers and observing that two entries determine the third gives

```text
|M_3|<=Phi(n)
 =sum_(r,s,t) min{s_r s_s-min(s_r,s_s),
                   s_r s_t-min(s_r,s_t),
                   s_s s_t-min(s_s,s_t)}.               (4)
```

Exact enumeration of the integer profiles in (3), with the parity sharpening
of (1), gives

| `V` | `E` | `L` cap | profiles | `Phi` cap | contacts |
|---:|---:|---:|---:|---:|:---|
| 170 | 85 | 29 | 139 | 9286 | `(15,76)` |
| 178 | 89 | 31 | 169 | 10374 | `(15,79)` |
| 186 | 93 | 31 | 183 | 10594 | `(15,78)` |
| 194 | 97 | 33 | 211 | 11750 | `(15,82)` |

The same exact Hermite check excludes all four rows.

## Quadratic rows

For the final four chambers, (1), parity, and (2) give the following bounds.

| `V` | `E` | `L` cap | `B` | `C` |
|---:|---:|---:|---:|---:|
| 202 | 101 | 33 | 84 | 2049 |
| 210 | 105 | 35 | 88 | 2129 |
| 218 | 109 | 35 | 88 | 2129 |
| 226 | 113 | 37 | 92 | 2209 |

On `0<x<=B`, define

```text
g(x)=log 18+(x-18)/18-(x-18)^2/C-log x.
```

Its derivative is `(x-18)(C-36x)/(18Cx)`. Since `18<C/36<B`, its minima
occur at `18` and `B`. Exact atanh intervals verify both

```text
(B-18)/18-(B-18)^2/C > log(B/18)
```

and

```text
64 log 18-64V/C < (1289/5) log 2
```

in every row. Thus each listed chamber has `R<2^(1289/5)`.

Finally, for

```text
p_min=B_P 2^128,
B_P=317494674775468773183020924238786383963,
```

exact integer arithmetic gives `(4p_min)^5>2^1289`. Hence every chamber from
`V=82` through the parent endpoint `V=226` contradicts `R=4p` with
`p>=p_min`. The parent congruence leaves precisely `10<=V<=74`, `V=2 mod 8`.
