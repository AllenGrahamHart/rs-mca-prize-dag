# Proof

For each cell in `(KBF4-1)`, reconstruct the positive source form over
`QQ(b,c,d)` with the pinned generic `5 x 5` source solver. At both roots of
`q=(T-c)(T-d)`, compare the two residual quadratics projectively with the
required target pair. Clearing primitive numerators gives the four equations
in the direct residual registry.

Reduce modulo `p=2130706433`. The registry supplies twelve
reconstruction-generated radical nonmonomial factors. The affine source
chart additionally requires `bcd!=0`, while the two distinct `J_1` labels
require `c-d!=0`. Sequentially saturating by these sixteen factors reaches
the unit ideal as follows:

```text
cell         first factor producing [1]
F04-A-RX     b*c - 1
F04-A-RL     b*c - 1
F04-A-RM     c-d
F04-OB-RX    b^2*c^2*d - b*c^2 - b*c*d - b^2 + b*c + b*d - c*d + c
F04-OB-RL    b*c - 1
F04-OB-RM    c-d.
```

The first-factor wording refers to the pinned sequential order; once the
localized ideal is unit, further localization remains unit. Thus every
complete chart in `(KBF4-1)` is empty.

For an independent exact formulation, multiply all sixteen factors to
obtain `L`. In every cell it has total degree `26`, `562` terms, and SHA-256

```text
9776700913d12aba7cc9e506024dd43ba8d27c00a6f3a2ddf2838ee16fa152b2.
```

A fresh four-variable computation forms `(KBF4-3)` directly from the four
equations. All six Groebner bases are `[1]`. By the Rabinowitsch criterion,
none of the six original varieties has a point with `L!=0` over the
algebraic closure. This proves all six exclusions. The exact literal
inversion transport identifies these six representatives with the complete
`F04/F05` direct-orbit block. QED.
