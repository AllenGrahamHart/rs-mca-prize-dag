# Source evidence

- The parent reconstruction theorem supplies the rank-four coefficient
  matrix and the negative image-plane test.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_symbolic.py`
  performs the bounded four-variable determinant expansion after the
  endpoint normalization `a=2`. Both templates finish in under three
  seconds under the `tiny` RAMguard profile and reproduce `(KBNF-4)`.
- `verify.py` independently evaluates the original augmented determinant
  and printed rational factors on exact rational fixtures, verifies that
  `A=0` forces `z=-1`, and retains distinct-label witnesses on `B=0` and
  `C=0`; `verify_audit.py` independently classifies all twelve edge
  assignments as `8+4`.

## Upstream custody

The theorem is vendored into the diagonal source-facet packet in draft PR
`przchojecki/rs-mca#1132` at commit
`fa40cba826cde6d6650be907eb678e35bece301c`:

```text
note blob:        de2af755db29db4690eef20beb189e695a6e123a
verifier blob:    a01b25d3d61c03f59a4e229ed646ad4b1c692784
certificate blob: 644f2d186880cb411117ed3aa8a6a40a96d54b55
payload SHA-256:  14fed959f081050228575a4b1d16b027c4343e330ae45872982862e6ad58e6bf
```

The upstream standard-library replay checks four generic determinant
fixtures, excludes the apparent `A=0` locus, retains distinct-label witnesses
on `B=0` and `C=0`, and rejects `124` of `124` hostile mutations. The
correction report is PR comment `5132360554`.
