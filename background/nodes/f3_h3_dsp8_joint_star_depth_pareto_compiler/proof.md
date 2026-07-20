# Proof

Fix one displayed `E`, put `L=17-E`, and take a positive summand in `(JDP1)`.
The retained conditions are

```text
e=P-18>=E+1,       R>=L+1=18-E.                    (1)
```

If `m` is the number of small unordered product representations, the proved
excess ladder gives

```text
m>=7+ceil(e/2),       e<=2(m-7),       m>=m_E=8+E/2. (2)
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

Substitution of `m_E=11,...,16` into `(3),(4)` gives exactly the six pairs
`(a_E^0,a_E^A)` in `(JDP3)`, proving `(JDP2)`.

Multiply `(JDP2)` by `17rho_E(t)` and sum by target class. The general
accident-depth reduction says that C36' follows if the resulting high tail is
at most

```text
B_(L_E,E)(n)
 =300n^2-17L_E(n-1)^2-17E(n-2)^2.                 (7)
```

This proves `(JDP4)`. Since `L_E+E=17`, the same compiler gives

```text
B_(L_E,E)(n)>11n^2.                                (8)
```

Write `w_E=a_E^A/a_E^0` and
`C_E=11/(17a_E^0)`. Substitution gives the six fractions in `(JDP5)`, and

```text
Dbar_E^0+w_E Dbar_E^A<=C_E n^2
  =>17(a_E^0Dbar_E^0+a_E^ADbar_E^A)<=11n^2
  <B_(L_E,E)(n).
```

This proves every sufficient moment condition.

For the packet table, the two average disjoint-six degrees are bounded below
by

```text
ceil(2d_0(m)/m),       ceil(2d_A(m)/(m-1)).         (9)
```

The second denominator is `m-1` because the antipodal floor counts only the
generic vertices. These averages increase with `m>=11`. Clearing
denominators between consecutive parities leaves respectively

```text
m^2+2m+12,       m^2+11,
m^2+16,          m^2-2m+17,                        (10)
```

which are positive. Evaluating `(9)` at `m_E` gives the degrees in `(JDP6)`.
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
