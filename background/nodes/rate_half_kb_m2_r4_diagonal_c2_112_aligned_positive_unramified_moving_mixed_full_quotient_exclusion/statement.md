# KoalaBear c2 (1,1,2) aligned positive unramified moving-mixed full-quotient exclusion

- **status:** PROVED
- **scope:** the aligned positive, unramified, moving-moving internal-edge
  template with the mixed residual-square allocation over
  `F_(2130706433^6)`
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`,
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`,
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize `J_0={2,1/2,b,1/b}`, `q(T)=T^2+tT+p`, `w!=0`, and
`trace=b+b^-1`. Exact scale retention and reciprocal trace descent make the
four q-slice equations quadratic in `trace`.

Their projection support consists of explicit open factors, the linear
component `4p+5t+4`, one irreducible 91-term component of bidegree `(12,12)`,
and twelve finite intersections among residual projection cofactors. The
linear component has only forbidden minor-conic support. All twelve
off-common intersections reduce to six distinct endpoint candidates, each
on the base forbidden product.

On the degree-12 component, the direct minor-conic norm has degree 1224 in
`t` and 38 irreducible factors. Exact finite-extension replay leaves four
admissible q-slice points, over fields of degrees `3,3,7,7`. The degree-7
points do not embed in `F_(p^6)`. Each degree-3 trace has two reciprocal
`b` orientations in `F_(p^3)`. Reconstructing `G=U^2-WV^2` reproduces the
q-slice identity on all four orientations, but every orientation fails both
necessary full-quotient norm identities

```text
Res_T(P_J,G) ~ K_5^4 q^2,
q^2 Res_T(P_I,G) ~ R_7^4.
```

Therefore no deployed-field moving-mixed candidate satisfies the full
colored quotient system. The q-slice itself is not empty. The three
fixed-moving sibling cells and all later packet/row assembly remain open.
