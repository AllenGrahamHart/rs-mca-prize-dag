# XR low-core `u=0` loop-defect ratio router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_lowcore_spread_heart`
- **dependency:** `xr_rank_five_extension_list_reduction`

Use the RowC rank-five P-B reduction with `u=0` and `v>=1`. Put

```text
B=8n^3,       N=R+4,       m=4+h+v,       B_v=B+1-v.
```

If a selected family has more than `B` slopes, delete the `v` kernel-loop
coordinates and every selected member agreeing at one of them. At most `v`
members are deleted. The retained family has at least `B_v` members on an
`N`-point domain, its kernel is `GRS_4`, every member has an actual agreement
set of size at least `m`, and two such sets intersect in at most `3+v` points.

Fix a four-set `T` contained in the actual agreement sets of two retained
members. For the normalized extension direction `q` and received word `U`,
let

```text
d_T=q-I_T q,       a_T=U-I_T U,
```

where `I_T` is degree-less-than-four interpolation on `T`. If `A_gamma` is
the actual agreement set of the member at slope `gamma`, then

```text
a_T(x)=gamma d_T(x)                    for x in A_gamma.       (LR1)
```

Moreover,

```text
#{x in A_gamma\T : d_T(x)=0} <= v-1.                         (LR2)
```

Consequently every retained member through `T` contributes at least `h+1`
points to the defined ratio fiber

```text
Phi_T(x)=a_T(x)/d_T(x)=gamma,
```

and distinct slopes contribute disjoint fibers. Hence the exact reused-core
line cap is

```text
#members through T <= floor(R/(h+1)).                         (LR3)
```

There is also a complete rich-core interface. Choose exactly `m` agreement
points for each retained member. For `r>=2`, put

```text
D_r=C(m,4)-floor((r-1)C(N,4)/B_v).                            (LR4)
```

Whenever `D_r>0`, some nonempty retained subfamily has every member incident
to at least `D_r` four-cores of multiplicity at least `r` inside that
subfamily. In particular, an over-budget family is impossible if

```text
r>floor(R/(h+1))       and       D_r>0.                       (LR5)
```

This is an arbitrary-`v` structural router. It extends the denominator part
of the one-loop GRS reduction, but it does not by itself pay the currently
residual values `v<=1,2,6` on the three RowC rates.
