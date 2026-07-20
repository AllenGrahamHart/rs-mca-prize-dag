# Proof

Every ordinary complement `H_z=G_z\R_A` represents `[h_1]`, so `w_z>=h`.
If `w_z=h`, choose that minimal support as `T`. The canonical representation
on `R_A union T` and the clean representation on `G_z` have union size at
most

```text
(r-1)+h<=2e+3(e+1)/2<2r+1.                            (1)
```

They are therefore identical by Vandermonde independence. Thus the fiber is
internal and has exactly `h-1` cancelled exceptional coefficients. Distinct
such fibers have disjoint cancellation sets, so their number `N_min`
satisfies

```text
N_min<=floor(2e/(h-1)).                                (2)
```

In the surviving high-distance interval `h>=2e/3+3`, the right side of `(2)`
is at most two; at the former ceiling it is one.

The exact intersection count from the quotient-distance ceiling is

```text
sum_z a_z=2e(e-1).
```

Since `w_z=r-a_z`, this is equivalently

```text
sum_z w_z=4er-2e(e-1)=6e(e+1).                        (3)
```

Put `H=3(e+1)/2`. If `h=H`, then `(3)` is exactly `4eH`. But `(2)` permits at
most one complement of size `H`; every other complement has size at least
`H+1`. Their sum would be at least `4eH+4e-1`, a contradiction. This proves
`(QSC1)`.

Now let `h=H-1`. Equation `(3)` says

```text
sum_z(w_z-h)=4e.                                      (4)
```

Again `(2)` gives `N_min<=1`. If `N_min=0`, all `4e` positive integer
excesses in `(4)` equal one, proving `(QSC2)`. If `N_min=1`, one excess is
zero and the other `4e-1` excesses are positive. Their sum is `4e`, so one
equals two and all the rest equal one. This proves the complement multiset in
`(QSC3)`. Subtracting each complement size from `r=2e+1` gives the printed
intersection multiset. QED.
