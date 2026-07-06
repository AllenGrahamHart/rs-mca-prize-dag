# proof: m720_mitm_gate

The proved predicate `m720_mitm_enumerator_soundness` establishes the scanner's
exactness contract: every counted window pair is a disjoint anchored trade with
matching lower elementary signatures and unequal top coefficient, every such
window-contained anchored trade is counted, toral pairs are classified exactly,
and incomplete window slices are not marked complete.

The proved predicate `m720_ground_truth_replay` supplies the calibration table
showing that the same arithmetic detects the banked h=3,4,5 rows, including
the exceptional h=4 non-toral detection row and the h=5 n=32 row.

Sound enumerator semantics plus exact ground-truth replay prove that the MITM
scanner detects the known small-h calibration facts and distinguishes toral or
paid cores from non-toral active cores. Therefore `m720_mitm_gate` is `PROVED`.
