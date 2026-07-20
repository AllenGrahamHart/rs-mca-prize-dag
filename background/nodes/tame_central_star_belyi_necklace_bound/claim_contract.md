# Claim contract

- **claim id:** `tame_central_star_belyi_necklace_bound`
- **status:** `PROVED`
- **mathematical statement:** a tame polynomial cover with passport
  `(3^h1^e; c1^(2h); m)` and `c=h+e`, `m=3h+e` has at most `N(c,e)` source-
  scaling classes, where `N` is the binary-necklace number
- **scope:** algebraically closed characteristic zero or `p>m`; labelled
  branch values and the distinguished multiplicity-`c` point are fixed
- **consumer:** `f3_hge4_near_third_belyi_necklace_bound`
- **falsifier:** two non-scaling-equivalent tame covers with the same plane
  tree, a cover whose forced tree is not central-star, or a disagreement
  between `(CSN1)` and binary-necklace enumeration
- **nonclaims:** existence of every necklace, field of definition, or any
  cyclotomic root condition
- **replay:** `python3 background/nodes/tame_central_star_belyi_necklace_bound/verify.py`
  and `verify_audit.py`
