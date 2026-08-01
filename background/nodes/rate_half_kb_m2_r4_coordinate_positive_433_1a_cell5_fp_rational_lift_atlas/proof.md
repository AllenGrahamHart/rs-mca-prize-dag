# Proof

Ordinary block elimination of the fully saturated common ideal gives the
printed `r` equation and four printed equations linear in `c`.  Since
`t^2+1` is a source-label collision guard, `(KBL-1)` uniquely determines `r`
at every point of `X`.

Let `L_2,...,L_5` denote the four `c` coefficients.  Exact deployed-field
reduction gives

```text
<P,L_2,L_3,L_4,L_5> = <G_1,G_2,E(t)>,

E(t)=(t-i)(t+i)^2 C(t),
C(t)=t^3-33423359t^2-33423357t-1.                (KBL-2)
```

The factors `t=+-i` are forbidden source-label collisions.  It remains to
show that `C` has no root in `F_p`.  Modulo `C`, exact binary powering gives

```text
t^p-t = -625851931t^2+304558258t-650418019 = R(t).
```

The sealed low-degree Bezout certificate verifies

```text
(875240034-43240565t) C(t)
 +(-92214746t^2-514662088t+491979529) R(t) = 1.  (KBL-3)
```

Thus `C` and `t^p-t` have no common root.  Therefore the four `L_j` cannot
vanish simultaneously at a guarded `F_p` point.  At least one printed
linear equation uniquely determines `c`; together with `(KBL-1)`, two
points of `X(F_p)` with the same `(b,t)` coincide. QED.
