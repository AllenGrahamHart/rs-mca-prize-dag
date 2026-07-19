# Audit

The endpoint uses the closed integer radius `r=(n-k)/2`, for which the exact
half-distance condition is equality. The field exponent is not rounded:
`q>=2^169` is exactly what makes `n/q<=2^-128` at `n=2^41`.

The verifier checks the radius, agreement, minimum-distance condition, prize
budget, DAG dependency, and failure immediately below the field cutoff. It
does not claim to replay the published CA theorem.
