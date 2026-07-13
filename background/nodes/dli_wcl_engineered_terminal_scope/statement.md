# DLI engineered terminal witness scope

- **status:** PROVED
- **closure:** computation

## Statement

For `z` of order `512`, put

```text
P(z) = 1-z^33+z^40-z^136-z^143+z^145.
```

Its exact cyclotomic norm is

```text
Norm(P) = 122312418397310579415219240127455896396372121843316076135243835573788121252866
        = 2 * 61156209198655289707609620063727948198186060921658038067621917786894060626433.
```

The 256-bit factor is prime and has `v_2(q-1)=9`. Thus this banked
weight-6 construction produces an exact order-512 terminal relation but no
prime factor of its norm can host the production ambient subgroup of order
`2^41`.

## Falsifier

A different exact resultant, a composite displayed factor, an incomplete
factorization, or `2^41 | q-1` for one of the prime factors.
