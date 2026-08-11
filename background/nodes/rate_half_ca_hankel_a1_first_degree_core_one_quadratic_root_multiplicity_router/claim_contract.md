# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_quadratic_root_multiplicity_router`
- **mathematical statement:** the core-one scalar quadratic obeys the exact
  gap and new-root bounds `(QRM2)--(QRM6)`; throughout `5u<e` it is either a
  heavy double root or two heavy simple roots
- **scope:** official first degree, core one, parameter-constant residual
  degree two
- **dependencies:** constant heavy-incidence identity and root-row cube
  correction
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a gap below four, failure of `(QRM4)` or `(QRM5)`, or a
  low-gap squarefree quadratic with only one heavy root
- **nonclaims:** neither retained pattern is excluded; `5u>=e` is untreated
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_root_multiplicity_router/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
