# Audit

The verifier pins both dependency statements, requires exactly those two
incoming requirement edges, and checks the four-profile partition and exact
`V<=36` frontier. The audit reruns the router, census, and norm checkers. No
new computation or assumption enters at synthesis.
