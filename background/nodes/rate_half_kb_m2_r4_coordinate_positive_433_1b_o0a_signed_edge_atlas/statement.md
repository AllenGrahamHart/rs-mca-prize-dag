# KoalaBear m2 r4 positive 433-1b/O0a signed-edge atlas

- **status:** PROVED
- **scope:** the saturated-defect positive residual route
  `433-1b -> O0a`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard` and
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`
- **consumer:** `rate_half_band_closure`

Name the common target pairs `A,B,C`, with common degrees `(4,3,3)`, common
loop `A`, and common multiplicities

```text
l=(1,0,0),             m_AB,m_AC,m_BC=(1,1,2).    (KBP1BA-1)
```

The loop costs one defect unit.  Since the route has total defect three,
the two `BC` records have opposite signed types.  Normalize the common
records to

```text
-a^2;  ab, ac;  bc,-bc.                           (KBP1BA-2)
```

The outside graph `O0a` has

```text
r=(0,0,2),             l=(0,0,0),
m_DE,m_DF,m_EF=(3,1,1).                            (KBP1BA-3)
```

Normalize its two colored incidences to `B-F,C-F`.  Its multiplicity-three
`DE` pair must split `2+1` between signed types, costing the remaining two
defect units.

After target-representative sign gauge, the seven active signs lie on

```text
AB, AC, BF, CF, DE, DF, EF.
```

The graph is connected with cycle rank two.  Its exact invariants are

```text
sigma_c=sign(AB BF CF AC),
sigma_o=sign(DE DF EF),       (sigma_c,sigma_o) in {+1,-1}^2. (KBP1BA-4)
```

Gauge-normalizing the spanning-tree signs gives the twelve target-product
records

```text
common:  -a^2; ab,ac; bc,-bc;
colored: bf, sigma_c cf;
outside: de,de,-de; df, sigma_o ef.                (KBP1BA-5)
```

Thus the 128 raw active-sign assignments form exactly four gauge orbits of
size 32.  Each orbit supplies one complete twelve-row product/squared-sum
lane for the Vieta compiler.

This theorem does not assign source fibers, impose a coefficient kernel,
prove a lane realizable or empty, close another route, K3, LIST, MCA, or
either Prize result.

## Falsifier

An actual `433-1b -> O0a` packet outside `(KBP1BA-5)`, an extra gauge
invariant, or failure of the displayed target degrees or defect count.
