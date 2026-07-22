# Claim contract

- **Claim:** every geometrically reducible degree-four common-fiber survivor
  is a cyclic or dihedral pullback under a subgroup-valued special deck
  automorphism.
- **Scope:** the official degree-four branch with at least `e-148` captured
  pairs.
- **Dependency:** degree-four irreducible router and its pinned subgroup
  estimate.
- **Consumer:** `rate_half_band_closure` and the symbolic support classifier.
- **Falsifier:** a reducible official degree-four survivor with no scaling or
  inversion deck automorphism, or a failure of the `2912` aggregate bound.
- **Nonclaims:** captured support pairs need not themselves be deck orbits;
  the cyclic/dihedral pullback families are not excluded here.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_reducible_deck_router/verify.py`
