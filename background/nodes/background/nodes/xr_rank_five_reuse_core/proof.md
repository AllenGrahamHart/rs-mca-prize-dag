# Proof

Work first with an arbitrary family `F` of `m`-subsets of an `N`-set whose
pairwise intersections have size at most four.  Every member contains exactly

```text
b=C(m,4)
```

four-subsets, drawn from a universe of size `T=C(N,4)`.

Call a four-subset reused in a subfamily if at least two members of that
subfamily contain it.  Starting from `F`, repeatedly delete a member having
fewer than `c` reused four-subsets.  At the moment of deletion it has at least

```text
b-c+1=floor(T/(B+1))+1                              (1)
```

four-subsets that are unique in the current subfamily.  Charge those labels
to the deleted member.

Charges made at different deletion times are disjoint.  Indeed, a label
unique when it is charged belongs to no other member still present, so it
cannot be charged later.  It also cannot have been charged earlier, because
the current member was present at that earlier time.  If the peeling process
deleted every member, `(1)` would give

```text
|F| (floor(T/(B+1))+1) <= T.
```

But `|F|>B` implies `|F|>=B+1`, and

```text
(B+1)(floor(T/(B+1))+1)>T,
```

a contradiction.  A nonempty subfamily remains, and every one of its members
has at least `c` reused four-subsets.

Apply this to the extension-list reduction.  At `u=v=0`, the punctured kernel
is `GRS_4`, so every four-subset is a kernel basis.  Choosing exactly `m`
agreements preserves the pairwise cap.  In P-A that cap is four.  If a basis
`T_0` is reused, two selected errors have the restored common zero set

```text
G union T_0,
```

of size `(k-4)+4=k`; the post-strip cap makes it exact.  Fixing the kernel
basis puts all selected points containing it on its affine kernel-basis
pencil, and the post-strip pencil theorem caps that line by `floor(R/h)`.
Two different reused bases through one selected point give different lines:
otherwise a second point on that line would share both bases, hence at least
five agreement coordinates, contrary to the P-A cap four.  The peeling result
therefore gives the printed collision-line degrees.

For P-B, the pairwise agreement cap is three.  Hence no four-subset can occur
in two selected agreement sets.  Counting four-subsets directly gives

```text
|P| C(m,4) <= C(N,4),
```

which is the displayed bound.  Exact substitution gives all six printed
integers and completes the proof.
