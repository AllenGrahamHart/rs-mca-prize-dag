# Proof

Let `A` be the selected explanations with deficit greater than `H`; these
are exactly the top-third explanations with missed-coordinate allowance at
most `s`. Let `D` be the exact boundary layer of deficit `H`, whose missed
allowance is `s+1`.

If `|A|<=1`, the prefix argument through `H` charges every explanation
outside `A` by `P_H`. Every top-third explanation owns at most one selected
slope, so `A` contributes at most one. This gives `|Z|<=P_H+1`.

Suppose instead that `|A|>=2`, and fix distinct anchors `a,b` in `A`. For
any `c` in `D`, the three agreement supports satisfy

```text
|S_a intersect S_b intersect S_c|
  >= e-s-s-(s+1)
   = K+q-1
  >= K.
```

On this intersection the normalized pair differences for `(c,a)` and
`(c,b)` both equal the gauged direction. They are degree-`<K` codewords, so
restriction injectivity makes them identical. The same synchronization
argument as in the top-third global-line theorem therefore places `c` on
the affine codeword line already containing `a`, `b`, and all of `A`.
This holds for every `c` in `D`.

The guard `2(s+1)<e` also ensures that every explanation in `A union D`
owns at most one selected slope. Consequently `A union D` is one
pair-noncontained affine codeword line. Its
total common agreement core has size at most `m-1`, and the off-core
agreement sets are disjoint, so the parent line-packing argument gives

```text
|A union D| <= N-m+1=t+1.
```

The remaining deficits are at most `H-1`. Applying the independently
truncated suffix-minimum prefix profile through `H-1` gives
`|Z|<=P_(H-1)+(t+1)`. Taking the larger of the two exhaustive cases proves
`(BA1)`.

At the official Mersenne support, `e-K=98224=3*32741+1`; hence the mixed
triple intersection has exactly `K` guaranteed coordinates. Exact integer
evaluation of the two prefix profiles gives the printed totals. The primary
verifier recomputes every cap through `H`; the independent audit reconstructs
the two profiles without importing the primary implementation and checks
hostile mutations.
