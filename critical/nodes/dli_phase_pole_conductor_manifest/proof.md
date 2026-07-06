# proof: DLI phase-side pole + conductor manifest (Pro; verified)

For each (central profile, nonzero frequency lambda, DLI harmonic h, square-root
component), parts 1-3 of the reduced-phase manifest hold:

- P_lambda(X) = sum_{r odd, 1<=r<=d} a_r X^r, a_d != 0, is odd of degree d, and
  at the prize rows d <= t < p = char F_q (q = p prime, t ~ 2^33). Near infinity
  (u = 1/X), hP_lambda(1/u) has leading pole ha_d u^{-d} with d odd, so p does
  not divide d.
- ARTIN-SCHREIER: a leading pole of prime-to-p order cannot be killed by
  G^p - G (those introduce poles of p-divisible order). So the reduced
  representative keeps a positive prime-to-p pole of order d at infinity.
- SQUARE-ROOT PULLBACK X = alpha Z^e (e a 2-power): the leading term becomes
  ha_d alpha^d v^{-ed}; the reduced pole order is ed, and since 0 < ed << p
  (verified) p does not divide ed. Nondegeneracy survives.
- CONDUCTOR MAJORANT: cond(L_{psi(hP_lambda)} tensor K_harm) <= ed + C_tame
  (C_tame = the Kummer/section harmonic + finitely many tame branch points).

VERIFIED (notes/): the pole divisibility (ed<<p) and the local expansion shape.
Discharges the local-expansion / prime-to-p pole / conductor-majorant parts. The
o(t) harmonic total is SEPARATE -> dli_harmonic_conductor_ledger.
