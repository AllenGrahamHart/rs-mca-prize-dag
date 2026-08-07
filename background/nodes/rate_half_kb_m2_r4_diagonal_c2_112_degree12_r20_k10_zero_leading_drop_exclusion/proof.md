# Proof

The exact branch constructor gives `b2=u*K10`, where `u` is a transported
named unit. Thus `K10=0` makes `B0` linear at every admissible point.

For a row `P=sum P_i w^i` of degree `d`, polynomial division gives the
identity

```text
b1^d P(w)-H_P = (b1*w+b0) Q_P(w)
```

for a polynomial `Q_P`; no inverse of `b1` is used. Therefore every common
zero of the four source rows on `K10=0` satisfies both `H_A1=0` and
`H_B1=0`, including the further degree-drop case `b1=0`. The selected
degree-12 branch also satisfies `R12=0`. Consequently every admissible
source point lies in the variety of the four-generator ideal in the
statement.

The pinned exact computations reduce the two `H` equations modulo `K10`
over `QQ[x,s,p]`, then map them to `F_p0[x,s,pvar]`. Their degrees are `58`;
the `A1` and `B1` equations have `5431` and `5293` terms in both
representatives. The resulting F04 and F06 ideals have dimension one and
Groebner bases of sizes `82` and `80`.

For each basis, form the product of `s`, `L6`, and all 24 irreducible
transported named-open factors. Adjoining an inverse of that product gives
the unit ideal in both representatives. This is an exact geometric
emptiness certificate over `F_p0`, hence over every extension. The proved
complete-system inversion identifies `F04` with `F05` and `F06` with `F07`
without changing the q-slice rows or complete open. All four `K10=0`
branches are empty. QED.
