# KoalaBear positive 433-1a cell-0 generic signed-pair orbit exclusion

- **status:** PROVED
- **scope:** all four root-sign rows in common matching cell `0` over the
  deployed field, both cycle signs and every outside case
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell0_common_lex_rational_witness`
- **consumer:** `rate_half_band_closure`

For the representative signs `(-1,-1)`, the cell-0 lex basis has exactly
two branches

```text
b=1547071505 or 583634934,
r=-16711679 t^2,
c=C_b(t).                                           (KBC0P-1)
```

On each branch the numerator and denominator of `C_b(t)` are coprime. The
unique common coefficient kernel reduces, after cancelling the common
nonzero projective scale

```text
t^6(t^4-1)^2 / D_b(t)^3,                           (KBC0P-2)
```

to eight polynomials of degree at most eight in `t`. In particular

```text
B_1(W)=k_b (t^2-1)(t^4+1)(t^2-W),                 (KBC0P-3)

k_1547071505=234633685,
k_583634934=759420084,
```

up to one common nonzero scalar. The exact normalized `A_2,A_0,B_1`
coefficients are sealed in the reduction packet.

For arbitrary proposed source roots `z_0,z_1`, put

```text
D_j=A_2(z_j^2),  N_j=A_0(z_j^2),
Q_j=z_j B_1(z_j^2).                                (KBC0P-4)
```

If those roots carry the target records `DE+=de` and `DE-=-de`, with
unsquared target sums `d+e` and `d-e`, then necessarily

```text
N_1D_0+N_0D_1=0,
Q_0^2D_1^2-Q_1^2D_0^2-4N_0D_0D_1^2=0.            (KBC0P-5)
```

For each branch, saturate `(KBC0P-5)` by the common-parameter guards,
`D_0D_1`, nonzero and distinct outside labels, and exclusion of all five
common labels. Exact Singular standard bases give

```text
<KBC0P-5, uG-1>=<1>                                (KBC0P-6)
```

on both branches. Every complete outside packet contains nonzero `DE+`
and `DE-` records at distinct source labels and has `D_0D_1!=0`, so
`(KBC0P-6)` excludes every outside case and both cycle signs. Exact source
projectivities transport this exclusion through all four cell-0 sign rows.

Therefore the cell-0 root-sign orbit is empty. Six common symmetry
representatives covering 40 raw rows remain:

```text
[3,6], [4,7], [9,10], [11], [12,13], [14].
```

This does not delete those six orbits, close the positive route, K3, a
Prize row, LIST, or MCA.

## Falsifier

An uncovered cell-0 common branch, a zero projective scale or `A_2` value
in an actual packet, an actual `DE+/DE-` lift violating `(KBC0P-5)`, or a
nonunit saturated branch ideal.
