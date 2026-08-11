# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_free_cubic_root_multiplicity_router`
- **mathematical statement:** in the core-free cubic scalar profile, simple
  heavy roots obey `(CRM6)`, triple roots obey `(CRM7)`, and `5u<e` leaves
  exactly the two root patterns in `(CRM9)`
- **scope:** official first degree, core zero, parameter-constant residual
  degree three
- **dependencies:** constant heavy-incidence pin and root-row mod-three
  correction framework
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** an incorrect omission/new-root identity, a simple root row
  violating `(CRM5)`, or a low-gap cubic with a nonheavy root or triple root
- **nonclaims:** neither retained root pattern is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_free_cubic_root_multiplicity_router/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
