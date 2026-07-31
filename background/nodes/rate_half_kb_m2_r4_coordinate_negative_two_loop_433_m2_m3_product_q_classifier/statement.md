# KoalaBear m2 r4 coordinate negative two-loop 433 M2/M3 product-q classifier

- **status:** PROVED
- **scope:** cells `M2,M3` in the residual `(4,3,3)` two-loop frontier
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m1_product_q_exclusion`
- **consumer:** `rate_half_band_closure`

Put `epsilon=-1` in cell `M2` and `epsilon=+1` in cell `M3`.  Normalize

```text
M2: (k_A,k_C,k_+,k_-,k_BC)=(-1,M,1,M^2,-M^2),
M3: (k_A,k_C,k_+,k_-,k_BC)=(-M^2,M,1,M^2,-1),
(p_A,p_C,p_+,p_-,p_BC)=(-1,-c^2,b,-b,bc).        (KB43M-1)
```

Define the reciprocal sextic and three locator polynomials

```text
P_6=M^6+2M^5+7M^4-4M^3+7M^2+2M+1,
A  =2M^5+3M^4+12M^3-14M^2+18M+3,
D  =2M^5+5M^4+16M^3-2M^2+6M+5,
E  =A-8.                                           (KB43M-2)
```

Every actual common-`K` product/q packet in cell `M2` or `M3` satisfies

```text
P_6=0,
4b^2+epsilon A b+4=0,
8c+bD+epsilon E=0.                                (KB43M-3)
```

Conversely, every root of `(KB43M-3)` satisfying the original label,
signed-pair, product, and leading-support guards makes all five product
minors and the remaining squared q weld vanish.  The free `BC` deck
orientation realizes the required unsquared sign, so the five common-`K`
Vieta rows reconstruct.

Each cell therefore has at most `6*2=12` geometric common-`K` candidates.
Both interfaces are genuinely nonempty before the seven complementary
fibers are imposed; guard-passing examples are

```text
M2 over F_41: (M,b,c)=(11,10,39),
M3 over F_41: (M,b,c)=(11, 4,21).                 (KB43M-4)
```

Together with the dependency nodes, this completes the `(4,3,3)`
common-`K` classification: `X1,N2,Z1,M1` are empty, while
`X2,N1,L1,M2,M3` lie in explicit zero-dimensional ledgers with total cap
`24+12+12=48` before Galois identification.

This theorem does not impose `eta` or the six complementary source fibers,
apply the paired-product involution to a complete packet, close the
`(4,3,3)` skeleton or coordinate orientation, move an owner/payment, close
a row, or prove either Prize result.

## Falsifier

An actual `M2` or `M3` packet outside `(KB43M-3)`, failure of the converse,
or a sixth guard-compatible common-`K` cell in this skeleton.
