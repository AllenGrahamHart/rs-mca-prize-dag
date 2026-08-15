# Audit

1. Every defect in `0..q` is generated at each support `2..5`.
2. `s=q` contributes zero circuits at its own support.
3. Every inherited and valid cross-support cap is retained.
4. The collision cap is applied only at supports `2..5`.
5. The joint cap is applied exactly when `s_4+s_5<q`.
6. All 120 high-support choices are generated before compression.
7. Pareto compression removes only componentwise dominated vectors.
8. Both implementations recover frontier sizes `1,1,7` on every row.
9. Every deficit weight, kernel corank, and rank-nine mark is retained.
10. All six safe signs and the adjacent wall sign are replayed exactly.
