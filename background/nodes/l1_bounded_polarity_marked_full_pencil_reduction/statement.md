# L1 bounded-polarity marked full-pencil reduction

- **status:** PROVED
- **role:** normalize the bounded-`p`, growing-cofactor branch
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use one maximal-sunflower chart and the polarized entropy

```text
p=sum_i min(a_i,ell-a_i),       a_i=|S_i|.
```

Suppose

```text
p<ell,       d>ell+p-1.                                  (MP1)
```

Then the word has at least two dense petals, meaning supports of size greater
than `ell/2`. Choose the canonical two largest dense supports, on petals
`T_i,T_j`, and put

```text
V_i=T_i\S_i,       V_j=T_j\S_j,
v_i=|V_i|,         v_j=|V_j|,
c=d-ell.
```

Their total mark degree satisfies

```text
v_i+v_j<=p.                                               (MP2)
```

Writing `F=L_D` for the exact split core locator and

```text
W-c_iF=L_(S_i)A_i,       W-c_jF=L_(S_j)A_j,
```

define

```text
J=L_(V_i)L_(V_j),
C_i=L_(V_j)A_i,       C_j=L_(V_i)A_j.
```

Then

```text
L_(T_i)C_i-L_(T_j)C_j=(c_j-c_i)FJ,                       (MP3)

deg J<=p,
deg C_i,deg C_j<=c+p.                                    (MP4)
```

Moreover `gcd(F,J)=1`, and exact defect gives `gcd(F,A_i)=gcd(F,A_j)=1`.
The canonical marked identity, together with `F,A_i` and the source chart,
reconstructs `W` and the listed codeword. Thus this is an injective reduction
of `(MP1)` to bounded-degree marked deformations of the full-petal
split-pencil identity.

For every fixed `P`, the choices of the canonical petal pair and marks with
`p<=P` are at most

```text
binom(M,2) sum_(v=0)^P binom(2ell,v),                     (MP5)
```

which is polynomial at the L1 lower cutoff. There is no hidden support-
pattern entropy outside the marked split-pencil count.

## Scope

The theorem does not bound the marked identities uniformly in `c=d-ell`,
prove stability of the full-petal atlas under marks, or promote either
target. It identifies that exact remaining theorem without creating it as a
speculative conditional node.
