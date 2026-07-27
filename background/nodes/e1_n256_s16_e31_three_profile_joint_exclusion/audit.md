# Audit

- Production Modal app: `ap-QVT4zR1b0UV4Z3QVYzLo4B`.
- Independent audit Modal app: `ap-09HiyZJzn23MDKtzPjXS1M`.
- Both runs used eight 256 MiB workers with a 60-second per-worker timeout.
- Production aggregate worker time: 21.161991623 seconds.
- Audit aggregate worker time: 31.04943181 seconds.
- Each run covered 2,480,992 heavy supports and 158,783,488 relative-sign
  vectors, with all eight rows marked complete.
- The engines agree exactly on profile counts, full-conductor counts,
  unrestricted maxima, and full-conductor maxima.
- Production uses folded unordered chords; audit uses ordered direct
  multiplication in `Z[x]/(x^128+1)` and checks the negacyclic identities.
- Witness replay independently reconstructs each stored production maximum.
- Both drivers checkpoint every completed template with explicit incomplete
  state, preserving partial results if a later worker fails or times out.
- Hostile checks reject a missing template, a changed count, a threshold of
  1205 on the `(3,7)` full-conductor branch, or omission of the proper-
  conductor dependency.

No heuristic or floating-point comparison is used in the closure.
