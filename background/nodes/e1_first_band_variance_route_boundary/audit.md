# Audit

## Provenance

- upstream repository: `przchojecki/rs-mca`
- upstream PR: `#1110`
- immutable head: `52775686c8f181c08d36de66d3ce0d3b556f8d74`
- harvested: `2026-07-27`
- classification: proved route cut, tool-relative

The three upstream packet files are vendored byte-for-byte under `upstream/`
and pinned in `source_pin.json`.  The upstream verifier passes from the
vendored layout.  It uses exact `Fraction` arithmetic, 40-term logarithm
intervals, two-sided threshold checks, and two hostile mutations.

`verify_audit.py` is an independent implementation.  It does not import the
upstream verifier, uses a different 53-term truncation, reconstructs all form
coefficients and derivatives, checks all six thresholds and all 24 dead even
levels, and repeats two structural mutations.

## Scope audit

- **field/domain:** this is a rational analytic certificate for the
  `N=256` folded model; it makes no field-uniform collision claim;
- **object:** collision-route instrumentation, not LIST or MCA counting;
- **projection/unit:** folded autocorrelation variance and chamber maximum,
  not slopes, codewords, supports, or collision pairs;
- **endpoint:** `V=50` is the last live even level and `V=48` the first dead
  one for this fixed tool;
- **normalization:** square mass is exactly `16` for profile `(3,4,0)`;
- **quantifier:** all even `V` in `2..48`, only for the pinned majorant;
- **nonclaim:** no variance level, profile, row, or prize terminal closes.

The source PR was unmerged when harvested.  Local `PROVED` status rests on the
independent exact replay, not on upstream merge or review state.
