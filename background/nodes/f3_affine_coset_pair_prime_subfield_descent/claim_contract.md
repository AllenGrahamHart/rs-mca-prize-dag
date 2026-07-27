# Claim contract

- **claim id:** `f3_affine_coset_pair_prime_subfield_descent`
- **proved claim:** a simultaneous affine-membership count over `F_q` is a
  prime-field count when the subgroup and both affine forms descend to
  `F_p`; Mattarei then applies with his original hypotheses
- **deployed application:** the KoalaBear order-`2^21` subgroup and its DSP8
  affine factors descend to `F_p`; the Mersenne-31 order-`2^21` subgroup does
  not
- **dependency:** the prime-field Mattarei affine-pair theorem
- **nonclaims:** no Mattarei theorem over a genuine extension-field subgroup,
  no Mersenne-31 affine-pair bound, and no DSP8 correlation estimate
- **falsifier:** an `x outside F_p` with `a*x+b in F_p` for `a!=0` and
  `a,b in F_p`, or failure of any exact arithmetic in `(PSD3)`
