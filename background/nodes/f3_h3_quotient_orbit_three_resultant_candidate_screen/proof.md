# Proof

First suppose all three resultants in `(TRS1)` vanish. The orbit polynomial
`q_O` is irreducible over `Q`, so it divides each of

```text
Pcal_n^[0],       Pcal_n^[1],       Pcal_n^[2]
```

over `Q[T]`. Every root of `q_O` would then be a root of `Pcal_n` of
multiplicity at least three. This contradicts dyadic shifted-product
Sidonicity: the ordered shifted-product polynomial has multiplicity at most
two in characteristic zero, with the only repetition coming from swapping
the two factors. Hence `(TRS2)` defines a nonzero odd integer.

Put

```text
J_O,35=(q_O,Pcal_n^[0],...,Pcal_n^[35]) subset R[T]. (1)
```

For each `i=0,1,2`, the Bezout identity for the resultant gives

```text
rho_(O,i)=A_i(T)q_O(T)+B_i(T)Pcal_n^[i](T)           (2)
```

with coefficients over `R` after clearing only powers of two. Thus every
`rho_(O,i)` belongs to `J_O,35 intersect R`. The exact scalar compiler says

```text
J_O,35 intersect R=(s_O,35).                         (3)
```

Equations `(2)--(3)` show that `s_O,35` divides each `rho_(O,i)` up to a
unit of `R`, and hence divides their positive odd gcd `g_O`. This proves
`(TRS3)`.

At an odd official prime, a target with `P(t)>=36` makes
`Pcal_n^[0](t),...,Pcal_n^[35](t)` vanish. Choose one quotient
representation of the same target and its canonical orbit block. Then `t`
is a root of that block polynomial; finite-characteristic quotient
collisions may place it in further blocks as well. The chosen block's exact
orbit scalar is divisible by the row prime, and `(TRS3)` retains that prime
in `g_O`. Taking the union over all blocks proves completeness of the
candidate superset.

Finally, replacing a polynomial by its remainder modulo monic `q_O` does not
change its resultant with `q_O`. The canonical manifest gives `24,534`
blocks at `n=8192`, so three resultants per block gives the printed count.
Factoring every `g_O` and checking every retained official prime exactly can
discard all false positives without risking an omitted survivor. QED.
