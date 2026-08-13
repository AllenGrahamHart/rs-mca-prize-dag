# Cycle 267: rate-half Shape-A tensor-rank-three projective frame (2026-08-13)

The first successor to the rank-two exclusion is now exact. In a minimal
rank-three representation, a projective line in the coefficient plane owns
at most `n` domain rows. Since Shape A has `R=3n+7` rows, three
noncollinear coefficient rows leave at least seven choices for a fourth row
outside their three pair-lines.

The four split row polynomials form a circuit with all coefficients nonzero.
No slope can root three circuit rows: it would root the fourth and make the
complete parameter fiber zero. Therefore every slope occurs at most twice,
forcing

```text
at least e-8 double incidences,
one pair overlap >= ceil((e-8)/6)=30541989660 officially.
```

```text
result:                  PROVED rank-three projective-frame router
fourth-row reserve:      7
triple incidences:       excluded
hostile mutations:       3/3 rejected
critical status effect:  none
```

The Shape-A frontier is now rank three with this explicit triple-free frame,
or tensor rank at least four. The next attack should use the support/source
semantics of the frame rather than repeat generic matrix-rank probes.
