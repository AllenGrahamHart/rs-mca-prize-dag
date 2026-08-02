# Proof

For each of the five primitive residue factors, the exact norm program
reconstructs `b,x0,x1,r,c` and computes resultants for the 22 common guards,
eight outside squared-incidence guards, and two chart denominators.  For each
rational norm it returns canonical numerator and denominator polynomials in
`F_p[t]`.  It computes their complete rational-root sets as

```text
gcd(f(t),t^p-t).
```

The standard-library checker independently replays this gcd for all 160 norm
records.  It obtains 18 numerator roots, three denominator roots, and 14
values after removing `F_bad`.

The pole census parses every rational denominator from the six named source
categories.  In particular, all 907 `//(...)` occurrences in the sealed
18-polynomial basis are parsed by a restricted polynomial AST rather than by
string evaluation.  Nemo computes the complete `F_p` root set of each unique
denominator by the same exact Frobenius-gcd criterion.  The local checker
reconstructs all source denominator multisets from their hash-pinned packets,
checks every returned coefficient vector, multiplicity, degree, source hash,
program hash, and listed root, and obtains the 61-value union.  Removing
`F_bad` leaves 56 values.

The two checkers return their explicit sets.  Direct set union gives

```text
14+56-1=69
```

and canonical sorted decimal serialization gives the digest in the
statement.

Outside this union, the monic squared-pair basis, primitive factorization and
coordinate maps, chart reconstruction, guard localization, and colored
Bezout identity all specialize without a pole or failed unit hypothesis.
The generic exclusion identity then remains valid over the deployed fiber.
Since its common factor is `1` or the target-collision guard `e^2-1`, no
admissible packet exists there.  Thus only the printed 69 fibers require
separate treatment. QED.
