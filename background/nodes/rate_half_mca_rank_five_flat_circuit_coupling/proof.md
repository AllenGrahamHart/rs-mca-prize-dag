# Proof

For a rank-three flat `F`, write `b=|F|` and let `t_F` be the number of
independent triples spanning `F`.  Every four-circuit in `F` exposes four
such triples, while an independent triple has at most `b-3` fourth points.
Consequently

```text
sum_F t_F(b-3) >= 4 C_4.                            (1)
```

For each pair consisting of an independent triple `A` spanning `F` and an
element `x` outside `F`, put `Q=A union {x}` and assign the pair weight
`b-3`.  The set `Q` is independent.  Its rank-four closure has at most
`B+1` elements.  A fifth point completing `Q` to a five-circuit cannot lie
in `F`, because then `A` together with that point is a dependent proper
subset.  Hence `Q` has at most

```text
(B+1)-b-1 = B-b
```

five-circuit completions.  The unrestricted rank-four-flat ceiling is
`B-3`, so this witness forces completion loss at least `b-3`.

An independent four-set has four triples and therefore receives at most four
witnesses.  If `c_5(Q)` is its number of five-circuit completions, summing
the witness weights gives

```text
sum_F t_F(N-b)(b-3)
 <= 4 sum_Q ((B-3)-c_5(Q)).                         (2)
```

Since `b<=B`, equations `(1)` and `(2)` imply

```text
sum_Q ((B-3)-c_5(Q)) >= (N-B) C_4.                 (3)
```

Every five-circuit is exposed by its five independent four-subsets, so
`sum_Q c_5(Q)=5C_5`.  There are at most `C(N,4)` independent four-sets.
Replacing their number by this upper bound in `(3)` proves `(FC)`.  QED.
