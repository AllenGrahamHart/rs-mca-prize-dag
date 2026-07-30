# KoalaBear m2 r4 diagonal facet-mixing obstruction

- **status:** PROVED
- **scope:** every actual diagonal-order-two component
  `S=<tau x tau>` in the residual `(m,r,delta)=(2,4,2)` row
- **dependency:**
  `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`
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

This theorem deletes the partition-preserving diagonal subcase and replaces
it by five exact mixing signatures. It does not delete all five signatures,
the source-line or biquadratic branch, the diagonal orientation, the full
order-two type, an owner, payment, row, or Prize result.

## Falsifier

An actual diagonal component with `tau(I)=I`; a fixed-point-free involution
whose orbit data lie outside `(KBDM-3)`; or a common-`K` fiber quartic
violating the corresponding support restriction in `(KBDM-4)`.
