# Proof

Every nonzero relation `c in K` contains a primitive support restriction. If
that restriction is not all of `c`, subtract it. The remainder has disjoint
support, still belongs to `K`, and has smaller support. Induction therefore
partitions `c` into pairwise support-disjoint primitive relations with matching
signs.

Let `I` be the independence polynomial of the primitive relations, evaluated
at activity `z(p)=2^(-|supp(p)|)`: sum the product of the activities over every
pairwise support-disjoint collection. The union map from such collections to
relations can have multiple preimages, but the preceding decomposition shows
that every relation has at least one preimage. Activities multiply on disjoint
supports, so

```text
Z <= I.
```

Dropping the disjointness restriction only enlarges the sum. Hence

```text
I <= product_(primitive p) (1+z(p))
  <= exp(sum_(primitive p) z(p))
  = exp(P),
```

where the second inequality is `1+x<=e^x`.

At one DLI level, each zero coefficient has two fused source states and each
nonzero sign has one. A relation of support weight `w` therefore represents
`2^(N-w)` of the `4^N` source states. If `A_total` is the zero-fiber count,

```text
A_total = sum_(c in K) 2^(N-|supp(c)|) = 2^N Z.
```

The banked normalization is

```text
E = q^ell A_total/4^N = (q^ell/2^N) Z = rZ.
```

The actual signed-shift orbit of a primitive relation has size at most `2N`.
Thus the raw convention charging every primitive orbit by `2N 2^-w`
dominates the direct primitive activity sum `P`. This proves
`E<=r exp(W_full)`.

Multiplying over the tower and using `N_j=256 ell_j` and
`sum_j ell_j=t` gives

```text
product_j E_j
 <= exp(sum_j W_full,j) product_j r_j
 = exp(sum_j W_full,j) (q/2^256)^t.
```

The stated aggregate budget makes the logarithm of the right-hand side at
most `100 log(2)`, proving the final implication.

The full spectrum is load-bearing. The C1' counterexamples show that replacing
`W_full` by the fixed window `ell+1<=w<=ell+5` does not preserve a linear
residual bound.
