# Proof

Every component of `C` is mixed, so the domain projection is finite flat of
degree `e`. Push the untwisted ideal sequence

```text
0 -> O(-d,-e) -> O -> O_C -> 0                       (1)
```

along `pi`. Since `e>1`, the first term has zero direct image and

```text
R^1 pi_*O(-d,-e)=O(-d)^(e-1).
```

Thus

```text
0 -> O -> pi_*O_C -> O(-d)^(e-1) -> 0.               (2)
```

It splits because `Ext^1(O(-d),O)=H^1(O(d))=0`, proving `(TPD2)`.

The local cube calculation gives contact multiplicity one at
`P_alpha,P_beta`; in particular they are effective Cartier points. Hence

```text
0 -> O_C -> O_C(P_alpha+P_beta)
  -> k_(P_alpha) direct_sum k_(P_beta) -> 0.           (3)
```

Finite pushforward is exact. Both residue fields are supported at `x_*`,
so `(3)` and `(TPD2)` give `(TPD3)`. The quotient is annihilated by the
maximal ideal at `x_*`. Over its DVR, Smith normal form therefore has two
distinct exponent-one modifications, not one exponent-two modification.
Equivalently, `(TPD3)` is specified by a two-dimensional subspace

```text
W subset (O direct_sum O(-d)^(e-1))|_(x_*).           (4)
```

Project `W` to the negative summand. Its rank is one or two: rank zero is
impossible because the `O` fibre is one-dimensional.

If the rank is one, `W` contains the `O` direction. A constant change of
basis in the equal negative summands and a map `O(-d)->O` with prescribed
value at `x_*` put it in the span of the `O` fibre and the first negative
fibre. The modification raises those summands by one, giving the PENCIL
splitting in `(TPD4)`.

If the rank is two, a constant negative-block change of basis makes its
projection the first two negative directions. Maps `O(-d)->O` remove both
`O`-components at `x_*`. The modification raises those two negative
summands, giving the CANONICAL splitting.

Because `d>1`, every displayed negative summand has no sections. This proves
the two values of `h^0`. Finite pushforward preserves global sections, so
they are also the section counts of `L_2`.

In the PENCIL branch, remove the common base divisor of the two independent
sections. The remaining basepoint-free linear series has degree one or two
(degree zero cannot have two independent sections on the connected reduced
curve). It therefore defines the asserted map. In the CANONICAL branch,
the canonical divisor section is nonzero and spans the one-dimensional
space. QED.
