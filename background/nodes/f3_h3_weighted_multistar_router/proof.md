# Proof

Let `a` be the number of squared-distance-four edges and `b` the number of
squared-distance-six edges among the selected seven vectors. The proved
distance-two exclusion and parity of every squared distance show that all
other pairwise distances are at least eight. The centroid identity gives

```text
4a+6b+8(21-a-b)
  <= sum_(i<j)||v_i-v_j||^2
   = 7 sum_i ||v_i||^2-||sum_i v_i||^2
  <= 7*21=147.
```

Consequently

```text
2a+b>=11.                                           (1)
```

Regard the seven vectors as a graph whose distance-four edges have weight two
and whose distance-six edges have weight one. Its total edge weight is the
left side of `(1)`. The sum of the seven weighted degrees is at least `22`, so
some vertex has weighted degree at least four. Starting with that vertex,
choose a minimal set of incident edges whose weight reaches four. Every edge
has weight one or two, so the set has between two and four leaves. This proves
`(WMS1)`.

All selected shifted products have one common residue at the degree-one row
prime

```text
P=(p,zeta_n-g).
```

Every shifted product is divisible by `pi^2`. The ideal-batching argument,
applied to all selected leaves, therefore gives

```text
(beta_(F_i)-beta_E : 1<=i<=r) subset (pi)^2 P.
```

Dividing by `(pi)^2` proves that the ideal in `(WMS2)` is contained in `P`.
Ideal norms reverse divisibility under inclusion, hence

```text
p=N(P) divides N(K_(E;F_1,...,F_r)).
```

For each generator `gamma_i=(beta_(F_i)-beta_E)/pi^2`, the principal ideal
`(gamma_i)` is contained in `K`. Therefore `N(K)` divides every
`|Norm(gamma_i)|`. This proves `(WMS3)`. Taking any two leaves shows that `K`
contains the corresponding two-generator star ideal, so its prime divisors
form a subset of the existing two-leaf candidate union.

It remains to prove the fixed-root sieve. Because `p=1 mod n`, the primes over
`p` are

```text
P_s=(p,zeta_n-g^s),       s mod n odd.
```

The ideal `K` has norm divisible by `p` exactly when it is contained in one
`P_s`, which is equivalent to

```text
beta_E(g^s)=beta_(F_1)(g^s)=...=beta_(F_r)(g^s).
```

Odd dilation by `s` preserves coefficient-vector norms, distances, and edge
weights, and sends evaluation at `g^s` to evaluation of the dilated pairs at
`g`. Taking the union over admissible multistars therefore removes the
quantifier over `s`. At the fixed root, the displayed equality says exactly
that one product fiber contains a vertex of weighted degree at least four.
This proves the sieve and the theorem. QED.
