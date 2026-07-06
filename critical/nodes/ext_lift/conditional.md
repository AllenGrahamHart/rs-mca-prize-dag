# ext_lift conditional proof

## Predicate nodes

- `f1_classification`

Evidence/support edges:

- `b_rational_lift`
- `f1_case_pole`
- `f1_case_tower`

## Claim

The extension lift has no content beyond the F1 trichotomy and the three case
pricing inputs.

## Proof

The predicate `f1_classification` partitions every F-valued bad slope above
the reserve into exactly three classes: B-rational, pole-type, or
intermediate-subfield/tower-confined, and it records that the three classes are
priced by their ledgers.  Its own proof packet consumes `b_rational_lift`,
`f1_case_pole`, and `f1_case_tower`.

Therefore `ext_lift` needs no second direct copy of those case ledgers.  Once
`f1_classification` holds, the extension-lift classification follows by
reading off the already-priced trichotomy.  The historical direct edges from
the case ledgers, plus `ext_import` and `generating_escape`, are evidence for
the F1 packet rather than logical predicates of this assembly step.

The remaining open mathematics stays in the predicate node, not in `ext_lift`.

## Weakening

WEAKENING 2026-07-06: the direct edges
`b_rational_lift -> ext_lift`, `f1_case_pole -> ext_lift`, and
`f1_case_tower -> ext_lift` are evidence rather than logical requirements.
The transitive dependency remains through `f1_classification`, whose statement
already packages the priced trichotomy.
