# L1 marked constant-shift Forney-window normal form

- **status:** PROVED
- **role:** classify every low-petal cell in the marked common-pencil window
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use the marked constant-shift setup with `t` distinct labels and

```text
P-a_i=S_iV_i,       J=product_i V_i,       v=deg J,
deg F=d,       deg W<=d,       gcd(F,W)=1,
S_i | W-c_iF.
```

Fix an integer `m>=1` and assume

```text
1<=t<=2m,       m ell<d,       d+v<(m+1)ell.       (FW1)
```

Define the interpolation module

```text
L={ (A,B) in K[Z]^2 : B(a_i)=c_iA(a_i) for every i },
Q(Z)=product_i(Z-a_i).                              (FW2)
```

Then `L` has a reduced polynomial basis `q_0=(A_0,B_0)`,
`q_1=(A_1,B_1)` with Forney degrees

```text
mu<=nu<=m,       mu+nu=t,                           (FW3)
A_0B_1-A_1B_0=kappa Q,       kappa!=0.             (FW4)
```

Equivalently,

```text
max(0,t-m)<=mu<=floor(t/2),       nu=t-mu.          (FW5)
```

The degree-at-most-`m` coefficient kernel has dimension exactly

```text
(m-mu+1)+(m-nu+1)=2m-t+2,                           (FW6)
```

so the `t` rows in the `2(m+1)`-column coefficient matrix are linearly
independent.

Put `F'=JF`, `W'=JW`. There are unique bivariate coefficient polynomials

```text
R_j(X,Z)=sum_s H_(j,s)(X)Z^s,
deg_X H_(j,s)<ell,
deg_Z R_0<=m-mu,       deg_Z R_1<=m-nu,             (FW7)
```

such that

```text
[F']   [A_0(P)]                 [A_1(P)]
[W'] = [B_0(P)] R_0(X,P) +     [B_1(P)] R_1(X,P).  (FW8)
```

Both evaluated multipliers are nonzero, and

```text
gcd(R_0(X,P),R_1(X,P)) | J.                          (FW9)
```

Thus every common-pencil survivor is indexed by one finite Forney degree
`mu` and has exactly `2m-t+2` coefficient generators. At `t=2m`,
`mu=nu=m` and this recovers the extremal two-generator determinant normal
form. At `t=2m-1`, the indices are `(m-1,m)` and the generators are
`q_0,Zq_0,q_1`.

## Sharpness

Every admissible index pair in `(FW3)--(FW5)` is populated. Split the labels
into disjoint sets of sizes `mu,nu` and put

```text
U(Z)=product_(i<=mu)(Z-a_i),
V(Z)=product_(i>mu)(Z-a_i).
```

The pairs `(1,U)` and `(V,0)` form a reduced basis of degrees `mu,nu` and
determinant `-Q`. Choose a monic `R` of degree `m-nu`, adjoin a
transcendental `lambda`, and for `1<=c<ell` set

```text
F=1+lambda X^cR(P)V(P),       W=U(P).               (FW10)
```

This is saturated, has `deg F=m ell+c`, and satisfies all `t` full-petal
congruences. Hence none of the Forney strata can be removed by a universal
emptiness theorem.

## Scope

The theorem does not count the coefficient multipliers, assign the sharp
families to a quotient/profile owner, or treat arbitrary petal locators.
