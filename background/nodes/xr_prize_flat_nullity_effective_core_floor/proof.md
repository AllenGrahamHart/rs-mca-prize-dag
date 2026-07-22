# Proof

In the flat-nullity notation,

```text
p=|P_0|=k-a-u-v=k-kappa.
```

Every selected error has at least `k+h` zeros. After deleting `P_0`, its zero
set therefore has at least `k+h-p=kappa+h` points in a ground set of size
`n-p=R+kappa=N`. The P-A post-strip cap says that two original zero sets
intersect in at most `k` points, so their residual zero sets intersect in at
most `k-p=kappa` points.

Choose one deterministic `(kappa+h)`-subset from each residual zero set.
These chosen blocks are distinct: equality would give an intersection of
size `kappa+h>kappa`. Call the resulting family `F`.

If `|F|>8n^3`, then `h|F|>2R=2N-2kappa`. Choose an inclusion-minimal
nonempty `G subset F` satisfying

```text
h|G|>=2|union G|-2kappa.                             (1)
```

Write `t=|G|`, `V=union G`, and

```text
h t=2|V|-2kappa+e.                                  (2)
```

Minimality and integrality give `0<=e<=h-1`. More precisely, if `p_A` is the
number of points private to `A` inside `G`, applying failure of `(1)` to
`G\{A}` gives

```text
e+2p_A<=h-1.                                        (3)
```

Since `|V|<=N`, `(2)` also gives

```text
t<=floor((2N-2kappa+h-1)/h)
 =floor((2R+h-1)/h)=L.                              (4)
```

Let `P` be the total number of points of block multiplicity one in `G`.
Total incidence is `t(kappa+h)`, while pair incidence is at most
`C(t,2)kappa`. The pointwise inequality
`m-2C(m,2)<=1_(m=1)` gives

```text
P>=t(kappa+h)-t(t-1)kappa
 =t h-t(t-2)kappa.                                  (5)
```

On the other hand, summing `(3)` over the blocks gives

```text
P<=t(h-1-e)/2<=t(h-1)/2.                            (6)
```

Combining `(5)--(6)` yields

```text
kappa>=(h+1)/(2(t-2))>=(h+1)/(2(L-2)).              (7)
```

It remains only to justify the denominator in `(7)`. A one-block core would
make `(1)` read `h>=2h`, impossible because `h>0`. For two blocks, the pair
cap gives

```text
|V|>=2(kappa+h)-kappa=kappa+2h,
```

whereas `(1)` would require `2h>=2|V|-2kappa>=4h`, again impossible.
Therefore `t>=3`. Taking the integer ceiling proves `(EF2)`. Official
substitution and subtraction of the first-open affine ranks give `(EF3)`.
QED.
