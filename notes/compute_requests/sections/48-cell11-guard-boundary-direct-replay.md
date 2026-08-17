## Preregistered repeated-BC cell-11 guard-boundary direct replay

- **decision:** determine whether any of the 160 exact guarded boundary
  source points supports a colored or uncolored missing-record packet
- **scope:** all eight repeated-BC cell-11 source towers; missing `BE`, `CF`,
  `DE+`, `DF+`, and `EF`; both outside signs and all fifteen residual
  matchings where applicable
- **replay SHA-256:**
  `40639f55d76c628b28982d52bd1cb7751f33fceb5de035d98a7649ba89681617`
- **boundary packet SHA-256:**
  `e01e1a6ceaf55f530c0bd62549c9d64b18e5eeacc5a95be24c543c18f6fbcac5`
- **envelope:** eight independent one-CPU workers, 1 GiB each, 120-second
  worker wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client; no local root extraction or
  packet enumeration

The replay reconstructs the common-kernel cofactors directly over
`F_2130706433` from each printed `(b,c,r,t)` point. It does not specialize the
function-field quotient algebra whose construction guard vanishes. The
missing product and squared sum are then used in two exact tests:

1. direct consistency for colored missing `BE` and `CF`;
2. exhaustive base-field endpoint roots for each uncolored missing record,
   followed by all three paired-product equations for both outside signs and
   all fifteen matchings.

`DIRECT_BOUNDARY_EXCLUDED` on all eight rows, zero denominator failures, and
an independent pure finite-field verifier authorize a PROVED registered-guard
boundary exclusion node. `DIRECT_BOUNDARY_CANDIDATE_PRESENT` prints every
candidate and sends only that finite packet to the original raw-system
replay. `REMOTE_ERROR` authorizes resumption of failed rows only. A candidate
is not by itself a counterexample: distinctness and the full raw cell system
remain downstream checks.
