# discharged conditional: m720_mitm_gate

## Predicate nodes

- `m720_mitm_enumerator_soundness`
- `m720_ground_truth_replay`

## Claim

The banked small-count replay is now proved by `m720_ground_truth_replay`, so
this conditional has been discharged.

## Proof

The predicate `m720_mitm_enumerator_soundness` proves that the `mitm_slice`
enumerator in `nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py` is an exact
anchored meet-in-the-middle enumerator for the declared window: every counted
pair is a disjoint anchored trade with matching lower elementary signatures
and unequal top coefficient, and every such pair whose support lies in the
window is counted.

The predicate `m720_ground_truth_replay` supplies the remaining empirical gate:
the same arithmetic machinery reproduces the banked h=3,4,5 small-cell census
facts used to calibrate sensitivity and toral/non-toral classification.

Together, soundness plus ground-truth replay show that the scanner detects the
known small-h facts and classifies paid/toral versus non-toral active cores as
required by `m720_mitm_gate`.
