# KoalaBear m2 r4 diagonal facet-mixing obstruction

- **status:** PROVED
- **scope:** every actual diagonal-order-two component
  `S=<tau x tau>` in the residual `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler` and
  `rate_half_kb_m2_u2_colored_source_resultant_split_compiler`
- **consumer:** `rate_half_band_closure`

Let `D` be the twelve source-label set, let `I` be the invariant-coordinate
six-set, put `J=D minus I`, and let `K subset I` be the common five-set. Write

```text
xi = the unique label in I minus K.
```

The endpoint deck involution `tau` is fixed-point-free on `D`. For the
diagonal orientation it cannot preserve the source-facet partition:

```text
tau(I) != I,       tau(J) != J.                    (KBDM-1)
```

Put

```text
c=|I intersect tau(J)|=|J intersect tau(I)|.
```

Then

```text
c in {2,4,6},       |I intersect tau(I)|=6-c.      (KBDM-2)
```

There is an exact five-row orbit census. If `a` is the number of `tau`
two-cycles contained in `K`, and `b` is one when `tau(xi) in K` and zero
otherwise, then

```text
(a,b,c) in {
  (2,0,2), (1,1,2),
  (1,0,4), (0,1,4),
  (0,0,6)
}.                                                       (KBDM-3)
```

The mixing is visible directly in the common-`K` fiber quartics. Define

```text
J_0=J intersect tau(J),       J_1=J intersect tau(I).
```

Thus `J=J_0 disjoint_union J_1`, with sizes `6-c` and `c`. For `k in K`,
let `R_k` be the whole-fiber split quartic of the diagonal fiber compiler.
Counting roots with divisor multiplicity:

```text
tau(k) in K       => Root(R_k) subset J_0;
tau(k) = eta      => Root(R_k) subset J_1;
tau(k) in L^c     => at least two roots of R_k lie in J_1. (KBDM-4)
```

Here `L=K union {eta}` is the invariant-fiber image six-set. The second
line includes the aligned case `L=I`, where `eta=xi`. In the last line the
remaining at most two roots lie in `J_0`.

The maximally mixed row has a further exact reduction. If `c=6`, then

```text
L != I,       tau(eta) in K,
ell:=tau(xi) in J intersect L^c.                   (KBDM-5)
```

Both stars above `xi` and both stars above `ell` are `I-J`; every other
`L^c` star is `I-I`. Equivalently, the four colored roots are exactly the
two complete source fibers over `xi` and `ell`. Thus the colored quartic
descends through `W=psi(X)`:

```text
C_H(X) ~ chi(psi(X)),
div(chi)={xi,ell},       [tau^*chi]=[chi].          (KBDM-6)
```

The binary quadratic `chi` is squarefree and lies in the positive
`tau`-eigenspace; in coordinates `tau(W)=1/W` it is reciprocal. If
`K_5(W)` and `R_7(W)` are the locators on `K` and its seven-label
complement, the two partial resultants descend to forms `Q_J,Q_I` with

```text
Q_J(W) ~ K_5(W)^2 chi(W),
chi(W) Q_I(W) ~ R_7(W)^2.                          (KBDM-7)
```

Hence the aligned `c=6` row is deleted and the near-aligned survivor has
an exact quotient-resultant interface in both diagonal source-subfield
branches.

This theorem deletes the partition-preserving diagonal subcase and replaces
it by five exact mixing signatures. It does not delete all five signatures,
the source-line or biquadratic branch, the diagonal orientation, the full
order-two type, an owner, payment, row, or Prize result.

## Falsifier

An actual diagonal component with `tau(I)=I`; a fixed-point-free involution
whose orbit data lie outside `(KBDM-3)`; a common-`K` fiber quartic violating
`(KBDM-4)`; an aligned `c=6` component; or a maximally mixed component whose
colored divisor or descended partial resultants violate `(KBDM-5)--(KBDM-7)`.
