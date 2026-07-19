# Proof

The quotient-block identity proves

```text
sum_(t!=1)R(t)=(n-1)(n-2).                         (1)
```

Every summand in `X_18^<=E` has `0<=e(t)<=E`. Multiplying `(1)` by `E`
therefore gives `(EBD1)`. If `(EBD2)` holds, then

```text
17X_18
 =17X_18^<=E+17X_18^>E
 <=17E(n-1)(n-2)+B_E(n)
 =300n^2.
```

This proves the sufficient reduction.

A target in the high tail has integer excess `e(t)>=E+1`. The proved
rich-excess degree ladder supplies at least

```text
7+ceil((E+1)/2)
```

small coefficient vectors and hence a center of degree `(EBD3)`. Direct
substitution gives degrees `4,6,8,10,12` at `E=0,2,6,10,14`.

For fixed guaranteed degree, increasing `E` decreases `B_E(n)`. The degree
changes first after cutoffs `0,2,6,10,14`; its next change would require
`E>=18`, where the conservative coefficient `300-17E` is negative. Thus the
five displayed choices are the Pareto cutoffs for this budget/degree
interface. Finally,

```text
B_E(n)=(300-17E)n^2+51E n-34E
```

proves that the table is conservative and that the exact budget is larger for
`E>0` and `n>=1`. QED.
