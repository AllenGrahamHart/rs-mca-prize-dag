# Audit

The primary verifier independently replays all `333375` normalized supports,
the Hasse valuation, folded parity mask, exact joint table, degree-`27`
exponential threshold, parent cofactor list, and twelve exclusions. The
independent verifier uses binomial-parity evaluation and an explicit
autocorrelation coefficient array rather than the primary bit-mask routines.

Both verifiers check hostile mutations of the joint table, energy branch,
threshold, and excluded list. They reject interpreting the `645` retained
cofactors as collision orbits.
