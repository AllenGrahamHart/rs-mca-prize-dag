# Proof - L1 general first-layout domination

Fix the layout `(GL1)--(GL3)` and a listed codeword `P` not in `Anch`. On the
core, `U=Q`. Let

```text
C_P={x in C:P(x)=U(x)},       D=C\C_P,       d=|D|.
```

The degree-below-`k` polynomial `P-Q` vanishes on `C_P`, so

```text
P-Q=L_(C_P)W
```

for a unique polynomial `W`. Since `|C_P|=k-1-d`,

```text
deg W < k-|C_P|=d+1.
```

Thus `deg W<=d`.

If `x` is a background agreement, `(GL2)` gives `P(x)-Q(x)=0`. Since
`x notin C`, the retained-core locator is nonzero there, hence `W(x)=0`.
If `x in S_i`, then

```text
L_(C_P)(x)W(x)=P(x)-Q(x)=c_iL_C(x)
                         =c_iL_(C_P)(x)L_D(x).
```

Canceling the nonzero retained-core factor proves the two pointwise equations
in `(GL5)`.

If some `|S_i|>d`, the degree-at-most-`d` polynomial `W-c_iL_D` has more than
`d` roots and is zero. Therefore

```text
P-Q=L_(C_P)c_iL_D=c_iL_C,
```

so `P=Q+c_iL_C`, contrary to `P notin Anch`. Hence every petal support has
size at most `d`. This proves universal non-planted carriage for arbitrary
`ell`; no sigma-one identity was used.

The disjoint identity `(GL4)` is the partition of `X` according to membership
in `Anch`, and `(GL3)` gives `|X intersect Anch|<=M`. For an ordered family of
layouts, a codeword not planted in the first layout is already carried there
by `(GL5)`. Thus every codeword whose first non-planted carriage occurs later
must belong to the first anchor set, proving `(GL6)`.

Finally maximal packing gives `M ell<=n-k+1<=n`. The L1 cutoff therefore
implies `(GL7)`.
