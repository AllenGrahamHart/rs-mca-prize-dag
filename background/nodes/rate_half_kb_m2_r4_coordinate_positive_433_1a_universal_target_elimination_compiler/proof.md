# Proof

Substituting `(KBUTE-1)` makes the first two equations of `(KBUTE-2)`
tautological.  The other two become

```text
(be)(cf)-sigma bc(sigma ef)=0,
b(de)(cf)-c(df)(be)=0,                            (1)
```

because `sigma^2=1`.  Hence every target realization satisfies the four
binomials.

Conversely, suppose the seven records are nonzero and satisfy
`(KBUTE-2)`.  Define `d,e,f` by `(KBUTE-3)`.  Then `be=X_BE`, `cf=X_CF`,
and `de=X_DE+`.  The cross binomial gives

```text
df=(b X_DE+/X_BE)(X_CF/c)=X_DF+.
```

The third binomial gives

```text
sigma ef=sigma X_BE X_CF/(bc)=X_EF.
```

The sign binomials supply `X_DE-` and `X_DF-`.  This proves necessity and
sufficiency of the product ideal and the explicit reconstruction.

For the squared sums, substitute `d=bX_DE+/X_BE`, `e=X_BE/b`, and
`f=X_CF/c`.  Clearing the respective nonzero denominators gives

```text
(d+e)^2=(b^2X_DE+ +X_BE^2)^2/(b^2X_BE^2),
(d-e)^2=(b^2X_DE+ -X_BE^2)^2/(b^2X_BE^2),

(d+f)^2=(c^2X_DF+ +X_CF^2)^2/(c^2X_CF^2),
(d-f)^2=(c^2X_DF+ -X_CF^2)^2/(c^2X_CF^2),

(e+sigma f)^2=(cX_BE+sigma bX_CF)^2/(b^2c^2),
(b+e)^2=(b^2+X_BE)^2/b^2,
(c+f)^2=(c^2+X_CF)^2/c^2.                        (2)
```

Equations `(2)` are exactly `(KBUTE-4)`.  The reconstruction proves the
converse as well, so the product and squared-sum target elimination is
exact.

Every formal outside case is only an assignment of the seven labeled
records to `xi` and three unordered source deck pairs.  The sealed symmetry
certificate lists all 267 representatives.  Replacing each `X_R,H_R` in
the universal equations by `F` and `H` at its assigned source slot therefore
compiles every case without further target algebra.

For template A, the record assignment is

```text
DE+=F(u), DF-=F(-u), DE-=F(v), CF=F(-v),
DF+=F(w), BE=F(-w), EF=F(xi).
```

The cross binomial becomes the first equation in `(KBUTE-6)`.  For template
B, use

```text
DE+=F(u), CF=F(-u), DE-=F(v), DF+=F(-v),
DF-=F(w), BE=F(-w), EF=F(xi),
```

which gives the second. QED.
