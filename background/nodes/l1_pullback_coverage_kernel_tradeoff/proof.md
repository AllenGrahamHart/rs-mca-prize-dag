# Proof - L1 pullback coverage/kernel tradeoff

## 1. Residue-class dimensions

Write

```text
k=us+v,       0<=v<s.                                 (1)
```

The number `k_j` is the count of exponents in `{0,...,k-1}` congruent to
`j modulo s`. Hence

```text
k_j=u+1 for 0<=j<v,
k_j=u   for v<=j<s.                                   (2)
```

If `b<=u`, every term in `(CK1)` is active, so

```text
kappa=sum_j(k_j-b)=k-sb.                              (3)
```

If `b>=u+1`, every term vanishes, while

```text
k-sb<=us+v-s(u+1)=v-s<0.                              (4)
```

There is no integer strictly between `u` and `u+1`. Equations `(3)` and `(4)`
prove `(CK2)`, including `b=0` and `k<s`.

## 2. Agreement forces coverage or partial loss

Let `E_f` be the fully agreed complete-fiber labels. Since `E_f subset B`,
the exact identity from the partial router gives

```text
a_*<=|Agr(f,U)|=s|E_f|+z(f)<=sb+z(f).                 (5)
```

Substituting `a_*=k+ell-1` proves `(CK3)`. If `sb>=k`, equation `(CK2)` gives
`kappa=0`, so `(CK4)` is immediate. If `sb<k`, then `(CK2)` and `(CK3)` give

```text
z(f)>=ell-1+(k-sb)=ell-1+kappa,                       (6)
```

which rearranges to `(CK4)`. The two implications in `(CK5)` follow.

Finally, on `z<=Z<=ell-1+K`, equation `(CK5)` supplies `kappa<=K` to
`l1_partial_pullback_johnson_router`. Its proved tame map aggregate is
`n^(3+gamma K)`, establishing `(CK6)` and the stated residual.
