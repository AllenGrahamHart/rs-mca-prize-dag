# Claim contract

- **scope:** the two exact unresolved rate-half budgets `2^39` and
  `2^39+1`, with `2^41|q-1`
- **input:** `q=p^f` and the exact budget interval
- **currency:** LTE degree collapse followed by a complete residue-class
  intersection and nontrivial-factor ledger
- **output:** `f=1` and `p=q>2^167`
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** exact floor budget, field order is a prime
  power, and the order-`2^41` multiplicative domain exists
- **nonclaim:** this does not classify any Hankel or split-pencil component
- **failure certificate:** an omitted integer in an admissible root class,
  or a printed factor that does not divide its candidate
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_residual_prime_field_collapse/verify.py`
- **upstream mapping:** exact finite SPI base-field-normalization and official
  field-scope router
