# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_ambient_defect_factorization`
- **mathematical statement:** each of the six first-degree profiles has a
  unique ambient lift `A_j` of bidegree `(d-3,j)`; every row-defect factor
  divides its specialization, and every row with deficit greater than `j`
  is a common split domain factor of `A_j`
- **scope:** `s in {0,1}`, `e=ceil((rho-1)/3)`, `j in {0,1,2}`
- **dependencies:** exact slope ledger, Forney pole absorption, and direct
  three-contact boundary
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a nonambient boundary section, a row where
  `q_x/gcd(q_x,H)` fails to divide `A_j(x)`, or a heavy row not shared by all
  parameter coefficients
- **nonclaims:** no bound on the residual factor is included here
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_ambient_defect_factorization/verify.py`
- **upstream mapping:** split-pencil / exact SPI row-defect ledger
