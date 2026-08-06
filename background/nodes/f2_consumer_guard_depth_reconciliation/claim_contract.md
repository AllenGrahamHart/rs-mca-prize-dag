# Claim contract

- **input:** the banked generated-field guard, the official degree/order
  classification, and fixed-depth ambient invariance;
- **output:** an exact scope test for ambient-balance and exact-slice depths;
- **proved distinction:** object invariance at fixed depth does not transport
  a depth chosen from the ambient field size;
- **nonclaims:** no F2 mass bound, no extras-budget close, no proof that the
  alternate `f1/ext` route covers every guard-excluded row, and no change to
  the prize threshold;
- **falsifier:** an official non-generating type passing the ambient-balance
  generated-field guard, or any official type passing it when
  `t log2(q)<N`.
