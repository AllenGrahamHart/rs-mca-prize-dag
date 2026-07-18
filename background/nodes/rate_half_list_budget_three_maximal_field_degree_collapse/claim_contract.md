# Claim contract

- **claim:** every maximal-domain rate-half row with `B*=3` has field degree
  `e in {1,2}` and the exact characteristic congruences `(MFC2)`.
- **scope:** `n=2^41`, `k=2^40`, `q=p^e`, and
  `floor(q/2^128)=3`.
- **requirement:** `rules_freeze`.
- **consumer effect:** reduces the maximal B*=3 arithmetic to prime-field and
  quadratic-extension cases; no status promotion.
- **nonclaim:** no smaller-domain field-degree collapse, split-pencil
  exclusion, safe list bound, or adjacent crossing is proved.
- **falsifier:** an admissible maximal B*=3 row of degree at least three, or a
  prime/quadratic row violating `(MFC2)`.
