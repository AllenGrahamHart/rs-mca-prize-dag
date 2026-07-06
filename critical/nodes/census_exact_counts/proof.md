# proof: census_exact_counts

## Claim
At the bounded deciding scales (N' in {128, 256, 512}, per census_bounded_scales),
the deciding class counts are exactly computable big integers K = C(N', l') with
the forced ratio l' = (j/n) N', replacing the leading+second-order expansion by
exact Diophantine arithmetic.

## Proof
Computability: K = C(N', l') is a single binomial with N' <= 512 — an exact
integer of at most ~508 bits, computed by exact big-int arithmetic (verify.py).
The forced ratio l'/N' = j/n is census_bounded_scales's Lemma (C); the scale
window is its Section 4. The computation (verify.py, exact, all four rates at
prize parameters n = 2^41, k = rho n, t = t* from xr_radius_arithmetic):

- rate 1/2:  N'=128, l'=63..64: log2 K = 124.149..124.171  (3.8 bits BELOW the
  gate 128 — the thin-margin finding, requantified exactly)
- rate 1/4:  N'=128 tops at 103.24; N'=256 starts at 206.66 — the gate sits in
  the between-scale staircase gap
- rate 1/8:  N'=256, l'=222..225: log2 K = 140.90..132.61 — the gate interior
- rate 1/16: N'=512, l'=478..481: log2 K = 176.59..165.00 — gate below the
  N'=512 band, N'=256 tops at 90.6

Every entry is an exact integer (not an estimate); the verifier recomputes all
of them and pins the log2 values above to 3 decimals. ∎
