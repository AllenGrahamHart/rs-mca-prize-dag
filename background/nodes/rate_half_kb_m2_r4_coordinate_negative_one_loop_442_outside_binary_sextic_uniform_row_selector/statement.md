# KoalaBear m2 r4 coordinate negative one-loop 442 outside binary-sextic uniform-row selector

- **status:** PROVED
- **scope:** the four deployed rank-six sextic common quotients for the live
  nonloop-singleton orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_eigenvalue_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler`
- **consumer:** `rate_half_band_closure`

Let `E_ell=T_ell-Delta^3 h_ell` be the seven coefficient equations from
`(KB41EV-3)`.  In each of the four root-sign rows, the coefficient submatrix
of `(E_0,E_1,E_2)` on `(h_0,h_1,h_2)` has multiplication norm

```text
1133299039 mod 2130706433.                         (KB41US-1)
```

This is nonzero, so that minor is a unit in every rank-six common quotient.
Because the full eigenvalue system has rank three, the uniform equations

```text
E_0=E_1=E_2=0                                    (KB41US-2)
```

are equivalent to all seven coefficient equations in every sign row.
Thus every one of the eighty canonical forced-record cells has the same
three-equation product-invariance interface.

This theorem does not evaluate a forced-record cell, impose its forced mate,
outside sums, or full interpolation, classify another common orbit, close
the coordinate orientation or a row, or prove either Prize result.

## Falsifier

A root-sign row where `(KB41US-1)` vanishes, or a guarded residual sextic
with `E_0=E_1=E_2=0` but some other `E_ell` nonzero.
