# Audit

1. `rank(ev_T)=10` and `rank(ev_B)=8` make `ev_{x,y}|_U` invertible.
2. The two received columns are solved separately, so one coordinate pair
   determines one point of the affine `U^2` owner flat.
3. Coordinate pairs outside the fixed nine-set are counted once, giving
   `C(n'-9,2)` rather than `C(n',2)`.
4. The factor `981105` counts records per fixed owner, not owner points.
5. The output retains `(record,T)` multiplicity and is compatible with the
   weighted concentrator.
