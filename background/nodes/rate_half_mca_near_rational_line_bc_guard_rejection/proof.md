# Proof

Use the deployed construction from upstream `#1160`.  Let

```text
E={e_1,...,e_w},  w=67472,
v(e_j)=1,          u(e_j)=-gamma_j,
u=v=0              on D\E,
```

where the `gamma_j` are distinct.  Fix one of the displayed bad slopes
`gamma_i` and put `U_i=u+gamma_i v`.  On `e_i` its value is zero.  On every
other `e_j` it is `gamma_i-gamma_j`, which is nonzero by distinctness, and it
is zero off `E`.  Therefore

```text
supp(U_i)=E\{e_i},  |supp(U_i)|=w-1=67471.
```

Let

```text
W_i(X)=product_{x in E\{e_i}} (X-x),  N_i(X)=0.
```

For every `x` in `D`, either `U_i(x)=0` or `W_i(x)=0`, so
`W_i(x)U_i(x)=N_i(x)`.  Thus `(W_i,N_i)` is a nonzero member of

```text
M_{U_i}={(W,N): W(x)U_i(x)=N(x) for every x in D}.
```

Under the effective source shift `K=k+1`, its shifted degree is

```text
max(deg W_i, deg 0-(K-1))=deg W_i=67471.
```

Consequently the minimal shifted degree `d1(U_i)` is at most `67471`.  The
cycle-19 candidate BC contract contains the necessary guard
`MINIMAL_SHIFTED_DEGREE_AT_LEAST_67472`.  That guard fails for `gamma_i`.
Since `i` was arbitrary, all `w=67472` displayed bad slopes are rejected.

This proves rejection without assuming an exact value of `d1`, constructing
a reduced basis, or enumerating any field elements.
