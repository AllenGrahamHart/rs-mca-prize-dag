# Proof

Fix `d` in `{3,...,9}` and let `J_d(S)` count rank-`(10-d)` nine-subsets of
`S`.  The shared nine-shadow theorem gives

```text
s_d I_d(S) <= E_d J_d(S).                               (1)
```

Now fix one such nine-subset `U`.  Write `C=cl_S(U)`, `c=|C|`, and
`X=S\C`.  The generalized-MDS closure cap is `c<=K'-d`, so

```text
q=|X|>=67472+d.
```

After contracting `U`, every parallel class in `X` has size at most
`K'-d+1-c`: adjoining that class to `C` gives a rank-`(11-d)` closure.
Consequently every `x in X` has at least

```text
q-(K'-d+1-c)=67471+d
```

partners outside its parallel class.  At least

```text
q(67471+d)/2 >= C(67472+d,2)=L_d
```

unordered pairs therefore raise the rank of `U` by two.  They produce
rank-`(12-d)` eleven-subsets counted by `I_(d-2)(S)`.

It remains to bound the reverse multiplicity.  Let `T` be one rank-`(12-d)`
eleven-subset and let `D=T\U`.  The dual-rank identity

```text
r_T(T\D)=r_T(T)-|D|+r_(T*)(D)
```

shows that `U` has rank `10-d` exactly when the complementary pair `D`
consists of two coloops of the evaluation matroid on `T`.  That matroid is
loopless, has rank `12-d`, and has eleven elements.  It has at most
`11-d` coloops: `12-d` coloops would leave the remaining elements as loops.
Thus `T` contains at most `Q_d=C(11-d,2)` such nine-subsets, and double
counting rank-raising pairs gives

```text
L_d J_d(S) <= Q_d I_(d-2)(S).                           (2)
```

Combining (1) and (2) proves `(H_d)`.
