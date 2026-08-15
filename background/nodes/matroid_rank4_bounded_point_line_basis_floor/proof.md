# Proof

Induct on `r=m-a`.  At `r=3`, rank four supplies at least one basis, so
`6b(M)>=6=Q_a(3)`.

First suppose `M` has a coloop `e`.  Its deletion is a loopless rank-three
matroid on `q=m-1` elements.  Choose an ordered triple sequentially.  There
are `q` choices for the first element, at least `q-a=r-1` choices outside
its parallel class, and at least `q-(a+1)=r-2` choices outside the rank-two
flat spanned by the first two.  Thus

```text
6b(M)>=q(r-1)(r-2)=C_a(r).                         (1)
```

Now suppose `M` has no coloop.  Choose `e` in a smallest parallel class
`P`, of size `c`.  The simplification has at least four points, so
`c<=floor(m/4)`.  A rank-two flat through `P` and any other parallel class
contains at least `2c` elements, so `c<=floor((a+1)/2)`.  Therefore

```text
c<=h_a(r).                                         (2)
```

Deletion preserves rank four and the two flat ceilings, hence induction
gives `6b(M minus e)>=Q_a(r-1)`.  In `M/e`, the other elements of `P` are
loops.  Delete them.  The remaining rank-three contraction has

```text
q=m-c
```

nonloops, and each of its parallel classes is a rank-two flat through `P`
with `P` removed.  Its parallel-class ceiling is therefore `a+1-c`.
The rank-three bounded-parallel theorem gives

```text
2b(M/e)>=(q-1)(q-1-(a+1-c))
         =(a+r-c-1)(r-2).
```

By `(2)`,

```text
6b(M/e)>=3(a+r-h_a(r)-1)(r-2)=L_a(r).              (3)
```

Deletion-contraction, induction, and `(3)` give the second branch in the
recurrence.  Together with the coloop branch `(1)`, this proves `(BPL)`.

For the explicit evaluator, unfold the recurrence.  Besides the base path,
every candidate chooses a last coloop reset at `j>=4` and then pays all
increments:

```text
C_a(j)+sum_(x=j+1)^r L_a(x).
```

The difference between the candidates at `j+1` and `j` is

```text
(j-1)(3h_a(j+1)-a-2).
```

Since `h_a` is nondecreasing, these candidates have one turn.  Also the
base path is no larger than the `j=4` reset by `6(h_a(4)-1)>=0`.  Thus the
minimum is the base path or the reset immediately before the first
nonnegative difference.  Splitting
`h_a(x)=min(floor((a+1)/2),floor((a+x)/4))` at its constant branch and by
`a+x modulo 4` evaluates every increment sum with integer polynomial sums.
