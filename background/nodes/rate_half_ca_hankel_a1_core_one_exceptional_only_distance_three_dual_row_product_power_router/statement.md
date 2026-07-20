# `A=1` core-one distance-three dual row-product power router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_boundary_root_unity_router`

Retain the pair-Lagrange generator and exact external split design. Put

```text
r=2e+1,       |C|=6e+3=3r,
Z_ext={the 3e external slopes},
P_Z(z)=product_(gamma in Z_ext)(z-gamma).             (DRP1)
```

Here `C(X)` is the monic locator of the active outside rows. For every root
`x` of `C`, write `Q_x(z)=Q(z;x)` and let `l_x` be its leading coefficient.
Then `Q_x` has degree exactly `e`, its roots are the `e` external blocks
containing `x`, and

```text
product_(C(x)=0) Q(z;x)=L P_Z(z)^r,
L=product_(C(x)=0) l_x !=0.                           (DRP2)
```

For an internal slope `xi_i`, matched pair
`D_i=(X-a_i)(X-b_i)`, and internal scalar `lambda_i`, define

```text
R_i=product_(C(x)=0) B(x)/D_i(x).
```

Evaluation of `(DRP2)` at `0` and `xi_i` gives the exact identity

```text
R_i=
 (P_Z(xi_i)/(lambda_i^3 P_Z(0)))^r.                  (DRP3)
```

In particular, every matched pair passes the support-only gate

```text
R_i in (F_q^*)^r.                                     (DRP4)
```

It can be evaluated without constructing `C` at official degree:

```text
R_i=Res(C,B)/Res(C,D_i)
   =-product_(t in T)C(t)/(C(a_i)C(b_i)),             (DRP5)

C(y)=P_X'(y)/(A(y)B'(y))             (y in T),
C(y)=P_X'(y)/(A'(y)B(y))             (y in R_A),
P_X'(y)=N y^(-1)/((y-s)(y-x_0)).                      (DRP6)
```

If `g_r=gcd(r,q-1)`, the finite-field test is

```text
R_i^((q-1)/g_r)=1.                                    (DRP7)
```

At the official distance-three parameters,

```text
e=2^38-1=3*174763*524287,
r=2^39-1=7*79*8191*121369,       gcd(e,r)=1.          (DRP8)
```

Thus the existing `e`th-root boundary labels and the new `r`th-power
residues involve disjoint prime-order field strata. If `gcd(e,q-1)=1`, the
former labels must equal one. If `g_r=1`, `(DRP4)` is automatic; otherwise
`(DRP7)` is a genuine power-residue obstruction.

The dual product and residue gates are necessary, not sufficient for an
external split design.
