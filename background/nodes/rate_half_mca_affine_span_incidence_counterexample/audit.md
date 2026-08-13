# Audit

The primary verifier constructs the line, enumerates every selected maximal
agreement support, checks pair noncontainment, recomputes affine rank and
direction separation, and evaluates all three violated bounds.

The independent verifier uses a separately written constructor and checks
all 100 domain coordinates for every selected slope.  It enumerates all
1,009 constant direction codewords when recomputing the separation maximum.

The counterexample is exact and small.  No Modal or probabilistic search is
used.  The construction also explains the proof gap: local full rank does
not control proper-subspace multiplicity among incident normals.

## External confirmations (2026-08-13 addendum, coordinator PR review)

Two independent same-night confirmations of this refutation, both by
scottdhughes on przchojecki/rs-mca:

1. **An independent second counterexample** (PR `#1164` comment,
   02:50 UTC — eleven minutes after our `#1165` went up): over
   `RS[GF(257), GF(257)^*, 1]` at `(n,K,m,w,s) = (256,1,86,85,1)`,
   87 distinct exact same-support pair-noncontained slopes with strict
   direction separation `85 < 86`, all selected words outside the
   near-rational radius, against a printed affine-span cap of 8.
   Python + independent Sage replays agree. Scott's diagnosis of the
   proof gap matches ours exactly: the final `r = s` normal-flat step's
   claimed codeword kernel has dimension zero, so the occupancy bound
   does not follow. Different field, different parameters, same defect
   — a genuinely independent refutation, not a replay.
2. **An independent replay of THIS counterexample**: PR `#1166`
   ("preserves and independently replays #1165") with isolated math
   and custody reviews GREEN, per Scott's `#1165` comment (04:46 UTC).
   `#1166`'s support-local transversality repair (the `theta` margin)
   was harvested in cycle 229 and is banked as
   `rate_half_mca_support_local_transversality_compiler`.

Scott's `#1164` comment also requests that `#1164` not be integrated
alone while the correction was in flight — consistent with our wave-60
handling (the `#1166` repair landed before any dependent payment was
banked here).
