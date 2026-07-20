# Claim contract

- **claim id:** `f3_h3_dsp8_unit_trace_elliptic_curve_router`
- **mathematical statement:** normalized decorated DSP8 triples are subgroup
  points on the trace cubic `(EC2)`; it is genus one off `sigma^3=27`, nodal
  genus zero on that locus, and the raw curve-pair ledger is exactly `4K=J`
- **scope:** every official H3 row; the geometric classification holds over
  any field of characteristic different from `2,3`
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependency:** the DSP8 unit-product trace normal form
- **new open content:** bound the signed-disjoint, rich, quotient-weighted
  point-pair correlation across the family `C_sigma`
- **falsifier:** a singular point outside `sigma^3=27`, a nonnodal singularity
  there, or a DSP8 record whose raw trace-curve multiplicity is not four
- **nonclaims:** no subgroup point bound, no trace-fiber flatness, no quotient
  decorrelation, and no DSP8 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_unit_trace_elliptic_curve_router/verify.py`
- **upstream mapping:** route fence for the same-`(e1,e2)` rational-conic
  guardrail; DSP8 is the same-`(e1,e3)` elliptic family instead
