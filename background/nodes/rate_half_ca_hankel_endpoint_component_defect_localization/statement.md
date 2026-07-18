# Component-defect localization at the strict endpoint

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Retain the strict-endpoint factorization from
`rate_half_ca_hankel_endpoint_rational_branch_exclusion`.  Thus

```text
rho=4m-1,       N=16m,       T=4m+1,
I=T*rho-O,       0<=O<=m-1,
Q=product_i Q_i,       (r_i,e_i)=(deg_X Q_i,deg_(U,V) Q_i),
```

and there is one defect-one component `i_*` with
`r_*=4e_*-1`; every other component has `r_i=4e_i`.  Put

```text
I_i=|{(x,gamma) in D x Z:Q_i(gamma;x)=0}|,
E=sum_i I_i-I,
D_i=T*r_i-I_i,
C_i=N*e_i-I_i,
b=sum_(i!=i_*) e_i=m-e_*.                            (CDL1)
```

Then `Q` is squarefree over the algebraic closure, `E>=0`, and the exact
component ledgers are

```text
sum_i D_i=O-E,
sum_i C_i=1+O-E.                                     (CDL2)
```

In particular `0<=E<=O`.  The dominant and residual deficits satisfy

```text
C_*-D_*=4b+1,
D_i-C_i=4e_i                    for i!=i_*.           (CDL3)
```

Consequently every residual parameter degree consumes four units of the
actual omission budget:

```text
4b<=O-E,
b<=floor((O-E)/4),
e_*>=m-floor((O-E)/4).                               (CDL4)
```

The defects are localized to a small exceptional part of the grid:

1. at least `3m+2` supported slopes make every `Q_i` squarefree and
   completely `D`-split, with pairwise disjoint component root sets;
2. at least `N-(1+O)>=15m` domain points make every `Q_i(x)` squarefree and
   completely `Z`-split, again with pairwise disjoint component root sets;
3. at least `3m+1-O>=2m+2` of the slopes in item 1 are also
   parameter-transverse at every component root.

For the official `m=2^37`, `(CDL4)` gives

```text
b<=floor((O-E)/4)<=2^35-1,
e_*>=2^37-floor((O-E)/4)>=3*2^35+1.                  (CDL5)
```

This theorem does not exclude the dominant component.  It replaces the
worst-case residual bound by an omission-sensitive exact ledger and pins
where any residual factor or component intersection must spend that budget.
