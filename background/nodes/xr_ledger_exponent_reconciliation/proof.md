# proof: xr_ledger_exponent_reconciliation

## Result (exact, verified at (k,t) = (4,3), (3,4), (5,2), k-independent)

For supports S, T of size k+t at exchange distance s, the dimension of
{w on S∪T : w|_S ∈ RS_k(S), w|_T ∈ RS_k(T)} gives pair-codimension

    codim(s,t) = t + min(s,t)     (exactly; s ≥ t is exact independence).

Hence:
- averaged_xr's stated shell cost q^{-min(s,t)} (conditional cost of the
  second event) is CORRECT as used — its statement and proof stand.
- qx13's ledger c(s,t) = min(s, t-1) is the ANCHORED rank — one dimension
  spent on the anchor/projectivization — correct in its own convention.
- The "off-by-one" is a convention dictionary entry, not an error. Each
  consumer uses its own form; the dictionary is now pinned by the exact
  table in verify.py.

## Verifier

verify.py recomputes the table by row-reduction over F_101 (rank of the
stacked explained-subspace bases), asserting codim = t + min(s,t) at all
three (k,t) pairs across s = 0..t+2.
