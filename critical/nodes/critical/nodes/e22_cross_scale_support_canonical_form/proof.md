# proof: e22_cross_scale_support_canonical_form

Fix a support `R` inside the multiplicative subgroup domain. For a divisor
`M` of the domain size, the quotient map `x -> x^M` partitions the domain into
fibers of size `M`.

Define `F_M(R)` to be the union of all quotient fibers fully contained in
`R`, and define `B_M(R)=R\F_M(R)`.

If `R` has a staircase representation at scale `M`, then

```text
R = B union (full selected M-fibers),    |B| < M.
```

Every selected full fiber is contained in `R`, so it is included in `F_M(R)`.
Conversely, the tail `B` has size `<M`, so it cannot contain an additional
entire `M`-fiber. Hence the fibers fully contained in `R` are exactly the
selected fibers, and the leftover set is exactly the tail:

```text
F_M(R) = union selected fibers,
B_M(R) = B.
```

This is the fixed-scale recovery argument applied simultaneously to every
divisor `M`. Thus, given only `R`, the candidate tail-plus-full-fibers scales
are exactly those with `|B_M(R)|<M`, and the recovered tail and selected
fibers at each such scale are uniquely determined. Some candidate scales may
have no selected full fibers; this node only proves canonical recovery, while
nondegeneracy and pricing are deferred to
`e22_cross_scale_pricing_multiplicity`.

If two cross-scale staircase representations have equal support, they are
therefore sent to the same canonical object:

```text
(R, {M : |B_M(R)|<M}, {B_M(R), selected M-fibers}_M).
```

This proves canonical support-scale recovery. Pricing the resulting canonical
classes is the remaining node `e22_cross_scale_pricing_multiplicity`.
