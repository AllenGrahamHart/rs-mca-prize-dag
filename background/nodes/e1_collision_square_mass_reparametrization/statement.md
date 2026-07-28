# E1 collision square-mass reparametrization

- **status:** PROVED
- **closure:** proof plus exact finite enumeration
- **canonical precursor:** prize commits `0acf7e8f`, `c90a724b`
- **dependencies:** `acl_count`, `e1_prime_field_l2_norm_collision_radius`
- **consumers (evidence only):** `e1_official_prime_exception_control`,
  `unsafe_crossing_family_instantiation`

Put `N=2h`. An antipodal-rearrangement class of `ell`-subsets is determined
by a signed singleton vector `x in {0,+-1}^h` and the number `u` of full
antipodal pairs. If `t=|supp(x)|`, then

```text
t+2u=ell,                 0<=u<=h-t,
t<=T:=min(ell,2h-ell),    t=ell (mod 2).
```

For two classes with singleton vectors `x,y`, their E1 difference is

```text
alpha = sum_i (x_i-y_i) zeta^i.
```

Let `a` count coordinates where `x_i=-y_i!=0`, and let `b` count coordinates
occupied by exactly one of `x,y`. Then the folded square mass and height are

```text
S=sum_i (x_i-y_i)^2=4a+b,
H=sum_i |x_i-y_i|=2a+b.
```

If raw representatives are used, a count `c` of cancelling same-sign
antipodal pairs gives raw swap distance `s=a+b/2+c`. The term `c` changes the
representatives but not `x-y`, `alpha`, `S`, its norm, or finite-field
divisibility. Thus a norm argument controls square mass, not raw distance.
At fixed `N,ell` the exact independent support bound is

```text
H<=2T,                   S<=4T,
```

so raw distance is finite; the stronger canonical wording that it is
"unbounded" at fixed quotient order is not used.

For the official clean-anchor parameters this gives:

| quotient lane | `h` | `ell` | `T` | square-mass range |
|---|---:|---:|---:|---:|
| `N=256`, rate `1/4` | 128 | 65 | 65 | even `S<=260` |
| `N=256`, rate `1/8` | 128 | 33 | 33 | even `S<=132` |
| `N=512`, rate `1/16` | 256 | 33 | 33 | even `S<=132` |

The norm bound `|Norm(alpha)|<=S^(h/2)` and the prime floor `p>=2^250`
exclude `S<=14` at `N=256` and `S<=2` at `N=512` when `b>0`. In the all-even
branch `b=0`, division by two instead excludes `a<=14` at `N=256` and
`a<=3` at `N=512`.

At `N=256,S=16`, the all-even split `(a,b)=(4,0)` is excluded. The remaining
splits are

```text
(3,4), (2,8), (1,12), (0,16).
```

All four are realized by distinct antipodal-rearrangement classes for each
official `N=256` value `ell in {33,65}`, with representatives having `c=0`.
Consequently `(2,8)`, `(1,12)`, and `(0,16)` are genuine norm-unresolved
profiles, not formal profiles ruled out by the class-size constraint. The
existing variance descent proves results only for `(3,4)`. This theorem does
not assert that any of the four profiles actually collides modulo an official
row prime and closes no prize row.
