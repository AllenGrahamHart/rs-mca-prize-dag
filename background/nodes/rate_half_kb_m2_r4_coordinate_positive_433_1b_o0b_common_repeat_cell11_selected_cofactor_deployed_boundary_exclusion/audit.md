# Audit

The primary verifier pins all four source files, checks the eight-row
Cartesian census and tower custody, and enforces the exact sign-specific
dimensions, norm degrees, irreducible-factor profiles, base-field roots, root
multiplicities, and vanishing-guard witnesses.  It also checks that no lifted
boundary point or deployed norm root was reported.

The hostile audit mutates the row census, tower validity, cofactor identity,
factor profile, base-field root, guard witness, deployed-root census, and
status.  Every mutation must be rejected.
