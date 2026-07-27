# Audit

Date: 2026-07-27.

The proof is field-theoretic and exact. Its critical distinction is between
the small-field norm, which is below `2^250`, and the full norm, which is a
power of the small norm and need not itself be small. Prime-divisor support,
not full-norm magnitude, supplies the exclusion.

The stronger proposed shortcut "low variance implies proper conductor" was
falsified before it entered the DAG. Modal run
`ap-p4xiPndsVLM81qNS4trQgp` exhausted the 17,920-state order-16 toy model
and tested one-coordinate deperiodizations. It found the full-conductor
profile vector recorded in `proof.md`, with exact variance `36`. The local
verifier independently replays its profile, gcd, and variance; the Modal run
is not load-bearing.

No norm census, factorization, sampled inequality, or numerical
approximation is used in the theorem.
