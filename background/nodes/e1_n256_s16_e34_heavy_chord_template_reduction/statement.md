# E1 N=256 E=34 heavy-chord template reduction

- **status:** PROVED
- **closure:** proof

Let `H` be the three coefficient positions of absolute value two and `L` the
four positions of absolute value one in a pair-feasible `V=68` vector. Write
`||x-y||` for unoriented circular distance modulo 128. Then exactly one of the
following templates holds.

1. **Quarter template.** Up to translation and reflection,
   `H={0,32,64}`. The light position `96` is absent, the endpoint heavy
   coefficients are opposite, and `(D_64,C)=(16,-26)`.
2. **Diameter template.** `H` contains an antipodal pair but is not the
   quarter template. Its two non-diameter heavy-heavy lengths are distinct,
   and each corresponding distance class contains a heavy-light chord.
   Here `(D_64,C)` is `(16,-26)` or `(20,-24)`.
3. **Progression template.** `H` has no diameter and two heavy-heavy chords
   have equal length. Thus `H` is a circular three-term progression. The
   third heavy-heavy class contains a heavy-light chord. The repeated class
   also contains a heavy-light chord unless the two outer heavy coefficients
   are opposite.
4. **Generic template.** `H` has no diameter and its three heavy-heavy
   lengths are distinct. Every one of the three classes contains a
   heavy-light chord.

In the last two cases `D_64` is one of `0,4,8,12` and
`C=-34+D_64/2`. In particular the quarter template cannot realize
`(D_64,C)=(20,-24)`.

This theorem classifies forced equal-chord origins. It does not exclude any
of the four displayed templates or the residual `(6,7)` profile.
