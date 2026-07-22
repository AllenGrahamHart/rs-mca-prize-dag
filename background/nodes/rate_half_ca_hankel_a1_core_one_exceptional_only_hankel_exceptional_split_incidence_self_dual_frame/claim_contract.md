# Claim contract

- **Claim:** exceptional columns are coefficient vectors of split incidence
  polynomials and form a weighted self-dual frame with exactly the flat or
  swapped replication profile.
- **Scope:** the two sharp high quotient-distance endpoint profiles.
- **Dependencies:** exceptional self-duality, exact row saturation, and the
  sharp endpoint incidence classification.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a nonsplit or repeated `g_a`, rank other than `e`, failure of
  weighted self-duality, or a replication profile outside `(HSF5)` and its
  flat counterpart.
- **Nonclaims:** neither frame class is proved empty. The exact `e=3` flat
  analogue is a route fence, not an official construction.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_split_incidence_self_dual_frame/verify.py`
