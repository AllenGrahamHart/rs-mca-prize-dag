# Audit

- Enumerated all `binom(127,3)=333,375` normalized light supports; exactly 63
  satisfy zero-odd parity, and all are two antipodal pairs.
- Repeated the classification in positive-gap coordinates and recovered the
  same six 2-adic affine-unit classes.
- Production Modal app `ap-Q9Gv4Od8ny1Ixkcb8ej0Q9` completed 48 disjoint
  shards and tested 119,087,616 signed vectors.
- Independent Modal app `ap-kKHuq4icz9mhgKv7qJJsD5` formed the full
  negacyclic product and independently tested the same vectors.
- Both engines report zero profile vectors in every template.
- Coverage checks reject a missing shard; the classifier rejects omission of
  the `t=32` orbit; packet checks reject any nonzero retained count.

Both remote engines used 256 MiB containers and 60-second function caps. The
local verifier performs only the small support classification and packet
arithmetic.
