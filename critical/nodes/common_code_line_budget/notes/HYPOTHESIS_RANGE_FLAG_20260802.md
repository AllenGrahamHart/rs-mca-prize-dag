# Range flag 2026-08-02: hypothesis fails at all six official rows for band use

The node's line-count formula (slopes <= floor((|Omega|-c0)/(h-c0)))
requires `a + b - n >= k`. For the band application (a = A, b = J with
J in [k+1, A-2]) this evaluates to 2k+h+d-n, which is NEGATIVE at all
six official rows — the banked theorem does NOT cover band cores.
The applicable statement is the same formula under the interpolation
hypothesis `J >= k` alone (four-line proof: forced-ray residual sets
of size >= A-J are pairwise disjoint off the core), proved and
verified tight at every band depth by the graded-band-ledger pilot
(`notes/pilots_20260802/xr_graded_band_ledger/`, THEOREM 3; 0
violations, L = cap achieved at d = 1,2,3). That version is queued for
minting with the band column. This node's own statement and status are
untouched — the flag records only that citations of it for band cores
are out of range.
