# Support-wise transverse LineRay rank charge

- **status:** PROVED
- **dependency:** `xr_all_lineray_affine_core_bound`
- **consumers:** `xr_tangent_support_mismatch_bridge`,
  `xr_highcore_collision_count`, `xr_lowcore_spread_heart`

Let `C=ker H` be a linear code of length `n` and minimum distance greater
than `r=n-A`. Fix received words `u,v`. For each retained finite slope
`z`, choose a codeword `p_z` and put

```text
e_z=u+zv-p_z,       E_z=supp(e_z),       S_z=D\E_z.
```

Assume `wt(e_z)<=r` and that `(p_z,S_z)` is support-wise MCA-nontrivial:
there is no codeword pair `(c_0,c_1)` which agrees with `(u,v)` on this same
set `S_z`. Then the LineRay transversality condition holds pointwise:

```text
{Hu,Hv} is not contained in H(F^E_z).                 (TR)
```

Consequently any set containing one selected error above every retained
slope satisfies the selector form of the proved all-LineRay affine-core
bound. If `sigma` is the minimum affine rank of such a selector, then

```text
# retained slopes <= C(sigma+r,sigma).                 (SWLR)
```

This conclusion is support-local. It remains valid when `(u,v)` has a joint
codeword-pair explanation on some other `A`-support, so it applies directly
to the support-mismatch population.

At all six XR rows, `sigma<=3` costs less than `8n^3`. Against the full
`16n^3` mismatch reserve, `sigma=4` is additionally paid at RowC rate
`1/4`:

```text
C(767,4)=14,307,629,505 < 16*1024^3=17,179,869,184.
```

Therefore any counterexample to P-A2's combined support-mismatch clause has
minimum selector rank at least five at RowC rate
`1/4`, and at least four at the other five rows. The theorem does not pay
those higher-rank families.
