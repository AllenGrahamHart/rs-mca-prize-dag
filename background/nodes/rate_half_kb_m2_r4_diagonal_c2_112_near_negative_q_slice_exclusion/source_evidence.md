# Source evidence

- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_negative_qslice_locus.py`
  supplies the previously audited exact negative reconstruction on `B=0`.
- `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_negative_qslice_locus.py`
  derives the template equivalence, minor factorization, three exact
  projections, residue-field fibers, and deployed-prime saturations.
- The aligned node's `verify_audit.py` is the independent standard-library
  five-row reconstruction engine reused only by this node's audit fixtures.

The three source SHA-256 values are pinned in `verify_runner.py`. Every
load-bearing process is serial under `ramguard tiny` and a hard 60-second
bound. No Modal credit or floating-point arithmetic is used.

The current upstream draft PR `przchojecki/rs-mca#1132` at
`c2edcfa5cbfb8a41e7dea04ae1b34325c90ed5dc` proves only the aligned negative
deletion. This near-aligned extension is not imported from that packet.
