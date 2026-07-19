# ATTACK - aqb_box_charge_amortization

Status: conditional.

The threshold accounting is proved in
`aqb_amortization_threshold_accounting`. The active mathematical leaf is
`aqb_shared_entropy_gain`, which depends on the family certificate from
`aqb_c2_family_certificate_payload`.

Once the family is fixed, prove an entropy inequality of the form:

```text
shared_family_entropy - charged_box_entropy >= 429,645,547 bits.
```

Use `aqb_deficit_arithmetic` for the exact required bit threshold. The proof
should be an exact or interval-certified inequality; avoid floating point
knife-edge decisions.
