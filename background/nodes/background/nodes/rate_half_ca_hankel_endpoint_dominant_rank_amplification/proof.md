# Proof

Work over the algebraic closure.  Linear independence of the full
generator's `m+1` parameter coefficients survives scalar extension, so the
rational-normal kernel-curve theorem gives

```text
sr(Q)=m+1.                                             (1)
```

Fix an irreducible component `Q_i`, and write

```text
Q=Q_i G_i,       deg_(U,V) G_i=m-e_i.                 (2)
```

If `h_i=sr(Q_i)` and `g_i=sr(G_i)`, choose separated expressions

```text
Q_i=sum_(a=1)^h_i A_a(X)B_a(U,V),
G_i=sum_(c=1)^g_i C_c(X)D_c(U,V).
```

Multiplying them expresses `Q` as a sum of at most `h_i g_i` separated
terms.  Hence

```text
sr(Q)<=h_i g_i.                                       (3)
```

A biform of parameter degree `m-e_i` has separation rank at most the number
of parameter monomials, namely

```text
g_i<=m-e_i+1.                                         (4)
```

Combining `(1)`--`(4)` gives

```text
h_i>=ceil((m+1)/(m-e_i+1)),
```

which is `(DRA1)`.

For the dominant component, `m-e_*=b`, while component-defect localization
proves

```text
b<=floor((O-E)/4)<=floor((m-1)/4)=m/4-1.              (5)
```

Substitution in `(DRA1)` gives the first two inequalities in `(DRA2)`.  The
last denominator in `(5)` is at most `m/4`, so

```text
(m+1)/(floor((O-E)/4)+1)>4.
```

Its ceiling is at least five.  If `b=0`, then `G_*=1`, so `(2)` identifies
`Q_*` with `Q` and `(1)` gives exact rank `m+1`.  QED.
