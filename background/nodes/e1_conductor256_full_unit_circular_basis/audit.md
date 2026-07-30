# Audit

- Miller's theorem is unconditional at conductor 256. The conductor-512
  theorem in the same paper is GRH-conditional and is not imported.
- The real class number is one; the full cyclotomic class number is not one.
- The Kummer-Sinnott formula is used only in its prime-power conductor form,
  where no extra multi-prime power-of-two index occurs.
- `eta_a` is real because conjugation multiplies `b_a` by `zeta^(1-a)`.
- Odd indices modulo sign have exactly 64 representatives; deleting `a=1`
  leaves 63 generators, matching the unit rank.
- Generation plus the rank count proves independence; no numerical
  regulator determinant is assumed.
- Roots of unity are retained separately and account for the 256-vector
  negacyclic shift/sign orbit in the E1 ledger.
- The log matrix uses squared moduli, hence the factor two in `(CUB4)`.
- No lattice enumeration, floating-point certificate, Modal run, or local
  arithmetic campaign is part of this proof.
