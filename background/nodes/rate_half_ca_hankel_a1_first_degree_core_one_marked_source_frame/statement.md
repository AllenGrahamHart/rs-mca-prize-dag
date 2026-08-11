# `A=1` first-degree core-one marked source frame

- **status:** PROVED
- **closure:** common coefficient isotropy and exact marked-source subset sum
- **consumer:** `rate_half_band_crossing_location`

Retain the first-degree core-one residual middle Hankel pencil

```text
M(z)=M_0+zM_1,       size (d+1) x (d+1),
d=rho-1=3e-2,       rank_F(z) M=d.                   (MSF1)
```

Expand its primitive kernel vector and apolar polynomial as

```text
q(z)=sum_(i=0)^e z^i q_i,
Q(z;X)=sum_(i=0)^e z^i Q_i(X),                       (MSF2)
W_q=span{q_0,...,q_e}.
```

Then

```text
dim W_q=e+1,
q_i^T M_s q_j=0       for s in {0,1}, 0<=i,j<=e.    (MSF3)
```

Thus `W_q` is a common totally isotropic coefficient plane for the two
endpoint Hankel forms.

Write the contracted endpoint moments in source coordinates on the residual
evaluation domain `D_res`:

```text
h_k^(s)=sum_(x in D_res) omega_x^(s)x^k,
mu_x(U,V)=U omega_x^(0)+V omega_x^(1).                (MSF4)
```

For

```text
v_x=(Q_0(x),...,Q_e(x))^T,                           (MSF5)
```

the coefficient plane gives the two exact frame cancellations

```text
sum_(x in D_res) omega_x^(s) v_xv_x^T=0,
s in {0,1}.                                          (MSF6)
```

Now let `nu_x=(1,x,...,x^d)^T`, fix the double heavy row `x_*` of the
core-one quadratic `u=4` packet, and define

```text
C_*(U,V)=
 sum_(J subset D_res\{x_*}, |J|=d)
 Vand(x_*,J)^2 product_(x in J)mu_x(U,V),             (MSF7)
```

where `Vand(x_*,J)` is the ordinary Vandermonde determinant on the
`d+1` distinct points `{x_*} union J`. Then

```text
det(M(U,V)+tau nu_x*nu_x*^T)=tau C_*(U,V),            (MSF8)
```

and the marked-Hankel gate identifies the subset sum exactly:

```text
C_*=D_1Q(U,V;x_*)^2
   =c^2D_1g_*^2S_B^6.                                (MSF9)
```

Here `deg D_1=e-2`, `g_*` is the squarefree degree-`e-6` supported factor,
`S_B` is quadratic, and `c in F^x`.

## Scope

The Vandermonde coefficients in `(MSF7)` are nonzero squares, but the
field-valued source weights can cancel. No positivity or termwise
noncancellation is asserted. The theorem converts the quadratic double-root
branch into an exact source-sum factorization; it does not exclude it.
