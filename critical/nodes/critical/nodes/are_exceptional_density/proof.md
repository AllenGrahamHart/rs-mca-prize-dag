# are_exceptional_density proof

For each non-quotient pair `(B,B')`, let

```text
N_{B,B'} = Norm(e1(B) - e1(B')).
```

By `collision_norm_criterion`, a collision modulo a row prime `p` can occur
only when `p | N_{B,B'}`. The same node gives a uniform height bound

```text
|N_{B,B'}| <= H
```

for the relevant bounded-height family.

The number of distinct rational prime divisors of a nonzero integer of size
at most `H` is at most `log_2 H`. Therefore

```text
sum_p #collisions(p)
  <= sum_{B != B'} omega(N_{B,B'})
  <= #pairs * log_2 H.
```

Restricting the left side to any dyadic prime range only decreases it. Hence,
for any collision threshold `T`, the number of primes in that range with at
least `T` collisions is at most

```text
(#pairs * log_2 H) / T.
```

Taking `T` to be the row's collision-lightness threshold gives the stated
poly-sized exceptional set. This is an almost-all-primes statement only; it
does not certify that a specific official prime avoids the exceptional set.
