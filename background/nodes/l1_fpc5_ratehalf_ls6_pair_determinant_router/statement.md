# Rate-half FPC5 guarded LS6 pair-determinant router

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **upstream interface:** primitive shift-pair / split-pencil control

Fix one guarded LS6 atom. Write

```text
M=L_2L_3,       deg M=2ell,
j=2ell-a,       s=ell-a,       e=deg E.
```

Every candidate has a unique quotient

```text
D_i E=M Q_i+V_i,       deg V_i<=s,                   (PD1)
```

with

```text
deg Q_i=e-a,       lc(Q_i)=lc(E),       gcd(D_i,Q_i)=1. (PD2)
```

For two candidates define

```text
H_12=D_1Q_2-D_2Q_1.                                  (PD3)
```

If the candidates are distinct, then

```text
0!=H_12=(D_2V_1-D_1V_2)/M,
deg H_12<=ell-2a.                                    (PD4)
```

Consequently

```text
gcd(D_1,D_2)|H_12,
deg gcd(D_1,D_2)<=ell-2a.                            (PD5)
```

The candidate locators are squarefree and split on the core, so their root
sets meet in at most `ell-2a` points and have symmetric distance at least

```text
2(j-(ell-2a))=2(ell+a).                              (PD6)
```

Fixing one candidate, the map from every other candidate to `H_12` is
injective. This gives the coarse exact-field bound

```text
#LS6<=|K|^(ell-2a+1),                                (PD7)
```

but it is not an admissible prize payment.

Indeed, for core size `N=4ell+b-2`, the constant-weight Johnson denominator
attached to `(PD5)` is exactly

```text
j^2-N(ell-2a)
 =ell(4a-b+2)+a^2+2ab-4a
 =J.                                                 (PD8)
```

The target is precisely the `J<=0` tail. Thus pairwise distance and ordinary
Johnson/Plotkin packing cannot close this atom; a proof must use the
collective low-degree determinant, source-ratio, splitness, quotient, or
owner structure.

## Scope

This theorem is a pair/shift-pair router and a quantified route fence. It
does not bound the number of split determinant-compatible locators by a
polynomial or assert that every abstract constant-weight code is realizable.
