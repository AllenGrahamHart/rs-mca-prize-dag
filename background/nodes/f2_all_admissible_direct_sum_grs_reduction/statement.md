# All-admissible F2 bounded-class direct-sum reduction

- **status:** REFUTED
- **closure:** counterexample

The claim that every official `n=2^41` admissible row decomposes each
antipodal F2 window into at most four prime-field proportionality classes is
false.

An official generating counterexample is

```text
p=2^61-1,
q=p^2,
ord_(2^41)(p)=2=[F_q:F_p].
```

Here `p=-1 mod 2^41`, so the intersection of the dyadic root group with
`F_p^*` is only `{+1,-1}`. After choosing one representative from each
antipodal pair, all `2^40` positions are distinct proportionality classes.
Thus the asserted bound `C<=4` fails with `C=2^40`.

The correctly scoped `p=1 mod 4` direct-sum theorem remains PROVED.

## Addendum (2026-08-07, wave-47 integration, coordinator)

The refutes edge is retargeted per the F2 auditor (the in-place
f2_admissible_object flip was REJECTED; the five-class correction
lives as addenda on canonical's node + the classification node).
