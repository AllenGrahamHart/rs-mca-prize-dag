# Proof

The extension-list reduction gives, before loop deletion, a five-dimensional
code containing a four-dimensional kernel. When `u=0`, deleting the `v`
kernel-loop coordinates and applying the fixed coordinate scaling identifies
the kernel with `GRS_4` on

```text
N=R+4
```

points. At a kernel loop outside the persistent set, the error coordinate of
a selected member is a nonzero affine function `b(x)+gamma q(x)` of its
slope. It vanishes at at most one slope. The union of the exceptional slopes
over all `v` loops therefore has size at most `v`.

The original family has integer size at least `B+1`, so at least
`B+1-v=B_v` members remain. None of their agreement points was deleted. The
extension-list reduction therefore gives at least

```text
m=4+h+v
```

actual agreement points per retained member. Its P-B intersection cap, after
the persistent set is removed, is `3+v`; deleting loop coordinates cannot
increase it.

Fix a reused four-set `T`. Write the retained extension codeword at slope
`gamma` as

```text
c_gamma=gamma q+w_gamma,       w_gamma in GRS_4.
```

On its actual agreement set `A_gamma`, one has `U=c_gamma`. Restriction to
`T` and uniqueness of degree-less-than-four interpolation give

```text
I_T U=gamma I_T q+w_gamma.
```

Subtracting this identity from `U=gamma q+w_gamma` proves `(LR1)`.

Let `eta!=gamma` be another retained slope whose agreement set contains
`T`. If `x in A_gamma\T` and `d_T(x)=0`, then `(LR1)` also gives
`a_T(x)=0`. The codeword at slope `eta` satisfies

```text
U(x)-c_eta(x)=a_T(x)-eta d_T(x)=0,
```

so `x` is an actual agreement point of the `eta` member as well. Thus `T`
together with all such zero-denominator points lies in the intersection of
the two actual agreement sets. Their intersection has size at most `3+v`,
which proves `(LR2)`.

Choose any `m` points of `A_gamma` containing `T`. There are `m-4=h+v`
points outside `T`, and at most `v-1` have zero denominator. At least `h+1`
therefore lie in the defined ratio fiber `Phi_T=gamma`. A point with
`d_T(x)!=0` has only one ratio value, so fibers belonging to distinct slopes
are disjoint. The post-loop domain outside `T` has `N-4=R` points. This gives

```text
(h+1)#members through T <= R,
```

and hence `(LR3)`.

It remains to prove the rich-core assertion. Choose one `m`-subset from each
retained actual agreement set. Suppose no nonempty subfamily has minimum
`r`-rich four-core degree at least `D_r`. Iteratively delete a member having
at most `D_r-1` four-cores whose current multiplicity is at least `r`.
Charge its other four-cores at deletion. A fixed four-core can receive at
most `r-1` such low-multiplicity charges. If `L>=B_v` is the retained family
size, deletion of the whole family would give

```text
L C(m,4) <= L(D_r-1)+(r-1)C(N,4).                    (1)
```

By `(LR4)`,

```text
C(m,4)-D_r+1
 =floor((r-1)C(N,4)/B_v)+1
 >(r-1)C(N,4)/B_v.
```

Multiplying by `L>=B_v` contradicts `(1)`. Therefore the asserted subfamily
exists. If `r` exceeds the line cap `(LR3)`, no four-core can have
multiplicity `r`; positivity of `D_r` is then impossible under the
over-budget assumption. This proves `(LR4)--(LR5)` and the theorem. QED.
