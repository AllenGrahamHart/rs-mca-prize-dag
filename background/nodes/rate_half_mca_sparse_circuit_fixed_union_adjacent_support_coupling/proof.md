# Proof

Fix `0<=i<=d-2` and an independent `i`-set `S subset D`. Contract `S` in
the evaluation matroid and restrict to the `N` points outside `D`. If `F` is
a rank-`r` flat in this restriction, choose a basis `A` of `F`. Imposing the
`r` outside evaluations on `W` leaves dimension at least `g-r`; this
subspace vanishes on `D` and on all of `F`. The common-root bound gives

```text
|F| <= K-u-(g-r)=R+r.                              (1)
```

Take `r=d-1-i`. Both `r` and `r+1` are at most `g-1`. Hence rank-`r`
flats have size at most `B=R+r`, rank-`r+1` flats have size at most `B+1`,
and `N>=R+d-1>=B`. Applying the adjacent-flat circuit coupling after
contraction gives

```text
(d+1-i) C_(d+1,i) + (N-R-d+1+i) C_(d,i)
 <= C(u,i) R C(N,d-i).
```

We retained every contracted circuit, so summing over the `C(u,i)` choices
of `S` is conservative and proves `(FAS1)`.

Expose a support-`d` circuit in this stratum by deleting one of its `d-i`
outside points. The remaining outside deletion points cut `W` by at most
`d-1-i`; after accounting for those already fixed roots, at most `R`
outside completions remain. Division by `d-i` proves `(FAS2)`.

Multiply `(FAS1)` by `w_(d+1)` and use `(FAS2)`. The coefficient of
`C_(d,i)` is `lambda_i`; its maximum over `0<=C_(d,i)<=L_i` is attained at
`L_i` when this coefficient is nonnegative and at zero otherwise. Integer
flooring gives `J_i`.

The two remaining support-`d` strata have bounds

```text
C_(d,d-1)<=C(u,d-1)R,              C_(d,d)<=C(u,d).
```

The three remaining support-`d+1` strata have bounds

```text
C_(d+1,d-1)<=floor(C(u,d-1)RN/2),
C_(d+1,d)<=C(u,d)R,                C_(d+1,d+1)<=C(u,d+1).
```

These follow by exposing one outside point, with division by two in the
two-outside stratum. Adding all strata proves `(FAS3)`. Finally, bounds on
disjoint support pairs concern disjoint census terms and may therefore be
summed. QED.
