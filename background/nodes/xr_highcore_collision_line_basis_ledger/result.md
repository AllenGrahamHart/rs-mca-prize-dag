# Replay certificate

The self-localized verifier was shipped by content to Modal and replayed in
app `ap-1izK1qM8XurEqhP79il7B8`. It returned

```text
XR_HIGHCORE_COLLISION_LINE_BASIS_LEDGER_PASS fixture=35,21,105
rowc-r1_4:B4>=4,localB4>=2,uniform_s<=13,grk_d<=3,r4=closed
rowc-r1_8:B4>=4,localB4>=3,uniform_s<=9,grk_d<=3,r4=b2-2
rowc-r1_16:B4>=7,localB4>=6,uniform_s<=7,grk_d<=3,r4=b2-5
prize-r1_4:B4>=4,localB4>=2,uniform_s<=60,grk_d<=11,r4=closed
prize-r1_8:B4>=5,localB4>=4,uniform_s<=40,grk_d<=10,r4=closed
prize-r1_16:B4>=10,localB4>=9,uniform_s<=30,grk_d<=9,r4=b8-8
```

The finite fixture is the seven-plane Vandermonde arrangement over `F_11`.
Its 35 triple points lie on 21 deduplicated two-plane collision lines with
105 point-line incidences. It attains both the basis injection
`sum b_ell=C(7,2)` and the five-points-per-line petal cap. Counting raw point
pairs instead of lines produces a strict overcount, a rank-deficient-core
mutation is rejected, and a sharp three-loop fixture checks the low-basis
global chart. Peak worker RSS was `55 MB`.

`B4` is the full-domain threshold and `localB4` is the exact threshold after
the minimum-basis line self-localizes the selector. `uniform_s` is the largest
selector rank paid when every collision-core restriction is uniform. The
remaining `r4` values are subsequently closed by the affine-core cogirth ray
bound; they are retained here to show the exact handoff.

The strengthened node was included in the `128/128` repository-wide replay in
Modal app `ap-IZqfGQD2KDhYQJwEl55Hb2` and the five-gate pass in
`ap-Hk6TgSQLiV1chotFlgLlzX`.
