# Claim contract

- **claim id:** `f3_h3_dsp8_rich_factorial_moment_compiler`
- **mathematical statement:** `(RFC1)--(RFC3)` in `statement.md`
- **scope:** every official H3 row and the live `P>=25` DSP8 interface
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependencies:** the split-pencil edge router, exact `K=2D`
  normalization, and the global overlap-cover payment
- **open content exposed:** prove the class-sensitive `(RFC2)` or the simpler
  but stronger unweighted `(RFC3)`
- **falsifier:** a retained target with more than `P(t)(P(t)-2)/8` disjoint
  generic edges, or a failure of either displayed premise to imply DSP8
- **nonclaims:** no factorial-moment estimate and no promotion of DSP8
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_rich_factorial_moment_compiler/verify.py`
- **upstream mapping:** primitive shift-pair control / target-weighted exact
  second-moment ledger
