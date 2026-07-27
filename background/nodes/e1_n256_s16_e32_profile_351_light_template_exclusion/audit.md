# Audit

- The proved common router supplies exactly 148 affine odd-unit light-support
  representatives covering 28,800 normalized supports.
- Production Modal app `ap-DuxqODKmBVrz1XwQGhui61` used a folded-chord kernel
  and exhausted 2,937,494,528 representative normalized signed vectors.
- Independent Modal app `ap-RjKrdoGVLkBnsZLmm9Loeu` used direct negacyclic
  multiplication and independently exhausted the same vectors.
- Both engines agree per template and globally: 29,238 profile vectors,
  15,440 at full conductor, and maximum `M_3=1392` in both ledgers.
- The lightweight verifiers check packet hashes, complete template coverage,
  every per-template ledger, direct recomputation of stored witnesses, DAG
  wiring, and the strict comparison `1392<1517`.

Both remote engines used 256 MiB containers and 60-second function caps. No
large census is replayed locally.
