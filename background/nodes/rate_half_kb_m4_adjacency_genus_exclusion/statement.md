# KoalaBear m4 adjacency-genus exclusion

- **status:** PROVED
- **scope:** sole surviving inner-degree-four transverse type
- **dependencies:** `rate_half_kb_q6_u2_primitive_subdegree4_route_cut`,
  `rate_half_kb_source_pencil_rank_transverse_compiler`,
  `rate_half_kb_m4_a6s6_genus_zero_passport_reduction`
- **consumer:** `rate_half_band_closure`

Let `Gamma_0` be an actual residual source component of bidegree `(2,4)`.
The proved source descent maps its normalization birationally to the
bidegree-`(4,4)` endpoint self-correspondence component `Gamma`. In the sole
surviving inner-degree-four route, `Gamma` maps with degree two to the
outer `r=8` component `C` of a degree-15 map with geometric monodromy `A6`
or `S6` on the two-subsets of six letters.

The `r=8` orbital consists of ordered adjacent two-subsets. It has 120
states and is transitive for both `A6` and `S6`. For the four exhaustive
outer passports, the induced branch indices and genera of `C` are

```text
passport                                             index   genus(C)
S6: 5.1, 2.1.1.1.1, 6                                 244       3
S6: 5.1, 2.2.2, 3.2.1                                 250       6
A6: 5.1, 2.2.1.1, 4.2                                 246       4
S6: 5.1, 2.1.1.1.1, 2.2.1.1, 2.2.2                  264      13
```

The normalization of `Gamma_0` has genus at most
`(2-1)(4-1)=3`. Since the challenge characteristic is odd, the degree-two
map `Gamma -> C` is separable. Riemann--Hurwitz requires

```text
g(Gamma) >= 2*g(C)-1,
```

whose weakest lower bound is five. This contradicts `g(Gamma)<=3` in all
four passports. Therefore the complete inner-degree-four transverse row is
empty. The independent transverse frontier consists only of the three
`m=2` and five `m=3` types.

## Falsifier

A nontransitive ordered-adjacency action; an incorrect induced branch index;
a fifth passport; failure of the actual `(2,4)` component to be birational
to `Gamma`; component-to-image degree other than two; or inseparability in
the challenge characteristic.
