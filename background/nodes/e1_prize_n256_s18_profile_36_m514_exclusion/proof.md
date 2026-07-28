# Proof

The parent theorem leaves exactly

```text
(E,q)=(7,3),(7,7),(8,4),(8,8),(9,5),(9,9),
      (10,6),(10,10),(11,11).                       (1)
```

Here `q` is the odd folded-chord weight of the six singleton positions.

## Complete singleton atlas

Multiplicity one gives an odd-separated singleton pair. Translation and an
odd Galois multiplier normalize that pair to `{0,1}`; a global sign fixes the
coefficient at zero. Exact enumeration of all `binom(126,4)=10009125`
normalized supports finds 5005539 of multiplicity one. The raw counts for the
weights used in (1) are

```text
q=3:6836, 4:350, 5:11490, 6:8216, 7:114212,
q=8:24048, 9:357190, 10:134638, 11:1248752.
```

Affine canonicalization leaves 123196 orbits, split as

```text
q=3:692, 4:23, 5:725, 6:496, 7:6930,
q=8:1728, 9:23227, 10:9043, 11:80332.               (2)
```

## Radius-zero/radius-one census

For `q=3,...,6`, (1) has `E=q+4`. Outside the odd-chord mask, at most one
autocorrelation half-entry can be odd. For `q=7,...,11`, (1) has `E=q`, so no
outside half-entry can be odd. Thus every candidate heavy triple satisfies a
radius-one or radius-zero XOR equation, respectively.

The primary engine uses an unordered pair multimap and probes each third
heavy position. The audit engine independently sorts all pair keys and uses
binary equal ranges. Both replay all eight heavy-sign choices and then test
all 128 primitive roots modulo 257. They agree exactly:

```text
affine orbits:             123196
singleton sign choices:   3942272
XOR probes:             922886080
candidate heavy supports:  883718
exact heavy-sign tests:    7069744
exact geometry: E8=4, E10=8; E7=E9=E11=0
primitive-root tests:         1536
factor-257 vectors: E8=2, E10=6.                    (3)
```

## Exact norms

The eight vectors in (3) have four distinct norms. FLINT resultants and
independent PARI/GP resultants agree entry by entry. Every norm has 2-adic
valuation one and is divisible by 514. The largest quotient is

```text
76286518954257624881921953724462535222876321872384746739394244519622714858497,
```

which is strictly below `B_P 2^128`. A cofactor-514 collision would have
`Norm(F)=514p` with `p>=B_P 2^128`, a contradiction.
