# L1 bounded-mark affine split-pencil compiler

- **status:** PROVED
- **role:** normalize the arbitrary-locator part of the bounded-polarity branch
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Let `K=F_q`, fix `d>=1`, and let `T_1,...,T_t` be pairwise disjoint
`ell`-point petals with distinct labels `c_i`. Choose nonempty partial
supports and their marks

```text
S_i subset T_i,       V_i=T_i\S_i,       v=sum_i |V_i|.       (AC1)
```

Any additional fixed interpolation equations, including equations on sparse
petal supports, may be imposed in every space below. Put

```text
A_d={(F,W): deg F=d monic, deg W<=d},

X_S={(F,W) in A_d: W(x)=c_iF(x) for x in S_i},

H_T^0={(G,B): deg G<=d-1, deg B<=d,
                 B(x)=c_iG(x) for x in T_i}.                 (AC2)
```

Define the missing-equation syndrome

```text
sigma:X_S -> K^(disjoint_union_i V_i),
sigma(F,W)=(W(x)-c_iF(x))_(x in V_i).                        (AC3)
```

Then:

1. `X_S` is the disjoint union of at most `q^v` nonempty affine fibers. For
   every syndrome `y` and representative `z_y in sigma^(-1)(y)`, one has

   ```text
   sigma^(-1)(y)=z_y+H_T^0.                                 (AC4)
   ```

2. The linear space

   ```text
   Hhat_y=span_K(z_y,H_T^0)                                  (AC5)
   ```

   has dimension `dim H_T^0+1`, and its monic-`F` hyperplane is exactly the
   affine fiber in `(AC4)`. Thus deleting `v` petal equations creates at most
   `q^v` one-direction projective extensions of the full-petal kernel, not an
   unrestricted new kernel family.

3. For an actual exact-defect L1 pair, write

   ```text
   W-c_iF=L_(S_i)A_i,
   J=product_i L_(V_i),       J_i=J/L_(V_i),
   C_i=J_iA_i.                                             (AC6)
   ```

   Then all arbitrary petal locators lie in the same bounded-basepoint split
   pencil:

   ```text
   L_(T_i)C_i=J(W-c_iF),
   deg C_i<=d-ell+v,
   gcd(JF,JW)=J.                                           (AC7)
   ```

In one fixed source chart and at one fixed defect degree, orienting every one
of the `M` petals as sparse or dense
and recording at most `P` exceptional points gives at most

```text
2^M sum_(e=0)^P binom(Mell,e)
 <=2^M(P+1)n^P                                             (AC8)
```

exact petal-support patterns with polarized entropy at most `P`. The dense
marks satisfy `v<=P`, so their syndrome count is at most `q^P`. If

```text
M<=log_2(n)/c_0,       q<=n^gamma,                         (AC9)
```

the support-pattern and syndrome pre-factor is at most

```text
(P+1)n^(1/c_0+P+gamma P).                                 (AC10)
```

Summing over the at most `n` defect degrees costs one further factor of `n`.
Consequently, inside each source chart the bounded-polarity
arbitrary-locator branch is reduced to a uniform count of exact split,
squarefree, saturated monic points in the one-direction extensions `(AC5)`.
If every such cell has size at most `n^B` and a canonical first-match source
atlas has at most `n^A` charts, the global contribution is at most

```text
(P+1)n^(A+B+1+1/c_0+P+gamma P).                         (AC11)
```

## Scope

This theorem does not bound the split/saturated points in one homogenized
cell, prove affine-coset stability of the full-petal payment, supply a
polynomial non-intrinsic source-chart atlas, or aggregate the growing-polarity
branch. Inside each chart it replaces the former unstructured
"arbitrary-locator" label by a precise affine-slice/basepoint split-pencil
problem.
