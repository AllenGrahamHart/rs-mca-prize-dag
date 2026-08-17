# Proof

Subtract PR `#1173`'s complete paid envelope from the least unsafe integer
cardinality. This gives `(RM1)`. The row-space partition relative to the
fixed anchor is disjoint, so every uncharged record lies in a represented
nontransverse rank-one or rank-two group.

The proved rank-one group cap is `8147918`. The rank-two affine-container
cap is

```text
R_2=(n-A) floor(C(n-K+2,2)/C(A-K+2,2))
   =982651*252
   =247628052.
```

Thus every original group has at most `R_2` records, and `(RM1)` forces at
least `ceil(E_rich/R_2)=8106` distinct row spaces.

Fix a nontransverse rank-`r` group `U`. There is a proper subspace
`F<U^perp` containing at least `42453` labelled anchor-good evaluation
columns. Extend `F` by a fixed deterministic rule to a hyperplane
`H<U^perp`, and put `W=H^perp`. Then

```text
U<W,  dim W=r+1,
```

and every polynomial in `W` vanishes on those same actual coordinates.
Assign the complete `U`-group to `W`, and merge assignments with identical
`W`. The original row-space partition makes the resulting buckets disjoint.

Every pair difference in a bucket has both rows in `W`; hence all its pair
types lie in one two-fold affine `W`-container. They retain common agreement
at least `A`. The ordinary affine-span cap and sub-square common-support
interleaving collapse bound their pair types by `M_2=252` in dimension two
and `M_3=4023` in dimension three. Fixed-pair slope ownership multiplies by
`n-A=982651`, giving

```text
R_2=247628052,    R_3=3953204973.
```

Summing the disjoint buckets proves `(RM2)`. Since `R_2<R_3`, it also gives

```text
B_2+B_3 >= ceil(E_rich/R_3)=508,
```

proving `(RM3)`.

If several groups merge into one `W`, take the union of their selected rich
zero sets. The common `W` vanishes on that union, which still lies in the
anchor-good set. Every assigned pair equals the anchor pair there, and the
anchor equals the received pair. Thus every owning explanation has those
coordinates in its maximal support. The proved common-core adapter chooses
actual witnesses through the set, divides by its squarefree locator, and
preserves slopes and pair noncontainment. This shortening is bucket-local,
as claimed.
