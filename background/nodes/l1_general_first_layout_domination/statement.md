# L1 general first-layout domination

- **status:** PROVED
- **role:** remove maximal source-layout multiplicity at every petal size
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Source layout

Let `U:H->F_q` be a received word for `RS[H,k]`. An admissible maximal
sunflower source layout consists of

```text
H=C disjoint_union B disjoint_union T_1 ... disjoint_union T_M,
|C|=k-1,       |T_i|=ell,       |B|=b<ell,              (GL1)
```

a polynomial `Q` of degree below `k`, and pairwise distinct nonzero labels
`c_i` such that

```text
U=Q                    on C union B,
U=Q+c_i L_C            on T_i.                          (GL2)
```

Its planted anchor set is

```text
Anch={Q+c_i L_C:1<=i<=M}.                               (GL3)
```

## Theorem

Fix any set `X` of listed codewords remaining after arbitrary global owners,
and fix one admissible source layout. Then

```text
X=(X\Anch) disjoint_union (X intersect Anch),
|X|<=|X\Anch|+M.                                       (GL4)
```

Every codeword in `X\Anch` is universally carried as a non-planted extra in
this one layout: after subtracting `Q`, it has the exact core-defect normal
form

```text
P-Q=L_(C_P)W,       deg W<=d,
W=0 on R_P,         W=c_i L_D on S_i,                  (GL5)
```

where `C_P` is its retained-core agreement, `D=C\C_P`, `d=|D|`,
`R_P` is its exact background agreement, and `S_i` is its exact agreement in
`T_i`. Moreover `|S_i|<=d` for every petal.

Consequently, if a source-admissible class is first-matched over any finite
nonempty family of maximal source layouts, every member first carried after
the first layout is one of that first layout's anchors. A bound `B(n)` for all
selected non-planted contributors in the first layout gives the global bound

```text
|X|<=B(n)+M.                                            (GL6)
```

At the L1 cutoff `ell>=c_0 n/log_2 n`,

```text
M<=n/ell<=log_2(n)/c_0,                                (GL7)
```

so the anchor remainder is polynomial.

## Scope

This removes the multiplier from distinct maximal sunflower **source
layouts**, including non-intrinsic ones. It does not pay the non-planted
contributors in the first layout. In particular, contributor-dependent
quotient, split-pencil, or Forney recharts internal to that fixed layout may
still require a first-owner payment theorem.
