# E1 N=256 E=30 profile-(4,2,2) exclusion

- **status:** PROVED
- **closure:** exact structured relaxation, exceptional census, and norms

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=60`,
the magnitude profile `(4,2,2)` cannot occur in a pair-feasible collision.

The six odd autocorrelation classes are the six distinct light-light
differences. Two independent exact relaxations enumerate all 1,234 odd
difference masks and

```text
1234*binom(6,2)*binom(57,2) = 29,541,960
```

compatible magnitude-layer assignments. Exactly three assignments exceed the
proved cubic cutoff `M_3=1087`; all have `M_3=1146` and are the primitive
pattern

```text
light {0,1,6,8}, odd {1,2,5,6,7,8},
magnitude three {1,2}, magnitude two {3,4}
```

and its dilates by two and four.

Independent folded-chord and direct-negacyclic engines each test
`59,543,808` representative signed vectors over these three affine light
orbits. Exactly two vectors survive per orbit. The four dilated survivors
have proper conductor. The two primitive full-conductor vectors are related
by `F_2(x)=F_1(-x)` and have common exact norm

```text
N_max = 4039047355553663302249733085042470588482730556495866201164489362016333826,
447*N_max < 2^250 < 448*N_max.
```

FLINT and PARI/GP agree on both norms. The cubic theorem excludes every
nonexceptional assignment, the proper-conductor theorem excludes the four
dilated vectors, and the exact norm criterion excludes the two primitive
vectors.
