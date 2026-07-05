# proof: e22_cofactor_petal_divisibility

The proved node `e22_agreement_cofactor_equations` supplies, for every petal
agreement point `x in T_i`, the equation

```text
U(x)L_{Z\C}(x) = a_i L_{C\Z}(x).
```

Define

```text
H_i(X) = U(X)L_{Z\C}(X) - a_i L_{C\Z}(X).
```

The pointwise cofactor equation is exactly the assertion that `H_i(x)=0` for
each `x in T_i`. The points of a petal are distinct field points, so the
agreement-set locator

```text
L_{T_i}(X) = prod_{x in T_i} (X-x)
```

is squarefree and has precisely those roots. Therefore `H_i` vanishes on
`T_i` if and only if every linear factor `(X-x)` for `x in T_i` divides
`H_i`, equivalently if and only if `L_{T_i}` divides `H_i`.

When the petal is full, `T_i=P_i`, so the full petal locator `L_{P_i}` divides
`H_i`. This proves the divisor form of the cofactor constraints.
