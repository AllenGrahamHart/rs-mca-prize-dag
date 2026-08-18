# Rank-eleven rich-atlas factor-presentation fence

- **status:** PROVED
- **scope:** logical strength of the bare full-span rich-container terminal

The following data do not imply an exact `2 x 5` factor presentation:

```text
dim C'=10,
the promoted dimension-two/three containers span C',
at least 16384884 distinct containers,
at least 38385 common actual zeros per container,
no line-global common zero.
```

Indeed, over every sufficiently large finite field supporting the official
evaluation set, there is a degree-`<K` polynomial space `C'` with all these
properties but no equality

```text
C'=span(PB),  dim P=2,  dim B=5.
```

One may take two coprime squarefree split locators `L_1,L_2` of degree
`H=38385`, put `d=H+4`, and choose five-spaces
`V_1,V_2 <= F[X]_(<=d)` so that

```text
C'=L_1V_1 direct_sum L_2V_2.
```

All two- and three-subspaces of either five-dimensional block are rich, and
their union spans `C'`. A dimension/counting argument proves that the
`V_1,V_2` can be chosen with global gcd one and outside every `2 x 5`
product locus.

## Consequence

Any theorem producing the factor presentation from an actual unsafe line
must use information absent from the bare terminal, such as the anchored
row-space partition, slope mass, minimizing-pair chronology, or first-owner
compatibility.

## Nonclaim

The construction is not an unsafe received line and does not refute a
chronology-aware synchronization theorem. It refutes only the unqualified
inference from rich-flat population and collective span.
