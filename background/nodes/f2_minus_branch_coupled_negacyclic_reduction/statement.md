# F2 minus-branch coupled negacyclic reduction

- **status:** PROVED
- **closure:** proof

Fix an official maximal rate-half row

```text
n=2^41, q=p^e<2^256, n divides q-1, p=3 mod 4,
b=v_2(p+1), k=ord_n(p).
```

Then `b>=39` and

```text
k=2^max(1,41-b) in {2,4}.                              (MINUS-ORDER)
```

Let `W` be the exact-order or nested window at order `2^a`,
`a in {40,41}`, choose one representative from every antipodal pair,
and put `m=|W|/2`. There is an element `omega` of order `2m` such that,
for `P_eps(X)=sum_(s=0)^(m-1) eps_s X^s`, the first `R` odd-moment
kernel is exactly

```text
K_W={eps in F_p^m : P_eps(omega^(2j-1))=0, 1<=j<=R}.    (MINUS-K)
```

The deployed range has `2R<2^36`. Put

```text
h=2                              for every exact-order window,
h=2                              for the nested order-2^40 window,
h=k                              for the nested order-2^41 window.
```

The Frobenius-closed root set

```text
Omega={omega^(p^i(2j-1)):0<=i<h,1<=j<=R}
```

has exactly `hR` elements, and

```text
G_W(X)=prod_(alpha in Omega)(X-alpha) lies in F_p[X],
K_W={coeff(P): deg(P)<m and G_W divides P},
rank_Fp(A_W)=hR, dim_Fp(K_W)=m-hR.                     (MINUS-RANK)
```

Thus the minus branch is one coupled prime-field subfield-subcode of an
extension-field GRS parity check, equivalently the printed negacyclic
root code. It is not a direct sum of singleton proportionality classes.
Its weighted mass obeys

```text
Z_W=2^-m sum_v N_W(v)^2 >= max(1,2^m/p^(hR)),           (MINUS-L2)
```

and every nonzero ternary kernel word has weight at least `2R+1`.
No upper bound on `Z_W` is asserted.

## Addendum (2026-08-07, wave-47 integration, coordinator)

Root-disjointness is argued in prose and corroborated on surrogates
only (the F2 auditor's request for a closed-form inequality stands);
the reduction is adopted as the minus-branch OBJECT MODEL candidate
(the round-20 f2_repose residual) with that gap named.
