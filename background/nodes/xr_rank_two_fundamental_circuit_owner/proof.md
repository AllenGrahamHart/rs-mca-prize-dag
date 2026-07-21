# Proof

Use the coefficient map `V` in the statement. The Segre-atlas dependency
proves that every support-minimal nonzero vector of `K` has support four or
five. Since the original trade gives `1_I in K`, the column family is
dependent. It lies in `F^4`, so `q<=4`. If `q<=2`, some at most three columns
would contain a circuit, contrary to the arity lower bound. This proves
`(FO1)`.

Fix the ordered basis `B`. For `e notin B`, write the unique basis expansion

```text
v_e=sum_(b in B) beta_(e,b)v_b.
```

Set `kappa^e_e=1`, `kappa^e_b=-beta_(e,b)`, and set every other coordinate
to zero. This gives `(FO2)`. Its nonzero support is minimal: a smaller
dependence containing `e` would be a second expression for `v_e` in the
independent basis `B`, while a smaller dependence not containing `e` would
be a dependence inside `B`. It is therefore a row-scaling circuit and has
four or five blocks by the dependency.

When `q=3`, `B union {e}` has at most four elements, so every fundamental
circuit has exactly four. All coefficient points lie in the same projective
hyperplane. Writing its equation as

```text
(A+C gamma)c+(B_0+D gamma)d=0
```

gives

```text
[c:d]=[B_0+D gamma:-(A+C gamma)].                    (1)
```

The split-pencil dependency supplies distinct slopes and pairwise distinct
row classes. If the two linear forms in `(1)` were proportional, all but at
most one of the at least four rows would have the same projective class.
Thus `(1)` is one nonconstant Mobius graph. When `q=4`, the expression of
`v_e` uses three anchors exactly when one `beta_(e,b)` vanishes, giving a
four-block circuit; it uses all four anchors exactly when every coefficient
is nonzero, giving a five-block circuit.

The vectors `kappa^e` are independent because their coordinates outside
`B` form the identity matrix. Their number is `|I|-q=dim K`, so they form a
basis of `K`. More explicitly, for any `alpha in K`, subtract

```text
sum_(e notin B) alpha_e kappa^e.
```

The residual is a kernel vector supported inside `B`, and therefore vanishes
because `B` is independent. This proves `(FO3)`. Taking `alpha=1_I` proves
`(FO4)` and the claimed unique non-anchor owner. QED.
