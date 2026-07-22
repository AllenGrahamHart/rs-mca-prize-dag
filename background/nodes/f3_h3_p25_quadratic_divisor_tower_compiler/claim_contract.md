# Claim contract

- **claim:** nonidentity `P>=25` is equivalent to solvability of the printed
  degree-25 modular repeated-squaring system, with all equations quadratic
  and exact size `98s+30` by `98s+54`.
- **scope:** every dyadic split row `p=1 mod 2^s`.
- **dependencies:** the shifted-factor polynomial identity and
  characteristic-zero shifted-product Sidonicity.
- **falsifier:** a row where system solvability disagrees with direct
  `P>=25`, a missing inverse/distinctness condition, or an incorrect variable
  or equation count.
- **certificate:** a modular solution is a falsifier for P24; a checked
  integer unit-ideal identity gives a complete characteristic outer set.
- **nonclaims:** no efficient solver, certificate, prime factorization,
  resource estimate, official P24 theorem, DSP8 promotion, or C36' close is
  asserted.
