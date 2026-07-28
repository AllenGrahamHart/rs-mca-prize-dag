# E1 low-square-mass weighted-kernel dictionary

- **status:** PROVED
- **closure:** proof plus exact integer ledger
- **dependencies:** `e1_collision_square_mass_reparametrization`,
  `e1_prime_field_l2_norm_collision_radius`,
  `e1_low_square_mass_plotkin_coloring_compiler`,
  `e1_prize_field_floor_even_norm_exclusion`
- **open consumer:** `e1_official_low_square_mass_pair_budget`

Fix an official prime-field E1 row with `N=2h`, `ell<=h`, and folded root
`zeta`. For a nonzero oriented folded vector

```text
d in {-2,-1,0,1,2}^h,
```

let `a(d)` count its entries of absolute value two, let `b(d)` count its
entries of absolute value one, and put `S(d)=4a(d)+b(d)`. Define

```text
T=min(ell,2h-ell),        n0=h-a-b,

M_ell(a,b) = sum_{j=0}^b sum_{r=0}^{n0}
             binom(b,j) binom(n0,r) 2^r
```

where a summand is retained exactly when

```text
a+j+r <= T,               a+b-j+r <= T,
a+j+r = ell (mod 2),      a+b-j+r = ell (mod 2).
```

Then `M_ell(a(d),b(d))` is exactly the number of ordered pairs of
antipodal-rearrangement classes `(x,y)` with `x-y=d`.

Let `D_p(ell)` contain the nonzero folded vectors with

```text
sum_i d_i zeta^i = 0 (mod p),
S(d)<=2ell,               M_ell(a(d),b(d))>0.
```

If `E_low` is the unordered low-square-mass collision-pair count, then

```text
E_low = (1/2) sum_{d in D_p(ell)} M_ell(a(d),b(d)).
```

This is an exact identity. In particular, no division by Galois, shift,
unit, or sign orbits is valid unless stabilizers and the displayed weight
are restored exactly.

After the proved norm floors remove impossible profiles, the maximum weight
and the largest uniform oriented-vector cap sufficient for each existing
edge budget are:

| row | eligible profiles | maximizing `(a,b,S)` | `M_max` | sufficient `|D_p(ell)|` cap |
|---|---:|---:|---:|---:|
| RowC `1/4` | 1090 | `(3,4,16)` | 2899001011559056192880793575925270505545118720240019736 | 1471225270732300083690 |
| RowC `1/8` | 275 | `(3,4,16)` | 4550972295647251657752808370587724056 | 2284491 |
| RowC `1/16` | 301 | `(0,4,4)` | 69817906094980867044033802642511381589872306283912 | 981163346005184 |
| prize `1/4` | 1086 | `(4,2,18)` | 1621868867923804840915753105221596984497856637426519762 | 44811343919980924354 |
| prize `1/8` | 271 | `(4,2,18)` | 1873053318886373426584792000465260242 | 69541 |
| prize `1/16` | 300 | `(1,2,6)` | 25912134061920884044549116258313478062341656144934 | 45700006676206 |

Each cap is `floor(2 E_max/M_max)`. The exact prize field floor removes every
`S=16` profile on the binding prize rate-`1/8` row, so its first live profile
is `(4,2,S=18)`. After also spending the sharpened prize second-moment
constant, the target is implied by at most `69,541` oriented low-mass folded
kernel vectors. The weighted identity is stronger than this uniform
sufficient condition and should be used whenever profile-resolved counts are
available. This node does not prove any of the six vector caps.
