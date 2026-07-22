# Proof

Let `mathcal U` be the nonidentical full outside involution-orbits. The
previous orbit count gives

```text
N=|mathcal U|>=3e-8       (antipodal),
N>=3e-11                  (constant product).        (1)
```

For every external slope `gamma`, its block has `r=2e+1` rows and therefore
meets at most `r` disjoint orbit pairs. Hence `gamma` belongs to at least
`N-r` complements.

Each actual complement relation has numerator and denominator degree at
most `t`. At a fixed `u`, either it equals the specialization of the static
relation defining `H`, or the two rational functions agree at at most `2t`
points of `H`. Call the first coordinates aligned and let their number be
`a`. A primitive class denominator has no root in `H`; otherwise its
numerator would vanish there too. Thus an aligned complement contains every
root of `H`. Counting incidences between `H` and the complements gives

```text
h(N-r)<=ah+2t(N-a),

a>=ceil([h(N-r)-2tN]/[h-2t]).                       (2)
```

For an aligned coordinate, uniqueness of the primitive relation makes its
gcd polynomial proportional to the fixed `B`. It is monic, so its degree is
`d=deg B`, and the complement identity is proportional to

```text
F_H(U,Z)=I(A_2U^2+A_1U+A_0)+B(U^2M_0-2UM_1+M_2).
```

The class polynomial divides `F_H` coefficientwise. Write

```text
F_H=P_H R,       deg_U R<=2.                         (3)
```

No root of `P_Z/P_H` makes `R(U,gamma)` identically zero, since that would
enlarge the relation class. Therefore each of the `3e-h` remaining external
roots occurs in at most two aligned residuals. With

```text
k=e+d-h=deg R_u,
```

the residual-root incidence count is

```text
ak<=2(3e-h).                                        (4)
```

The right side of `(2)` is increasing in `h`, while the ratio
`2(3e-h)/a` is decreasing. At the exact lower class sizes `172410` and
`2128`, substitution in `(2)--(4)` gives `k<=6`. Hence `h=e+d-k>=e-6`.
Repeating the same exact integer calculation at `h=e-6` gives `k<=4` and

```text
a>=e-33       (antipodal),
a>=e-44       (constant product).                   (5)
```

Finally `k` is not zero. If two complements `K_u,K_v` were proportional,
evaluate at three of the at least `e-t` good internal pairs and cancel the
nonzero common factor `B(xi_i)mu_i`. This would give one scalar `c` with

```text
(u-u_i)^2=c(v-u_i)^2
```

at at least three distinct `u_i`. The quadratic identity forces `u=v`.
Thus aligned coordinates give distinct projective complements, whereas
`k=0` would make every complement proportional to `P_H`. This proves
`(QPAR1)--(QPAR3)`. QED.
