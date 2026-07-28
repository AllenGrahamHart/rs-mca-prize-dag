# Audit

The verifier pins both dependency statements, requires exactly those two
incoming requirement edges, and checks the two-profile partition and exact
`V<=28` frontier. The audit reruns the router, census, and odd-part norm
checkers. No new computation or assumption enters at synthesis.
