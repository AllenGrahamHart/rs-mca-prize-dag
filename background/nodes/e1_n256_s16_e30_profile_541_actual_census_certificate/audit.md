# Audit

The two implementations share only the light-orbit task list and output
contract.  Their sparse-vector arithmetic, iteration order, and profile
reconstruction differ.  The targeted verifier checks all rows and directly
recomputes profile, cubic moment, and conductor for every retained witness.

