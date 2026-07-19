# F3 h=8 non-antipodal supports are rotation-aperiodic

Status: PROVED COMBINATORIAL REDUCTION + EXACT COUNT REPLAY.

This packet sharpens the h=8 n=64 support-certifier target.  The previous
rotation-orbit compiler treated the non-antipodal orbit count as a Burnside
subtraction.  In fact, every non-antipodal 16-support has trivial rotation
stabilizer.

## Statement

Let `R` be a 16-subset of `Z/64Z`.  If `R` is fixed by a nonzero rotation
`x -> x+t`, let `K=<t>` be the generated subgroup.  The `K`-orbits all have
size

```text
d = |K| = 64 / gcd(64,t).
```

Since `R` is a union of `K`-orbits, `d` divides `|R|=16`.  Thus

```text
d in {2,4,8,16}.
```

Every nontrivial subgroup of `Z/64Z` whose order divides `16` contains the
unique order-two element `32`.  Hence `R+32=R`; that is, `R` is antipodal.

Contrapositively:

```text
R non-antipodal  =>  R has trivial rotation stabilizer.
```

Therefore every non-antipodal rotation orbit has size exactly `64`.  In each
such orbit, exactly `16` rotated supports contain exponent `0`, one for each
element of `R`.  Hence

```text
anchored_nonantipodal_supports = 16 * nonantipodal_rotation_orbits.
```

For h=8 n=64 this gives the exact identity

```text
122,131,731,640,320 = 16 * 7,633,233,227,520.
```

## Role in T4

The h=8 n=64 support-first residual is not hiding a separate periodic
non-antipodal branch.  Periodic supports are antipodal and are already routed
to the paid quotient ledger by `F3_H8_ANTIPODAL_X83_QUOTIENT.md`.  The primitive
support certifier may target aperiodic non-antipodal rotation orbits directly.

This does not certify those aperiodic supports; it only removes a possible
periodic subcase from the residual.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_nonantipodal_aperiodic.py
```

Expected digest:

```text
H8_NONANTIPODAL_APERIODIC_PASS
```
