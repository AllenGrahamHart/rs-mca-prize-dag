# Claim contract

## Claim

For E1 class differences at quotient order `N=2h`, the folded square mass
`S = 4a+b` is a collision invariant and the raw swap distance
`s = a + b/2 + c` is not. No bound on `|Norm(alpha)|` can bound `s` above. The
collision floor is `S >= 15` at `N=256` and `S >= 4` at `N=512`, equivalent to
the pinned `s<=4` / `s=1` exclusions on the opposite-sign-only family.

## Dependencies

- `e1_prime_field_l2_norm_collision_radius` supplies the coordinates
  `(a,b,c)`, the folded element `alpha`, the bound `|Norm(alpha)| <= S^(h/2)`,
  the `b=0` branch `alpha = 2 beta`, and the `p >= 2^250` row-prime floor.

## Nonclaims

- **no variance level, profile, row, or prize terminal is closed**;
- no claim that `(2,8)`, `(1,12)`, `(0,16)` at `S=16` are open — only that we
  found no exclusion for them and the band-`s=5` scope sentence does not reach
  them (see `frontier.md`);
- no claim that the descent campaign is wrong; its `(3,4)` results stand
  exactly as verified;
- no upper bound on `S` is proved here — that needs `ell'` or another height
  input, which we could not locate;
- the coordinate identities are RECONSTRUCTED from the pinned definitions, not
  quoted; they are validated against four pinned profiles and the band-`s=5`
  survivor set, and nothing more.

## Falsifier

A profile with a same-sign antipodal pair that does not cancel in `alpha`; a
pair `(a,b,c)` whose pinned band index differs from `a + b/2 + c`; a band-`s=5`
enumeration returning a survivor set other than `{(3,4,0),(4,2,0)}`; a norm
bound that does constrain `s` above at fixed `(a,b)`; or a citation excluding
any of `(2,8)`, `(1,12)`, `(0,16)` at `S=16`, which would answer the frontier
question in the affirmative.
