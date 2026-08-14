# Proof

The residual correction space has empty common zero set. Thus every
coordinate evaluation vector is nonzero, so the evaluation matroid
restricted to `T` has no loops.

Fix any rank basis `B` of `T`. There are

```text
|T minus B|=11-r=d+1
```

elements outside `B`. For each `e` outside `B`, its fundamental circuit
`C(e,B)` contains `e` and at least one element `b_e` of `B`; otherwise
`e` would be a loop. Fundamental-circuit exchange makes

```text
B_e=(B minus {b_e}) union {e}
```

a basis. The bases `B_e` are pairwise distinct because they contain
different outside elements, and none equals `B`. Hence `T` has at least

```text
1+|T minus B|=d+2                                      (1)
```

bases. The bound is sharp: take `r-1` coloops and one parallel class of
size `12-r=d+2`.

Now decorate each rank-`r` incidence `(gamma,T)` by all rank bases
`B subset T`. Fix one basis `B`. Every decorated record over `B` satisfies
the same coordinate equations on `B`. The common-quotient argument in the
canonical-basis globalizer therefore supplies one affine translation for
the complete set of such records; it did not use the canonical choice,
only that `B` is a basis. After cancellation, support-local transversality
bounds the number of records by `M_d`.

For every extension `T` of `B` with rank still `r`, all `d+1` coordinates
of `T minus B` are common zeros of `ker(ev_B)`. Generalized MDS leaves at
most `K'-10` choices outside `B`, hence at most
`C(K'-10,d+1)` extensions per record. Summing over all
`C(n',r)=C(n',10-d)` bases bounds the number of decorated incidences by

```text
D_d=C(n',10-d) M_d C(K'-10,d+1).                     (2)
```

If `I_d` is the undecorated rank-`d` incidence count, (1) gives
`(d+2)I_d<=D_d`. Taking the integer floor proves the displayed capacity.
