# Proof - L1 core bipolar signed-quotient normal form

For every dense fiber, `D` contains exactly `T_a\H_D`; for every sparse
fiber, it contains exactly the points recorded in `S_D`. The fibers are
disjoint, so `(SQ5)` holds and `H_D` and `S_D` are disjoint.

Adding the holes to `D` fills every dense fiber and changes no sparse fiber:

```text
D disjoint_union H_D
 =S_D disjoint_union disjoint_union_(a in A_+(D)) T_a.  (1)
```

Taking monic locators of the disjoint unions in `(1)` gives

```text
F_D L_(H_D)
 =L_(S_D) product_(a in A_+(D))L_(T_a)
 =L_(S_D) product_(a in A_+(D))(P-a),
```

which is `(SQ3)`. Disjointness of the two mark sets gives their coprimality.

If `r_a=|D intersect T_a|`, then a dense fiber contributes `ell-r_a` holes
and no sparse marks, while a sparse fiber contributes `r_a` sparse marks and
no holes. The tie convention puts `r_a=ell/2` in the second case. Therefore
the contribution of every fiber to `|H_D|+|S_D|` is
`min(r_a,ell-r_a)`, proving `(SQ4)`.

The dense-label set is determined by `D` and the fixed tie convention. Once
it is known, the holes and sparse points are the set differences in `(SQ2)`,
so the triple is unique. Conversely, the printed per-fiber inequalities make
the fibers indexed by `A_+` dense and all others sparse after reconstruction
by `(SQ5)`. Reversing `(1)` proves the locator identity and degree formula for
every such triple.

