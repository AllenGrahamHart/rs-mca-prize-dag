# Cycle 255: rate-half shape-A bordered-Hankel flag (2026-08-13)

The omitted-recurrence flag from Cycle 253 was coupled to the existing
core-one adjugate and directly to the finite source moments.

If

```text
M=(h_(i+j))_(0<=i,j<=d),
adj M=D_1qq^T,
v_s=(h_(d+1+s+i))_(0<=i<=d),
R_(d+1+s)=q^Tv_s,
```

then every column-replacement minor and every bordered determinant is exact:

```text
det M[k<-v_s]=D_1q_kR_(d+1+s),
det widehat M_s=-D_1R_(d+1+s)^2.
```

Cauchy-Binet rewrites the latter as one explicit source subset sum over
`d+2=3e` source columns. In shape A,

```text
B_s=c g_*(S_B Lambda Theta_s)^2,
Theta_0=[X^n]G.
```

The complete off-line flag now splits into two disjoint pieces:

```text
padding singular flag: e-7 slopes cut out by g_off,
regular source flag:   2e+7 slopes cut out by H_reg.
```

On every regular slope, a degree-drop run of length at least `r+1` is
equivalent to the middle Hankel rank remaining `d` after the first `r+1`
next moment columns are appended. The regular flag is therefore an exact
source rank-stagnation locus; the padding flag is deliberately separate.

```text
start:                   382141e6c
canonical prize:         fdfb20a42 (clean; unchanged)
result:                  PROVED bordered-Hankel/source flag presentation
DAG delta:               +1 PROVED node, +5 req edges, +1 ev edge
critical status delta:   none; rate_half_band_crossing_location remains open
official regular slopes: 366503875933
official padding slopes: 183251937956
compute:                 two constant-size exact local audits; no Modal spend
next route action:       attack the padding singular flag or prove a
                         source subset-square non-stagnation theorem on H_reg
```
