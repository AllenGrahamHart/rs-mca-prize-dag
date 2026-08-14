# Audit

1. Normalize by the unknown actual record count before using its lower bound.
2. Keep each individual cap as the minimum of the ambient and record orders.
3. Use exact rational weights and capacities throughout the LP.
4. Check that weights increase before applying the greedy optimizer.
5. Compare the unrounded rational demand and capacity, then print integer gaps.
6. Stop at the first reversal `K'=15446`.
