# XR trade-circuit arity and rank-two Segre atlas

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_higher_rank_uniform_split_pencil_reduction`

Let `Lambda=(lambda_i)_(i=1,...,t)` be a nonzero uniform split-pencil trade
with distinct slopes `gamma_i` and trade-matrix rank `r`. Call it a
row-scaling circuit if no nonzero family

```text
(alpha_i lambda_i)_i
```

is a trade on a strict nonempty subset of its active block rows. Then

```text
r+2<=t<=2r+1.                                        (CA1)
```

Every trade is a sum of row-scaling circuits of rank at most its own rank.
Consequently every rank-two trade is a sum of rank-two circuits on exactly
four or five active blocks.

The rank-two circuit coefficients have a complete constant-arity atlas.
Choose a basis `F,G` of the row space and write

```text
lambda_i=c_iF+d_iG,
v_i=(c_i,d_i,gamma_i c_i,gamma_i d_i) in F^4.       (CA2)
```

Every `v_i` lies on the Segre quadric

```text
v_1v_4-v_2v_3=0.                                   (CA3)
```

The original trade gives `sum_i v_i=0`, and circuit minimality gives

```text
t=4: rank(v_1,...,v_4)=3,
t=5: rank(v_1,...,v_5)=4, and every four are independent. (CA4)
```

For `t=4`, the projective row parameter `[c_i:d_i]` is a nonconstant
fractional-linear function of the slope `gamma_i`; this is the four-point
Mobius/Plucker circuit. For `t=5`, the five Segre points form a projective
three-space circuit with one all-nonzero dependence; no four-block subtrade
is present.

Thus arbitrary-size proper rank-two relations are not a remaining template
class. Their complete row-scaling decomposition uses only four/five-block
circuits. The theorem does not count embeddings of those circuits, prove
first-match ownership across different Maxwell cores, pay their slopes, or
classify circuits of rank at least three.
