# KoalaBear m2 r4 positive ramified-loop multiplicity exclusion

- **status:** PROVED
- **scope:** every positive coordinate-order-two packet in the residual
  `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_source_row_interpolation_compiler`,
  `rate_half_kb_m2_r4_coordinate_coefficient_normal_form`, and
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate`
- **consumer:** `rate_half_band_closure`

Let `w_0` be either branch value of the source quotient `W=X^2`, and let
`u` be a local parameter at its unique ramified source point, so
`W-w_0` has order two.  Suppose the positive component has the antipodal
star `{a,-a}` there.  If `B_1(w_0)!=0`, no actual complete-source packet
exists.

Indeed, with `D=A_2`, `E=A_0`, the positive normal form is locally

```text
H(T,u)=D(u^2)T^2+E(u^2)+u T C(u^2),               (KBPRM-1)
```

where `D(0) a C(0)!=0` after moving either branch to `u=0`.  The loop
product row gives `E(0)=-a^2D(0)`.  Therefore

```text
ord_u H(a,u)=ord_u H(-a,u)=1,
ord_u H(t,u)=0  for every other target label t.    (KBPRM-2)
```

The source-row complete-square identity would consequently have local
order two on its left and order four on its right:

```text
ord_u Res_T(A(T),H(T,u))=2,
ord_u (constant * B_source(u)^2)=4.                (KBPRM-3)
```

Here the ramified complete source fiber is `2[u=0]`, so
`ord_u B_source=2`.  This contradiction proves the local exclusion at
both branch charts.

At any nonramified one of the twelve complete source fibers, a loop has
target sum zero, so the positive Vieta sum row and leading support force
`B_1=0` at its quotient label.  The local exclusion above says the same is
necessary for a ramified loop.  Since `B_1` is a nonzero projective linear
form, every positive packet therefore has at most one loop over all twelve
complete source fibers:

```text
ell_positive,total <= 1.                           (KBPRM-4)
```

In particular all positive two-loop and three-loop 442/433 rows are
empty.  If the sole loop of a surviving positive one-loop row is ramified,
it must be the unique zero of the nonzero linear form `B_1`.  A packet with
one common loop has no outside loop; a zero-common-loop packet has at most
one outside loop.

This theorem does not treat positive zero-loop or surviving one-loop rows,
the diagonal or trivial-stabilizer orientations, K3 payment, a row
threshold, or either Prize result.

## Falsifier

An actual positive complete-source packet with a ramified antipodal star,
`B_1` nonzero there, and the complete-source square identity; or a positive
packet with two or more complete-source loops.
