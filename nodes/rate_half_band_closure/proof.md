# proof: rate_half — dihedral sibling window route (Pro P6, arithmetic verified)

## Verdict: NOT bracket-grade. A concrete priced covering mechanism exists.
The band [M0=2^33, sigma*=8,592,912,738] (size 2,978,147, VERIFIED) is the shadow
of the 2-power quotient-core floor cap n/256=2^33. The DIHEDRAL/Chebyshev quotient
x -> x + x^{-1} has twin-pair fibers {x, x^{-1}}, giving FINE-GRAINED scales d (NOT
restricted to the 2-power lattice). Under the strict window convention (scale d
covers sigma < d), the even dihedral scales 2^33+2, 2^33+4, ..., cover
[2^33, sigma*-1] (half-lattice = 1,489,073 scales, VERIFIED), each with count
C(2^40, 2^32+1), log2 ~ 4.05e10 (VERIFIED) — a 3e8x margin over the trigger
B* < 2^128. This is NON-AQB (explicit single-family lower-bound witnesses, no
averaging => no convex-combination cancellation) and non-giant-M.

## Endpoint patch (fixed-point sibling)
Inversion has fixed points +-1 in mu_n; adding one fixed singleton to a twin-pair
support shifts the effective dihedral scale by one parity, giving d = sigma*+1, so
the strict condition covers sigma = sigma*. Count loses only a poly/constant factor
(still ~1e10 bits >> 128) — a degree/support-certification question, not entropy.

## Remaining obligation (residual leaf: dihedral_sibling_window_certificate)
The Chebyshev/fixed-point CERTIFICATE (concrete, not numerical): (1) degree audit
(twin + singleton locators stay deg<k); (2) distinctness/noncontainment (dihedral
witnesses distinct on D, NOT silently the old qcore witnesses); (3) strict-window
endpoint (sigma<d, use d=sigma+1, fixed-point sibling for top parity); (4) priced
count certificate (trivial: 4.05e10 >> 128). Supported by: E26 dihedral plan,
floor-depth verdict (cap = n/256), B2b no-concentration scan (39/39, max excess
2^4.18 << falsifier). Fallback bracket ONLY if this certificate fails formally.
