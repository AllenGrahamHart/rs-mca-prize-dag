# Source evidence

- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_negative_qslice_locus.py`
  reconstructs each normalized template directly from a `3 x 3` exact
  system, verifies the unused forced row, forms the two residual quadratics
  over `QQ(c,d,w)`, and reproduces `(KBNA-1)--(KBNA-2)`. Each template
  finishes in under thirty seconds under the `tiny` RAMguard profile.
- `verify.py` checks the exact factor-locus symmetry, denominator router,
  coefficient contradiction, DAG dependencies, and scope fences.
- `verify_audit.py` independently reconstructs both templates with only
  standard-library rational arithmetic and checks the two mismatch identities
  on disjoint generic and `cd=-1` fixtures.
- The optional `--eliminate` audit also obtains
  `Res_w(N_1,N_3)=21233664*c^6*(c-1)^6*(c+1)^6`; this resultant is not used
  in the proof.

No remote computation or floating-point arithmetic is used.

## Upstream custody

The theorem is vendored into the diagonal source-facet packet in draft PR
`przchojecki/rs-mca#1132` at commit
`c2edcfa5cbfb8a41e7dea04ae1b34325c90ed5dc`:

```text
note blob:        cc315015998cf9ab0ecf2970c13f1e27f1f132d6
verifier blob:    e810f286d5b67d19660c3c382501a690e3e76fb0
certificate blob: 844b7885620bf10fe19336f3acd7866cf1d9a204
payload SHA-256:  8f768cfded349dc3dd40cf6214ffe980c69ff18ae2d8c209e63b4307767429d2
```

The upstream standard-library replay solves the full `5 x 4` system on the
special locus, checks eight admissible exact fixtures, and rejects `129` of
`129` hostile mutations. The extension report is PR comment `5132707876`.
