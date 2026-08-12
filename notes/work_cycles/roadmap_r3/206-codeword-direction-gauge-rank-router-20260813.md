# Cycle 206: codeword-direction gauge rank router (2026-08-13)

The direction-distance route chooses a codeword `b` nearest to the shortened
received direction.  Subtracting that codeword is also an exact MCA gauge:

```text
(r_0,r_1,c_gamma) -> (r_0,r_1-b,c_gamma-gamma b).
```

The transformation preserves every slope, agreement support, and
same-support pair-noncontainment.  The original and transformed selected
explanation affine ranks differ by at most one, since their difference
spaces differ by a rank-one update in the direction `b`.

Applying the support-wise affine-span compiler to transformed rank `r` in
ambient shortened dimension `K` gives

```text
A_(K,r)=floor(max(
  (R+K)^(falling r+1)/((d+K)d^(rising r)),
  (R+r)^(falling r+1)/d^(rising r+1))).
```

Exact deployed walls are:

```text
KoalaBear:   r<=11 through the full K<=1048576 cap;
             r=12 through K=745260;
             r=13 through K=289603;
             r>=14 not uniformly paid by this compiler.
Mersenne-31: r<=4 through the full cap;
             r=5 through K=482472;
             r>=6 not uniformly paid.
```

The adjacent finite boundaries are particularly tight:

```text
KB r=12: 274980259855184513 <= B* < 274981914318597687
KB r=13: 274980152556476265 <= B* < 274982259324238595
M31 r=5: 16777192 <= B* < 16777228.
```

For fixed `r`, the ratio `T_(K+1)/T_K` changes direction exactly when the
linear expression `rK+(r+1)d-R+r` changes sign, proving that the
ambient-dimension sequence has only one turn.  The primary checker scans
7,339,974 exact values and four mutations; an independent ratio/binary-search
audit uses 81 evaluations and three controls.

```text
start:                   c25e21360
result:                  PROVED codeword-direction gauge rank router
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none
upstream terminal delta: every surviving direction cell now also carries
                         a transformed affine-rank floor
delta-star movement:     none
compute:                 bounded integer scans under RAMguard;
                         no Modal spend
next route action:       combine transformed rank with sparse-direction
                         punctured-list payment
```
