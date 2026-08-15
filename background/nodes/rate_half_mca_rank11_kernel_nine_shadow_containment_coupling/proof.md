# Proof

Fix one record support `S`, and let `J_1` be the number of its rank-nine
nine-subsets. Every counted kernel eleven-set contains exactly
`C(11,9)=55` nine-subsets.

If a rank-nine nine-subset `U` lies in a counted rank-deficient eleven-set
`T`, then `T` also has rank nine: it cannot have smaller rank than `U` and
the kernel lane has rank at most nine. Both coordinates of `T minus U`
therefore lie in `cl(U)`. The kernel of evaluation on `U` is
one-dimensional, so generalized MDS gives

```text
|cl(U)| <= K'-1.
```

After removing the nine points of `U`, there are at most `K'-10` choices,
and hence at most

```text
E_1=C(K'-10,2)                                      (1)
```

extensions.

Every lower-rank nine-subset has at most the unrestricted support-pair
count

```text
E_0=C(m'-9,2)                                       (2)
```

extensions to an eleven-subset of `S`. Partitioning all nine-subset flags
by these two rank classes gives

```text
55 I(S) <= E_1 J_1 + E_0(B_9-J_1)
          = E_0 B_9-(E_0-E_1)J_1.                  (3)
```

The nine-shadow theorem says that every corank-one eleven-set has at least
three spanning rank-nine nine-subsets. Double counting those spanning
flags with (1) gives

```text
3 I_1(S) <= E_1 J_1,
J_1 >= 3 I_1(S)/E_1.                               (4)
```

Here `E_0>E_1`, since `m'=K'+67472`. Substitute the lower bound (4) into
the decreasing right side of (3):

```text
55 I(S)
 <= E_0 B_9-3(E_0-E_1)I_1(S)/E_1.
```

Moving the final term left and separating `I_1` yields (FC), because

```text
55+3(E_0-E_1)/E_1 = 52+3E_0/E_1.
```

When `E_1=0`, no corank-one eleven-set has two extension coordinates, so
`I_1=0` and the remaining unrestricted flag count proves the stated
convention.
