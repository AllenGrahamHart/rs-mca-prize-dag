# Proof - L1 bounded-polarity marked full-pencil reduction

Call a touched petal dense when `a_i>ell/2` and sparse otherwise. If every
petal were sparse, then

```text
h=sum_i a_i=p<ell,
```

contradicting the reserve reduction `h>=ell`. Thus a dense petal exists.

Suppose it were unique. Write its size as `ell-v` and let `S` be the sum of
all sparse support sizes. Then `p=v+S` and

```text
h=ell-v+S.
```

The list threshold and maximality `r<ell` give

```text
d<=h+r-ell<=h-1=ell-v+S-1<=ell+p-1,
```

contradicting `(MP1)`. Hence at least two dense petals exist. Their deficits
are terms in the polarized sum, proving `(MP2)`.

For either selected petal, the exact agreement equation gives

```text
W-c_iF=L_(S_i)A_i,       deg A_i<=d-a_i=c+v_i,
W-c_jF=L_(S_j)A_j,       deg A_j<=d-a_j=c+v_j.
```

Subtracting yields

```text
L_(S_i)A_i-L_(S_j)A_j=(c_j-c_i)F.                       (1)
```

Since `L_(T_i)=L_(S_i)L_(V_i)` and similarly for `j`, multiplying (1) by
`L_(V_i)L_(V_j)` gives exactly `(MP3)`. The degree bounds are

```text
deg J=v_i+v_j<=p,
deg C_i<=v_j+c+v_i<=c+p,
deg C_j<=v_i+c+v_j<=c+p,
```

which proves `(MP4)`.

The core and petals are disjoint, so `gcd(F,J)=1`. Exact defect gives
`gcd(F,W)=1`. Since `W-c_iF=L_(S_i)A_i` and `L_(S_i)` is also coprime to
`F`, one has `gcd(F,A_i)=1`, and similarly for `j`.

Fix the source chart's total order and choose the first pair among the two
largest dense supports. This makes the reduction canonical. Given its
un-cleared data, reconstruct

```text
W=c_iF+L_(S_i)A_i,
P_word=Q+L_(C\D)W.
```

All other exact agreement supports are then determined by this word, so they
create no extra multiplicity in the reduction.

Finally, for fixed total mark size `v`, choosing `V_i` and `V_j` costs at
most `binom(2ell,v)`, and there are `binom(M,2)` petal pairs. Summing
`0<=v<=P` proves `(MP5)`. Fixed `P`, `M=O(log n)`, and `ell<=n` make this
polynomial at the lower cutoff.
