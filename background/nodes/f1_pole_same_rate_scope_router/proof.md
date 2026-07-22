# Proof

The F1 minimal-field theorem assigns each pencil datum one field

```text
B subseteq K subseteq F.                              (1)
```

The construction used by the proved interleaved pole import fixes a domain
`D subset B`, a degree bound `kappa`, and the two codes

```text
C_K=RS[K,D,kappa],       C_B=RS[B,D,kappa].          (2)
```

Coordinate expansion along a `B`-basis of `K` gives

```text
Phi(C_K)=C_B^e,       e=[K:B].                       (3)
```

Thus Weil restriction replaces one `K`-valued codeword by `e` coupled
`B`-valued codewords.  It leaves the evaluation set `D`, its cardinality
`n`, and the polynomial degree bound `kappa` unchanged.  Both sides of `(2)`
therefore have the same RS rate

```text
rho=kappa/n.                                        (4)
```

The pole itself also preserves these parameters.  For `alpha in K\B`, the
proved construction takes a polynomial `P` of degree below `kappa` and forms

```text
f_alpha(x)=U(x)/(x-alpha),
g_alpha(x)=-1/(x-alpha),
z=P(alpha).
```

On the selected support,

```text
f_alpha+z g_alpha=(P(X)-P(alpha))/(X-alpha),
```

whose degree is again below `kappa`.  No puncture, shortening, or dimension
shift occurs in the extension-pole/list-window import.

At an intermediate tower level, replace `K` by the next field between `B`
and `F`.  The same argument applies with the same `D` and `kappa`; induction
therefore preserves `(4)` through the whole tower.

The imported list threshold is read at the corresponding base row.  By
`(4)`, an ambient clean-rate row can only call the base-list theorem at that
same clean rate.  A rate-`1/2` base-list theorem enters only from a
rate-`1/2` ambient row.  This proves the claimed scope separation.  QED.
