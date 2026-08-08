# Proof

Reduce the four registry equations and all ten radical localizer factors
modulo `p=2130706433`. For each cell, let `I` be the four-equation ideal.

The primary computation saturates sequentially by each irreducible localizer
factor. This is equal to saturation by their product. It returns unit for the
four cells in `(KBF2S-1)`: the `A` cells become unit after six linear factors;
`OB-RX` becomes unit after all ten; and `OB-RL` becomes unit at the tenth.

Independently, let `L` be the product of all ten factors and introduce one
new variable `y`. The Rabinowitsch ideal

```text
<I, 1-yL> subset F_p[y,b,c,d]                    (1)
```

is unit if and only if the variety of `I` has no point with `L!=0`. A fresh
four-variable Groebner computation returns basis `[1]` for every cell in
`(KBF2S-1)`. This proves named-open emptiness over the algebraic closure.

For the two mixed cells, sequential saturation processes all ten factors and
leaves nonunit bases of sizes 8 and 13. They are retained exactly as open
cells. Applying the already proved literal transports to the four unit cells
closes their complete semantic orbits, leaving 26 representatives. QED.
