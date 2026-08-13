# Cycle 257: rate-half Shape-A static-source arbitrary-drop fence (2026-08-13)

The bordered-Hankel source presentation from Cycle 255 was tested for a
source-pointwise non-stagnation theorem. That route is false in complete
generality.

For `R=d+n+2` source points and every `0<=q<=n`, choose a squarefree
degree-`d` polynomial `Q`, a degree-`n-q` polynomial `G`, and

```text
omega_x=G(x)/(Q(x)L_U'(x)).
```

All weights are nonzero. Lagrange extraction gives

```text
R_(d+1)=...=R_(d+q)=0,
R_(d+1+q)=lc(G)!=0.
```

The residue pairing

```text
sum_x omega_xP(x)S(x)
 =-sum_(Q(r)=0) G(r)P(r)S(r)/(Q'(r)L_U(r))
```

is nondegenerate on polynomials of degree below `d`, proving that the
middle Hankel matrix has exact rank `d` and no kernel beyond `Q`.
Thus every run length is compatible with all-nonzero static sources,
exact corank one, replacement minors, and bordered source determinants.

This is a route fence, not a Shape-A counterexample. A useful
non-stagnation theorem must use the global parameter-linear source pencil,
the three-class partition, the split-fiber weld, or collision geometry.

```text
start:                   9f7e6e78f
result:                  PROVED characteristic-free route fence
primary fixture:         F_101, (d,n,R)=(3,3,8), q=0,1,2,3
primary subset replay:   560 generalized-alternant terms
independent audit:       F_127, (d,n,R)=(4,2,8), q=0,1,2
hostile mutations:       6/6
manifest-aware replay:   2/2 new verifiers PASS
composed replay:         pre-existing Modal baseline row is non-PASS
                         (dli_wcl_weight5_first64_mitm_exclusion)
compute:                 constant-size local exact arithmetic; no Modal spend
critical status delta:   none; rate_half_band_crossing_location remains open
next route action:       exploit coupling across parameter values
```
