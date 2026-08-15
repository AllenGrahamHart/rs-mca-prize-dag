# Proof

Induct on `m`.  The rank-three base case `m=3` is immediate.

If `M` has a coloop `e`, then `M minus e` is a loopless rank-two matroid on
`q=m-1` elements.  If its parallel-class sizes are `q_1,...,q_j`, then

```text
2 b(M) = q^2-sum_i q_i^2
       >= q^2-a q
        = (m-1)(m-1-a),
```

because `q_i<=a` gives `sum_i q_i^2<=a sum_i q_i=aq`.

Now suppose `M` has no coloop.  Choose an element `e` in a smallest
parallel class `P`, and put `c=|P|`.  Deletion preserves rank three, so
induction gives

```text
2 b(M minus e) >= (m-2)(m-2-a).                  (1)
```

In `M/e`, the other `c-1` elements of `P` are loops.  Every nonloop
parallel class of the rank-two contraction is a union of parallel classes
of `M`: geometrically, it is the union of the points on one line through
the point represented by `P`.  Since `P` was smallest, each such class has
at least `c` elements.  There are at least two of them, and their total
size is `m-c`.

For fixed total size, merging contraction classes can only decrease the
number of independent pairs.  Subject to having at least two classes, each
of size at least `c`, the minimum therefore has class sizes `c` and
`m-2c`; hence

```text
b(M/e) >= c(m-2c).                                (2)
```

The simplification of a rank-three matroid has at least three points, so
`m>=3c`.  For `c=1`, the right side of `(2)` is `m-2`.  For `c>=2`,

```text
c(m-2c)-(m-2)
 >= 3c(c-1)-2c^2+2
  = (c-1)(c-2) >= 0.
```

Thus `b(M/e)>=m-2`.  Deletion-contraction and `(1)` now give

```text
2 b(M) >= (m-2)(m-2-a)+2(m-2)
         = (m-2)(m-a)
         = (m-1)(m-1-a)+(a-1),
```

which proves `(BP)`.  In the stated coloop construction (where
`m-1>=2a` ensures at least two rank-two classes),
`sum_i q_i^2=a(m-1)`, so equality holds.
