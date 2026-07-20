# Claim contract

- **claim id:** `f3_hge4_nonfull_complement_third_gate`
- **status:** `PROVED`
- **mathematical statement:** a non-full constant-difference pair of
  degree-`h` subgroup locators leaves at least `h` complement roots; at
  dyadic exact ratio level `m`, all widths with `3h>=m` are empty
- **scope:** characteristic zero or characteristic greater than `m`; the
  HGE4 application uses `m|n`, `p=1 mod n`, and hence `p>m`
- **dependencies:** exact-ratio tower routing and the primitive near-square
  union dictionary
- **consumer:** `f3_hge4_norm_gate_count`
- **new open content:** prove
  `sum_(h=4)^floor((m-1)/3) E_h^prim(m,p)<=(21/2)m^2`
  uniformly, or provide another aggregate payment
- **falsifier:** one non-full pair satisfying the stated characteristic and
  root hypotheses with `h>m-2h`
- **nonclaims:** no count below the third line; no full-fiber statement; no
  result when the characteristic kills `2`, `m`, or `h`
- **replay:** `python3 background/nodes/f3_hge4_nonfull_complement_third_gate/verify.py`
  and `verify_audit.py`
