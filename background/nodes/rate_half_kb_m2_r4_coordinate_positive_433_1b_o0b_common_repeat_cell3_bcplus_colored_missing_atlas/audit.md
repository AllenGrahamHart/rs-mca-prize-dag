# Audit

The verifier pins both launchers, both results, and the torus input; checks
the eight finite standard bases and all embedded basis digests; then checks
every resultant/root row, direct equation replay, guard status, and lifted
missing product and sum. Hostile controls remove a row, change a dimension,
admit a live `BE` point, alter a guard status, and corrupt a lifted `CF` sum.
