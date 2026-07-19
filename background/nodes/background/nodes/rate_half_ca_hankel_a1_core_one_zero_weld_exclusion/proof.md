# Proof

Assume `K=0`. By the zero-weld quartic-boundary theorem, the only possible
profile has `b=0,D_*=1`, and

```text
F(U,V)-G_0(X)=Q_*(U,V;X)V_0(U,V;X).                   (1)
```

Here `Q_*=Qbar` is the full irreducible residual generator of parameter
degree `e`; `F` is the squarefree product of the `4e` clean supported-slope
linear forms; and `G_0` has as roots exactly `8e+4` of the `8e+7` points of
`D\S`. Let the remaining three domain points be `x_1,x_2,x_3`.

For a residual domain point `x`, let `v_x` be the number of distinct roots of
`Q_*(U,V;x)` in the full supported-slope set. The component norm theorem
defines

```text
C_*=sum_(x in D\S)(e-v_x)=e-5b-1+D_*=e.              (2)
```

If `G_0(x)=0`, equation `(1)` gives

```text
F(U,V)=Q_*(U,V;x)V_0(U,V;x).                          (3)
```

The specialization `Q_*(U,V;x)` is nonzero, because `F` is nonzero. As a
nonzero homogeneous form it retains parameter degree `e`. Since the right
side divides the squarefree split form `F`, it has `e` distinct roots among
the clean supported slopes. Thus `v_x=e`, as is also consistent with the
nonnegative component-deficit ledger.

Now take one of the omitted points `x_j`. Then `G_0(x_j)!=0`. For every clean
supported slope `gamma`, evaluating `(1)` at `gamma` gives

```text
-G_0(x_j)=Q_*(gamma;x_j)V_0(gamma;x_j)!=0.            (4)
```

Hence `Q_*(gamma;x_j)!=0` at all `4e` clean slopes. The full supported set
has only one further slope, the exceptional slope isolated by the dependency.
Therefore `v_(x_j)<=1`, and `x_j` contributes at least `e-1` to `(2)`.

Summing only these three nonnegative contributions yields

```text
C_*>=3(e-1).                                          (5)
```

The official `e=2^38-1` is greater than one, so `3(e-1)>e`, contradicting
`C_*=e` in `(2)`. The quartic boundary is impossible. It was the sole
possible zero-weld profile, hence `K!=0` throughout the stated face. QED.
