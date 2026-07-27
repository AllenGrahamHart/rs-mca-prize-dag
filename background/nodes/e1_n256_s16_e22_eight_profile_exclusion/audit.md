# Audit

The first count launch, Modal app `ap-P1qQjalsb356Myrg2vdPGB`, failed during
remote module import before completing any template and supplies no evidence.
Corrected app `ap-dpRsXRNVjQZefmrwM9Z1kz` completed all 1,321 templates with
two exact 256 MB engines and 60-second task timeouts, using 7,919.618 aggregate
dual worker-seconds.  App `ap-Z4JCbeBxhxRPjAlBxbUvLV` independently repeated
the complete dual census and collected the full-conductor residue in 7,774.627
aggregate dual worker-seconds.  Checkpoint files were written throughout.

The count and collection checkers validate source hashes, atlas pins, all
1,321 rows, exact engine equality, profile/conductor totals, two content
fingerprints, every retained vector, and hostile mutations.  Modal app
`ap-hxfrf1vAUiZNYnbuVtAfNZ` computed the exact norm ledger in 15 batches per
engine.  The norm checker validates source/collection hashes, vector ordering,
exact FLINT/PARI agreement, positivity, distinct count, profile maxima, global
maximum, threshold count, maximizing indices, and a hostile mutation.
