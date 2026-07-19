# Proof - PMA sigma-one paired-core normalization

Fix `C`. Interpolation at its `k-1` distinct points gives a unique `Q_C` of
degree at most `k-2`. The locator `L_C` is nonzero on `H\C`, so `(PC1)` is
well-defined.

Suppose first that a source layout `(PC2)` is given. Both `P_0` and `Q_C`
have degree below `k` and agree on `C`. Their difference is therefore
divisible by the degree-`k-1` polynomial `L_C`, with constant quotient:

```text
P_0=Q_C+a_0L_C
```

for a unique `a_0 in F`. On the background point `y`, equation `(PC2)` gives
`phi_C(y)=a_0`. On `T_i` it gives

```text
phi_C(x)=a_0+c_i.
```

The values `c_i` are nonzero and pairwise distinct. Since `(PC2)` is a
disjoint exhaustive partition of `H\C`, `phi_C` therefore has the singleton
fiber `{y}` and exactly the `M` doubleton fibers `T_i`.

Conversely, suppose `C` is paired. Let `{y}` be the singleton fiber, set
`a_0=phi_C(y)`, and let `T_i` be the doubleton fibers with values `a_i`.
Define `P_0` and `c_i` by `(PC3)`. Distinct fibers give distinct `a_i`, and
none equals `a_0`, so the `c_i` are distinct and nonzero. Equation `(PC1)`
then gives

```text
U(x)=Q_C(x)+a_0L_C(x)=P_0(x)              on {y},
U(x)=Q_C(x)+a_iL_C(x)=P_0(x)+c_iL_C(x)    on T_i.
```

On `C`, both `P_0` and `Q_C` equal `U` because `L_C` vanishes. This proves
`(PC2)`. The construction uses the actual fibers of `phi_C`, so every part of
the layout is unique apart from ordering its doubletons. The two
constructions are inverse.

For planted codewords from two different fibers,

```text
P_i-P_j=(c_i-c_j)L_C.
```

The scalar is nonzero. Since `L_C` has degree `k-1` and exactly the distinct
roots in `C`, the difference recovers `C` and spans the direction of the
affine line. Every point `x in H\C` selects the unique member of that line
which equals `U(x)`; its line parameter is precisely `phi_C(x)` up to the
common affine shift used to choose a base point. Hence the line and `U`
recover the fiber partition and the source layout. Two layouts sharing two
planted codewords have the same line, the same recovered core, and the same
fiber partition, so they coincide.

Finally, the source-layout order in the carried-layout Top/Post theorem may
be replaced by the induced order on paired cores, because the layout over a
fixed core is unique. First-match ownership makes the sets `E_C` disjoint and
their union is `Post(U)`. Taking cardinalities proves `(PC4)`. No estimate of
that sum is used.
