# KoalaBear c2 (1,1,2) aligned positive unramified moving-same exclusion

- **status:** PROVED
- **scope:** the aligned positive, unramified, moving-moving internal-edge
  template with the same-side residual-square allocation
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize `J_0={2,1/2,b,1/b}`, `q(T)=T^2+tT+p`, `w!=0`, and
`trace=b+b^-1`. Exact scale retention and reciprocal trace descent make the
four q-slice equations quadratic in `trace`.

Their maximal-minor projections have one nonboundary linear component and
one reciprocal cubic. The linear component has only forbidden minor-conic
support. A direct minor-conic resultant is not divisible by the cubic; its
degree-272 endpoint norm has 21 irreducible factors. Exact finite-extension
replay makes every component `p` gcd linear. Eight factors are boundary,
eight have no common determinant/conic `w`, and the five remaining `w`
candidates fail the original four trace equations.

The finite off-common projection ledger has seven endpoint factors and seven
distinct `p` candidates, all on the explicit base forbidden product. Hence
the complete moving-moving same-side cell is empty.

This proves only that cell. The four fixed/moving sibling cells and all later
packet/row assembly remain open.
