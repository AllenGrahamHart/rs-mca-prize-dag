# proof: e22_dyadic_local_to_common_saturation

Work in the cyclic multiplicative subgroup domain `D` of dyadic size `n`.
Every admissible quotient modulus is a power of two. Hence the finite set
`{M_j}` is totally ordered by divisibility, and its minimum `M_*` divides
every `M_j`.

For a quotient modulus `M`, the fibers of

```text
pi_M(x) = x^M
```

are the cosets of the subgroup of `M`-th roots of unity in `D`.
If `M_* | M_j`, then the subgroup of `M_*`-th roots of unity is contained in
the subgroup of `M_j`-th roots of unity. Therefore each `M_j`-fiber is a
disjoint union of `M_j/M_*` fibers of `pi_{M_*}`.

Each local non-tail block `S_j` is, by hypothesis, a union of full
`M_j`-fibers. Replacing every such fiber by its decomposition into
`M_*`-fibers shows that every `S_j` is also a union of full `M_*`-fibers.
Taking the union over `j` preserves that property, so

```text
S = union_j S_j
```

is saturated on full fibers of `x -> x^{M_*}`.

Finally, every local modulus satisfies `M_j > t`, so the minimum local modulus
also satisfies `M_* > t`. The fixed tail `B` is unchanged throughout this
argument; the lemma only glues the non-tail saturated blocks to one common
dyadic quotient modulus.
