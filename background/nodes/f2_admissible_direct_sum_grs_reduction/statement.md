# Admissible-row F2 direct-sum reduction

Fix an official maximal row with

```text
n=2^41,  q=p^e<2^256,  n divides q-1,
e_p=v_2(p-1),  D=(41-e_p)_+,  k=ord_n(p)=2^D.
```

The official degree bound gives `k|e` and `e<=6`, hence `D<=2`.

Let `W` be either an exact-order layer or its nested subgroup, choose one
representative from each antipodal pair, and let `m=|W|/2`. Suppose the odd
exponent set contains a run of `R` consecutive odd exponents. The
representatives split into `C` prime-field proportionality classes, where

```text
C=1 if D_a<=1 and C=2^(D_a-1) otherwise    (exact-order layer),
C=2^D_a                                      (nested layer),
S=m/C.
```

On every admissible row `C<=4`, and the F2 dual kernel satisfies

```text
L^perp = direct_sum_(c=1)^C ker(A_c),
ker(A_c) is an [S,S-R,R+1]_p GRS/MDS code,
dim_Fp L = C min(S,R),
Z(L)=sum_(eps in L^perp cap {-1,0,1}^m) 2^-wt(eps)=Z_1^C.      (ADM)
```

Moreover all equations lie in `F_p(mu_n)=F_(p^k)`, so

```text
dim_Fp L <= min(m,k|Lambda|)                                  (TRACE)
```

even when the ambient coefficient field is `F_(p^e)` with `e>k`.
Multiplying the domain by a nonzero coset representative scales each moment
equation and therefore leaves `L^perp`, its dimension, distance, and ternary
mass unchanged. No upper bound on `Z_1` is asserted.
