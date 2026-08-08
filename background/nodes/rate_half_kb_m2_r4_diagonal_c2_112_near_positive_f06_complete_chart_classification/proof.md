# Proof

For each cell in `(KBF6-1)`, reconstruct the positive source form over
`QQ(b,c,d)` with the pinned generic `5 x 5` source solver. Comparing the two
residual quadratics at the roots of `q=(T-c)(T-d)` with the required target
pair gives the four primitive equations in the direct residual registry.

Reduce modulo `p=2130706433`. Sequentially saturate by the twelve recorded
reconstruction factors and by `b,c,d,c-d`. The first factor producing the
unit ideal in the pinned order is:

```text
cell         first factor producing [1]
F06-A-RX     b*c - 1
F06-A-RL     b*c - 1
F06-A-RM     c-d
F06-OB-RX    b^2*c^2*d - b*c^2 - b*c*d - b^2 + b*c + b*d - c*d + c
F06-OB-RL    b*c - 1
F06-OB-RM    c-d.
```

Once a localized ideal is unit, further localization remains unit.

For an independent exact formulation, multiply all sixteen factors to
obtain `L`. In every cell it has total degree `26`, `566` terms, and SHA-256

```text
f29b4351caccad2aabb06696f4bb5b0b6526ec572b96dbe09dabd42526a1a96b.
```

Fresh four-variable computations form `(KBF6-2)` directly from the original
equations. All six bases are `[1]`. The Rabinowitsch criterion excludes a
point with `L!=0` over the algebraic closure. The proved literal inversion
transport identifies these six representatives with the complete
`F06/F07` direct-orbit block. QED.
