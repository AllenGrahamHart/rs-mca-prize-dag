# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 11 is

```text
(de,bf), (de,sigma_c cf), (-de,sigma_o ef).
```

Let `F(x,y)=paired(x,y)`. Formal expansion proves that `F` is symmetric and
biquadratic. For fixed `q`, write

```text
F(q,y) = A(q)y^2 + B(q)y + C(q),
```

where `A,B,C` are quadratic polynomials in `q` over the six-dimensional
source algebra.

Put `q=de`, `m=df`, `s=(d+f)^2`, `z=1/d`, `U=bm`, and
`V=sigma_c cm`. The first two matching-11 equations are

```text
F(q,Uz)=0,    F(q,Vz)=0.
```

The target guards give `z(U-V)(U+V) != 0`. Subtraction therefore gives

```text
D(q)z+B(q)=0,             D(q)=(U+V)A(q).
```

Their compatibility is the quartic

```text
G(q)=C(q)A(q)(U+V)^2-B(q)^2UV=0.
```

The missing-record relation is

```text
1+(2m-s)z^2+m^2z^4=0.
```

On the regular branch, substitute `z=-B/D` and clear denominators to obtain
the degree-at-most-eight cut

```text
K(q)=D(q)^4+(2m-s)B(q)^2D(q)^2+m^2B(q)^4=0.
```

Exact modular multiplication reduces `K` modulo `G` to a cubic `R`. The
division-free 4-by-4 Bezout determinant of `G` and `R` is the resultant
times the guarded leading coefficient of `G`, hence is a valid common-root
eliminant. Its norm is computed through the quadratic-over-cubic tower in
the basis `1,t,t^2,b,bt,bt^2`. The cached inverse used to reduce modulo `G`
is retained in the exceptional-root ledger.

Every field root of the norm numerator and denominator, every inverse-guard
numerator and denominator, and the base-cubic leading coefficient is lifted
through the base cubic, the `b` quadratic, linear `c` recovery, product-rank
cofactors, and compact kernel. At each source point all roots of `G(q)` are
enumerated. If `D(q)` is nonzero, `z=-B(q)/D(q)` is replayed. If
`D(q)=B(q)=0`, every root of the missing quartic is replayed instead; thus
the denominator-degenerate branch is not discarded. Both defining paired
equations and the missing relation are checked directly before evaluating
the final equation `F(-q,sigma_o ef)`.

Across 16 rows there are 160 candidate `r` values, 208 source points, 240
enumerated `q` rows, and 64 reconstructed targets. Every one of the 64 final
paired evaluations is nonzero. The witness, boundary, and unresolved ledgers
are empty. This proves all 16 raw matching-11 cases empty.

The transposition of residual positions zero and one exchanges two records
that are both exactly `de`. It maps canonical matching 11 to matching 14.
Symmetry of `F` preserves every paired equation, while the missing relations
and target guards are unchanged. Hence the 16 matching-11 exclusions
transport to all 16 matching-14 cases. All 32 stated cases are empty. QED.
