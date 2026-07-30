# KoalaBear m2 r4 diagonal fiber-resultant interpolation compiler

- **status:** PROVED
- **scope:** actual `(m,r,delta)=(2,4,2)` component with stabilizer
  `S=<tau x tau>`
- **dependencies:** `rate_half_kb_m2_v4_outer_recurrence_router` and
  `rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`
- **consumer:** `rate_half_band_closure`

Let `H(T,X)` define the actual bidegree-`(2,4)` source component, let
`b` be the deck involution of `psi(X)`, and write

```text
psi^(-1)(alpha_p)={x_p,b(x_p)}.
```

The fiber resultant

```text
R_p(T)=H(T,x_p) H(T,b(x_p))                       (KBDI-1)
```

is a nonzero split quartic, well defined projectively. If `bar(p)` is the
fixed-point-free permutation induced by the endpoint deck involution
`tau(alpha_p)=alpha_bar(p)`, diagonal stabilization gives

```text
[R_bar(p)]=[tau^* R_p].                            (KBDI-2)
```

This is a whole-quadratic-fiber identity. It does not assert that either
individual quadratic star over `x_p` maps to one star over the paired
fiber.

Here `tau^*` is pullback on binary quartics, including the homogenizing
factor of the projective involution. The common-five source facets give
the exact support constraints:

- `p in K`: both quadratic factors of `R_p` are supported on `J=I^c`;
- `p=eta`, where `eta` is the unique label in `L minus K`: both are
  supported on `I`;
- `p in L^c`: the two factors lie in the paired one-exchange facets of
  Corollary 9.27.

Every source label occurs with total multiplicity four, so

```text
product_(p=1)^12 R_p(T) = constant * A(T)^4.       (KBDI-3)
```

There is an exact interpolation test. Write

```text
R_p(T)=sum_(a=0)^4 r_(p,a) T^a
```

and let `P` be any `7 x 12` parity-check matrix for evaluations of
degree-at-most-four polynomials at the twelve distinct `alpha_p`. Form the
`35 x 12` matrix

```text
M_(s,a),p = P_(s,p) r_(p,a).                       (KBDI-4)
```

The projective quartics `[R_p]` are the twelve fibers of a biform
`G(T,W)` of bidegree at most `(4,4)` if and only if `M` has a kernel
vector `c=(c_p)` with every `c_p` nonzero. For fixed `c` the biform is
unique. Thus failure of the full-support kernel deletes a proposed
diagonal source-facet packet exactly.

This compiler does not prove that every admissible packet fails the kernel
test. It does not close the diagonal or transposed coordinate orientation,
the order-two type, the trivial-stabilizer type, an owner, payment, row, or
Prize result.

## Falsifier

An actual diagonal component violating `(KBDI-1)--(KBDI-4)`, or projective
quartics passing the printed full-support kernel test but admitting no
bidegree-at-most-`(4,4)` interpolant.
