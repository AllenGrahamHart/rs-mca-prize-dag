# Claim contract

## Claim

Every residual progression vector has one of 62 printed normal forms,
opposite outer heavy coefficients, and a light in the exact four-position
singleton-weld set. The resulting enumeration chamber has 1,195,965 supports
per form and 2,372,794,560 signed vectors. Odd cyclotomic automorphisms reduce
every invariant profile/moment census to five representatives containing
191,354,400 signed vectors.

## Dependencies

- `e1_n256_s16_e34_heavy_chord_template_reduction` for the progression split
  and singleton-class weld;
- `e1_n256_s16_e34_parity_profile_reduction` for profile `(6,7)` and the
  light-Sidon bound.

## Nonclaims

- no assertion that every counted support realizes compatible signed chords;
- no `E=34`, conductor, moment, or norm conclusion;
- no exclusion of the progression or generic templates.

## Falsifier

A residual progression collision outside the 62 forms, with equal outer
heavy signs, without a light in `W_t`, a failure of the five-orbit invariant
transport, or an error in either chamber count refutes the claim.
