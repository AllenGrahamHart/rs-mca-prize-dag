# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition`
- **mathematical statement:** every clean slope and saturated row in either
  live active system gives an exact squarefree complementary partition with
  both factors attaining the printed global degree; active bad-row clean
  incidences satisfy `(ATP7)--(ATP8)`
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** exceptional-trace nonvanishing and the inherited active-core
  equations
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** classify the degree-tight two-sided partition families
  under the Hankel adjugate equations
- **falsifier:** a clean or saturated quotient with a repeated/shared factor,
  a degree drop in `A_a` or `V_a`, or failure of the incidence sum `(ATP7)`
- **nonclaims:** no classification or nonexistence of the partition family
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition/verify.py`
- **upstream mapping:** exact SPI ledger / two-sided active divisor partition
