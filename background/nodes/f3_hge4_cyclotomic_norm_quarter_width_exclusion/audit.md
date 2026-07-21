# Audit

## Forward audit

1. Top-shift equality gives the first `h-1` power-sum congruences because
   `p>h`.
2. Primitivity makes the characteristic-zero first power-sum difference
   nonzero; otherwise odd Fourier inversion gives a common antipodal
   stabilizer.
3. Complete splitting of `p` in the dyadic cyclotomic field turns the odd
   congruences into `floor(h/2)` distinct prime-ideal divisors of one norm.
4. Odd-frequency Parseval gives the exact energy `sum(f_t-f_(t+m/2))^2` and
   the AM--GM norm upper bound.
5. The only generic inequality gap is `h=m/4+1`. The Belyi midpoint degree
   excludes zero loss, and the second power sum excludes loss two.
6. The remaining parity cases reduce to the printed elementary inequalities.

## Consumer-backward audit

The exact-ratio compiler needs a uniform level sum. This theorem deletes only
the interval `m/4<=h<m/3`; it contributes zero debit there and leaves the
lower-quarter sum unchanged. No scalar trace count, pencil-fiber estimate, or
fixed-prime computation is imported into the proof.

## Scope checks

- `p>=n^2` and `m|n` imply `p>=m^2`; primality makes this strict.
- The Belyi dependency is invoked only where `m=3h+e` with `0<e<h`.
- The equality width `h=m/4` is handled without Belyi.
- No claim is made for `m<16`, which supplies no live HGE4 width in this
  interval.

## Independent replay

The main verifier checks every claimed parity inequality through `m=8192`,
exhausts the first finite level `(m,p)=(16,257)`, and checks DAG wiring. The
audit verifier independently exercises the two delicate mutations: omitting
the four-unit energy saving at `h=m/4+1`, and weakening `p>m^2` to equality.
