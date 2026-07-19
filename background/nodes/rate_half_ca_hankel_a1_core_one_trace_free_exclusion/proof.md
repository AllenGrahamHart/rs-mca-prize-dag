# Proof

Assume every defect trace of `K` vanishes. The allocation-rigidity theorem
supplies the reduced complement square and its two possible exceptional
allocations.

Suppose first that `D_*=1` and `Z_W=E_Z`. Then the first reduced complement is
`(TFE1)`. The exceptional trace theorem gives

```text
deg gcd(q_0,P_X)>=e+3b>0.                             (1)
```

Choose a common root `x` over the splitting field. At `(gamma_0,x)`, both
terms on the left of `(TFE1)` vanish, whereas `P_cl(gamma_0)` is nonzero
because `gamma_0` is not a clean slope. This contradiction excludes the
`Z_W` allocation.

Therefore `Z_B=E_Z` when `D_*=1`. If `D_*=0`, there is no exceptional factor.
In both cases `P_clZ_B=P`, so the second reduced complement is `(TFE2)`.
Specializing at any supported slope `gamma` gives

```text
Q(gamma;X)A_1(gamma;X)=P_X(X).                        (2)
```

The specialization `Q(gamma;X)` is nonzero, hence divides `P_X`.

Now let `x` be a root of `B_X`. The products `P_X,B_X` have disjoint
squarefree root sets. If `Q(U,V;x)` had a supported root `gamma`, then
`Q(gamma;x)=0`; divisibility in `(2)` would imply `P_X(x)=0`, a contradiction.
Thus `v_x=0` at every one of the `c` nonsaturated rows. Saturated rows have
zero deficit, so the exact component ledger gives

```text
C_*=c e_*.                                             (3)
```

But direct subtraction yields

```text
e_*-C_*=4b+1-D_*>=0,                                  (4)
```

with equality exactly at `b=0,D_*=1`. Since `c>=1`, equation `(3)` and
`C_*<=e_*` force equality, `c=1`, and `(TFE5)`.

It remains to exclude this sole profile. The only possible exceptional
allocation is `Z_B=E_Z`, so the allocation theorem makes `q_0` squarefree of
degree `r-1`. Equation `(2)` at `gamma_0` is `(TFE6)`, and degree additivity
gives

```text
deg_X A_1(gamma_0;X)=(D_0-1)-(r-1)=D_0-r.             (5)
```

Allocation rigidity also gives `A=B_XA_1`. Here `deg B_X=c=1`, while the
original slope-side complement has `deg_X A=D_0-r`. Hence

```text
deg_X A_1<=D_0-r-1,                                   (6)
```

contradicting `(5)`. The trace-free branch is empty, so every surviving weld
has an active defect trace. QED.
