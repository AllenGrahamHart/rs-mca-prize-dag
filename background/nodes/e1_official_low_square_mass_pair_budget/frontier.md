# Frontier

The binding finite statement is

```text
E_low <= 65127585921474870475467050631501738502567
```

for every pair-feasible prize rate-`1/8` row. Since
`K=38001322036274275320505631960233903602944`, a maximum-degree-three theorem
gives `E_low<=3K/2` and closes this entry with room.

The proved weighted-kernel dictionary gives the exact alternative form

```text
E_low=(1/2) sum_{d in D_p(33)} M_33(a(d),b(d)).
```

The prize field floor removes every `S=16` profile. The former largest live
weight was the `(4,2,S=18)` value
`1873053318886373426584792000465260242`; the complete cofactor chain now
proves that profile empty on prize-envelope rows. Therefore the coarse
post-exclusion ledger now makes `(3,6,S=18)` the maximum-weight remaining
profile, with weight `1386246316188473270092082114587711840`. The uniform
cap therefore sharpens to `|D_p(33)|<=93962`; 93,963 is not certified by this
inequality. The exact profile-weighted inequality remains weaker and
preferred.

The existing `(3,4,S=16)` variance campaign remains relevant to RowC but is
superseded on the binding prize row by the field-floor exclusion. The prize
row has 271 norm-eligible profiles through `S=66`; its leading `(4,2,S=18)`
profile has exactly seven possible prize cofactor values after local
reciprocity, the field floor, and the residue-degree sieve. RowC retains the
419-class interface.

The proved variance/cofactor window theorem sharpens that leading prize
interface again. Every collision has `V=2 mod 8`; exact Lucas resultants remove
`V=2`, and the logarithmic norm deficit removes cofactor `1538` completely.
Six cofactor classes remain. The narrowest is `m=1028`, with only
`V in {10,18}`; the other residual upper bounds are 50 for `m=514`, 74 for
`m=256`, 178 for `m=16`, 226 for `m=4`, and 250 for `m=2`. These are vector
classification windows, not yet an aggregate edge count.

The subsequent dual normalized census closes both `m=1028` chambers: among
320292000 exact signed vectors there are no `V=10` vectors and only 16 at
`V=18`, none with norm divisible by 257. Thus `1028=4*257` is impossible and
five prize cofactors remain. The narrowest is now `m=514`, with
`10<=V<=50` and `V=2 mod 8`.

The next dual census finds 184 normalized vectors in the six `m=514`
chambers whose norms are divisible by 257. FLINT and PARI agree on all exact
resultants, and every quotient `Norm/514` lies below the prize interval. Thus
`514` is also impossible. Four prize cofactors remain: `2,4,16,256`; the
narrowest window is `m=256`, `10<=V<=74`, `V=2 mod 8`.

The `m=256` dual census leaves 20756 vectors in nine chambers. Committed FLINT
and PARI norm ledgers agree on all exact resultants: every `V=18` quotient is
above the prize interval and every `V>=26` quotient is below. Thus `256` is
impossible. Three prize cofactors remain: `2,4,16`; the narrowest is `m=16`,
`10<=V<=178`, `V=2 mod 8`.

The analytic `m=16` high-variance child proves the profile-specific chord
bound `4L<=E+35`. Six quadratic majorants and three layered-third-moment
Hermite certificates remove every chamber from `V=114` upward, reducing this
cofactor to `10<=V<=106`, `V=2 mod 8`, without making its planning census
load-bearing.

The dual residual census leaves 540332 vectors through `V=106`. Streamed
FLINT and independently enumerated PARI resultants agree through a 64-bucket
multiset fingerprint; all 540332 quotients `Norm/16` lie outside the prize
interval. Thus `m=16` is impossible, and the leading profile now has only
cofactors `2,4`.

The `m=4` chord/Hermite split reduces that branch to `10<=V<=74`; dual
FLINT/PARI streams then put all 21,376 quotients outside the prize interval.
The analogous `m=2` split reduces the final branch to `10<=V<=98`; dual
streams agree on all 511,272 exact resultants and again find no interval
quotient. Thus every prize cofactor of `(4,2,S=18)` is impossible. RowC's 419
classes are unchanged, and later prize profiles still require aggregate
weighted accounting. The next binding profile is `(3,6,S=18)`.

