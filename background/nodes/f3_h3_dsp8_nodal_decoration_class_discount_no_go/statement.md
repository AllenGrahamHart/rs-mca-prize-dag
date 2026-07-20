# DSP8 nodal decoration class-discount no-go

- **status:** PROVED
- **closure:** exact finite counterexample
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_unit_product_trace_normal_form`,
  `f3_h3_dsp8_nodal_target_divisor_pruning`

There is no row-independent `4/9`, `5/9`, or `2/3` cap on the fraction of
antipodal decorations contributed by one signed-disjoint pair of singular
product-one triples, even after imposing the live `P>=25` richness and
nonidentity quotient-support predicates.

The exact fixture is over `F_769`. Let `H=<562>` have order 256 and put
`A=(1-H)\{0}`. The two triples

```text
U={218,643,680},       V={94,679,768}
```

have product one, common trace three, and twelve distinct signed coordinates.
Thus they lie on the singular trace `sigma=3`. For distinguished roots
`r in U`, `s in V`, put

```text
t_(r,s)=1-rs(3-r-s).
```

All nine targets are nonzero and nonidentity, have `P(t)>=72` and `R(t)>=79`,
and therefore survive the DSP8 richness and quotient gates. Exactly seven of
the nine satisfy `1-t in H^2`, so exactly seven are antipodal.

This fixture has `769<256^2`. It does not falsify DSP8, its official
`p>=n^2` scope, or a class discount that genuinely uses that size hypothesis.
It proves that a nodal class discount cannot come from the nine-decoration
packet, signed disjointness, richness, and quotient support alone.
