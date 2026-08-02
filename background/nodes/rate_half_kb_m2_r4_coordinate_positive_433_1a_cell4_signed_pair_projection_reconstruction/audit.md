# Audit

The verifier pins all three result artifacts, their source hash chain, the
resultant and factor shapes, multiplicities, exact small-factor texts, the
pseudo-remainder identity, the complete canceled-factor ledger, and the
primitive reconstruction shapes.  It also checks the deployed square root of
`-1`, every canceled source guard, DAG dependencies, consumer edge, and the
explicit nonclaim.

The mutation audit removes a live factor, changes the resultant exponent,
and corrupts a canceled-factor multiplicity.  Each mutation must fail.