The coloring target is an independent alternative. Degree two pays both;
degree three pays this pair-budget route even when the graph is not
three-colorable.

The new maximum-weight `(3,6,S=18)` profile now has a proved finite interface.
Its six singleton coefficients force
`mu in {1,2,3,4,5,6,8,9,10}` and exactly twelve prize cofactors. Variance zero
and two are impossible; a profile-specific logarithmic deficit leaves even
windows ending at 350 for `m=2`, 68 for `m=512,514`, 34 for `m=1024,1028`,
and 12 for `m=1538`. A dual exact affine/XOR classification subsequently
proves every `mu=1` energy from two through six empty, excluding `m=1538`.
The sharp fixed-moment product envelope then contracts both `m=1024,1028`
branches from `V<=34` to `V in {4,6,8,10,12}`. A dual exact affine/XOR
census proves the `mu=10` geometry empty and excludes `m=1024`. Ten cofactors
remain. The sibling `m=1028` census finds exactly 16 energy-five vectors, but
none vanishes at a primitive root modulo 257, excluding that cofactor as well.
Nine cofactors remain. The capped sharp product envelope contracts all of
their windows: the upper endpoints for `m=2,4,8,16,32,64,256,512,514` are now
`284,266,254,216,170,130,60,34,34`. Thus `m=512,514` are the shortest
interfaces. The multiplicity-nine `m=512` branch then admits a complete
radius-two mod-four census: two independent exact engines find only four
vectors through `E=17`, and dual exact resultants place every quotient
`Norm/512` below the prize interval. Thus `m=512` is impossible and eight
cofactors remain. The shortest live branch is `m=514`, with `mu=1`,
`2<=E<=17`, and a required factor 257. Integer autocorrelation then gives the
adaptive cap `y_u<=min(144,18+V)`. The exact product envelope contracts
`m=256` from `V<=60` to `V<=46` and `m=514` from `V<=34` to `V<=22`.
The complete multiplicity-one emptiness through `E=6` and parity-adaptive
caps leave exactly nine `m=514` chambers:
`(7,3),(7,7),(8,4),(8,8),(9,5),(9,9),(10,6),(10,10),(11,11)`, where the
second coordinate is odd autocorrelation weight. Adversarial vectors at
`E=15,17` falsify any stronger modular-emptiness premise, but their exact
quotients are below the prize interval and those energies are now excluded
analytically. A dual exact radius-zero/radius-one census of the nine live
chambers then leaves twelve geometric vectors and eight with factor 257.
FLINT and PARI/GP agree on all eight norms, whose quotients by 514 are below
the prize interval. Thus `m=514` is impossible and seven cofactors remain.
For `m=256`, exact parity-product certification removes every chamber above
`E=20` and leaves 45 `(E,q,L)` triples. A complete 5920-orbit
multiplicity-eight census has two independent radius implementations; both
find the same 54 product-live vectors. FLINT and PARI/GP agree on every norm,
and all quotients by 256 are below the prize interval. Thus `m=256` is also
impossible. Six pure cofactors remain: `2,4,8,16,32,64`. The shortest proved
window is `m=64`, with `V<=130` or `E<=65`. No broad support-9 census is
authorized.

The subsequent complete `m=64` and `m=32` exclusions leave
`m in {2,4,8,16}`. At `m=16`, the once- and twice-divided support branches
are also empty, leaving only the primitive multiplicity-four branch. The
proved common-prime associate router now couples every retained vector at one
fixed `(p,r)`:

```text
alpha=pi^mu u g,       mu in {1,2,3,4},       (g)=P_r,
```

for one prime generator `g` and a cyclotomic unit `u`. This is the selected
non-computational interface for the profile. In a fixed cofactor, both `u`
and `u^(-1)` have power-basis coefficient bounds `1006,503,251,125` for
`mu=1,2,3,4`. A bounded-unit associate count or height theorem is still
required, and lower-weight profiles still enter the exact weighted sum.
