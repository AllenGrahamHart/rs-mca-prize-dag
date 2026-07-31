# KoalaBear m2 r4 coordinate negative two-loop 433 constrained outside-product compiler

- **status:** PROVED
- **scope:** every exact `X2,N1,L1` common-`K` candidate
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate`,
  and `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`
- **consumer:** `rate_half_band_closure`

Put `b=-c^3`.  The two complete antipodal pairs, remaining singleton, and
missing mate in the label involution are

```text
cell  known product pairs       singleton (label,product)  xi
X2    (-1,-b), (-c^2,bc)       (1,b)                      -1
N1    (-1,b),  (-c^2,bc)       (M^2,-b)                   -M^2
L1    (-c^2,bc),(b,-b)         (L,-1)                     -L. (KB43W-1)
```

The common-`K` Mobius map forces the product at `xi` to be

```text
X2: p=P_X/22,
 P_X=-2M^3c+3M^3-16M^2c+24M^2+6Mc-9M-36c+32;

N1: p=P_N/22,
 P_N=2M^3c+3M^3+16M^2c+24M^2-6Mc-9M+36c+32;

L1: p=(3c^2+10)/8.                              (KB43W-2)
```

Crossing the two known pair rows gives the product involution

```text
Gamma yz-Alpha(y+z)-Beta=0,                      (KB43W-3)

X2:
 Gamma=c^3+c-1,
 Alpha=-c^3(c^2-c+1),
 Beta=c^5(c^3-c^2-1);

N1:
 Gamma=c^3+c+1,
 Alpha=-c^3(c^2+c+1),
 Beta=-c^5(c^3+c^2+1);

L1:
 Gamma=-c^2(c^2+1),
 Alpha=2c^6,
 Beta=c^8(c^2+1).                                (KB43W-4)
```

In deployed characteristic, `b,c,p,Gamma,Alpha,Beta` and
`Alpha^2+Gamma Beta` are units on every exact ledger.  Thus the forced
product is finite and nonzero and the involution is nonsingular.

The universal complete-edge classifier gives the same outside multiset

```text
{bD,cE,tau DE,DF,-DF,EF,-EF},       tau=+/-1.    (KB43W-5)
```

Consequently `p` lies in one of five canonical forced types
`bD,cE,tau DE,DF,EF`.  The constrained complete-product frontier consists
of exactly `3 cells x 2 tau x 5 types = 30` cells.

This theorem does not delete one of those cells, impose complete product
matching or interpolation, close the `(4,3,3)` skeleton or coordinate
orientation, close a Prize row, or prove either Prize result.

## Falsifier

A guarded constrained packet with a different missing mate or forced
product, a singular printed involution, or a complete outside packet not
routed through the 30 cells.
