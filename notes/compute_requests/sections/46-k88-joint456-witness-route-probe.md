## Preregistered K'=88 joint raw-clipped 4/5/6 witness probe

- **decision:** decide whether a genuine three-support fixed-union LP can
  repair the exact witness that defeats both independent adjacent edges
- **scope:** one printed offset-1 witness, one fixed-union charge `(38,6)`
- **probe SHA-256:**
  `10fc0f244b87978bc0e479ca9409dd5ce004f6a6d4d1d121a6e0eb444de81ecf`
- **dispatcher SHA-256:**
  `d7ddd4e827f2ea8f8001441637e6f5da8b2539cb1452c2a8f537b6f13367ce7d`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 512 MB, 105-second child wall and 120-second
  container wall; projected cost below `$0.02`
- **local safety:** one RAM-guarded Modal client; no local solve

The 14 nonnegative variables are the three support-4 strata, four support-5
strata, four support-6 strata, and three direct strata. The constraints are
both fixed-union incidence families, the exact direct caps, and the three
global raw circuit caps. Thus support 5 is shared inside one LP rather than
charged independently to overlapping adjacent edges.

This first probe deliberately uses floating-point HiGHS dual-simplex and
interior-point algorithms only to decide whether exactification is worth
pursuing. `PROMISING` requires both algorithms to agree well inside the
leader; `DEAD` means the estimated optimum remains above the leader;
`INCONCLUSIVE` includes solver disagreement or a near-zero margin. No output
from this probe is proof evidence, and it cannot move DAG status. A promising
result must be reconstructed as an exact rational primal/dual certificate
with an independent verifier before entering any theorem or larger scan.

**Outcome:** `DEAD` as a heuristic route. Modal app
`ap-meBQmnvkmsD3FoYCpUtHPJ` completed in 5.06 seconds at 182 MB peak RSS.
Capture SHA-256:
`f07bab7fc16b5917c0bee80d32325beeb73882ae177d316575228c031a394e47`.
Dual simplex and interior point return the same objective estimate. The
resulting repaired premium is approximately
`46573494499935690501632509827776156475058710877`, above the leader by
approximately `5088564702309253289926741066030525546321864177`.

This separation is decisive for route selection, so no exactification or
larger scan is warranted. The values remain floating-point heuristic output
and are not promoted as a theorem, proof node, or falsification of any
asserted DAG claim.
