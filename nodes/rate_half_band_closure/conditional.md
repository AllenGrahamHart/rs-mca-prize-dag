# rate_half_band_closure conditional proof

## Predicate node

- `aqb_averaged_quotient_box`

## Claim
AQB-I closes the residual band 2^33 < sigma <= sigma* for all admissible q in (2^255.9, 2^256).

## Proof (Pro Brief I, verified)
Conservative trigger log2 L > Q - 40. The c=2 exact-crossing row's deficit Delta(Q) = d*Q - 40 - log2 C(2^40, m) is increasing in Q, worst at Q=256 where Delta = B_I = 429,645,546.773. AQB-I supplies 429,645,547 bits, so the AVERAGE list exceeds the trigger for every admissible q; hence some family member fails MCA at sigma*, and radius monotonicity propagates the failure down the band. Combined with the proved safe side above sigma*, the determination closes.
