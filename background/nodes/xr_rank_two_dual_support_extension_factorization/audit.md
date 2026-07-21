# Audit

1. `Z_i` and `T_i` are each disjoint from `S_i`, but they need not be
   disjoint from each other.
2. The exact extension size is `h-d-1+z_i`; dropping the `-1` changes the
   cofactor degree.
3. Equality of the cofactors uses equality of the same normalized extended
   row on `S_i`, plus at least `a+1` support points.
4. Both degree bounds land at `d-z_i`, so interpolation uniqueness is strict.
5. Root avoidance on `S_i` is necessary for the claimed support to be exact.
6. The converse is only at the dual-codeword level. It does not reconstruct
   the received pair or certify that `A_i` is an agreement block.
7. The certificate applies to both the dual-`GRS_3` and quadric-centroid
   coefficient branches without altering either coefficient atlas.
8. No Modal or candidate-row computation is used.
