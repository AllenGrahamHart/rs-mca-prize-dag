# XR quotient image descends to remainder-one tangent boundaries

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependency:** `xr_threshold_quotient_image_lcm_normal_form`

Let `C=RS[F,D,k]`, let `D` be partitioned into fibers of size `c|n`, and
assume `A>=k+1`. For `B=mc+s`, `0<=s<c`, let `S_c(B)` be the supports made
from `m` complete fibers and `s` residual points outside those fibers.

For a received line `u+Zv`, let `Q_c(B)` be the distinct finite slopes having
a support-wise noncontained explanation on some support in `S_c(B)`, and put

```text
Q_c(>=A)=union_(B=A)^n Q_c(B).                         (QRD1)
```

Define the remainder-one boundary set `T_c(A)` as follows. A slope belongs to
`T_c(A)` when, for some `B>A` with `B=mc+1`, it is noncontained and explained
on

```text
S=S_0 union {x},
```

where `S_0` is a union of `m` complete fibers and `(u,v)` is simultaneously
explained on `S_0`.

Then

```text
Q_c(>=A)=Q_c(A) union T_c(A).                          (QRD2)
```

Moreover every member of `T_c(A)` is a genuine tangent factor: if
`(c_0,c_1)` explains `(u,v)` on `S_0` and `p_z` explains `u+zv` on `S`, then

```text
p_z=c_0+z c_1
```

globally, while `x` is a discrepancy coordinate of `(c_0,c_1)` satisfying
the tangent cancellation.

Equivalently, the threshold-union radical lcm from
`xr_threshold_quotient_image_lcm_normal_form` has no new factors away from
the exact-`A` quotient image and the remainder-one tangent boundary.

The theorem does not bound the boundary tangent image, prove first-match
coverage, aggregate generic charts, or close XR.
