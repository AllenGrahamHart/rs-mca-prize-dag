# conditional: worst_word_challenger_pricing

## Predicate nodes

- `e22_two_class_exhaustion`
- `e22_challenger_staircase_pricing`

## Claim

Conditional on the two predicate nodes, the revised E15 challenger column is
classified and priced well enough for `worst_word_planted` and
`list_planted_arithmetic`.

## Proof

The node's obligation has two independent parts.

First, the revised worst-word statement must know that the E15 successor
family is exhaustive: after planted sunflower words are removed, every
low-slack non-planted crossing word is a structured challenger of the
mixed-petal or full-petal type. This is exactly
`e22_two_class_exhaustion`.

Second, the structured challenger class must be an explicit integer column.
The X-4 ledger identifies the mixed-petal anomaly with a quotient-coset
staircase family; `e22_challenger_staircase_pricing` is the missing formula,
injectivity/no-overlap proof, and row comparison.

Together these predicates say there is no unpriced third class and that the
known second class has an exact count. Hence the list-side consumers may use
the two-column inventory

```text
planted sunflower column + structured E15 challenger column
```

with no hidden assumptions. That is precisely the content required by
`worst_word_planted` and by the exact arithmetic reduction
`list_planted_arithmetic`.

## Evidence ledger

The local E15 gate was replayed on 2026-07-05 by

```text
python3 nodes/worst_word_challenger_pricing/notes/e22_gate_local.py
```

and reproduced the documented n=16, sigma=1 challenger: k=2,4,8 beat the
planted count by mixed/full-petal challengers and every gate cell had
UNCLASSIFIED=0. This supports the two-class predicate but does not prove it.

The detached E22 Modal run recorded in `notes/e22_reconstruction.md` was
canceled at 130/135 cells and did not emit a complete `E22_RESULTS` line in
the retrieved logs. It is therefore not used as a closure certificate.
