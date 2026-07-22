# L1 m=4, h=3 Cartier resonance reduction

- **status:** PROVED
- **dependency:** `l1_m4_h3_mason_defect_budget`
- **consumer:** `l1_mixed_petal_amplification`

Use the notation of the Mason defect node. Thus

```text
n=4(p+1),  u=p+4,  R=X^nu U,
H=3XU'D+XUD'-(n-3nu)UD,
H!=0,      deg H<=4-nu.                                (CRR1)
```

For `nu=0,1,2,3,4`, choose

```text
s_nu = p-4, p-1, 2, 5, 8, respectively.                (CRR2)
```

Then `s_nu+n-3nu=0` in characteristic `p`, and the exact derivative identity
is

```text
(X^s_nu U^3D)'=X^(s_nu-1) U^2 H.                       (CRR3)
```

The coefficient of `X^(jp-1)` in a formal derivative is always zero. If
`deg H=4-nu`, the right side of `(CRR3)` has a nonzero leading coefficient
in degree `3p-1` for `nu=0,1` and degree `2p-1` for `nu=2,3,4`. Therefore

```text
nu in {0,1,2,3},
delta_A+delta_B<=deg H<=3-nu.                           (CRR4)
```

In particular, `nu=3` has constant nonzero `H` and zero defect: `U` is
squarefree and coprime to `D`, and `B_0` is squarefree.

The remaining derivative resonances give exact coefficient constraints:

```text
nu=0: [X^4](U^2H)=[X^(p+4)](U^2H)=0,
nu=1: [X^1](U^2H)=[X^(p+1)](U^2H)=0,
nu=2: [X^(p-2)](U^2H)=0,
nu=3: [X^(p-5)](U^2H)=0.                               (CRR5)
```

Thus the former five-case branch has four cases, carrying cubic, quadratic,
linear, and constant nonzero eliminants respectively. This does not exclude
`nu=0,1,2,3`, count components, classify nonembedded `h=2`, treat `m=8,16`,
or close L1.
