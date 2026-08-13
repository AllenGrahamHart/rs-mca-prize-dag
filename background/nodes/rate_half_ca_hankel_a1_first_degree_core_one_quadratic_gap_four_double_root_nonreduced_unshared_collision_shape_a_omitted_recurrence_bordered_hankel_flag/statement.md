# `A=1` collision shape-A omitted-recurrence bordered-Hankel flag

- **status:** PROVED
- **closure:** every omitted defect is a source-bordered determinant square
- **consumer:** `rate_half_band_crossing_location`

Retain shape A. Write

```text
M(t)=(h_(i+j)(t))_(0<=i,j<=d),
M(t)q(t)=0,       adj M(t)=D_1(t)q(t)q(t)^T,       (BHF1)
```

where `q=(q_0,...,q_d)^T` is primitive. For `s>=0`, put

```text
v_s(t)=(h_(d+1+s+i)(t))_(0<=i<=d),
R_(d+1+s)(t)=q(t)^T v_s(t).                        (BHF2)
```

Let `M[k<-v_s]` denote `M` with column `k` replaced by `v_s`. Then

```text
det M[k<-v_s]=D_1 q_k R_(d+1+s).                   (BHF3)
```

Consequently, for every `r>=0`, the monic gcd of all replacement minors is

```text
gcd_(0<=k<=d,0<=s<=r) det M[k<-v_s]
 =D_1 gcd(R_(d+1),...,R_(d+1+r))                  (BHF4)
```

up to the fixed scalar normalization of `D_1`.

There is also a square determinant identity. Let `widehat M_s` be the
moment submatrix with row and column exponent set

```text
E_s={0,1,...,d,d+1+s}.
```

Then

```text
det widehat M_s=-D_1 R_(d+1+s)^2.                  (BHF5)
```

If `A_s(J)=det(x^(a))_(a in E_s,x in J)` is the generalized alternant,
Cauchy-Binet gives the source form

```text
B_s(t):=sum_(J subset U_0, |J|=d+2)
             A_s(J)^2 product_(x in J)omega_x(t)
       =-D_1(t)R_(d+1+s)(t)^2.                    (BHF6)
```

For `s=0`, `A_0(J)` is the ordinary Vandermonde determinant.

In shape A, every omitted defect is divisible by the three-center form:

```text
R_(d+1+s)=Lambda Theta_s,       deg Theta_s<=e-2,  (BHF7)
```

and the regular factor is

```text
D_1=c_D g_*S_B^2.
```

Thus every bordered source sum has the exact squarefree-times-square form

```text
B_s=c'_D g_*(S_B Lambda Theta_s)^2.                (BHF8)
```

For `s=0`, `Theta_0=[X^n]G`.

Finally write

```text
H_off=g_off H_reg,
g_off=g_*/gcd(g_*,Lambda),
deg g_off=e-7,       deg H_reg=2e+7.               (BHF9)
```

The factors are squarefree and `gcd(H_reg,D_1)=1`. If

```text
C_r^pad=gcd(g_off,R_(d+1),...,R_(d+1+r)),
C_r^reg=gcd(H_reg,B_0,...,B_r),                    (BHF10)
```

then the omitted-recurrence flag splits exactly as

```text
C_r=C_r^pad C_r^reg.                               (BHF11)
```

At a root `delta` of `H_reg`,

```text
q_delta>=r+1
 iff rank [M(delta)|v_0(delta)|...|v_r(delta)]=d.  (BHF12)
```

## Scope

This is a source-side determinantal presentation of the complete regular
flag, not a bound on it. The `e-7` padding-heavy roots remain a separate
singular-regular-factor flag. Shape A is not excluded.
