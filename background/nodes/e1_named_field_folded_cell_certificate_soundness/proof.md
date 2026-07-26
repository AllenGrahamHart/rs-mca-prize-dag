# proof: e1_named_field_folded_cell_certificate_soundness

Fix `N' in {128,256}`.

The E1 cell payload asks for a named exhibit field, a primitive `N'`th root
for the folded equation, and a complete certificate excluding every nonzero
non-cyclotomic folded vector in `{-2,-1,0,1,2}^{N'/2}`.

The proved field node supplies the first two pieces: a prime field `F_p` with
`p = 1 mod N'` and a displayed primitive `N'`th root. The corresponding
no-vector payload supplies the remaining piece: a complete certificate, over
that exact named field/root, whose result count is zero.

Combining those records gives exactly the cell schema: named field, primitive
root, complete folded certificate, and zero nonzero folded vectors. Hence the
cell payload holds.
