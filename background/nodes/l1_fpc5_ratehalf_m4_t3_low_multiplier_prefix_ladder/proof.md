# Proof: low-multiplier prefix ladder

Let `D` be in the monic unguarded LS6 flat. Euclidean division gives

```text
D E=M Q+V,       deg V<=s.                            (1)
```

The left side has degree `j+e=2ell-a+e`; since `M` is monic of degree
`2ell`, equation `(1)` forces

```text
deg Q=e-a,       lc(Q)=lc(E)=c.                       (2)
```

For this `Q`, divide

```text
M Q=E T_Q+R_Q,       deg R_Q<e.                       (3)
```

Reducing `(1)` modulo `E` says `V==-R_Q mod E`. Under `(PL1)`, every
degree-at-most-`s` polynomial in this residue class is uniquely

```text
V=-R_Q+E R,       deg R<=s-e.                         (4)
```

Substitution of `(3)` and `(4)` into `(1)` gives `D=T_Q+R`. Conversely, any
pair `(Q,R)` in `(PL2)` defines `(D,V)` by `(PL3)` and satisfies `(1)` with
the required degree bounds. Equation `(2)` makes `T_Q`, and hence `D`, monic
of degree `j`; adding `R` cannot change its leading coefficient. This proves
the exact disjoint parametrization.

For fixed `Q`, two locators differ by a polynomial of degree at most `s-e`.
Thus their coefficients in degrees

```text
j-1,j-2,...,s-e+1
```

are fixed. The number of these nonleading coefficients is

```text
j-1-(s-e)=ell+e-1,
```

proving `(PL4)`. A degree-`e-a` polynomial with prescribed nonzero leading
coefficient has exactly `Q_0^(e-a)` choices, proving the cell count. Formula
`(PL5)` is immediate. Finally, the split-core and exactness requirements are
additional filters on `(D,V)`, so deleting them for an upper envelope is
safe. QED.
