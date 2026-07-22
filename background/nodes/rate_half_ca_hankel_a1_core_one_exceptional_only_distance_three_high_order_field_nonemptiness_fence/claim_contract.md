# Claim contract

- **Claim:** each retained value `g in {e/3,e}` occurs as
  `gcd(e,p-1)` for an explicit prime in the official `B=2^39+1` interval
  with `2^41 | p-1` and `gcd(2^39-1,p-1)=1`.
- **Scope:** arithmetic nonemptiness of the two rank-two field strata.
- **Dependency:** dihedral boundary-order router.
- **Consumer:** `rate_half_band_closure` route selection.
- **Falsifier:** a failed Lucas certificate, interval test, divisibility test,
  or either gcd test for either printed integer.
- **Nonclaim:** neither prime is asserted to support a valid split-pencil or
  distance-three packet.
