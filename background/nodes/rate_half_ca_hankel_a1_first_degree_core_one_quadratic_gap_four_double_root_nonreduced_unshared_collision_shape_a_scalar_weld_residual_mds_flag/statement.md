# `A=1` shape-A scalar-weld residual-MDS flag

- **status:** PROVED
- **closure:** every fiber degree drop is an exact parity run on the unique
  projective scalar-weld vector
- **consumer:** `rate_half_band_crossing_location`

Retain shape A. Let `X=U_0` be its `R` classified rows and write the exact
row factorization as

```text
G(t,x)=lambda_x P_x(t),       lambda_x!=0,          (RWF1)
```

where each `P_x` is monic of degree `m=e-2`. The coefficient-MDS and
connected scalar-weld gates make `lambda` one projective vector; it can be
reconstructed from any passing scalar-weld certificate.

Fix an off-line supported slope `delta`. Retain the all-excess notation

```text
I_delta=S_delta intersect U_0,
X_delta=U_0\I_delta,
A_delta(X)=product_(x in I_delta)(X-x),
G(delta,X)=zeta_delta A_delta(X)H_delta(X)R_delta(X),
deg H_delta=a_delta-q_delta.                        (RWF2)
```

All roots of the padded-heavy factor `R_delta` lie outside `U_0`. Hence,
for `x in X_delta`, define

```text
u_(delta,x)(lambda)
 =lambda_x P_x(delta)/[A_delta(x)R_delta(x)].       (RWF3)
```

Put

```text
L_delta(X)=product_(x in X_delta)(X-x),
E_(delta,j)(lambda)
 =sum_(x in X_delta)
   u_(delta,x)(lambda)x^j/L_delta'(x).              (RWF4)
```

In shape A,

```text
R=(9e-7)/2,       n=(3e-7)/2,       R-n=3e.        (RWF5)
```

If

```text
j_delta=3e+r_delta-1,                              (RWF6)
```

then the degree drop is exactly the initial zero-run length of the
residual-MDS parity flag:

```text
E_(delta,j_delta)=...=E_(delta,j_delta+q_delta-1)=0,
E_(delta,j_delta+q_delta)!=0.                       (RWF7)
```

The empty equality string for `q_delta=0` means that the first displayed
parity is already nonzero. The lower consistency parities satisfy

```text
E_(delta,j)=0,       0<=j<j_delta.                  (RWF8)
```

Equivalently, define the explicit row vectors

```text
K_(delta,s),x
 =1_(x in X_delta) P_x(delta)x^(j_delta+s)
   /[A_delta(x)R_delta(x)L_delta'(x)].              (RWF9)
```

Then `q_delta` is the exact initial zero-run length of

```text
K_(delta,0)lambda,
K_(delta,1)lambda,... .                             (RWF10)
```

Consequently the concentrated excess norm has the globally coupled form

```text
deg T=e-sum_(delta in Gamma)q_delta,                (RWF11)
```

where every summand is determined by the same projective vector `lambda`
and the classified incidence data. There are no independent residual
coefficients to choose fiber by fiber.

## Scope

The theorem does not bound the stacked flag in `(RWF10)` or exclude shape
A. It replaces the static-source flag by an exact scalar-weld/support
matrix. A closing argument must prove that the unique passing `lambda`
cannot sustain the required collection of extra parity zeros.
