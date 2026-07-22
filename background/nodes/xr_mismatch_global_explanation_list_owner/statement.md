# XR mismatch global-explanation list owner

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependencies:** `xr_mismatch_accumulated_locator_flag_normal_form`,
  `xr_true_tangent_coordinate_injection`,
  `list_subsqrt_interleaving_collapse`

Let `C` be the original length-`n` code and fix agreement `A>K`. For a
received pair `(u,v)`, let

```text
E_A(u,v)={(c_0,c_1) in C^2:
          #{i:u_i=c_0(i) and v_i=c_1(i)}>=A},
E=|E_A(u,v)|.                                          (GEO1)
```

Fix the initial explanation used by the XR mismatch descent, and process any
set of retained mismatch slopes with deterministic choices. Let `Z_tan` be
the slopes whose first terminal payment in this descent is a genuine tangent
to a lifted explanation pair. Then

```text
|Z_tan|<=(n-A)max(E-1,0).                              (GEO2)
```

Thus recursive depth and repeated appearances of one explanation do not
multiply the tangent currency. Every such slope is owned once by one distinct
nonroot member of the original common-support pair list.

Let

```text
L_A=max_w #{c in C:agr(c,w)>=A},       q=|F|.           (GEO3)
```

The pair list in `(GEO1)` is a two-fold common-support interleaved list.
Consequently, if `1<=L_A<q`, then

```text
E<=floor(L_A(q-1)/(q-L_A)),                            (GEO4)
```

and if `L_A^2<q`, then

```text
E<=L_A,
|Z_tan|<=(n-A)(L_A-1).                                (GEO5)
```

In particular, under `L_A^2<q`, the terminal tangent currency fits the whole
XR residual slot whenever

```text
L_A<=1+floor(16n^3/(n-A)).                             (GEO6)
```

The simpler `L_A<=n^2+1` spends strictly less than `n^3` because `A>0`.
This theorem does not prove either list bound, aggregate slopes terminating
on generic canonical charts, or close the mismatch bridge.
