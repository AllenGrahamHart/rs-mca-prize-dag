## MCA O0b `FFF` direct `R76` determinant pivot (2026-08-18)

### Exact cross-check

The direct 16-dimensional resultant construction independently gives

```text
det(M_R76)|_(t=2) = 244686406.
```

This agrees exactly with the block-algebra identity

```text
244686406 = 1573108971^2 * 443644136 mod 2130706433,
```

where the two factors are the prior `D2` and q6 determinants. Thus the direct
quadratic-resultant formula and the inverse-based 32-dimensional norm agree
at the certified generic witness.

### Symbolic frontier

Modal app `ap-9BUD9SrIBSZusMY2nn9i8h` constructed the complete symbolic
16-by-16 multiplication matrix for `R76=Res_E(q7,q6)`. Every one of its 256
entries is a nonzero rational function in `t`. The 1,800-second child wall
expired only while taking the determinant.

This is a route decision: repeating the generic rational determinant with a
longer wall is not the preferred next step. The matrix should be emitted as
a reusable exact bank, each entry represented by numerator and denominator
coefficient arrays. A second program should clear denominators column-wise
or globally and take the determinant over `GF(2130706433)[t]`, where
fraction-free polynomial algorithms avoid rational-expression growth.

### Proof boundary

The generic emptiness theorem remains proved by the prior witness. This
packet adds an independent resultant cross-check and isolates the exact
symbolic bottleneck, but it does not enumerate exceptional roots or close
the `FFF` chart.

Result SHA-256:
`7b889840b303ea9e61961f53eb608134081dadc5fa5e138f7a903bc319d2be07`.
