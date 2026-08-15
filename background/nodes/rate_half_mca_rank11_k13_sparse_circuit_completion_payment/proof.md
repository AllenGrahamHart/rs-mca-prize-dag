# Proof

Put `P_13=F[X]_<13` and `Lambda=(V')^perp`, so `dim Lambda=3`.  Partition
the dense-locator component incidences by the rank on their eleven-set `T`.

## 1. Rank-deficient capacity

At shortening excess `K'-10=3`, the canonical-basis extension factor in
corank `d` is `C(3,d+1)`.  Only `d=1,2` survive.  The proved record caps are

```text
M_1(13)=16295594,       M_2(13)=253241283.
```

Therefore

```text
K_cap=3 C(1048589,9)*16295594 + C(1048589,8)*253241283
     =206481189843433295842936213010503229833431068859362597823. (1)
```

This is an absolute capacity for every rank-deficient component incidence,
not a dominant-lane estimate.

## 2. Rank-nine chart capacity

Suppose `rank(ev_T|V')=10`.  Then

```text
dim(Lambda intersect E_T)=1.
```

Let `C_T` be the unique quotient circuit and put `c_T=|C_T|`.  A rank-nine
shadow has common-core size `j in {9,10,11,12}`.  With

```text
P=m'-j,       S=n'-j,       r=j-9,
```

the weighted common-core offset theorem gives exact chart caps

```text
j=9:  9275234985700485,
j=10: 9276176591408201,
j=11: 9277118227920090,
j=12: 9278059895199813.
```

Hence every rank-nine chart has marked load at most
`C_*=9278059895199813`.

Exactly

```text
55-C(11-c_T,2)
```

of the nine-shadows of `T` have rank nine.  For `c_T>=6` this is at least
45, so all high-circuit incidences have capacity

```text
H_cap=floor(C(1048589,9)C_*/45)
     =870791924265139618716231673259817164224620222733319378834968170. (2)
```

For `c_T<=5`, the correction space has empty global common zero set and the
codimension-three completion theorem applies to each selected record
support.  Its per-record cap is

```text
L_*=99254447944649683780146155758753837527116020.             (3)
```

## 3. Exact contradiction

For `R_actual` residual records, `(1)`--`(3)` give

```text
I_component <=K_cap+H_cap+R_actual L_*.
```

The dense-locator theorem requires at least

```text
ceil((990810934/10^9) R_actual C(67485,11)).
```

The demand coefficient minus `L_*` has positive cross numerator

```text
3179892509671792384744396543086450191690406044908895900.
```

Thus the gap is smallest at
`R_actual=N_min=274980728111260126`.  At this floor the demand and capacity
are the two printed integers, with positive difference

```text
3617026878762290164882578515067303096680225900459379608374624.
```

This contradiction closes `K'=13`.  QED.
