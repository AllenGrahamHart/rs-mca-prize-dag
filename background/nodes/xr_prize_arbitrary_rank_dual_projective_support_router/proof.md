# Proof

Extend every trade row by zero to the union `X` of their supports. Each row
annihilates `W`, so its `r`-dimensional span `L` satisfies `(AR1)`. The general
row-scaling circuit theorem gives `(AR2)`.

Choose a basis `F_1,...,F_r` and write

```text
lambda_i=sum_j c_(ij)F_j.
```

No point of `X` is a common zero of all basis vectors, since it would vanish
in every row and hence lie outside the support union. This proves `(AR3)`,
and `(AR4)` follows directly.

For row scalars `alpha_i`, the scaled rows satisfy both trade equations
exactly when

```text
sum_i alpha_i c_i=0,
sum_i gamma_i alpha_i c_i=0.                          (1)
```

Thus their scaling kernel is the column kernel of `(AR5)`. Circuit minimality
makes this kernel one-dimensional with a generator having no zero entry.
After row rescaling, that generator is all-one. Therefore the columns have
rank `t-1` and every proper subset is independent.

If three coefficient vectors had the same projective direction, their three
Segre columns `(c_i,gamma_i c_i)` would lie on one two-dimensional ruling
space and be dependent. That would be a proper scaling subtrade, impossible
for a circuit of rank `r>=2`. Hence direction multiplicity is at most two.
For a repeated pair the corresponding rows are proportional and have the same
support. The two selected slopes force both received directions to restrict
into `W` on that support, giving the proved basis/flat owner.

For selected block `i`, pairing its zero equation with `lambda_i` gives

```text
sum_j c_(ij)<F_j,b>+
gamma_i sum_j c_(ij)<F_j,q>=0.                       (2)
```

This is exactly `theta dot z_i=0`. Since the `z_i` span dimension `t-1`,
their annihilator has dimension `2r-(t-1)=2r-t+1`, proving `(AR7)`. At
`t=2r+1` it is zero, so every basis vector annihilates both `b` and `q`.

Conversely, `(AR1)` makes every row a valid `W` parity vector. The projective
circuit dependence supplies both vector trade equations, and an interaction
vector in the column annihilator supplies every selected trade-row pairing in
`(2)`. Certified parent blocks retain actual agreement realization. This
proves the stated converse and no more. QED.
