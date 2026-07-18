# Frontier

## Proved

- Worst-list size is integer-valued and monotone in agreement.
- The cyclically rotated prefix construction is ordinary-list unsafe through
  excess `17,179,869,183=2^34-1` at the prize-max razor row.
- The exact balanced-incidence Johnson theorem supplies a bigint-computable
  safe anchor `a_IJ(C)`. At the prize maximum it ranges from `3n/4` for
  `B*=1,2,3` down to `1554944255988` once `B*>=332114441762`.
- Explicit two- and three-codeword predecessor constructions meet that safe
  anchor for `B*=1,2`. Hence both complete budget branches have the exact
  crossing `a_L=3n/4` and list radius `1/4`.
- This is the unique largest cap-uniform maximal-prefix specialization of that
  cyclic construction.
- Diagonal tuples preserve every ordinary unsafe witness for all constant
  interleaving arities.
- Once an ordinary safe value is at most `B*`, the official field cap gives
  `B*^2<q`, and the sub-square-root interleaving theorem preserves that safe
  value for every arity.

## Open

For every remaining branch `B*>=3`, locate the first safe agreement inside
the now-proved bracket. In the razor case,

```text
k+2^34 <= a_L(C) <= a_IJ(C).
```

For `B*=3` and all larger budgets, the integer Johnson test failing at
`a_IJ-1` is not evidence of unsafety.
A closure still needs a stronger upper profile theorem and a matching
predecessor witness at the same candidate.

The existing clean-rate corridor ledger does not cover rate `1/2`, and the
rate-half MCA node is a different counting object.
