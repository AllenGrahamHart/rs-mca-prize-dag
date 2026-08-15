# Proof

Let

```text
C'={f in F[X]: deg f<K'}
```

be the residual Reed-Solomon polynomial space.  The dense-root high-span
saturation theorem gives

```text
V' <= C',       dim V'=10.                           (1)
```

Set `K'=10`.  Then `dim C'=10`, so (1) forces `V'=C'`.

Fix any nine distinct residual evaluation points

```text
B={b_1,...,b_9}.
```

For arbitrary values `y_1,...,y_9`, Lagrange interpolation gives a unique
polynomial `f` of degree at most eight satisfying `f(b_i)=y_i`.  This
polynomial belongs to `C'=V'`.  Hence the restriction map

```text
ev_B:V' -> F^B
```

is surjective and has rank nine.  Equivalently, the `9` by `9`
Vandermonde minor formed by `1,X,...,X^8` is

```text
product_(1<=i<j<=9) (b_j-b_i) !=0.
```

The rank-eight branch of the target router requires `rank(ev_B)=8`, which
is impossible.  Therefore that branch is empty at `K'=10`.

The adjacent-row boundary is genuine for this method.  At `K'=11`, the
fixed-chart fence takes

```text
V'=span{1,X,...,X^7,L_B,XL_B},
```

where `L_B` is the locator of a nine-set `B`; its restriction to `B` has
rank eight.  Thus only the row `K'=10` follows from dimension equality.
