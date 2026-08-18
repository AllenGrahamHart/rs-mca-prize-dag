# Proof

The triple-owner parent gives

```text
M_3=322359637,       Q_4=58361.                      (1)
```

Apply the multi-anchor exchange theorem to every first-owned pair type with
at least 29 records. If any resulting packet is high complexity, output 1
holds. Assume no such packet exists. Every type with at least 29 records then
has one fixed rational pencil containing all of its record locators.

Partition the pair types. If a synchronized pencil is a normalized nonzero
affine reflection, the exact fixed-pencil cap bounds its record count by
`1154`: distinct records have pairwise-disjoint exception locators and hence
use distinct reflection orbits. A type outside the synchronization range has
at most `28` records. Charge both categories by the larger uniform cap
`1154`. First-owner pair types have disjoint record currencies, so their
total contribution is at most

```text
Q_4*1154=58361*1154=67348594.                        (2)
```

Subtracting from `(1)` leaves

```text
322359637-67348594=255011043                         (3)
```

records on synchronized pencils outside the normalized nonzero affine class.
There are at most `Q_4` such pair types. Since

```text
255011043=4369*58361+31834,
```

one owns at least `4370` records. It is above the 29-record threshold, so the
multi-anchor theorem places all of its exception locators in one fixed
coprime rational pencil. QED.

Equation `(2)` is now owner-safe: it sums disjoint first-owned pair-type
currencies after each large type has a canonical synchronized pencil. It does
not assert equality of pencils across types.
