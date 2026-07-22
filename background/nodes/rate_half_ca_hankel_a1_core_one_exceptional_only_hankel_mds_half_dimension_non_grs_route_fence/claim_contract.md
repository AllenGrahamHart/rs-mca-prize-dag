# Claim contract

- **Claim:** half-dimension MDS, weighted self-duality, and codimension-one
  Schur square do not force generalized Reed--Solomon structure.
- **Scope:** a route fence for the MDS side of the exceptional endpoint.
- **Dependency:** the MDS-Schur router identifies exactly these abstract
  properties.
- **Consumer:** route selection under `rate_half_band_closure`.
- **Falsifier:** a failed exact check of self-duality, one zero maximal minor,
  square rank other than seven, or a nonzero linear syzygy among `(2)`.
- **Nonclaims:** the official split-incidence/Forney code is not asserted to
  realize this small witness or to be non-GRS.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_mds_half_dimension_non_grs_route_fence/verify.py`
