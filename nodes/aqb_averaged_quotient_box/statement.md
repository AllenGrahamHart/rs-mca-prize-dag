# aqb_averaged_quotient_box

- **status:** CONDITIONAL
- **closure:** proof

## Statement

AQB-I (Pro Brief I, verified constants): an averaged family over the c=2
quotient geometry gains at least 429,645,547 total bits over the single-word
floor at

```text
sigma* = 8,592,912,738.
```

Equivalently, the average supplies

```text
0.000390760348 bits per 2^40 fiber coordinates.
```

The finite arithmetic residue is:

```text
B_I = d*256 - 40 - log2 C(2^40, 2^39 + d)
d   = 4,296,456,369
```

with worst case at `Q = log2 q = 256`. The unamplified equality threshold

```text
Qcrit = (log2 C(2^40, 2^39 + d) + 40) / d
```

reproduces the Modal q-threshold (`Qcrit = 255.90000002...`).

## Conditional decomposition

The finite arithmetic is closed by `aqb_deficit_arithmetic`. The remaining
open predicates are:

- `aqb_c2_average_family`, now reduced to the concrete certificate payload
  `aqb_c2_family_certificate_payload`;
- `aqb_box_charge_amortization`.

## Open content

The constants are finite arithmetic. The open mathematical content is the
existence of the averaged c=2 quotient-box family achieving this gain. Do not
promote this node on constants alone.

## Falsifier

A theorem or certified model showing that c=2 quotient-box averaging cannot
amortize the box charge by 429,645,547 bits at `sigma*`.
