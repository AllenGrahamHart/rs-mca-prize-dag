# CORRECTION C25-5 (2026-08-09, coordinator-applied on round-25 replay)

`official_scale.json` line 83 prints:

    "exceeds_2^21_iff": "256 - log2 q < 107/2^33 = 1.24556e-05"

The FRACTION `107/2^33` is correct; the DECIMAL is wrong by 10^3
(and its digits are slightly off). True value:

    107/2^33 = 1.245644e-08

Every formula in the packet uses the fraction, so no downstream
number changes. The banked JSON is left verbatim per the
verbatim-artifact rule; this sidecar is the correction of record.
Discovered by round-25 pilot c2pp_falsifier_redesign (catch C25-5),
independently confirmed by the coordinator
(python3: 107/2**33 = 1.245644e-08). The same pilot's analytic law
explains the constant: 107 = e - 21 = 128 - 21 exactly.
