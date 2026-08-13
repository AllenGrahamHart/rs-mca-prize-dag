# Proof

Minimality makes both coefficient families linearly independent. The
`A_j` have no nonconstant common factor. A common finite root would divide
every exact degree-`m` row polynomial; all row roots are simple members of
`Gamma`, and the common root would make the complete parameter fiber zero.
Exact row degree excludes a common basepoint at infinity. Hence `a` is a
basepoint-free morphism with

```text
a^*O(1)=O_(P^1)(m).                                 (1)
```

Let `d` be the degree onto the normalization of the image and let `c` be
the image degree. Pullback of a generic hyperplane gives

```text
m=dc,                                                (2)
```

so `d|m`.

For `delta in Gamma`, let `I_delta` be the actual `U_0` incidence set.
The all-excess factorization and Shape-A ledgers give

```text
|I_delta|=n-a_delta-r_delta,
sum_delta(a_delta+r_delta)=2e-7.                    (3)
```

An empty actual column costs `n=(3e-7)/2`. Since

```text
2n=3e-7>2e-7,                                       (4)
```

at most one of the `3e` columns is empty. Write the active-column count as
`3e-z`, where `z in {0,1}`.

Factor `a` through the normalization of its image. Take an active slope
`delta` and an incident row `x`. The row hyperplane contains the image
point of `delta`, so its pullback contains the complete normalization fiber
through `delta`. That pullback is the official row polynomial
`G(t,x)`, whose roots are simple and all lie in `Gamma`. Thus the fiber
is reduced, consists of exactly `d` active slopes, and the active set is a
disjoint union of complete degree-`d` fibers. Therefore

```text
d | (3e-z).                                         (5)
```

Since `e=m+2`,

```text
3e=3m+6,       3e-1=3m+5.                          (6)
```

The official `m=183251937961` is coprime to both `6` and `5`. Combining
`d|m` with `(5)--(6)` gives `d=1` for either value of `z`. QED.
