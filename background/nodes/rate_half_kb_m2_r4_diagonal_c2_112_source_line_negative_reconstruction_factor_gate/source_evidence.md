# Source evidence

- The parent reconstruction theorem supplies the rank-four coefficient
  matrix and the negative image-plane test.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_symbolic.py`
  performs the bounded four-variable determinant expansion after the
  endpoint normalization `a=2`. Both templates finish in under three
  seconds under the `tiny` RAMguard profile and reproduce `(KBNF-3)`.
- `verify.py` independently evaluates the original augmented determinant
  and printed rational factors on exact rational fixtures; `verify_audit.py`
  independently classifies all twelve edge assignments as `8+4`.

## Upstream custody

Pending export to the existing draft source-facet PR packet.
