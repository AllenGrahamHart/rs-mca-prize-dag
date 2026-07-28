# Proof

Write the positive-half negacyclic autocorrelation coefficients as
`A_1,...,A_63` and put

```text
E=sum_d A_d^2=V/2,       L=sum_d |A_d|.
```

The six support coefficients have magnitudes `2,2,2,2,1,1`. Their fifteen
raw chord products therefore comprise six `4`s, eight `2`s, and one `1`, with

```text
W=41,       Q=129.                                      (1)
```

For one non-diameter difference class, let its signed chord products be
`w_j`, put `a_j=|w_j|`, `S=|sum_j w_j|`, and define

```text
H_d=sum_j a_j-S,       Q_d=sum_j a_j^2-S^2.
```

Then

```text
Q_d<=4H_d.                                               (2)
```

Indeed, reverse every sign if necessary and write the positive and negative
masses as `P>=N`, so `S=P-N` and `H_d=2N`. Since `a_j^2<=4a_j`, (2) is
immediate for `S=0` and `S>=4`. For `S=1,2,3`, the maximum square mass of
parts in `{1,2,4}` with total `x` is

```text
g(x)=16 floor(x/4)+h_(x mod 4),       h=(0,1,4,5).
```

Checking `N mod 4` gives the nonnegative slacks

```text
8N-[g(N+S)+g(N)-S^2]

S=1:  0,4,8,4
S=2:  0,6,0,6
S=3:  4,0,4,8.
```

If `W_64,D_64` are the raw mass and square mass in diameter chords and
`H=sum_d H_d`, then `D_64<=4W_64`. Summing (2) gives

```text
L=W-W_64-H,
Q-E=D_64+sum_d Q_d<=4(W_64+H)=4(W-L).
```

Together with (1), this proves the profile-specific bound

```text
4L<=E+35.                                               (3)
```

Put `y_u=|F(zeta^u)|^2`. Autocorrelation antisymmetry and (3) give

```text
0<y_u<=18+2L<=18+2 floor((E+35)/4),                    (4)
```

unless some `y_u=0`, in which case `R=0` and there is no collision.

## Quadratic rows

For each row in the following table, (4) gives `y_u<=B`:

| `V` | `E` | `L` upper bound | `B` | `C` |
|---:|---:|---:|---:|---:|
| 138 | 69 | 26 | 70 | 1767 |
| 146 | 73 | 27 | 72 | 1808 |
| 154 | 77 | 28 | 74 | 1848 |
| 162 | 81 | 29 | 76 | 1888 |
| 170 | 85 | 30 | 78 | 1929 |
| 178 | 89 | 31 | 80 | 1969 |

On `0<x<=B`, define

```text
g(x)=log 18+(x-18)/18-(x-18)^2/C-log x.
```

Its derivative factors as

```text
g'(x)=(x-18)(C-36x)/(18Cx).
```

Every table row has `18<C/36<B`. Thus the only minima are `18` and `B`.
We have `g(18)=0`, while exact atanh-series bounds certify

```text
(B-18)/18-(B-18)^2/C > log(B/18)
```

in all six rows. Therefore `g>=0`. Averaging and using the zero mean and
variance `V` of `y_u-18` gives

```text
log R<=64 log 18-64V/C.                                (5)
```

The same exact logarithm bounds verify, row by row,

```text
64 log 18-64V/C < (1299/5) log 2.                     (6)
```

## The cubic rows

For every integer `a`, `|a|=a^2 mod 2`, so

```text
L=E mod 2.                                               (7)
```

Extend the positive-half autocorrelation to

```text
c_0=c_64=0,       c_d=A_d,       c_(128-d)=-A_d.
```

The third central moment is

```text
M_3=mean_u (y_u-18)^3=(c*c*c)_0.
```

Let `n_j` count positive-half coefficients with `|A_d|=j`. There are at most
fifteen nonzero classes, and

```text
sum_j j^2 n_j=E,       sum_j j n_j<=L,
sum_j n_j<=15.                                           (8)
```

