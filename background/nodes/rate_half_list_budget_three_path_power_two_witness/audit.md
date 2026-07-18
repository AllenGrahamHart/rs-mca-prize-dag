# Audit

- The domain is the complete multiplicative group `F_17^*`, so its order is
  the power of two `16`; this is not an arbitrary evaluation set.
- All four actual agreement supports, not merely selected subsets, have size
  exactly eleven and realize the stated path incidence type.
- The degree-`d` pencil has exactly three fully split members, consistently
  with `rate_half_list_budget_three_path_mobius_transversal`. The witness
  therefore kills the inference from "no fourth member" to "no path witness."
- The second pencil theorem in that parent starts at `d>=6`; this fixture has
  `d=4` and does not test that later threshold.
- "Budget three" names the four-codeword Johnson-predecessor branch. Since
  `floor(17/2^128)=0`, this finite field is not itself a prize-budget-three
  row.
- No lifting theorem to the official `n=2^41` subgroup is claimed. The same
  exponent partition fails over `F_97`, so it is not a characteristic-free
  cyclotomic identity. A complete normal-form search on the proper order-16
  subgroup of `F_97` checks `3,830,400` path assignments and finds no witness;
  this is bounded evidence that subgroup properness may matter, not a uniform
  theorem.
- The independent audit mutates the received word and checks that the exact
  four-way agreement certificate is destroyed.

The bounded search is replayed by

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_list_budget_three_path_power_two_witness/notes/search_order16_proper.py
```
