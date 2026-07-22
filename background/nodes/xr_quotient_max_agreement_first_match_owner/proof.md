# Proof

Write

```text
Q_A=union_(c in C_fib) Q_c(A),
Q_>=A=union_(c in C_fib) Q_c(>=A).
```

The quotient boundary agreement owner gives

```text
Q_>=A subseteq Q_A union B_(A+1)(u,v).                  (1)
```

Split the exact-threshold set as

```text
Q_A=(Q_A \ B_(A+1)) union (Q_A intersect B_(A+1)).     (2)
```

The second term of `(2)` is already contained in the agreement carry. The
first is the union of the scale-wise sets `Q_c^max(A)` after deterministic
cross-scale first match. Substitution in `(1)` proves `(QMF2)`.

Now take `z in Q_c^max(A)` and a quotient witness `(p_z,S)` with `|S|=A`.
The global agreement set

```text
E_z(p_z)={x in D:u(x)+zv(x)=p_z(x)}
```

contains `S`. If it contained any additional point, then
`|E_z(p_z)|>=A+1`, so `z in B_(A+1)(u,v)`, contrary to `(QMF1)`. Hence
`E_z(p_z)=S`, proving `(QMF3)`.

Every slope in `Q_c^max(A)` has maximum code agreement exactly `A`: membership
in `Q_c(A)` gives agreement at least `A`, while exclusion from `B_(A+1)`
forbids more. It therefore cannot reappear as an unpaid slope at a later
agreement. At one threshold, order the declared scales and then the possible
witness codewords; assign each slope to its first witness. This makes the
owner disjoint without changing the union. QED.
