# Audit

- The moment maximizer is universal over all positive 64-tuples with the two
  printed moments; no cyclotomic shape is assumed.
- Monotonicity in `V` makes the 62 exact comparisons at `V=6` cover every
  larger feasible variance.
- The `V=2` Lucas remainder is recomputed from the recurrence.
- At `V=4`, integer energy forces exactly two signed unit lags.
- The valuation-one filter `d+e` odd is checked before canonicalization.
- All 128 primitive roots modulo `769` and all signed lag pairs are screened;
  640 hits map to five and only five Galois types.
- The verifier constructs `C_64` from its recurrence and recomputes each norm
  as a 64-dimensional exact multiplication determinant using only the Python
  standard library.
- The result uses the field interval, not probable-prime tests.

