# dependency sub-DAG: aqb_averaged_quotient_box

Edges are directed from dependency to consumer.

```text
aqb_deficit_arithmetic
    -> aqb_averaged_quotient_box
    -> rate_half_band_closure

aqb_family_certificate_semantics [PROVED]
    -> aqb_c2_average_family [CONDITIONAL]
    -> aqb_averaged_quotient_box
    -> rate_half_band_closure

aqb_c2_family_certificate_payload [TARGET]
    -> aqb_c2_average_family [CONDITIONAL]
    -> aqb_averaged_quotient_box
    -> rate_half_band_closure

aqb_box_charge_amortization
    -> aqb_averaged_quotient_box
    -> rate_half_band_closure

aqb_c2_average_family [CONDITIONAL]
    -> aqb_box_charge_amortization

aqb_amortization_threshold_accounting [PROVED]
    -> aqb_box_charge_amortization

aqb_c2_average_family [CONDITIONAL]
    -> aqb_shared_entropy_gain_payload [TARGET]
    -> aqb_shared_entropy_gain [CONDITIONAL]
    -> aqb_box_charge_amortization

aqb_entropy_ledger_certificate_soundness [PROVED]
    -> aqb_shared_entropy_gain [CONDITIONAL]
```

## Status

- `aqb_averaged_quotient_box`: CONDITIONAL.
- `aqb_deficit_arithmetic`: PROVED by the Robbins-interval verifier.
- `aqb_family_certificate_semantics`: PROVED.
- `aqb_c2_family_certificate_payload`: TARGET.
- `aqb_c2_average_family`: CONDITIONAL.
- `aqb_box_charge_amortization`: CONDITIONAL.
- `aqb_amortization_threshold_accounting`: PROVED by the same
  Robbins-interval finite-deficit verifier.
- `aqb_entropy_ledger_certificate_soundness`: PROVED.
- `aqb_shared_entropy_gain_payload`: TARGET.
- `aqb_shared_entropy_gain`: CONDITIONAL.

The constants and threshold comparison are closed; the averaged family and its
concrete net shared entropy ledger are not.
