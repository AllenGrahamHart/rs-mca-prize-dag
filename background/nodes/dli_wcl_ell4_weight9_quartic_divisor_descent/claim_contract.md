# Claim contract

- **claim id:** `dli_wcl_ell4_weight9_quartic_divisor_descent`
- **mathematical statement:** `(QDD1)--(QDD11)` in `statement.md`
- **scope:** the exact WCL `(ell,w)=(4,9)` slot at root order `2048`
- **consumer:** `dli_wcl_slot_4_9_emptiness`
- **status:** `PROVED`
- **proved dependency:** the odd-moment Newton cutoff
- **new open content:** compute a compact nonzero `Delta`, factor it
  completely enough for the official field scope, and exclude or classify
  every surviving characteristic
- **falsifier:** a reduced `(4,9)` relation whose normalized locator does not
  have `(QDD5)--(QDD7)`, or a quartic divisor whose reconstruction fails
- **nonclaims:** no bad-characteristic integer is computed; no official
  characteristic is excluded; the WCL slot and zone remain open
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell4_weight9_quartic_divisor_descent/verify.py`
- **upstream mapping:** exact finite shift-pair / sparse cyclotomic ledger
