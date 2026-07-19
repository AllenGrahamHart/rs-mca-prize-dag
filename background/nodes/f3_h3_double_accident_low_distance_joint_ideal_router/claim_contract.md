# Claim contract

- **claim id:** `f3_h3_double_accident_low_distance_joint_ideal_router`
- **mathematical statement:** every positive cutoff-18 double-accident
  summand supplies one normalized four-generator cyclotomic ideal, coupling a
  low-distance product star, a nonunique quotient, and equality of their
  finite-field target; the row prime divides its ideal norm
- **scope:** every dyadic order and every official row prime
- **consumer:** `f3_h3_mobius_excess_half`
- **status:** `PROVED`
- **proved dependencies:** cutoff-18 double-accident reduction,
  low-distance ideal-star router, and shifted-product Sidonicity
- **new open content:** efficient orbit/template generation for the joint
  ideals and control of the surviving rows
- **falsifier:** one row with `Y_18>0` for which no admissible joint ideal has
  norm divisible by its row prime
- **load-bearing generator:** `lambda=(beta_E C_0-D_0)/pi`; deleting it
  permits unrelated product and quotient targets
- **nonclaims:** no efficient candidate census, no factorization result, no
  survivor bound, and no unconditional global C36' close
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_double_accident_low_distance_joint_ideal_router/verify.py`
- **independent audit:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_double_accident_low_distance_joint_ideal_router/verify_audit.py`
- **upstream mapping:** primitive shift-pair control; exact finite
  double-accident preprocessing request
