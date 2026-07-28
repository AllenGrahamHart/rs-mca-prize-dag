# E1 collision square-mass reparametrization

- **status:** PROVED
- **closure:** proof plus exact enumeration
- **dependency:** `e1_prime_field_l2_norm_collision_radius` (definitions + norm bound)
- **consumers (evidence only):** `e1_official_prime_exception_control`,
  `unsafe_crossing_family_instantiation`

Using the pinned coordinates of `e1_prime_field_l2_norm_collision_radius` —
`(a,b,c)` counting opposite-sign antipodal pairs, singleton terms, and
same-sign antipodal pairs, with `alpha = sum_{i<h} c_i zeta^i`, `S = sum_i
c_i^2`, and raw swap distance `s = |B\B'| = |B'\B|` — the two coordinates are

```text
S = 4a + b,          s = a + b/2 + c          (so b is even).
```

**(1) The swap distance is not a collision invariant.** A same-sign antipodal
pair cancels in `alpha`:

```text
eps zeta^i + eps zeta^(i+h) = eps zeta^i (1 + zeta^h) = 0     since zeta^h = -1.
```

Hence `c` contributes to `s` and contributes nothing to `alpha`. Fixing `(a,b)`
and increasing `c` yields the same `alpha`, the same `Norm(alpha)`, the same
divisibility by any row prime — and unbounded `s`. **No bound on the norm can
ever bound `s` above.**

**(2) The square mass is the invariant.** The pinned bound `|Norm(alpha)| <=
S^(h/2)` depends on `(a,b)` only through `S`. A collision requires a row prime
`p >= 2^250` to divide the nonzero `Norm(alpha)`, hence `S^(h/2) >= 2^250`:

```text
N=256 (h=128):  S >= 15.        N=512 (h=256):  S >= 4.
```

These are the same facts as the pinned `s>=5` and `s>=2` cutoffs, stated in the
coordinate that controls them. Restricted to the opposite-sign-only profiles
the two forms agree exactly: the norm test excludes `s<=4` at `N=256` and
`s=1` at `N=512`, both reproduced here.

**(3) The band-`s=5` enumeration is exactly as pinned.** All 21 profiles with
`a + b/2 + c = 5` at `N=256` were enumerated and tested; the survivors are
exactly `(3,4,0)` and `(4,2,0)`, with every other cell dying either by
`S <= 14 < 15` or, when `b=0`, by the `alpha = 2 beta` branch.

**(4) Consequence for the exhaustion.** Because collisions are governed by `S`,
an exhaustion should be indexed by square mass, not by band. At `N=256` the
admissible splits at `S=16` are

```text
(a,b) = (4,0)   excluded (b=0 -> alpha = 2 beta)
        (3,4)   live -- minimal band s=5
        (2,8)   live -- minimal band s=6
        (1,12)  live -- minimal band s=7
        (0,16)  live -- minimal band s=8
```

The variance-descent campaign works `(3,4)` only. The other three live splits
have the same square mass, survive the norm test, and sit in higher bands, so
they are **not** covered by the band-`s=5` scope sentence "only folded profiles
`(4,2,0),(3,4,0)` remain". Whether some further argument disposes of them is
**open** — see `frontier.md`.
