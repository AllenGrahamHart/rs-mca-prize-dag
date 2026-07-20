# DSP8 disjoint distance-six multiplicity gate

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_excess_multistar_degree_ladder`,
  `f3_h3_distance_four_fiber_degree_cap`,
  `f3_h3_distance_six_support_overlap_payment`

Fix a DSP8 product target `t!=0,1` with `P(t)>=25`, and let `m` be the
number of its unordered squared-norm-at-most-three representations. Write
`D_6(t)` for the number of generic--generic squared-distance-six edges whose
signed supports are disjoint. If `t` is antipodal-free, then

```text
D_6(t)>=D_0(m):=ceil(m(m-4)/2)-2m-6.               (DSM1)
```

If `t` is antipodal, then

```text
D_6(t)>=D_A(m):=ceil(m(m-2)/2)-4(m-1)-8.           (DSM2)
```

Every retained target has `m>=11`. Consequently

```text
D_6(t)>=11  on the antipodal-free class,
D_6(t)>=2   on the antipodal class.                 (DSM3)
```

In the first class, the disjoint distance-six graph contains a two-leaf
star. In the second class it contains two distinct edges, not necessarily
incident. Put `O=Z[zeta_n]`, `pi=1-zeta_n`, and let `beta_E` be the shifted
product represented by `E`. The corresponding normalized ideals are

```text
K_0=((beta_F-beta_E)/pi^2,
     (beta_G-beta_E)/pi^2),                         (DSM4)

K_A=((beta_F-beta_E)/pi^2,
     (beta_J-beta_G)/pi^2,
     (beta_G-beta_E)/pi^2),                         (DSM5)
```

where `E--F,E--G` are distinct disjoint distance-six edges for `K_0`, and
`E--F,G--J` are any two distinct such edges for `K_A`. The centers `E,G` in
`(DSM5)` may coincide. In either case the official row prime divides the
ideal norm.

On the separate `P(t)>=33` tail, the disjoint distance-six graph has a center
of degree at least seven in the antipodal-free class and at least five in the
antipodal class. Thus that tail admits pure disjoint-distance-six multistar
ideals with respectively seven and five leaves.

This is a necessary candidate sieve. It does not bound the number of ideal
norm prime divisors, their survivors, or the quotient weight `R(t)`.
