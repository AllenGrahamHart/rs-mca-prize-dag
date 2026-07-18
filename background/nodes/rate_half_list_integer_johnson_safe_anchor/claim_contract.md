# Claim contract

- **claim:** the exact balanced-incidence inequality `(IJ2)` and the resulting
  safe anchor `(IJ3)`
- **scope:** ordinary Reed-Solomon lists; all fields and distinct evaluation
  domains; official rate-half specialization in `(IJ5)`
- **dependency:** the proved cyclic floor only for the lower half of `(IJ5)`;
  the safe theorem itself is self-contained
- **consumer:** safe-side evidence for `rate_half_list_adjacent_crossing`
- **nonclaims:** no unsafe witness at `a_IJ-1`, no exact adjacent crossing, no
  MCA/CA assertion, and no interleaved-list assertion
- **falsifier:** `B+1` distinct degree-`<k` polynomials and one word with at
  least `a` agreements each when `J_(n,k,B)(a)>0`
- **replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_list_integer_johnson_safe_anchor/verify.py`
