# L1 core bipolar signed-quotient normal form

- **status:** PROVED
- **role:** identify the exact algebraic object behind growing core polarity
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Let a quotient/coset chart core be the disjoint union

```text
C=disjoint_union_(a in A) T_a,
T_a={x:P(x)=a},       L_(T_a)=P-a,       |T_a|=ell.   (SQ1)
```

For an exact defect set `D subset C`, orient a fiber as dense when
`|D intersect T_a|>ell/2`; ties are sparse. Put

```text
A_+(D)={a: T_a is dense},
H_D=disjoint_union_(a in A_+(D)) (T_a\D),
S_D=D\disjoint_union_(a in A_+(D)) T_a.              (SQ2)
```

Then `H_D,S_D` are disjoint and the exact defect locator satisfies the signed
quotient identity

```text
F_D L_(H_D)
 =L_(S_D) product_(a in A_+(D))(P-a).                 (SQ3)
```

Moreover

```text
deg L_(H_D)+deg L_(S_D)
 =sum_(a in A) min(|D intersect T_a|,
                    ell-|D intersect T_a|)
 =p_core(D),                                             (SQ4)
```

and `gcd(L_(H_D),L_(S_D))=1`. The triple
`(A_+(D),H_D,S_D)` is unique under the tie convention and reconstructs

```text
D=(disjoint_union_(a in A_+(D)) T_a\H_D) disjoint_union S_D.  (SQ5)
```

Conversely, every triple consisting of dense labels `A_+`, a hole set
`H subset disjoint_union_(a in A_+)T_a` with fewer than `ell/2` holes in
each selected fiber, and a sparse set
`S subset disjoint_union_(a notin A_+)T_a` with at most `ell/2` points in
each unselected fiber, yields one exact defect set by `(SQ5)` and satisfies
`(SQ3)--(SQ4)`.

## Scope

This is an exact locator normal form, not a count of growing signed-mark
degree and not an exact-periodic owner. It assumes the core is partitioned by
the same quotient polynomial `P`; arbitrary cores and cross-chart
multiplicity remain outside its scope.

