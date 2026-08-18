# DLI fixed-weight ambient-Q bridge

Let `B` be a finite field of odd order `q`, let `n` and `t=2^m` be powers
of two with `t<n`, and let `zeta in B` have exact order `n`. Use the Haar
events `O_0,...,O_(m-1),T_m` and the antipodal first-owner residual `Prim`
from `dli_primitive_haar_event_correlation`. Put

```text
Phi(x) = (sum_i x_i zeta^(ri))_(1<=r<=t),
Omega_w = {x in {0,1}^n : |x|=w},
M_w = binom(n,w),
f_w = |Omega_w intersect Prim intersect Phi^(-1)(0)|,
L_w = |Phi(Omega_w)|.
```

Define the image-normalized primitive-Q inflation, effective-image defect,
and ambient inflation by

```text
kappa_img(w) = f_w L_w/M_w,
Delta_img(w) = q^t/L_w,
kappa_amb(w) = Delta_img(w) kappa_img(w) = q^t f_w/M_w.   (AQ1)
```

Then every Haar marginal is Fourier-positive and

```text
P(O_j) >= q^(-|U_j|),       P(T_m) >= q^(-1),
P(T_m) product_(j<m) P(O_j) >= q^(-t).                    (AQ2)
```

Consequently the primitive Haar correlation ratio satisfies the exact
finite bridge

```text
J_prim
 <= q^t P(Prim intersect Phi^(-1)(0))
  = sum_(w=0)^n [M_w/2^n] kappa_amb(w)
  = sum_(w=0)^n [M_w/2^n] Delta_img(w) kappa_img(w).       (AQ3)
```

Moreover,

```text
f_w=0 for w<=t and for w>=n-t.                            (AQ4)
```

Thus the weighted finite ambient-Q payment

```text
sum_w [M_w/2^n] Delta_img(w) kappa_img(w) <= 2^21         (AQ5)
```

is sufficient for `dli_c2pp_joint_reserve`. At the official aspect
`t/n=1/256`, every surviving layer is fixed-density. Uniform asymptotic
primitive Q together with a uniform full-image certificate gives only
`J_prim<=exp(o(n))`; it does not imply the official 21-bit constant.

