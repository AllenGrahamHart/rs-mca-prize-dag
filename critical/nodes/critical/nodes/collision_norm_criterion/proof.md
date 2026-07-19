# collision_norm_criterion proof

Let

```text
alpha = e1(B) - e1(B') in Z[zeta_N].
```

If `B` and `B'` are not quotient-related, the proved node
`char0_collision_classification` says that `alpha != 0` in characteristic
zero.

For a prime ideal `frak-p` above the row prime `p`,

```text
e1(B) = e1(B') mod frak-p
```

is equivalent to `alpha in frak-p`, i.e. `frak-p | (alpha)`. Taking norms,
this implies that the rational prime `p` divides the nonzero integer

```text
Norm_{Q(zeta_N)/Q}(alpha).
```

Conversely, if a prime ideal above `p` divides `(alpha)`, then the same
congruence holds modulo that prime ideal. Thus finite-field collisions in
the non-quotient class are exactly divisibility events for this explicit
cyclotomic norm.

Finally, every archimedean conjugate of `alpha` is a difference of two sums of
`l'` roots of unity, so its absolute value is at most `2l'`. Hence

```text
|Norm(alpha)| <= (2l')^[Q(zeta_N):Q].
```

The unresolved zone-(b) problem is therefore reduced to counting prime
divisors of a bounded-height family of nonzero cyclotomic integers.
