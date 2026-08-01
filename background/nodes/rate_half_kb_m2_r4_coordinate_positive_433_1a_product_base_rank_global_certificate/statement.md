# KoalaBear m2 r4 positive 433-1a global product-base rank certificate

- **status:** PROVED
- **scope:** all fifteen common matching cells of the positive route
  `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_five_orbit_exclusion`
- **consumer:** `rate_half_band_closure`

The five common product rows have rank five on every admissible deployed-
field point in all fifteen matching cells.  Consequently the six-row base
`B`, obtained by adjoining the loop sum row, has rank six globally.  The
base-rank-drop branch of the positive route `433-1a -> O0b` is empty.

The five-orbit parent handles `[0]`, `[4,7]`, `[5,8]`, `[11]`, and `[14]`.
For `[3,6]`, put `R=r^2,T=t^2` and

```text
U=-R^2-3RT+3R+T,       V=-R^2+RT-R+T.
```

Two stripped maximal minors are

```text
D_1=(b+c^2)(bU+cV),
D_4=-(b+c^2)(bV+cU)/3.                             (KBPBG-1)
```

Away from `b=-c^2`, their residual determinant is

```text
U^2-V^2=8R(T-1)(R-1)(R+T),                        (KBPBG-2)
```

a nonzero guard product.  On `b=-c^2`, another maximal minor is a nonzero
scalar times

```text
(T-1)R^2c^3(c+1).                                 (KBPBG-3)
```

For the remaining representatives `1,9,12`, let `D_0,...,D_5` be the six
guard-stripped product minors in variables `b,c,R,T`, and put

```text
H=RTbc(b-1)(b+1)(c-1)(c+1)(b-c)(b+c)
  (R-1)(R+1)(T-1)(T+1)(T-R)(T+R).                 (KBPBG-4)
```

Exact Singular computation over `F_2130706433` gives

```text
<D_0,...,D_5,zH-1> = <1>                          (KBPBG-5)
```

for each of cells `1,9,12`.  The duplicate-role involution transports these
certificates to cells `2,10,13`.  The replay run prints `UNIT`, basis size
one, and first basis element one for all three inputs; canonical input and
equation hashes are stored in the result JSON.

This theorem does not solve any principal three-minor chart, append outside
rows, delete `433-1a -> O0b`, close positive coordinate parity, close K3 or
a Prize row, or prove either Prize result.

## Falsifier

An admissible point in any matching cell with product rank below five, a
failed identity `(KBPBG-1)--(KBPBG-3)`, or a replay of `(KBPBG-5)` whose
canonical input hashes match but whose reduced basis is not `[1]`.
