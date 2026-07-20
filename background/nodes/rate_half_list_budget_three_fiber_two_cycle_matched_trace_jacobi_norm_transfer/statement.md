# Budget-three fiber-two matched-cycle trace-Jacobi norm transfer

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_matched_post_field_compiler`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_jacobi_norm_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_torsion_cyclotomic_norm_decomposition`

Retain the exact nonharmonic matched-cycle parity compiler at

```text
M=2^36,       L=2M=2^37,       N=8M=2^39.            (JNT1)
```

Put

```text
y=(r+r^(-1))/2,       x=2y^2-1,
epsilon=r^(8L)=r^(2^40) in {1,-1}.                  (JNT2)
```

Every survivor satisfies

```text
T_(8L)(y)=epsilon,       C_L^(1/4)(x)=0,             (JNT3)
```

and, for one of two choices `s^2=-epsilon`, one of

```text
P_(2L-1)(x)=s(2y-1),
P_(2L-1)(x)(y-1)=s(y+1),
P_(2L-1)(x)y=s(y-2).                                 (JNT4)
```

All signs lie in `F_p`. In the nonsplit field class only `epsilon=1` occurs;
the `epsilon=-1` packet belongs only to `p=1 mod 2^41`.

Let `C=C_L^(1/4)`, let `R=P_(2L-1) mod C`, and put

```text
G_-=T_(2L),       G_+=U_(2L-1),                     (JNT5)

E_(0,s)=(R+s)^2-2s^2(x+1),
E_(1,s)=2(R+s)^2-(x+1)(R-s)^2,
E_(2,s)=(x+1)(R-s)^2-8s^2.                          (JNT6)
```

For `epsilon in {+1,-1}`, a signed branch exists over the algebraic closure
if and only if

```text
gcd(C,G_epsilon mod C,E_(j,s) mod C)!=1.             (JNT7)
```

For each fixed `epsilon`, this gives six exact one-variable gcds of degree at
most `L=2^37`; across both torsion signs there are at most twelve.

The even-Jacobi transform halves the degree. Put

```text
w=2x^2-1,       z=(w+1)/2,
J(w)=J_M^(-1/4,-1/2)(w),
Q(w)=J_(L-1)^(0,1/2)(w) mod J(w),       deg Q<M.     (JNT8)
```

For one sign `s^2=-epsilon`, define

```text
A_0=zQ^2-s^2,                    B_0=2s(Q-s),
A_1=zQ^2+2szQ+s^2,              B_1=6sQ-zQ^2-s^2,
A_2=zQ^2-2szQ-7s^2,             B_2=zQ^2-2sQ+s^2,
F_(j,s)=A_j^2-zB_j^2,                               (JNT9)

K_-=T_L,       K_+=U_(L-1).                         (JNT10)
```

Then `(JNT7)` is coverage-equivalent to the six degree-`M` tests for each
fixed `epsilon`

```text
gcd(J,K_epsilon mod J,F_(j,s) mod J)!=1,             (JNT11)
```

where every representative has degree at most `M=2^36`. Thus the complete
interface consists of two six-gcd packets, one for each torsion sign.

There is an exact torsion-only prefilter. Define

```text
R_-=Res_w(J,T_(2M)),       R_+=Res_w(J,U_(2M-1)),
H_M(z)=z^M J((z+z^(-1))/2).                          (JNT12)
```

Every minus-sign survivor requires its odd characteristic to divide `R_-`,
and every plus-sign survivor requires it to divide `R_+`. Up to printed
powers of two,

```text
R_-^2  <->  Res_z(Phi_(8M),H_M),       8M=2^39,      (JNT13)

R_+^2  <->  product_(d=2^j, 2<=j<=38)
                 Res_z(Phi_d,H_M).                   (JNT14)
```

Thus the plus packet has exactly `37` levels. Equivalently,

```text
R_+=(2M)^M product_(j=0)^36 Res_w(J,T_(2^j)).        (JNT15)
```

For the minus packet, `theta^2=2` lies in `F_p` and

```text
T_(2M)=(theta T_M-1)(theta T_M+1),                  (JNT16)
```

so two conjugate degree-`M` resultants replace the degree-`2M` input.

This is a complete doubled-order exclusion interface: if neither torsion
resultant has an official-compatible prime divisor, the matched parity branch
is empty. Any compatible divisor must pass `(JNT11)` and then the corrected
post-field test `T/q_out=W^4`. The theorem does not evaluate these norms,
make a dense implementation affordable, cover other matched denominator
geometries or `c=1,2`, or prove the adjacent crossing.
