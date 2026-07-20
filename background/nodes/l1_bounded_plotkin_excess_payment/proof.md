# Proof - L1 bounded Plotkin-excess payment

Let `mathcal A` be the combined-set code from the Plotkin-boundary theorem.
It has length

```text
V=4ell+E
```

and minimum Hamming distance at least `2ell`.

Choose any fixed set `J` of `E` coordinates and partition `mathcal A` by the
binary pattern on `J`. There are at most `2^E` classes. Within one class,
all codewords have the same pattern on `J`, so deleting those coordinates
does not change any pairwise distance. The punctured class therefore has

```text
length 4ell,       minimum distance at least 2ell.       (1)
```

Its sign vectors have pairwise nonpositive inner products. The Rankin lemma
from the boundary theorem bounds the class by `2(4ell)`. Summing the
`2^E` classes gives

```text
|mathcal A|<=2^E*2(4ell)=2^(E+1)(V-E),                  (2)
```

which is `(PX2)`.

At fixed `p<=P`, there are at most `2^M(P+1)n^P` exact petal-support patterns
and at most `n` defect degrees. Under `E<=E_0`, multiply these factors by
`(PX2)<=2^(E_0+1)n` and use `2^M<=n^(1/c_0)` to obtain `(PX3)`. This proves
the escape statement `(PX4)`.

Finally, the official source equation is

```text
(r-1)N+r=Mell+b.
```

Multiplying `E=N+b-4ell` by `r-1` and substituting `b=ell-g` gives

```text
(r-1)E
 =Mell+b-r+(r-1)b-4(r-1)ell
 =(M-3(r-1)+1)ell-r(g+1),
```

which proves `(PX5)` including every additive constant.
