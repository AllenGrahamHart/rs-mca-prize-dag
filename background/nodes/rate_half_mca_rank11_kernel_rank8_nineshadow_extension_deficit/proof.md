# Proof

Fix a rank-eight nine-subset `U subset S` and let

```text
C=cl_S(U), c=|C|, X=S minus C, q=|X|.
```

The kernel of evaluation on `U` has dimension two, so generalized MDS
gives

```text
c<=K'-2,  q=m'-c>=67474.                            (1)
```

The full support has evaluation rank ten: otherwise a nonzero degree-below
`K'` polynomial would vanish on all `m'>K'-1` support coordinates. Thus
the contraction by `U` has rank two on `X`.

For `x in X`, its parallel class in this rank-two contraction is

```text
P_x=cl_S(U union {x}) minus C.
```

The rank-nine closure `cl_S(U union {x})` is the common-zero set of a
one-dimensional polynomial space, so

```text
|P_x|<=K'-1-c.                                      (2)
```

Every `x` therefore has at least

```text
q-|P_x| >= (m'-c)-(K'-1-c)=67473                  (3)
```

partners outside its parallel class. Such a pair is independent in the
rank-two contraction and raises the rank of `U` to ten. Counting ordered
pairs in (3) and dividing by two gives at least

```text
67474*67473/2=C(67474,2)=L_2                       (4)
```

full-rank extensions. Hence at most `D_2=E_0-L_2` support pairs extend `U`
to a kernel eleven-set.

For the resource inequality, let `J_1,J_2,J_<2` count the record's
rank-nine, rank-eight, and lower-rank nine-subsets. Counting all 55
nine-subsets contained in every kernel eleven-set gives

```text
55 sum_d I_d
 <= E_1 J_1 + D_2 J_2 + E_0 J_<2
 =  E_0 C(m',9)-(E_0-E_1)J_1-L_2 J_2.             (5)
```

The spanning nine-shadow theorem gives

```text
3I_1<=E_1J_1,  6I_2<=E_2J_2.                       (6)
```

Substituting the lower bounds from (6) into the decreasing right side of
(5) and moving the resulting terms left gives (R8FC).
