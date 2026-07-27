# E1 N=256 E=33 profile-(1,8) light-template exclusion

- **status:** PROVED
- **closure:** proof plus two complete finite censuses

No pair-feasible folded-profile `(3,4,0)` collision at `N=256`, `V=66` has
autocorrelation magnitude profile

```text
(n_1,n_2)=(1,8).
```

Exactly one light-light chord is a diameter. The requirement that the five
remaining unit chords have exactly one odd distance class puts the four light
positions, up to translation and an odd cyclotomic unit, in one of eleven
forms:

```text
{0,64,+/-1}, {0,64,+/-2}, {0,64,+/-4},
{0,64,+/-8}, {0,64,+/-16},
{0,64,1,63}, {0,64,2,62}, {0,64,4,60},
{0,64,8,56}, {0,64,16,48}, {0,16,32,64}.              (1)
```

A complete signed-chord census over (1), all three-position heavy supports,
and all coefficient signs tests

```text
11 * binom(124,3) * 64 = 218,327,296
```

normalized vectors. Exactly 17,144 have profile `(1,8)`, and their exact
maximum absolute third moment is

```text
M_3=1356<1732.
```

An independent ordered-negacyclic-product implementation gives the same
per-template totals and maxima. The exact `V=66` cubic-Hermite norm
certificate therefore excludes the profile.
