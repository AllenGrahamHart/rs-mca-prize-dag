# Proof

Fix `d,t` in the displayed range and let `J_(d,t)(S)` count rank-`(10-d)`
subsets of `S` of size `11-t`.

First count the spanning shadows of one eleven-set `T` counted by `I_d`.
The dual of its loopless evaluation matroid is coloopless of rank `d+1`.
In any coloopless rank-`r` matroid, every independent `j`-set `A`, `j<r`,
has at least `r-j+1` one-element independent extensions.  Otherwise exactly
`r-j` elements would lie outside `cl(A)` and every one would occur in every
basis, making them coloops.  If `f_j` counts independent `j`-sets, double
counting extensions gives

```text
(j+1)f_(j+1) >= (r-j+1)f_j.
```

Starting with `f_0=1` and iterating to `j=t-1` gives

```text
f_t >= C(r+1,t)=C(d+2,t)=s_(d,t).                    (1)
```

A size-`(11-t)` subset spans `T` exactly when its complementary `t`-set is
independent in the dual.  Conversely, one fixed rank-`(10-d)` shadow has
closure size at most `K'-d`, and therefore at most

```text
E_(d,t)=C(K'-d-(11-t),t)
```

same-rank eleven-set extensions.  Hence

```text
s_(d,t) I_d <= E_(d,t) J_(d,t).                       (2)
```

Now fix a shadow `U` counted by `J_(d,t)`.  After `j` independent support
points have been adjoined, where `0<=j<t`, the closure has rank `10-d+j`
and generalized-MDS size cap `K'-d+j`.  At least

```text
m'-(K'-d+j)=67472+d-j
```

support points extend the independent sequence.  Dividing the ordered count
by `t!`, at least

```text
L_(d,t)=C(67472+d,t)                                  (3)
```

unordered `t`-sets raise the rank by `t`.  They produce rank-`(10-d+t)`
eleven-sets counted by `I_(d-t)`.

For the reverse multiplicity, fix such a target `T` and write `D=T\U`.
The dual-rank identity

```text
r_T(T\D)=r_T(T)-t+r_(T*)(D)
```

shows that `U` has rank `r_T(T)-t` exactly when all elements of `D` are
coloops of `T`.  The target is loopless, has rank `10-d+t`, and has eleven
elements.  It has at most `9-d+t` coloops: one more would leave the remaining
nonempty set as loops.  Thus at most

```text
Q_(d,t)=C(9-d+t,t)                                    (4)
```

source shadows produce one target.  Equations (3) and (4) give
`L_(d,t)J_(d,t)<=Q_(d,t)I_(d-t)`.  Combining with (2) proves every
`H_(d,t)`.
