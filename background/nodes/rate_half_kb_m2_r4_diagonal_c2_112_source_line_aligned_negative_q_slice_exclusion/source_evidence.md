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
