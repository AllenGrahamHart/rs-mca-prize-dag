# KoalaBear c2 (1,1,2) aligned positive unramified moving-swap exclusion

- **status:** PROVED
- **scope:** the aligned positive, unramified, moving-moving internal-edge
  template with the swapped residual-square allocation
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
  and `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize

```text
J_0={2,1/2,b,1/b},       q(T)=T^2+tT+p,
w!=0,                    trace=b+b^-1.
```

Retaining the exact relative `U/V` scale, the four swapped-allocation
q-slice equations are reciprocal quartics in `b`. Exact trace descent makes
them quadratic in `trace`. A common trace root forces the four `3 x 3`
coefficient minors to vanish and their first-two-row kernel to lie on the
Veronese conic.

The three star projections of the four residual minors have only two
admissibility-relevant common components: `4p+5t+4=0` and
`p*t+5p+t=0`. The first has only forbidden minor-conic support. On the
second, the generic common determinant root misses the conic. Exact replay
over every irreducible factor of the degree-26 exceptional norm leaves four
boundary factors and two determinant candidates; both candidates fail the
original four trace equations.

After removing the common components and open factors, the three projection
cofactors have finite common support. Its endpoint norm has seven factors;
their endpoint gcds yield eight distinct `p` candidates, all on the explicit
base forbidden product. Therefore no admissible point remains in this cell.

This proves only the moving-moving swapped allocation. The other five
aligned-positive unramified cells and all later packet/row assembly remain
open.
