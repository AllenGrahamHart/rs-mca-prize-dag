# Proof

Fix one displayed `E`, put `L=17-E`, and take a positive summand in `(JDP1)`.
The retained conditions are

```text
e=P-18>=E+1,       R>=L+1=18-E.                    (1)
```

If `m` is the number of small unordered product representations, the proved
excess ladder gives

```text
m>=7+ceil(e/2),       e<=2(m-7),
m>=m_E=7+ceil((E+1)/2).                              (2)
```

The disjoint-six multiplicity gate gives the class-sensitive floors

```text
d_0(m)=ceil(m(m-4)/2)-2m-6,
d_A(m)=ceil(m(m-2)/2)-4(m-1)-8.                    (3)
```

Thus `N_6^disj(t)>=d_c(m)`. For `m>=11`, both floors are positive. The two
ratios

```text
g_0(m)=2(m-7)/d_0(m),       g_A(m)=2(m-7)/d_A(m)   (4)
```

are strictly decreasing. To see this without an asymptotic estimate, use the
parity formulas

```text
2d_0(m)=m^2-8m-12  (m even),   m^2-8m-11  (m odd),
2d_A(m)=m^2-10m-8  (m even),   m^2-10m-7  (m odd).
```

After positive denominators are cleared, the four comparisons
`g_c(m)>g_c(m+1)` have differences

```text
m^2-12m+54,       m^2-14m+67,
m^2-12m+64,       m^2-14m+77,                      (5)
```

according to class and parity. They are positive for every `m>=11`.
Combining `(2)--(4)` gives

```text
e/N_6^disj(t)<=g_c(m)<=g_c(m_E).                   (6)
```

Substitution of `m_E=11,...,16` into `(3),(4)`, repeating the endpoint pair
at each odd `E`, gives exactly the eleven rows `(a_E^0,a_E^A)` in `(JDP3)`.
This proves `(JDP2)`.

Multiply `(JDP2)` by `17rho_E(t)` and sum by target class. The general
accident-depth reduction says that C36' follows if the resulting high tail is
at most

```text
B_(L_E,E)(n)
 =300n^2-17L_E(n-1)^2-17E(n-2)^2.                 (7)
```

This proves `(JDP4)`. There is a stronger payment when `E` is odd. The swap
involution on ordered product representations has exactly `D(t)` fixed
points, so

```text
P(t)=D(t) (mod 2).                                 (8)
```

On the low part `e(t)<=E`, with odd `E`, this implies

```text
e(t)<=E-1+1_(D(t)>0).                             (9)
```

Indeed `D(t)=0` forces `P(t)` and hence `e(t)` to be even. In the
accident-depth proof, replace the payment `E T_(L_E)` by

```text
(E-1)T_(L_E)+S_(D,E)
 <=(E-1)(n-2)^2+S_(D,E).                         (10)
```

Since `rho_E(t)<=R(t)`, it remains to sum a one-fiber bound over the diagonal
targets. Their set is the image of a subset of `(1-H)\{0}` under squaring and
therefore has at most `n-1` elements. For every `t!=1`,

```text
R(t)+1=#{z in H:1-t(1-z) in H}.
```

The two forms are nonconstant and nonproportional. The affine subgroup-line
Stepanov theorem therefore gives, conservatively,

```text
S_(D,E)<(51/16)(n-1)n^(2/3).                     (11)
```

Consequently `(JDP4)` may be strengthened on every odd row to

```text
17(a_E^0Dbar_E^0+a_E^ADbar_E^A)<=B_par,E(n).     (12)
```

Direct expansion gives

```text
B_par,E(n)
 =28n^2+(510+34E)n-(221+51E)-17S_(D,E).          (13)
```

Every official order has `n^(1/3)>20`. Thus the final term in `(13)` is
strictly larger than `-(867/320)n^2`, while the displayed linear-minus-
constant term is positive for `E=7,9,11,13,15`. Hence

```text
B_par,E(n)>(8093/320)n^2.                         (14)
```

For even `E`, the original compiler and `L_E+E=17` give

```text
B_(L_E,E)(n)>11n^2.                               (15)
```

Write `w_E=a_E^A/a_E^0`. For even `E`, put
`C_E=11/(17a_E^0)`; for odd `E`, put
`C_E=(8093/320)/(17a_E^0)`. Substitution gives all eleven fractions in
`(JDP5)`. In the even case,

```text
Dbar_E^0+w_E Dbar_E^A<=C_E n^2
  =>17(a_E^0Dbar_E^0+a_E^ADbar_E^A)<=11n^2
  <B_(L_E,E)(n).
```

The same implication on an odd row has `(8093/320)n^2` in the middle and
`B_par,E(n)` on the right. This proves `(JDP5a)--(JDP5c)` and all eleven
sufficient moment conditions.

For the packet table, the two average disjoint-six degrees are bounded below
by

```text
ceil(2d_0(m)/m),       ceil(2d_A(m)/(m-1)).        (16)
```

The second denominator is `m-1` because the antipodal floor counts only the
generic vertices. These averages increase with `m>=11`. Clearing
denominators between consecutive parities leaves respectively

```text
m^2+2m+12,       m^2+11,
m^2+16,          m^2-2m+17,                       (17)
```

which are positive. Evaluating the degree averages at `m_E` gives the degrees
in `(JDP6)`.
At `E=6` on the antipodal class, the stronger floor `d_A(11)=2` retains both
edges even though averaging guarantees only degree one; the cross-center
packet is exactly the one proved by the multiplicity gate.

Finally `(1)` supplies `r_E` distinct quotient lifts. The nonzero-coupling
part of the odd-saturation theorem says at most one coupling is zero, so a
nonzero anchor exists and at least `r_E-1` couplings are nonzero. Apply that
theorem with `J=J_E` to obtain `(JDP7)`. Every product and quotient generator
vanishes in the same degree-one official row-prime ideal. That prime lies
above an odd rational prime, so localization at two preserves its valuation;
ideal-norm divisibility follows. QED.
