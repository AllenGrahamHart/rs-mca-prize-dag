# XR first residual rank-two shell is quadratic-involutional

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_higher_rank_collapsed_face_exclusion`

Work over an official field, hence in odd characteristic, in the uniform
high-core split-pencil setup at affine kernel rank `a`. Quotient the regular
minimum-face Plucker syzygies. Let `Lambda` be a surviving rank-two trade on
the first possible active-union shell

```text
X,       |X|=a+3.                                    (FR1)
```

If `t` is the number of active rows and `Z_i` is the zero set in `X` of row
`i`, then

```text
4<=t<=floor((a+4)/2),
|Z_i| in {1,2},
Z_i pairwise disjoint,
at most one |Z_i|=1.                                 (FR2)
```

There are coprime polynomials `F,G` of degree at most two such that the row
space is represented on `X` by their pencil. The associated rational map

```text
phi=[F:G]:P^1 -> P^1
```

has degree exactly two. Its unique nontrivial deck transformation is an
involution

```text
iota in PGL_2(F).                                    (FR3)
```

Every two-point `Z_i` is a complete unramified fiber of `phi` and hence one
two-cycle of `iota`. If a singleton `Z_i` occurs, its other fiber point is
outside `X` or it is a ramification point fixed by `iota`.

Writing the active rows as

```text
lambda_i(x)=(c_i F(x)+d_i G(x))/Lambda'_X(x),
```

the coefficient vectors obey

```text
sum_i c_i=sum_i d_i=sum_i gamma_i c_i
 =sum_i gamma_i d_i=0.                               (FR4)
```

When `t=4`, the fiber labels are a projective-linear change of the four
selected slopes. For `a=4`, `(FR2)` recovers exactly the nonlocal
seven-coordinate profile `{1,2,2,2}` from the finite rank-five atlas.

Thus the first residual shell is not an unstructured larger-union trade: it
is a single quadratic-pullback chart. The theorem does not count embeddings
of those charts, pay their slope fibers, classify shells `|X|>=a+4`, handle
trade rank at least three, or promote the consumer.
