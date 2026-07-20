# Audit

- Kept ordered shift pairs distinct from unordered trades: the two
  orientations pay the existing at-most-two direct-record convention.
- Applied the primitive deletion before comparison with the stripped target;
  p-specific quotient pullbacks are therefore not silently counted as
  primitive.
- Used prefix rigidity only at `m=h,w=h-1`, where its lower bound forces the
  two size-`h` subsets to be disjoint.
- Used `max(1,x)<=1+x`; no assumption that the entropy benchmark exceeds one
  is needed.
- Checked the factorial tail and all 29 official values of `n` with exact
  rational arithmetic.
- `(PSA3)` remains open and is not represented as a new red node.

