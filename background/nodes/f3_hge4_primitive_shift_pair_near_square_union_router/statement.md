# HGE4 primitive shift-pair near-square union router

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_primitive_shift_pair_orbit_aggregate_router`

Fix an official row, `4<=h<=H_max`, and a `2h`-subset `U` of `H=mu_n`.
Let

```text
D_U(X)=prod_(u in U)(X-u).
```

Call `U` a valid primitive near-square union if there is a monic polynomial
`S_U` of degree `h` such that

```text
S_U(X)^2-D_U(X)=d_U^2 in F_p^*                    (NSU1)
```

for a nonzero `d_U`, and the reconstructed pair of root sets of
`S_U-d_U` and `S_U+d_U` is primitive. The polynomial `S_U` is unique; changing
the sign of `d_U` only exchanges the two root sets.

The map

```text
(P,Q) -> P union Q
```

is therefore a bijection from unordered primitive top shift pairs to valid
primitive near-square unions. It replaces an `h|h` partition search by one
deterministic centered-square test on the union locator.

Let `V_h^free` count scaling orbits of valid primitive unions with trivial
union stabilizer, and let `V_h^swap` count those with stabilizer
`{1,-1}`, where `-1` exchanges the reconstructed fibers. If `O_h^prim` is
the ordered-pair orbit count from the proved orbit router, then

```text
O_h^prim=2V_h^free+V_h^swap.                       (NSU2)
```

If `A_h^union` counts distinct valid primitive unions containing `1`, then

```text
A_h^union=2hV_h^free+hV_h^swap=hO_h^prim.          (NSU3)
```

Consequently `(OAR2)` is exactly

```text
sum_(h=4)^H_max A_h^union/h<=14n^2,                (NSU4)
```

and the stronger unweighted union-orbit condition

```text
sum_(h=4)^H_max (V_h^free+V_h^swap)<=7n^2          (NSU5)
```

also implies HGE4.

The stronger per-width estimate `(PSA3)` is equivalently

```text
A_h^union<=7000h max(1,B_h).                        (NSU6)
```

A left-anchored ordered-pair scanner has

```text
binom(n-1,h-1)binom(n-h,h)
```

raw candidates. The near-square union scanner has `binom(n-1,2h-1)`, an
exact reduction factor

```text
binom(2h-1,h-1).                                   (NSU7)
```

This is a complete fixed-row generator reduction. It does not prove `(NSU4)`
or supply a uniform finite-row census.
