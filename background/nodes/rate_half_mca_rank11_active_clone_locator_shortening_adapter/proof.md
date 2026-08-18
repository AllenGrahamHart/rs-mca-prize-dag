# Proof

Choose one coordinate `x_0 in D`. Base-freeness says evaluation at `x_0`
is a nonzero functional on the five-space `B`. Hence its kernel has
dimension four. Every evaluation functional indexed by `D` is a nonzero
scalar multiple of this one, so all have the same kernel `B_D`.

Every `b in B_D` vanishes at the distinct field points of `D`. The
squarefree locator `L_D` therefore divides `b`. Division by one fixed
nonzero polynomial is injective, so

```text
bar(B)_D={b/L_D:b in B_D}
```

has dimension four and proves `(AS1)`.

The factor presentation has `span(PB)<=F[X]_{<K}`. Consequently every
product in `P B_D` is divisible by `L_D`, and after cancellation

```text
span(P bar(B)_D)<=F[X]_{<K-c}=F[X]_{<s}.               (1)
```

For completeness, finite-dimensional nonzero polynomial spaces `V,W`
satisfy

```text
dim span(VW)>=dim V+dim W-1.                            (2)
```

Indeed, choose degree-echelon bases with degrees
`a_1<...<a_r` and `b_1<...<b_q`. The products

```text
v_1w_1,...,v_rw_1,v_rw_2,...,v_rw_q
```

have strictly increasing degrees and are linearly independent. Apply `(2)`
to `dim P=2` and `dim bar(B)_D=4`. The left side of `(1)` has dimension at
least five, while `F[X]_{<s}` has dimension `s`; hence `s>=5`. The lower
bound `c>=10001` gives `s<=1048576-10001=1038575`, proving `(AS2)`.

By definition of `mu_D`, every associated residual class satisfies
`B_i<=B_D`. Division by `L_D` preserves its dimension, and every associated
correction `g b`, with `g in P` and `b in B_i`, becomes `g(b/L_D)`.

Every coordinate in `D` is anchor-good. Each associated explanation pair
therefore equals the anchor pair and the received pair on `D`, so `D` is a
common subset of their maximal agreement supports. For each explanation,
the size-`m` subsets of its maximal support that contain `D` form a connected
exchange graph. Adjacent sets overlap in `m-1>=K` points. If every such set
were pair-contained, uniqueness of degree-`<K` interpolation would propagate
one explaining pair to their union, the complete maximal support,
contradicting the actual noncontained witness. Thus a noncontained witness
through `D` exists.

The subtraction, division, and inverse-lift maps from the proved same-record
common-core adapter now apply verbatim with locator `L_D`. They preserve
slopes and pair noncontainment in both directions and give the parameter
change `(AS3)`. Since the parent factor router's classes are first-match
disjoint and no class is reassigned, their total mass `mu_D` is preserved.

Subtracting `c` from all three row parameters leaves the displayed
differences unchanged. The quotient spaces give the asserted active
shortened `2 x 4` presentation. QED.
