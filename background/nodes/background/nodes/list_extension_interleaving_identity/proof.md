# Proof

Fix a basis `e_1,...,e_m` of `E` over `B`. Expand every coefficient of a
polynomial `P in E[X]_{<k}` uniquely as

```text
P = sum_(i=1)^m e_i P_i,  with P_i in B[X]_{<k}.
```

Because every evaluation point lies in `B`, evaluation commutes with
coordinate projection:

```text
Phi(P(x)) = (P_1(x),...,P_m(x)).
```

Thus `Phi` maps the evaluation of `P` to an `m`-tuple of codewords of `C_B`.
Conversely, any such tuple recombines to a unique polynomial `P` over `E`.
Therefore `Phi(C_E)=C_B^{==m}` bijectively.

At each coordinate, an extension symbol equals the received symbol exactly
when all of its `B`-coordinates agree. Hence `Phi` preserves the Hamming
agreement set pointwise. It therefore gives a bijection between the two lists
for every received word and radius. Taking the maximum over received words
proves `(EI)`.

The isometry changes the alphabet presentation, not the challenge statement's
normalizing field. The grand list challenge for `C_B^{==m}` prints `|B|` in
its denominator, so no `|E|` credit follows.
