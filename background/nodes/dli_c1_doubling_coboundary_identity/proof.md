# Proof

## (i) The identity

From `1 + x = (1 - x^2)/(1 - x)` factor-by-factor:

```text
A(C) D(C) = prod_(h in H) (1 + zeta^(ch))(1 - zeta^(ch))
          = prod_(h in H) (1 - zeta^(2ch)).
```

As `h` runs over `H`, `2ch` runs over the coset `2cH`, so the right side
is `D(2C)`. Every factor of `D(C)` is nonzero (`ch != 0 mod q`), so
division is legitimate. QED (i).

## (ii) Positivity and telescoping

`-1 in H` pairs `h` with `-h`:
`(1 - zeta^(x))(1 - zeta^(-x)) = |1 - zeta^x|^2 > 0`, and likewise for
`A`. Taking logarithms, `(DB-1)` reads
`log A(C) = L(sigma C) - L(C)` — an exact coboundary — and summing around
any `sigma`-orbit telescopes to zero, giving `(DB-2)`. QED (ii).

## (iii) Consumer form

With `|H| = 2N` and `omega^N = -1`, the second half of the orbit consists
of the negatives of the first, so

```text
A(C) = prod_(i<N) (1 + zeta^(c omega^i))(1 + zeta^(-c omega^i))
     = prod_(i<N) |1 + zeta^(c omega^i)|^2
     = prod_(i<N) 4 cos^2(pi c omega^i / q) = 2^(2N) T(c).
```

`T` is constant on cosets. Summing over `F_q^* = union of (q-1)/(2N)
cosets of size 2N`:

```text
sum_(t != 0) T(t) = 2N * 2^(-2N) sum_C A(C)
                  = (q-1) 2^(-2N) avg_C A(C).
```

Parseval gives `sum_s mu(s)^2 - 1/q = q^(-1) sum_(t != 0) T(t)`, and
`X = Z - 2^N/q = 2^N (sum_s mu(s)^2 - 1/q)`; combining yields `(DB-3)`,
and `(DB-4)` is `(DB-3)` with `X <= 4`. QED (iii).

## (iv) Small orbits

If the class of `2` has order `r` in `Q`, then `2^r in H`, so
`(2^r)^(|H|) = 1` in `F_q^*`, i.e. `q | 2^(|H| r) - 1`. At `r = 1`,
`2C = C` for every coset, so `(DB-1)` gives `A(C) = D(C)/D(C) = 1`, and
`(DB-3)` evaluates `X` exactly. QED (iv).
