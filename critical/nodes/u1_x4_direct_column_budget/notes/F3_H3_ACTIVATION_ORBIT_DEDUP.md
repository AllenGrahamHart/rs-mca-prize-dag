# F3 h=3 activation orbit dedup

Status: MACHINE-VERIFIED DEDUPLICATION OF BANKED EVIDENCE.

This note performs the final symmetry deduplication layer on the `n=96`
Terminal C activation list.  It does not create new activation data and does
not prove the uniform `H3-ACT(C)` theorem.

## Object

Input:

```text
f3_h3_all_core_census_summary.json
```

That file contains `720` oriented activation records from one complete
oriented `B`-slice for each of the `91` affine/Galois orbits of the first h=3
core.

Deduplication group:

```text
x -> u*x + s,       u in (Z/96Z)^*, s in Z/96Z,
```

plus side swap.  This is the same affine/Galois symmetry used by the Terminal C
orbit-count note, and it preserves the common-root activation predicate.

## Result

The replay gives:

```text
raw oriented activation records:      720
unique affine/Galois pair-orbits:     167
activation primes:                    82
max deduped per-prime activation:     27 at p=37633
repeated canonical orbits across p:   0
```

This improves the h=3 evidence scale: the previous oriented maximum was `92`
at one prime, while the deduped orbit maximum is `27`.  Both are below the
compiler's `C=1` target at `n=96`.

The absence of repeated canonical orbits across threshold primes is also the
right prime-ideal/common-root version of the old pair-coprimality heuristic.
It is not the rational norm-gcd statement, which is already refuted.

## Scope

This is exact for the activation records present in the banked all-core JSON.
It relies on the coverage claim of that JSON: one complete oriented `B`-slice
for each first-core affine/Galois orbit.  It is not an independent all-shapes
census and should not be promoted beyond evidence for `H3-ACT(C)`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_orbit_dedup.py
```

Expected digest:

```text
H3_ACTIVATION_ORBIT_DEDUP_PASS
```
