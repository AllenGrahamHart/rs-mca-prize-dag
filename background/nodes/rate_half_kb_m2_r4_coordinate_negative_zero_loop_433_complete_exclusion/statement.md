# KoalaBear m2 r4 coordinate negative zero-loop 433 complete exclusion

- **status:** PROVED
- **scope:** every complete negative zero-loop `(4,3,3)` packet over the
  deployed field `F_(2130706433^6)`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_vieta_exclusion_router`
- **consumer:** `rate_half_band_closure`

The four residual product-complete lanes

```text
12/Z2,       12/Z3,       13/Z2,       14/Z2       (KBZ433X-1)
```

are empty.  Every isolated guarded Smith solution fails the first outside
squared-sum row.  For each collision-free rank-deficient product system,
let `I_fam subset F_p[D,E,F]` be its exact binomial ideal and let
`R_0,...,R_6` be the cleared outside squared-sum residuals.  Exact
Groebner reduction gives

```text
12/Z2:             I_fam+<R_0>       =<1>;
12/Z3:             I_fam+<R_0,R_1>   =<1>;
13/Z2 and 14/Z2:   I_fam+<R_0,R_1,R_2>=<1>.       (KBZ433X-2)
```

Across all distinct product rows, `(KBZ433X-2)` consists of 384
family/common-record unit-ideal certificates.  It holds over the algebraic
closure of `F_p`, so it excludes every value of the free multiplicative
parameter, not merely sampled extension exponents.

Together with the parent router, no complete negative zero-loop 433 packet
exists.

This theorem does not exclude another common degree profile or parity,
close the coordinate orientation, move an owner/payment, close a Prize row,
or prove either Prize result.

## Falsifier

A complete negative zero-loop 433 packet, a nonunit ideal in one of the 384
printed family/common-record routes, or a guarded isolated Smith solution
passing all seven outside squared-sum rows.
