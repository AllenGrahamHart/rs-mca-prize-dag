# proof: e22_agreement_cofactor_equations

Use the notation of `nodes/worst_word_challenger_pricing/notes/e22_core.py`.
Let `C` be the core, `B0` the background, and `P_i` a petal with scalar
`a_i`. The received word is zero on `C union B0` and equals `a_i L_C(x)` on
`P_i`.

Let `f` be a listed codeword, and let `Z subset C union B0` be the coordinates
where `f` agrees with the zero part of the received word. Since every point in
`Z` is a root of `f`, write

```text
f = U L_Z
```

with `deg U < k - |Z|`.

Split the zero-agreement roots by their relation to the core:

```text
Z = (Z cap C) union (Z \ C),
C = (Z cap C) union (C \ Z).
```

At a petal agreement point `x in P_i`, we have

```text
U(x) L_Z(x) = f(x) = a_i L_C(x).
```

Petal points are disjoint from the core and background, so
`L_{Z cap C}(x)` is nonzero. Cancelling that common locator factor gives

```text
U(x) L_{Z\C}(x) = a_i L_{C\Z}(x).
```

This is exactly the claimed cofactor equation. The argument applies to every
petal agreement point, regardless of whether the touched petal is full or
partial. Therefore the mixed/full-petal support-forcing problem can be
reduced to these cofactor equations without losing any agreement information.
