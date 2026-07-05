# proof: e22_planted_profile_disjointness

Let `L_C` be the core locator and let the planted petal scalars be distinct
and nonzero. The planted codewords are

```text
f_i = a_i L_C.
```

On every core point, `L_C` vanishes, so `f_i` agrees with the received word's
zero value on the whole core.

On petal `P_i`, the received word is exactly `a_i L_C`, so `f_i` agrees on
all of `P_i`.

On a different petal `P_j`, the received word is `a_j L_C`. Petal points are
disjoint from the core, so `L_C(x) != 0` there. Agreement would require

```text
a_i L_C(x) = a_j L_C(x),
```

hence `a_i = a_j`, impossible because the scalars are distinct. Thus no
second petal is touched.

On background points the received word is zero, while `L_C(x) != 0` and
`a_i != 0`, so there is no background agreement.

Therefore every planted codeword has exactly the planted one-petal profile.
Any nondegenerate staircase challenger classified as mixed-petal or
full-petal touches at least two petals by definition, so it cannot be one of
the planted codewords.
