# Proof

Fix `d`, put `r=10-d`, and restrict the evaluation matroid to one counted
eleven-set `T`. This rank-`r` matroid `M` is loopless. Its dual `M*` has
rank

```text
c=11-r=d+1
```

and has no coloops. A nine-subset spans `M` exactly when its complementary
two-subset is independent in `M*`.

Ignore loops of `M*` and partition its other elements into parallel
classes. If there are at least `c+1` classes, choosing one representative
from each of `c+1` classes exhibits at least `C(c+1,2)` independent pairs.
If there are exactly `c` classes, their simplification is a rank-`c` free
matroid. A singleton class would then be a coloop, so every class has at
least two elements. There are at least

```text
4 C(c,2) >= C(c+1,2)       (c>=2)
```

independent cross-class pairs. Thus `T` has at least

```text
C(c+1,2)=C(d+2,2)                                  (1)
```

spanning nine-subsets. Equality is possible: `M` may have `r-1` coloops
and one parallel class of size `d+2`.

Now fix a rank-`r` nine-subset `U subset S`. Its kernel

```text
H=ker(ev_U)
```

has dimension `d`. Every coordinate in the matroid closure of `U` is a
common zero of `H`. Generalized MDS bounds this closure by `K'-d`
coordinates. Since `U` already contains nine coordinates, at most
`K'-d-9` further coordinates are available. Hence `U` lies in at most

```text
C(K'-d-9,2)                                         (2)
```

rank-`r` eleven-subsets.

Let `J_d(S)` count rank-`(10-d)` nine-subsets of `S`. Double-counting
pairs `(T,U)` with `U subset T` and `rank(U)=rank(T)=10-d`, using (1) and
(2), gives

```text
C(d+2,2) I_d(S) <= C(K'-d-9,2) J_d(S).              (3)
```

Every nine-subset has one rank from 1 through 9 because the evaluation
matroid is loopless, so

```text
sum_d J_d(S)=C(m',9).
```

Divide (3) by its extension coefficient and sum over `d` to obtain (NS).
If the coefficient is zero, (3) forces `I_d(S)=0` directly.
