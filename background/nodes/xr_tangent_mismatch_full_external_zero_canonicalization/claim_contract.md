# Claim contract

- **Claim:** one selected nonzero mismatch uses its full external zero set,
  not an arbitrary witness subset, and retains excess at least `A-K`.
- **Selection:** any fixed deterministic first-match order, once per slope.
- **Output:** one punctured GRS chart `(T,Z_z,K-d_z,A-d_z)` per selected
  slope/codeword pair.
- **Consumer:** the XR tangent/support-mismatch bridge.
- **Nonclaim:** no bound on the number of distinct `Z_z` charts and no
  distinct-slope aggregate.
- **Falsifier:** a selected witness whose full external locator fails to
  divide `q_z`, or whose scaled agreement is below `A-d_z`.
