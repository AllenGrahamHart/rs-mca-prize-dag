# Proof

Let `k_*` be the unique label of `K minus K_0`. By `(KBDM-8)`,

```text
R_(k_*) ~ P_(J_1)^2.                               (1)
```

Each of the two component stars factoring `R_(k_*)` is a reduced quadratic.
Since `J_1` has exactly two labels, the only reduced quadratic divisor
supported on `J_1` is `P_(J_1)`. Thus the corresponding star vertex occurs
with weight at least two and contributes at least `binom(2,2)=1` to the
complete-source defect.

Whole-fiber transport gives

```text
R_(tau(k_*)) ~ tau^*R_(k_*) ~ P_(tau(J_1))^2.       (2)
```

The same reduced-factor argument gives a second weight-at-least-two star
vertex. It is distinct from the first because `J_1 subset J` while
`tau(J_1) subset I`. Equations `(1)--(2)` therefore cost at least two
defect units. This argument counts coincident source points with divisor
multiplicity and is unchanged at a ramified source fiber.

For each of the four labels in `K_0`, `(KBDM-4)` puts both reduced component
stars on `J_0`. Hence there are eight further star units on unordered
two-subsets of the four-label set `J_0`. There are six such subsets. If
their six weights are `e_i`, padded by zeros, then `sum e_i=8` and

```text
sum_i binom(e_i,2)>=2,                              (3)
```

with equality only at the balanced profile `(2,2,1,1,1,1)`. These vertices
use only labels in `J_0`, so they are distinct from both square vertices.
Combining `(1)--(3)` yields `Delta_star>=4`, contradicting the proved
complete-source quartic defect budget three. This proves `(KBD2-2)` in both
source-subfield branches. QED.
