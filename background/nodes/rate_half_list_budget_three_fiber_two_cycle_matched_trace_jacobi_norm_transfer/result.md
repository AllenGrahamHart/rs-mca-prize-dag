# Result

The matched cycle parity branch now has a complete mathematical exclusion
interface through the trace-Jacobi and cyclotomic-norm stages at `M=2^36`.
It consists of two torsion-sign packets, each with six degree-`2^36` signed
gcds, one top norm at order `2^39`, and a 37-level plus tower through order
`2^38`.

This makes CR-002-C precise enough for an algorithm contributor, but not yet
runnable: no compressed implementation, measured pilot, memory/storage
profile, or cost ceiling exists. Every torsion survivor must still pass the
corrected twisted-fourth-power compiler.
