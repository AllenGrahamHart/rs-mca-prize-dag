# Proof

Fix a source-sign pair and target lane. Use the proved cell-4 four-basis
tower over `F_p(r)`. For `xi=0`, the ordered residual products are

```text
de, -de, df, sigma_o ef, bf, sigma_c cf.
```

At matching 6, the first two paired cuts are

```text
P_u(u)=Pair(-de,df),       P_v(v)=Pair(de,sigma_o ef),
```

with `u=df` and `v=ef`. Both are quadratic. If `s` is the omitted source
squared sum, every target satisfies

```text
H(u,v)=de*(u+v)^2-s*u*v=0.                             (1)
```

As in the pairing-3 theorem, eliminate `u` from `P_u` and (1), take a
division-free pseudo-remainder modulo `P_v`, multiply by the `P_v` leading
coefficient to retain degree drop, and take the four-dimensional tower norm.

For each of 16 sign/lane rows, collect every field root of the norm
numerator, norm denominator, and all four inversion-guard numerators and
denominators. Directly lift their union through the original quadratic
`t`, quadratic `b`, linear `c`, and compact-kernel equations. At each guarded
source point, solve both paired quadratics, test (1), reconstruct
`f^2=uv/de`, `d=u/f`, and `e=v/f`, and evaluate the colored pair.

The exact ledger has 160 candidate `r` values and 176 guarded source points.
Of 608 `(u,v)` pairs, 560 fail (1). The remaining 48 each have two nonzero
`f` roots, and all 96 reconstructed rows have a nonzero colored-pair cut.
Thus there are no target boundaries, colored solutions, witnesses, or
unresolved branches, proving `xi=0` empty.

Deleting `xi=1` instead of `xi=0` leaves the residual system value-for-value
unchanged, so 16 further cases transport. Hence all 32 stated cases are
empty. QED.
