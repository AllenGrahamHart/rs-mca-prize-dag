# Consumer-backward audit

- **verdict:** NO ISSUE
- **consumer:** `f3_h3_mobius_excess_half`
- **scope:** the `Y_18` residual, not the already-paid `R=1` layer

## Load-bearing checks

1. The integral separator uses numerator differences. Its omitted
   denominators are products of `1-zeta^u`, whose norms are powers of two;
   all are units at the odd row prime.
2. Nonidentity quotient uniqueness makes every `Delta_i` nonzero and makes
   `Delta_i` a unit precisely when the selected quotient lift is alone modulo
   the row prime.
3. The sum ideal `J_i+(Delta_i)^B_n` uses ideal addition, hence the minimum of
   valuations. Multiplication would not remove `R=1` fibers.
4. The exponent
   `B_n=min(n-19,ceil(33n^(2/3))-19)` dominates every official cutoff-18
   product excess: the first term is the exact nonzero-fiber cap and the
   second comes from the proved uniform product-fiber theorem. Thus a quotient
   collision cannot truncate the derivative-ideal valuation needed in
   `(JD4)`.
5. The proof checks the converse `q=0 => J_i` is a unit using the `m`th Hasse
   derivative. This is required for the `iff` in `(JD5)`; the earlier lower
   valuation alone would prove only one direction.
6. Collapsing all quotient separators to `Disc(Q_n)` is valid and gives
   `f_n|gcd(e_n,h_n^B_n)`, but loses targetwise coupling. In the cutoff-two
   order-eight fixture this gcd is exactly `e_8`, whereas
   `e_8/f_8=5^8`; the global gcd detects none of that strict refinement.
7. The factorwise discriminant-height route is quantitatively fenced. With
   `M=(n-1)(n-2)` and `|eta_ij|<=8`, it only gives
   `log h_n<=M(M-1)log 8`. On all 29 official orders, the resulting upper
   envelope for `17log f_n` exceeds even the largest middle-field C36 budget
   (at `p=6^(n/4)`) by a factor greater than `16,000,000`. This does not rule
   out a structured factorization or local-valuation use of the discriminant;
   it rules out the naive global height endpoint.
6. Ordered quotient lifts overcount a cluster by `qr` rather than the desired
   `q(r-1)`. The direction is safe and is stated; no equality is claimed.
7. `K_i` contains `J_i`, so its norm divides the old norm. This establishes
   `f_n|e_n` and proves the exceptional set is refined, not merely renamed.

The exact order-eight cutoff-two fixture independently computes both ideal
norms and finds `e_8/f_8=5^8`. Among eight split-prime fixtures, `Y>0` occurs
exactly at `p=17,41`, exactly the official primes dividing `f_8`. This is a
mechanism replay, not evidence about cutoff eighteen at official orders.
