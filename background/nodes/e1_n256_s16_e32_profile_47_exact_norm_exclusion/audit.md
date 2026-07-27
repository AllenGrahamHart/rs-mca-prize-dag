# Audit

- The proved router supplies exactly 148 affine odd-unit light-support orbits.
- Production Modal app `ap-wUY2sEVOlPTj95cuuaJhkT` uses folded chords plus
  Python FLINT resultants. It processes 60,148 full-conductor profile vectors
  in 377.786140 aggregate worker-seconds.
- Independent Modal app `ap-b1DkMwYxO1Wt886rrpSVYT` uses direct negacyclic
  multiplication plus PARI/GP resultants. It processes the same vectors in
  631.679933 aggregate worker-seconds.
- The engines agree on every per-template count and maximum, zero norms at or
  above `2^250`, the global maximizing witness, and the exact maximum integer.
- Three-template pilots included the heaviest profile count and agreed before
  either full campaign was authorized.
- Lightweight verifiers check source and result hashes, complete orbit and
  template coverage, per-template equality, witness profile and conductor,
  the exact norm inequality, DAG wiring, and hostile packet mutations.

Workers used 512 MiB and a 60-second cap. The largest observed task remained
well inside the cap; no exact resultant census is replayed locally.
