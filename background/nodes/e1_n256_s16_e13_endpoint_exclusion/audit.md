# Audit

The verifier pins both dependency statements, requires exactly those two
incoming requirement edges, and checks the four-profile partition and exact
`V<=24` frontier. The audit reruns the router, census, norm-ledger, and
large-odd-candidate checkers. No new computation or assumption enters at
synthesis.
