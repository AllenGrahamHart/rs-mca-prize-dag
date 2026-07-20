# Claim contract

- **claim id:** `dli_wcl_ell1_weight6_even_norm_divisor_descent`
- **mathematical statement:** `(END1)--(END8)` in `statement.md`
- **scope:** exactly the WCL `(ell,w)=(1,6)` slot
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **status:** `PROVED`
- **proved dependency:** the odd-moment Newton cutoff
- **new open content:** compute, factor, and apply the official field scope to
  a checked nonzero `Delta_6`
- **falsifier:** a reduced relation or divisor packet violating either
  direction of `(END3)--(END6)`
- **nonclaims:** no certificate integer or characteristic is classified; the
  slot and WCL zone remain open
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell1_weight6_even_norm_divisor_descent/verify.py`
- **upstream mapping:** exact finite sparse cyclotomic / shift-pair ledger
