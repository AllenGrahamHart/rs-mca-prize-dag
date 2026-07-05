# conditional: petal_mixed_amplification_step

## Predicate node

- `petal_residue_line_uniformity`

## Claim

Conditional on residue-line uniformity, the full-petal bound at excess `c`
implies the corresponding bound at excess `c+1` with polynomial constants
controlled uniformly in `c` throughout the corridor range.

## Proof

Use the proved `l1_coset_chart_residue_bridge` coordinate system. In that
chart, the new full-petal configurations appearing when the cofactor excess
passes from `c` to `c+1` are accounted for by the residue-line kernel

```text
K_{I,d} = ker(pi_{>d} R_{I,d})
```

at the next value of `d`.

The predicate `petal_residue_line_uniformity` says precisely that, over the
whole corridor range, the exact realizable full-petal extras controlled by
this residue-line kernel are bounded by a polynomial whose exponent is
independent of `c`. The ambient kernel itself is only known to obey the proved
linear Lemma 13 ceiling `dim K <= c+1`; literal ambient flatness is not used.

Assume the full-petal count at excess `c` is bounded by a polynomial `P(n)`
with exponent independent of `c`. The excess `c+1` layer is the old
excess-`c` contribution plus the residue-line extras introduced at the next
layer. The first term is bounded by `P(n)` by hypothesis; the second is
bounded by the uniform polynomial supplied by `petal_residue_line_uniformity`.
Their sum is still polynomial with exponent independent of `c`.

Thus residue-line uniformity supplies the desired mixed-amplification
transition. The remaining mathematical content of the petal branch is the
uniformity predicate itself.
