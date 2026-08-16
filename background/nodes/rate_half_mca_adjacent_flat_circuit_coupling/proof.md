# Proof

For a rank-`r` flat `F`, put `b=|F|` and let `t_F` be the number of
independent `r`-sets spanning `F`.  Every `(r+1)`-circuit exposes `r+1`
independent `r`-sets in its rank-`r` closure.  Hence

```text
sum_F t_F(b-r) >= (r+1) C_(r+1).                  (1)
```

For every independent `r`-set `A` spanning `F` and every `x` outside `F`,
put `Q=A union {x}` and give this witness weight `b-r`.  The set `Q` is
independent.  Its rank-`(r+1)` closure has at most `B+1` elements.  A point
completing `Q` to an `(r+2)`-circuit cannot lie in `F`, since `A` together
with that point would be a dependent proper subset.  Thus `Q` has at most

```text
(B+1)-b-1 = B-b
```

exact circuit completions.  The unrestricted completion ceiling from the
same flat cap is `B-r`, so the witness certifies loss at least `b-r`.

An independent `(r+1)`-set has only `r+1` subsets of size `r`, and therefore
receives at most `r+1` such witnesses.  If `c(Q)` is its number of exact
`(r+2)`-circuit completions, summing witness weights gives

```text
sum_F t_F(N-b)(b-r)
 <= (r+1) sum_Q ((B-r)-c(Q)).                     (2)
```

Since `b<=B` and `N>=B`, equations `(1)` and `(2)` imply

```text
sum_Q ((B-r)-c(Q)) >= (N-B) C_(r+1).              (3)
```

Every `(r+2)`-circuit is exposed by its `r+2` independent `(r+1)`-subsets,
so `sum_Q c(Q)=(r+2)C_(r+2)`.  There are at most `C(N,r+1)` independent
`(r+1)`-sets.  Substitution in `(3)` proves `(AFC)`. QED.
