# Proof

The vendored certificate fixes four rational Hermite rows `h_0,...,h_3`.
Since the moment vector is

```text
(1, 16, 256+V, 4096+48V+M_3),
```

each of the three resulting form coefficients is affine in `(V,M_3)`.  The
coefficient of `log(2)` is independently reconstructed as

```text
(-7488 V + 128 M_3 - 270521) / 2544224,
```

so the complete margin is affine as well.

Both verifiers enclose `log(2)`, `log(8/7)`, and `log(64/57)` by rational
partial sums of

```text
log(x) = 2 sum_{j>=0} y^(2j+1)/(2j+1),  y=(x-1)/(x+1),
```

with an explicit positive geometric tail.  The upstream verifier uses 40
terms.  The independent local audit uses 53 terms and reconstructs the form
without importing upstream code.

Applying the sign-correct lower and upper logarithm bounds gives:

1. an exact negative upper bound for one unit of `M_3`, proving strict
   monotonicity;
2. a positive lower margin at each of `1947,1732,1517,1302,1087` and a
   negative upper margin one integer later at `V=68,66,64,62,60`;
3. exact derivative bounds placing the affine boundary slope in `(107,108)`;
4. a negative upper margin at `(V,0)` for every even `V` from `2` through
   `48`; and
5. positive lower margin at `(50,13)` and negative upper margin at `(50,14)`.

Monotonicity turns item 4 into the claimed method boundary whenever the
chamber maximum satisfies `M_3^max>=0`.  It does not turn the failed majorant
into a statement about whether the chamber is empty or whether its exact
cyclotomic norms can meet an official prime.
