# Proof - L1 background-surplus Plotkin payment

Let `R_P` now be the full background agreement set of contributor `P`, so
`|R_P|=u+z` in the fixed stratum. The cross-determinant root argument gives

```text
|D_P intersect D_Q|+|R_P intersect R_Q|<=r=2d-h.       (1)
```

Every combined set `A_P=D_P disjoint_union R_P` has size

```text
|A_P|=d+u+z=r+ell+z.                                   (2)
```

Thus `(1)--(2)` give

```text
|A_P triangle A_Q|>=2(ell+z),                          (3)
```

proving `(PS3)`.

If `E_z<=0`, the sign-vector/Rankin argument applies directly at length
`V<=4(ell+z)` and gives at most `2V<=2n` contributors. If
`0<E_z<=E_0`, partition by the pattern on any `E_z` coordinates and puncture
inside each pattern class. Every class has length `4(ell+z)`, unchanged
distance at least `2(ell+z)`, and hence at most `2*4(ell+z)<=2n` members.
There are at most `2^E_z<=2^E_0` classes. This proves `(PS4)`.

At fixed `p<=P`, there are at most `2^M(P+1)n^P` exact petal-support patterns,
at most `n` defect degrees, and at most `n` exact background counts. Multiply
these by `(PS4)` and use `2^M<=n^(1/c_0)` to obtain `(PS5)`. If
`E_z<=C log_2 n`, then `2^E_z<=n^C`; substituting this directly in the same
aggregate gives `(PS5B)`. Thus a counterfamily must escape every fixed
logarithmic cap, which is exactly `(PS6)--(PS7)`.

Finally `(PS8)` is obtained from the bounded Plotkin-excess identity by
subtracting `4(r-1)z` from both sides. No background-subset enumeration is
introduced: the exact set is determined by the contributor's numerator.
