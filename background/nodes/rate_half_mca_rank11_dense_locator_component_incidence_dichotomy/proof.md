# Proof

Let the eighteen distinct dense-pair anchor slopes be
`gamma_1,...,gamma_18` and set

```text
q(Z)=product_i (Z-gamma_i).
```

Every other record has a distinct slope, so `q(gamma)` is nonzero. Its
deviation

```text
d_gamma=h_gamma'-a_0'-gamma b_0'
```

lies in `V'`. Define `R_gamma=d_gamma/q(gamma)`. Multiplication of each
vector by a nonzero field scalar preserves the span. The ten deviation-basis
anchors are not among the eighteen zero deviations, so the normalized
family still spans `V'`.

At a coordinate in the selected agreement support,

```text
h_gamma'(x)=r_0'(x)+gamma r_1'(x).
```

Substitution of `h_gamma'=a_0'+gamma b_0'+q(gamma)R_gamma` gives equation
(1) in the statement. After bihomogenization it is a divisor of class at
most

```text
18 H_Z+H_R
```

on `P^1 x P^10`.

## Isolated-point incidence

Fix eleven coordinates. Generic independent perturbations inside the same
basepoint-free divisor classes make their intersection proper. Every
isolated point of the original intersection persists under perturbation
with at least its local intersection multiplicity. The generic total is
the multihomogeneous Bezout number

```text
(18H_Z+H_R)^11=18*11 H_Z H_R^10=198 H_Z H_R^10.
```

Therefore the sum of isolated multiplicities is at most 198 even when the
original intersection also has positive-dimensional components.

Let `I_iso` count incidences `(gamma,T)` for which the rich point is isolated
in the eleven-coordinate intersection. Summing the preceding bound over
all coordinate tuples gives

```text
I_iso<=198*C(n',11).                                 (4)
```

Every record contributes `C(m',11)` total incidences. Thus, for `N`
non-dense records, the proportion not lying on a positive-dimensional
component through the point is at most

```text
198*C(n',11)/(N*C(m',11))<=A_iso(K')/N.              (5)
```

The binomial ratio is the product of eleven factors

```text
(1048576+K'-i)/(67472+K'-i),       0<=i<=10.
```

Every factor decreases with `K'`, since `1048576>67472`. Hence the maximum
is at `K'=10`. Exact integer evaluation gives (3).

An unsafe line has at least `B_*+1` records before the disjoint near charge.
Removing its exact charge `134944` and the eighteen dense anchors leaves

```text
N>=B_*+1-134944-18
 =274980728111260126=N_min.                          (6)
```

Equations (5)--(6) bound the isolated fraction above by `9189066` parts per
billion, so the component-incidence fraction is at least `990810934` parts
per billion.

## Component classification through a rich point

For a tuple `T`, inspect `ev_T:V'->F^T`. At rank ten, choose a ten-coordinate
evaluation basis `B`. Equations on `B` uniquely give

```text
q(Z)R_B(Z)=U_0+ZU_1,       U_0,U_1 in V'.
```

The remaining equation is identically zero precisely when the affine pair

```text
(a_0'+U_0,b_0'+U_1)
```

agrees with the received pair at the extra coordinate. A
positive-dimensional component through the rich point is therefore the
affine-owner clone curve.

At evaluation rank at most nine, the kernel is nonzero. At any compatible
slope, the complete affine kernel fiber lies in the intersection, so the
rich point is nonisolated. If compatibility occurs only at that slope this
is vertical; if the slope projection is nonconstant, the kernel-shortening
router applies. These alternatives are exhaustive.

Finally split all component incidences according to these two evaluation
ranks. Their combined density is at least `990810934` parts per billion, so
one lane has density at least half, namely `495405467` parts per billion.
No division by overlap multiplicity is made, so no record or component count
is inferred.
