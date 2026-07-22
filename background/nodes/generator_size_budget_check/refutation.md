# Refutation

Write `N'=128` and partition `mu_128` into its 64 antipodal pairs

```text
P_j={zeta^j,-zeta^j},       0<=j<64.
```

A signed-8 core chooses eight pair indices and one endpoint from each. The
construction then chooses 28 of the remaining 56 antipodal pairs as padding,
so every resulting subset has size

```text
8+2*28=64.
```

For a fixed core `C`, every padding `T` satisfies

```text
e_1(C union union_(j in T)P_j)
 =e_1(C)+sum_(j in T)(zeta^j-zeta^j)
 =e_1(C).                                             (1)
```

Hence the `binom(56,28)` subsets attached to `C` are not pairwise distinct
under `e_1`; every pair has zero difference. Zero is not a nonzero
height-budget unit times an element of a multiplicative semigroup in
`F_q^*`, and these repeats cannot certify a value-set lower bound.

There are only `19 binom(64,8)` named signed cores in the proposal, so this
is an upper bound on its distinct `e_1` values. Direct integer comparison
gives `(GSB2)`. The bound `(GSB3)` allows every possible sign pattern and is
still smaller than `2^89` by nearly 49 bits. Therefore no choice of the 19
patterns, and no deduplication of the proposed family, repairs its budget.
QED.
