# Proof - L1 Mersenne HNF m=8 cubic three-two-one role-polynomial compiler

The ratio (RPC4) is unchanged when all three colors are multiplied by one
eighth root. Normalize `alpha=1`, and put

```text
u=beta/alpha,       v=gamma/alpha.
```

Pairwise distinctness gives `u,v in mu_8\{1}` and `u!=v`, while (RPC4) is
equivalent to

```text
v=1+lambda(u-1).                                   (1)
```

The roots of `C` are exactly `mu_8\{1}` in every official characteristic,
because those characteristics do not divide eight. By the root formula for
the resultant,

```text
R(lambda)=product_(u in mu_8\{1}) C(1+lambda(u-1)). (2)
```

Each of the seven factors in (2) has degree seven in `lambda`, with nonzero
leader `(u-1)^7`, proving `deg R=49`.

For each fixed `u`, the choice `v=u` is exactly `lambda=1`, so every factor
in (2) vanishes there. The root is simple: differentiating that factor at
`lambda=1` gives

```text
(u-1)C'(u)!=0,                                     (3)
```

since `u!=1` and `C` is separable. Hence the multiplicity of `lambda-1` in
`R` is exactly seven, proving (RPC3) and its degree.

After removing those seven diagonal choices, the roots of the quotient are
the six choices `v in mu_8\{1,u}` for each of the seven choices of `u`.
They are precisely the 42 ordered normalized triples. Different triples may
give the same ratio, so squarefree reduction merges rather than deletes role
values. Conversely every root of the resultant over an algebraic closure
comes from at least one pair of roots `u,v` of `C`; after the diagonal factor
is removed, they are distinct and reconstruct (RPC4). This proves (RPC5) and
the claimed exact role set. QED.
