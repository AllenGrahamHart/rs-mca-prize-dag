# M31 top-neighbor core-shadow payment

- **status:** PROVED
- **closure:** proof
- **requires:** `l1_m31_rank7_dense_top_decorated_shift_pair_router`,
  `upstream_gfv4_affine_span_list_compiler`
- **route context:** `l1_m31_fixed_support_divisor_direction_cap_route_cut`

Use the combined-domain M31 constants

```text
N=1053557,  k=4981,  t=k-1=4980,
m=72428,    w=m-k=67447.
```

Fix an exact-weight listed anchor `a_0`, and let `S_0` be its agreement
support. For every top neighbor `a_j`, write

```text
a_j-a_0=c_j J_j,
```

where `c_j` is nonzero and `J_j` is the monic degree-`t` locator of
`S_0 intersect S_j`.

For `0<=r<=t`, fix a monic degree-`t-r` divisor `R` of the anchor locator.
Then the number of top neighbors whose `J_j` is divisible by `R` is at most

```text
B_r=floor(C(N-k+r+1,r+1)/C(w+r+1,r+1))-1.          (CS1)
```

In particular,

```text
B_0=14,                    B_1=240.                 (CS2)
```

Thus the one-root-swap family above any fixed degree-`4979` core contains at
most `240` actual top neighbors, even though the corresponding support-only
plane can contain `67449` abstract divisor directions.

If an anchor has `d` top neighbors and `Sh_(t-r)` is the set of degree-`t-r`
core divisors occurring in their directions, then

```text
|Sh_(t-r)| >= ceil(d C(t,r)/B_r)                    (CS3)
```

whenever `B_r>0`. At the forced degree `d>=215793`, the codimension-one
shadow therefore satisfies

```text
|Sh_4979| >= ceil(215793*4980/240)=4477705.          (CS4)
```

## Scope

This is an actual-list payment, not support-only geometry: all words lie in
one affine RS flat and agree with one received table. It does not bound the
number of different cores, sum the core payments without overlap, prove the
local cap `215792`, or close the `Q=147595` terminal.
