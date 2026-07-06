# multiplier_exactness proof

Fix a multiplier `c` and let `r_x` be the chosen reduced integer
representative of `c zeta^x mod p`.

For a ternary vector `v` of support at most `2l'`, define

```text
S = sum_x v_x r_x.
```

If `v` is in the modular kernel, then

```text
S = 0 mod p.
```

The hypothesis says `|S| < p`. The only integer strictly between `-p` and
`p` that is divisible by `p` is `0`. Therefore `S = 0` as an exact integer
relation.

This proves the multiplier bridge. The separate fact that no useful
multiplier exists at the relevant official scales is a scoping/negative
result, not part of this exactness lemma.
