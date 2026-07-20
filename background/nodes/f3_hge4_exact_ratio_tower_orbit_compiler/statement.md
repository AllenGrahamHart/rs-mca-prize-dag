# HGE4 exact-ratio tower orbit compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:**
  `f3_hge4_primitive_shift_pair_orbit_aggregate_router` and
  `f3_hge4_nonfull_near_square_straight_line_lift`

Fix an official row `(n,p)`, with `n=2^s`, and a width `h>=4`. For an
ordered primitive top shift pair `(P,Q)` in `mu_n`, define its ratio subgroup

```text
G(P,Q)=<xy^(-1): x,y in P union Q>=mu_m.             (ERT1)
```

Its order `m` is a dyadic divisor of `n`, is invariant under scaling, and
satisfies `m>=2h`. Let `E_h^prim(m,p)` count scaling orbits of ordered
primitive top shift pairs in `mu_m` whose ratio subgroup is exactly `mu_m`.
Then

```text
O_h^prim(n,p)=sum_(m|n, m>=2h) E_h^prim(m,p).        (ERT2)
```

This is a bijective decomposition, not an inequality. If `C_h^prim(m,p)`
counts its left-anchored presentations, then

```text
C_h^prim(m,p)=h E_h^prim(m,p).                       (ERT3)
```

Consequently the levelwise estimate

```text
sum_(h=4)^floor(m/2) E_h^prim(m,p)<=(21/2)m^2        (ERT4)
```

for every `m|n` implies

```text
sum_(h=4)^H_max O_h^prim(n,p)<14n^2,                (ERT5)
```

and hence the HGE4 norm-gate target. Equivalently, the left-anchored target
at level `m` is

```text
sum_(h=4)^floor(m/2) C_h^prim(m,p)/h<=(21/2)m^2.     (ERT6)
```

There is an exact near-square implementation of each level. Write

```text
D=S^2-a^2,          deg S=h, S monic.
```

The left-anchored exact-level non-full locus is the projection of

```text
D | X^m-1,
S(1)-a=0,
sum_(j=1)^(h-1) z_j s_j=1,
D does not divide X^(m/2)-1.                         (ERT7)
```

In the repeated-squaring presentation, the last two divisor conditions are
exactly `V_r=1` and `V_(r-1)!=1`, where `m=2^r`. The latter is encoded without
case splitting by a coefficient selector for `V_(r-1)-1`. If
`C_hat_h(m,p)` counts base pairs `(S,a)` in this projected locus, without
counting selector witnesses, then

```text
C_h^prim(m,p)<=C_hat_h(m,p).                         (ERT8)
```

Thus `(ERT6)` remains sufficient with `C_hat_h` in place of `C_h^prim`.
No estimate `(ERT4)` or `(ERT6)` is proved here.
