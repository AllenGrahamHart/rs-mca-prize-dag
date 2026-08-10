# Audit

The primary verifier pins source and result, checks all 54 guard identities,
reconstructs every field-part polynomial from its listed roots, divides that
field part into the source guard, and reconstructs the 67-value/78-incidence
index. Completeness of each high-degree field part is computed exactly as
`gcd(g,u^p-u)` by the custodied launcher.

Hostile controls remove a guard, invent a root, truncate the root union, and
corrupt an incidence list.
