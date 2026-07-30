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
`34f74fece1f9a54f73b04c31932c899465d40a89`:

```text
note blob:        d1f93e975a149dac6b9acc530dc6268a59550279
verifier blob:    6725a86eda538d38a1414ce8933cdeee67ed89e0
certificate blob: f70c6c4e8861db9231459fb5e9576943730d564
payload SHA-256:  a919a052d67da8a35bec299ffaa1b0f22974d0b543cf05cbcb09e5d504db450e
```

The pinned upstream packet predates the `A=0` admissibility correction: its
determinant identities remain valid, but its survivor report retains the
spurious fixed-point locus. Corrected upstream custody is recorded after the
replacement packet is pushed.
