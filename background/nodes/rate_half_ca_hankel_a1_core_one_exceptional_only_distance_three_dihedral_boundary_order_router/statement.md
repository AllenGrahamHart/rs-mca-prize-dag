# `A=1` core-one distance-three dihedral boundary-order router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_mobius_subgroup_reduction`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_matching_free_boundary_power_router`

Retain either surviving rank-two dihedral matching. Put

```text
e=2^38-1=3*174763*524287,
N=8e+8=2^41,
g=gcd(e,p-1),
F(X)=(X-s)(X-x_0)B(X)^4.                            (DBO1)
```

## Antipodal matching

If every pair is `{a,-a}`, then necessarily

```text
g in {e/3,e}.                                        (DBO2)
```

## Constant-product matching

If every pair is `{a,c/a}` for one `c in mu_N`, then `(DBO2)` also holds.
The only apparent constant-map alternative would require

```text
F_c(X)=X^14 F(c/X) is proportional to F(X).          (DBO3)
```

The exceptional alternative `(DBO3)` is exactly the boundary-divisor
symmetry

```text
{s,x_0} is invariant under x |-> c/x,
T is invariant under x |-> c/x.                     (DBO4)
```

Because the two boundary classes are disjoint, `(DBO4)` has the exact orbit
normal form

```text
c=s x_0 is a square in mu_N,
T={u,t,c/t},       u^2=c,       t^2!=c.              (DBO5)
```

But the triple boundary-power gate then gives

```text
(u/t)^(3e)=1,                                        (DBO6)
```

which contradicts `gcd(3e,N)=1` and `t!=u`. Thus `(DBO3)` is empty.

Thus the complete rank-two branch is reduced to the two high-order field
strata `g=e/3` and `g=e`. This theorem does not exclude those retained cases.
