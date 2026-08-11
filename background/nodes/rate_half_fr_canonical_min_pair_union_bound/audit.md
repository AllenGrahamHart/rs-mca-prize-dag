# Audit

1. `W*` is a pair union, not an arbitrary set of the same cardinality.
2. The quantified slope `gamma` is distinct from the minimizing pair. Those
   two pair members are the type-1 slopes and are not charged by `(FRC2)`.
3. The first inequality may double-count the triple intersection. This only
   enlarges its right side and is safe for an upper bound.
4. Defects are retained exactly in `(FRC2)--(FRC3)` before the clean endpoint
   specialization.
5. No saturation or realizability premise appears in the proof. Those
   premises enter only when the set identity is consumed by the pencil
   ledger.
6. The older incidence fence remains valid for arbitrary `W`; its distinguished
   witness set is not a pair union. It does not contradict this theorem.
7. `verify.py` exhausts all three-set families on five points.
   `verify_audit.py` independently exhausts all four-set families on four
   points and every minimizing pair.
