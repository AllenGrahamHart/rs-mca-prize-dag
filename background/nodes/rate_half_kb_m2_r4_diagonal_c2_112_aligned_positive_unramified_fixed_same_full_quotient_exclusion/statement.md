# KoalaBear c2 (1,1,2) aligned positive unramified fixed-same full-quotient exclusion

- **status:** PROVED
- **scope:** the aligned positive, unramified, fixed-moving internal-edge
  template with the same residual-square allocation over
  `F_(2130706433^6)`
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`,
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`,
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize `J_0={2,1/2,b,1/b}`, `q(T)=T^2+tT+p`, and `w!=0`. Exact scale
retention makes the four q-slice equations quadratic in the fixed-moving
coordinate `b`.

Their common projection support consists of explicit open factors, the
linear component `4p+5t+4`, and one reciprocal quartic. The linear component
has only forbidden support. A direct affine minor-conic resultant on the
quartic gives a degree-472 norm with 28 irreducible factors. Exact replay of
every factor that can have a root in `F_(p^6)` gives 20 endpoint candidates:
12 are boundary, four are empty, and four base-field q-slice points survive.

Each survivor reconstructs `G=U^2-WV^2` and reproduces `(KBQS-1)`, but all
four fail both necessary full-quotient norm identities

```text
Res_T(P_J,G) ~ K_5^4 q^2,
q^2 Res_T(P_I,G) ~ R_7^4.
```

After common/open removal, the three projections have `2`, `1`, and `1`
residual cofactors. Both off-common combinations factor over linear endpoint
fields and yield seven distinct `(p,t)` values, all on the base forbidden
product. Therefore no deployed-field fixed-same candidate satisfies the full
colored quotient system. Fixed-swap, fixed-mixed, and later assembly remain
open.