For the symmetric nested layer sets `S_r={d:|c_d|>=r}`, put
`s_r=|S_r|=2 sum_(j>=r)n_j`. If `R(U,W,Z)` counts ordered zero-sum triples
from three layers, then choosing two entries determines the third and the
`|U intersection W|` opposite pairs force the forbidden third entry zero.
Consequently

```text
R(U,W,Z)<=min{|U||W|-|U intersection W|,
               |U||Z|-|U intersection Z|,
               |W||Z|-|W intersection Z|}.
```

Expanding `|c|` into its layers yields

```text
|M_3|<=Phi(n)
 =sum_(r,s,t) min{s_r s_s-min(s_r,s_s),
                   s_r s_t-min(s_r,s_t),
                   s_s s_t-min(s_s,s_t)}.               (9)
```

At `V=114`, equation (3) gives `E=57,L<=23`. At `V=122`, it first gives
`E=61,L<=24`, and (7) sharpens this to `L<=23`. There are respectively 52
and 57 integer profiles satisfying (8). Direct exact substitution in (9)
gives

```text
V=114: Phi<=4702, attained in the relaxed ledger at (1,5,4,0,0,0,0),
V=122: Phi<=5118, attained in the relaxed ledger at (0,4,5,0,0,0,0).
```

Let `p_62` be the cubic Hermite interpolant to `log` at `15` and `62`. Its
Hermite remainder has sign `-(x-15)^2(x-62)^2/(4 xi^4)`, so `log x<=p_62(x)`
for every `x>0`. Its leading coefficient is

```text
(3619-1860 log(62/15))/96555390>0;
```

indeed `log(62/15)<3/2`, as the first four positive terms of `exp(3/2)`
sum to `67/16>62/15`. The moment substitutions give

```text
V=114:
 mean log y_u
 <=(97990/103823)log 15+(5833/103823)log 62+5045/205437
 <(1299/320)log 2,

V=122:
 mean log y_u
 <=(97838/103823)log 15+(5985/103823)log 62+17881/1027185
 <(1299/320)log 2.                                    (10)
```

The verifier certifies both strict inequalities with exact atanh-series
intervals.

At `V=130`, equations (3)--(4) give `E=65`, `L<=25`, and `y_u<=68`. There
are exactly 73 integer profiles satisfying (8). Exact substitution in (9)
gives

```text
Phi(n)<=5950,
```

with equality in this relaxed layer ledger at
`(n_1,...,n_8)=(0,5,5,0,0,0,0,0)`. Hence `M_3<=5950`.

Let `p(x)` be the cubic Hermite interpolant to `log x` at `15` and `66`,
matching both values and first derivatives. Since
`(log x)''''=-6/x^4`, its Hermite remainder proves

```text
log x<=p(x)       for every x>0.                       (11)
```

The leading coefficient is

```text
gamma=(459-220 log(66/15))/14591610>0;
```

indeed `log(22/5)<2<459/220`. The first three raw moments satisfy

```text
mean y_u=18,
mean y_u^2=18^2+130=454,
mean y_u^3=18^3+3*18*130+M_3<=18802.
```

Because `gamma>0`, exact substitution in (11) gives

```text
mean_u log y_u
 <=(125678/132651)log 15+(6973/132651)log 66+2879/143055
 <(1299/320)log 2.                                    (12)
```

Twenty terms of the exact atanh series, with its geometric tail bound,
certify the final strict inequality.

Finally, with

```text
p_min=B_P 2^128,
B_P=317494674775468773183020924238786383963,
```

exact integer arithmetic gives `(16p_min)^5>2^1299`. Equations (5)--(6),
(10), and (12) therefore imply

```text
R<2^(1299/5)<16p_min
```

at every listed variance, contradicting `R=16p` with `p>=p_min`. The parent
congruence `V=2 mod 8` and parent upper bound `V<=178` leave precisely
`10<=V<=106`, as claimed.
