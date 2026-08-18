# Proof

The high-margin, anchor, and transverse terms are exactly those of PR `#1173`,
with `tau=1549` and `h=42451`. The ordered-basis argument gives

```text
N_1=floor(m^(underline 9)/(c-h)^9)=7367375311,
N_2=floor(m^(underline 8)/(c-h)^8)=590128056.
```

At this cutoff the dimension-two interleaved pair-type cap is `M_2=252`, so
one rank-two row-space group costs at most

```text
R_2=(n-A)M_2=247628556.
```

Together with the proved rank-one group cap `R_1=8147918`, the complete paid
transverse envelope is

```text
near                                      134944
high tail                    68786172991636274
anchor                                    982653
rank-one transverse          60028769909252498
rank-two transverse         146132558362367136
------------------------------------------------
E_transverse                274947501264373505.             (1)
```

Consequently an unsafe line, which has at least `B*+1` selected slopes,
leaves nontransverse mass at least

```text
E_nt=B*+1-E_transverse=33226847021583.                       (2)
```

Every original nontransverse row-space group costs at most `R_2`, hence (2)
forces at least `ceil(E_nt/R_2)=134181` represented row spaces. Canonically
promote and merge them exactly as in the rich-flat residual mass compiler.
A dimension-two promoted container costs at most `R_2`; a dimension-three
container costs at most

```text
R_3=(n-A) floor(C(n-K+3,3)/C(A-K+3,3))
   =982653*4023=3953213019.
```

Therefore at least `ceil(E_nt/R_3)=8406` distinct promoted containers remain.
Their defining nontransverse flats supply at least `h+1=42452` common actual
zero coordinates.

It remains to prove the span claim. Suppose `r=dim(V_nt)<=6`. For every
nonanchor low pair type `e`, both rows of its difference from the anchor lie
in `U_e`, hence in `V_nt`. Thus all nontransverse pair types lie in

```text
(a_0+V_nt) x (b_0+V_nt).                                   (3)
```

The ordinary affine-span list theorem at agreement `A` bounds either
projection in an affine `r`-flat by

```text
M_r=floor(C(n-K+r,r)/C(A-K+r,r)).                           (4)
```

For `0<=r<=6`, the exact values are

```text
1, 15, 252, 4023, 64001, 1017939, 16190045,
```

so `M_r<=M_6=16190045`. The deployed line field has size
`q=2130706433^6` and `M_6^2<q`. Applying the proved sub-square common-support
interleaving collapse to (3) therefore leaves at most `M_6` distinct ordered
pair types. Fixed-pair slope ownership costs at most `n-A=982653` slopes per
type. Hence all nontransverse groups together cost at most

```text
R_6=(n-A)M_6=15909196289385.                               (5)
```

Adding (5) to (1) gives `274963410460662890`, below `B*` by
`17317650732197`, contradicting unsafety. Therefore `dim(V_nt)>=7`.

The verifier scans every legal cutoff and proves that `42451` is the largest
threshold paid by this low-span envelope, attained at cutoffs
`1547,1548,1549`; among them `1549` has the largest slack. At `1549`, replacing
`h` by `h+1` produces `274982532307986188`, over budget by
`1804196591101`.
