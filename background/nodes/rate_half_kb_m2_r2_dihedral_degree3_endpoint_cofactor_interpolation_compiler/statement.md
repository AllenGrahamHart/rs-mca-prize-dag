# KoalaBear m2 r2 degree-three endpoint-cofactor interpolation compiler

- **status:** PROVED
- **scope:** actual-endpoint realization of the sole residual full-V4
  `n=3` geometric component
- **dependencies:**
  `rate_half_kb_m2_r2_dihedral_degree3_geometric_realization_fence` and the
  fixed endpoint source presentation imported by
  `rate_half_kb_q6_u2_primitive_subdegree4_route_cut`
- **consumer:** `rate_half_band_closure`

Let the twelve distinct source labels be `alpha_i`, let `A` be their monic
locator, and let

```text
M(T,X)=sum_i kappa_i L_i(T) B(X)/z_i(X),            (KBM3I-1)
```

where `L_i` is the normalized Lagrange basis, every `kappa_i` is nonzero,
the pairwise coprime coordinate quadratics `z_i` multiply to `B`, and the
actual residual component `H(T,X)` has bidegree `(2,4)`. Put

```text
H_i(X)=H(alpha_i,X),
E_i(X)=B(X)/(z_i(X) H_i(X)).                        (KBM3I-2)
```

The complete-source condition makes every `E_i` a degree-18 form. Then
`H` divides the actual endpoint form `M` if and only if there are twelve
nonzero scalars

```text
w_i=kappa_i/A'(alpha_i)
```

satisfying the two polynomial identities

```text
sum_i w_i E_i=0,
sum_i alpha_i w_i E_i=0.                           (KBM3I-3)
```

Equivalently, the `38 x 12` matrix whose `i`th column is the coefficient
vector of `(E_i,alpha_i E_i)` has a kernel vector with all twelve entries
nonzero. This is an exact necessary-and-sufficient actual-component gate,
not merely a necessary rank heuristic.

There is also a local cycle form of the obstruction. At a simple root `x`
of `B`, write

```text
star(x)={a,b},       x in div(z_c).
```

Locator avoidance gives `c notin {a,b}`. Any full-support solution of
`(KBM3I-3)` must obey

```text
(alpha_a-alpha_c)w_a E_a(x)
 +(alpha_b-alpha_c)w_b E_b(x)=0.                  (KBM3I-4)
```

Thus the directed star edge `a -> b` at `x` carries the nonzero transport

```text
rho_(a->b)(x)=
 -[(alpha_a-alpha_c)E_a(x)]/[(alpha_b-alpha_c)E_b(x)],
```

and every directed star-graph cycle must have transport product one. This
holonomy condition is necessary, though not asserted sufficient.

The pinned split specialization over `F_47`, with cubic pole values `7,18`,
contains an exact `s=6` locator ownership, six invariant coordinate
quadratics, the required two-regular noninvariant pole graph, and exactly
four edges carried by the degree-two component. Its first 19-row block has
rank 11, but its stacked interpolation matrix has rank 12; the minor on
rows `0,...,10,19` has determinant `7 mod 47`. More locally, the six
standard `K_(2,2)` square transports in the two `K_(2,2,2)` components are

```text
11,26,17 and 2,41,31 mod 47,
```

so none is one. Hence that fully admissible abstract source/locator packet
is not an endpoint component.

This theorem does not prove that every admissible locator ownership has
full rank. It deletes the pinned packet and replaces the vague "fixed active
pencil" obstruction by the exact full-support kernel gate `(KBM3I-3)`. It
constructs no owner, moves no payment, and closes no `m=2` type, K3,
KoalaBear row, or Prize problem.

## Falsifier

An actual factorization `M=HN` for which `(KBM3I-3)` fails, a full-support
kernel that does not interpolate a bidegree-`(9,18)` cofactor, or failure of
the pinned determinant or square-holonomy values.
