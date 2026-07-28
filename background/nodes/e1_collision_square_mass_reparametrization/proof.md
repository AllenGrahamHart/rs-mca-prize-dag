# Proof

Throughout, `N = 2h`, `zeta` is a primitive `N`-th root of unity, and the
coordinates are those pinned in `e1_prime_field_l2_norm_collision_radius`.

## The coordinate identities

Write the raw signed difference of the two class representatives over the `N`
positions and fold across antipodes. Position `i < h` receives a contribution
from the raw positions `i` and `i+h`, and `zeta^(i+h) = zeta^i zeta^h =
-zeta^i`.

- An **opposite-sign antipodal pair** contributes `eps zeta^i - eps zeta^(i+h)
  = 2 eps zeta^i`, so `|c_i| = 2` and it adds `4` to `S`.
- A **singleton** contributes `eps zeta^i`, so `|c_i| = 1` and it adds `1`.
- A **same-sign antipodal pair** contributes `eps zeta^i + eps zeta^(i+h) =
  eps zeta^i (1 + zeta^h) = 0`, so `c_i = 0` and it adds `0`.

Hence `S = 4a + b`. Counting raw positions where the representatives differ:
each antipodal pair (of either sign) uses two, each singleton uses one, and
that count is `|B\B'| + |B'\B| = 2s`. So `2s = 2a + b + 2c`, i.e.
`s = a + b/2 + c`, and `b` is even. Both identities are checked against all
four pinned first-band profiles and their pinned band indices in `verify.py`.

## (1) No norm bound can bound `s`

Fix `(a,b)` and let `c` vary. By the computation above the folded element
`alpha` is unchanged — same coefficient vector, same `S`, same `Norm(alpha)`,
hence the same divisibility by any row prime — while `s = a + b/2 + c` takes
every value from `a + b/2` upwards. So `s` is not a function of `alpha`, and no
inequality on `|Norm(alpha)|` can constrain it above. QED.

The construction is exhibited in `verify.py` over 60 consecutive values of `c`.

## (2) The square-mass floor

`Norm(alpha)` is a nonzero rational integer (nonzero because the two classes
are distinct in characteristic zero, per the pinned lemma). A collision at a
pair-feasible row means the row prime `p` divides it, and every such `p` is at
least `2^250`; a nonzero integer with a divisor `>= 2^250` has absolute value
`>= 2^250`. Combined with `|Norm(alpha)| <= S^(h/2)`:

```text
S^(h/2) >= 2^250   <=>   S >= 2^(500/h).
```

For `h=128` this is `S >= 14.99`, so `S >= 15`; for `h=256`, `S >= 3.87`, so
`S >= 4`. Since `S = 4a+b` with `b` even, `S` is even, so at `N=256` the first
admissible square mass is `S = 16`.

## (3) Agreement with the pinned cutoffs

For the opposite-sign-only family the pinned lemma uses `S <= 4s-2`. Requiring
`(4s-2)^(h/2) < 2^250` gives `s <= 4` at `N=256` and `s <= 1` at `N=512`,
which are exactly the pinned exclusions. `verify.py` recomputes both.

The `b=0` branch is separate: there `alpha = 2 beta` with
`|Norm(beta)| <= s^(h/2)`, excluded when `s^(h/2) < 2^250`, i.e. `s <= 14` at
`N=256`. This is why `(4,0,1)` and `(5,0,0)` die in band `s=5` despite square
masses `16` and `20`.

## (4) The band-`s=5` enumeration

All 21 triples `(a,b,c)` with `a + b/2 + c = 5`, `b >= 0` even, were
enumerated and tested against whichever of the two branches applies. Survivors:
`(3,4,0)` with `S=16` and `(4,2,0)` with `S=18`. Every other cell has either
`S <= 14 < 15` or `b = 0` with `s = 5 <= 14`. This reproduces the pinned
survivor set exactly, which is the check that the coordinates above are the
intended ones.

## (5) The `S=16` split inventory

Solving `4a + b = 16` with `b >= 0` even gives `(a,b) in
{(4,0),(3,4),(2,8),(1,12),(0,16)}`. The first dies on the `b=0` branch. The
remaining four all have `S = 16 >= 15` and therefore survive the norm test. Their
minimal bands are `s = 5,6,7,8` respectively. QED.
