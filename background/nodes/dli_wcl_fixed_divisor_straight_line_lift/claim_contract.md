# Claim contract

- **claim id:** `dli_wcl_fixed_divisor_straight_line_lift`
- **mathematical statement:** `(SL1)--(SL11)` in `statement.md`
- **scope:** exactly the four residual WCL fixed-divisor ideals
- **consumers:** the corresponding four slot-emptiness targets
- **status:** `PROVED`
- **proved dependencies:** the `(1,5)/(2,7)`, `(1,6)`, and `(4,9)` divisor
  descents
- **new open content:** compute, independently verify, and factor at least one
  integer straight-line certificate per slot; classify every compatible bad
  characteristic
- **falsifier:** a commutative-ring point where `(SL4)` does not give the
  unique monic remainder sequence, or a slot for which the counts or degree
  bounds in `(SL7)` or `(SL10)` fail
- **nonclaims:** no `Delta` is computed; sparse does not mean computationally
  easy; no characteristic or WCL slot is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/dli_wcl_fixed_divisor_straight_line_lift/verify.py`
- **upstream mapping:** exact finite sparse cyclotomic / shift-pair ledger
