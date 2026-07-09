# F3 h=3 hyperbola-line degeneracy

Status: PROVED SYMBOLIC CLASSIFIER + FINITE-FIELD REPLAY.

This packet classifies the `3 | q-1` line cell that was left as an explicit
exception in the repaired h=3 rich-curve route.  It is not an activation bound
and it does not prove the geometric batching theorem; it pins the exact
coefficient condition under which the hyperbola normal form degenerates into
two rational lines.

## Statement

In the notation of `F3_H3_HYPERBOLA_IDENTITY.md`, assume the coefficient field
has characteristic not `3` and contains a primitive cube root `omega`.

For

```text
F(T) = T^3 + a T^2 + b T + c
G_F(u,v) = u^2 + uv + v^2 + a(u+v) + b
```

the hyperbola identity gives

```text
G_F(u,v) = X Y - Delta
Delta = a^2 alpha beta - b.
```

With

```text
alpha = (omega + 2)/3,    beta = (1 - omega)/3,
```

one has

```text
alpha beta = 1/3,
Delta = a^2/3 - b.
```

Therefore the same-fiber conic is a union of the two rational asymptote lines
exactly when

```text
b = a^2/3.
```

On that cell,

```text
G_F(u,v)
  = (u - omega v + a(1 - omega)/3)
    (u - omega^2 v + a(omega + 2)/3).
```

If `Delta != 0`, then `XY - Delta` is irreducible over the coefficient field.
Indeed, any nontrivial factorization of a degree-two polynomial must be a
product of two affine linear forms.  Comparing coefficients in

```text
XY - Delta = (rX+sY+t)(RX+SY+T)
```

and using `Delta != 0` gives `tT != 0`.  The `X^2`, `X`, `Y^2`, and `Y`
coefficient equations then force `r=R=s=S=0`, contradicting the `XY`
coefficient `1`.

## Role in T1

This closes one theorem-statement ambiguity in the repaired rich-curve route.
The hyperbola-line exception is not only the toral point `a=b=0`; it is the
whole codimension-one cell `b=a^2/3` after adjoining `omega`.  The eventual
bridge theorem should either pay this cell separately or exclude it before
applying `RC-RANK`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_hyperbola_line_degeneracy.py
```

Expected digest:

```text
H3_HYPERBOLA_LINE_DEGENERACY_PASS
```
