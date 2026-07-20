# Proof - L1 fixed-support codeword quotient bound

Every codeword in `Z_X` agrees with the same received word on `X`. Therefore
`P-P_0` vanishes on all `h` distinct points of `X`, and

```text
L_X | P-P_0.                                            (1)
```

Both codewords have degree at most `k-1=N`, so the quotient in `(CQ1)` has
degree at most `N-h`. Equality of two quotient images gives equality of the
two codeword differences and hence of the codewords, proving injectivity.
If `h>N`, a nonzero degree-at-most-`N` difference cannot vanish on `X`, so
the cell is a singleton. The target polynomial space has
`q^(N-h+1)` elements when `h<=N`, proving `(CQ2)`.

For the aggregate, orient every source petal as sparse or dense and record
the at most `P_0` exceptional points. The number of exact petal-support
patterns with `p<=P_0` is at most

```text
2^M(P_0+1)n^P_0.                                       (2)
```

On `(CQ3)`, each pattern contributes at most `q^(E+1)`. Using

```text
2^M<=n^(1/c_0),       q<=n^gamma                       (3)
```

gives `(CQ4)`. No defect-degree or syndrome multiplier is needed: a
reconstructed codeword determines its exact missed core, numerator, and
background agreements.

Finally `N=d+a` and `h=d+s`, so

```text
N-h=a-s.                                               (4)
```

Every fixed upper bound on this quantity is paid by `(CQ4)`, which proves
`(CQ5)`.
