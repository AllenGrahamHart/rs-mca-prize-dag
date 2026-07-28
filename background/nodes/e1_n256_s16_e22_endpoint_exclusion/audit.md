# Audit

The verifier pins both dependency statements, requires exactly those two
incoming requirement edges, and checks the eight-profile partition and exact
`V<=42` frontier.  The audit reruns the router, count, collection, and norm
checkers.  No new computation or assumption enters at synthesis.
