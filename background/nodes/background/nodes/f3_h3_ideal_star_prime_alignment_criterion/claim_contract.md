# Claim contract

- **claim id:** `f3_h3_ideal_star_prime_alignment_criterion`
- **mathematical statement:** divisibility of an admissible rooted ideal-star
  norm by a split prime is equivalent to simultaneous collision at a
  degree-one prime; one fixed primitive root screens the complete star union
- **scope:** every dyadic `n>=4` and every prime `p=1 mod n`
- **consumer:** `f3_h3_mobius_excess_half`, fixed-order candidate sieve
- **status:** `PROVED`
- **proved dependency:** `f3_h3_low_distance_ideal_star_router`
- **new open content:** produce the complete relevant-prime list at official
  order without raw star enumeration, then run this exact alignment sieve
- **falsifier:** a split prime dividing an ideal-star norm with no simultaneous
  collision at any primitive root, or a failure of one-root Galois transport
- **proof route:** complete splitting, ideal-norm divisibility, and odd Galois
  dilation
- **replay:**
  `python3 background/nodes/f3_h3_ideal_star_prime_alignment_criterion/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
