# ext_lift conditional proof

## Predicate nodes

- `f1_classification`
- `b_rational_lift`
- `f1_case_pole`
- `f1_case_tower`

## Claim

The extension lift has no content beyond the F1 trichotomy and the three case
pricing inputs.

## Proof

The predicate `f1_classification` partitions every F-valued bad slope above
the reserve into exactly three classes: B-rational, pole-type, or
intermediate-subfield/tower-confined.

The B-rational class is priced by `b_rational_lift`. The pole class is priced
by `f1_case_pole`, whose own dependencies carry the imported extension-pole
list bridge. The tower-confined class is priced by `f1_case_tower`.

These classes are exhaustive by `f1_classification`, so assembling the three
case ledgers proves the extension-lift classification. The remaining open
mathematics stays in the predicate nodes, not in `ext_lift`.
