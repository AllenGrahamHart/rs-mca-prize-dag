# F1 pole/tower same-rate scope router

- **status:** PROVED
- **closure:** proof
- **consumers:** clean-rate milestone audit; `f1_pole_list_threshold_location`
- **dependencies:** `f1_minimal_field_descent`, `interleaved_floor_import`

Let `D subset B subseteq K subseteq F` be the domain and fields in the F1
extension classification, put `n=|D|`, and fix the RS degree bound `kappa`.
The base and extension codes in the pole construction are

```text
C_B=RS[B,D,kappa],       C_K=RS[K,D,kappa].          (SR1)
```

Minimal-field descent, tower recursion, coordinate expansion, and the
extension-pole construction change the coefficient field but do not change
`D` or `kappa`.  Consequently every base-list threshold imported while
pricing an ambient row of rate `rho=kappa/n` is a threshold for a base row of
the same rate `rho`.

In particular, pole pricing for rates `1/4,1/8,1/16` consumes only the
corresponding clean-rate list crossings.  The rate-`1/2` list crossing is
needed only when the ambient row itself has rate `1/2`; it is not a premise
of the clean-rate extension column.

This is a rate-scope theorem.  It does not prove any list crossing, extension
upper bound, or prize row.
