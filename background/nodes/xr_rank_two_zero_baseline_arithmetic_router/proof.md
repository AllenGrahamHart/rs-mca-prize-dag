# Proof

The collision-defect identity gives

```text
Delta=D_0+2((t-2)I+sigma+H).
```

For a full minimal Maxwell core, `Delta=-e<=0`. Under `D_0=0` the right side
is nonnegative, so `Delta=e=0` and every nonnegative charge vanishes. This is
`(ZB3)`. In particular `I=0`, every individual pair slack is zero, and
`H=0` says that every outside multiplicity is at most two.

The baseline equation is

```text
2(t-2)Z=t h+(t-2)(t-1)D.                            (1)
```

Put `g=t-2`. Reduction modulo `g` shows `g|2h`. Suppose `h` is odd. If `g`
were odd, then `g|h`, and division of `(1)` by `g` would give

```text
2Z=h+2h/g+(g+1)D.
```

The right side is odd, a contradiction. Hence `g=2s` with `s|h`. Dividing
`(1)` by `2s` now gives

```text
2Z=h+h/s+(2s+1)D.
```

The first two terms are even and `2s+1` is odd, so `D` is even. This proves
`(ZB2)`.

It remains to count the outside collision design. Since `I=0`, every
extension lies outside `X`. Pair-budget saturation gives

```text
|O_i intersect O_j|=ell_ij=z_i+z_j-D.
```

No point lies in three outside sets. Therefore the number `Q` of
multiplicity-two points is

```text
Q=sum_(i<j) ell_ij=(t-1)Z-C(t,2)D.                  (2)
```

Equation `(1)` substituted into `(2)` gives the formula for `Q` in `(ZB4)`.
The total outside incidence is

```text
sum_i |O_i|=sum_i(h-D+z_i)=t(h-D)+Z=P+2Q.           (3)
```

Substituting the formulas for `Z,Q` into `(3)` gives the displayed formula
for `P`; adding `P+Q` gives `th/2-D`. Nonnegativity of `P,Q` proves the two
continuous bounds on `D`.

Two discrete bounds remain. First, every `z_i<=d=D-1`, so

```text
Z<=t(D-1).
```

Substitution of `(1)` and rearrangement gives the second lower bound in
`(ZB5)`. Next let `p_i` count outside points used only by row `i`. Pair
saturation and multiplicity at most two give

```text
p_i=h+(t-2)D-(t-3)z_i-Z.                            (4)
```

Put `m=t-3`, `L=h+h/s`, and `A=(h-h/s)/2`. Equations `(1)` and `(ZB2)` turn
`(4)` into

```text
h+(t-2)D-Z=A+mD/2,
p_i congruent r:=A mod m                (mod m).     (5)
```

Since every `p_i>=0`, their sum must satisfy `P>=tr`. Using
`P=(mD-L)/2` gives the third lower bound in `(ZB5)`. All allowed `D` are even,
so taking the least even ceiling is exact for this arithmetic filter.

The zero fibers are disjoint in

```text
|X|=a+D,
```

so `Z<=a+D`. Substituting `t=2s+2` into `a>=Z-D` proves the rank bound in
`(ZB5)`.

For `t=4`, the lower and upper bounds both give `D=2h`. Then `P=Q=0`.
Every nonnegative pair intersection `ell_ij` is zero, so
`z_i+z_j=2h` for all pairs and hence every `z_i=h`. Finally
`|T_i|=h-D+z_i=0`, proving `(ZB7)`.

For the official rows, factor

```text
2^33+1=3^2*67*683*20857,
2^32+1=641*6700417.
```

Enumerate `s|h`, set `t=2s+2`, choose the least positive even integer `D`
satisfying all three lower bounds in `(ZB5)`, and reject it if it exceeds the
upper bound. Compute `a_min=Z-D`, reject the arity if `a_min>k`, and minimize
the remaining rank floors. This gives exactly the table and tuples `(ZB6)`.
The inherited flat-nullity parameter satisfies `u=k-a-g>=0`, so the rejection
`a_min>k` is unconditional on this branch.
The accompanying verifier recomputes every divisor, residue, interval,
dimension rejection, and minimum using exact integers. QED.
