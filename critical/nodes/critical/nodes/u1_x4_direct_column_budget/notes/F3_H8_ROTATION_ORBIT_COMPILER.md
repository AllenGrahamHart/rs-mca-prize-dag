# F3 h=8 rotation-orbit compiler

Status: PROVED ROTATION-SYMMETRY COMPILER / NEGATIVE CERTIFIER-SCALE AUDIT, NOT
A FULL h=8 CERTIFICATE.

This packet records the safe symmetry reduction available for the h=8 n=64 x83
support certifier.  It uses only root-scaling rotations

```text
R -> c R,  c in mu_64.
```

It does not use arbitrary exponent-unit maps.  Those maps may be useful for
shape heuristics, but they are not banked here as x83-support symmetries.  The
exponent-unit falsifier now also rules out the usual dihedral reflection
`e -> -e mod 64` as a free x83-support symmetry.

## Pre-registration

Question:

```text
If the future h=8 support certifier canonicalizes supports under the obvious
root-scaling symmetry, how many non-antipodal support orbits remain?
```

Success criterion:

- prove that root scaling preserves the x83 support condition;
- compute the cyclic Burnside orbit count for all 16-subsets of `mu_64`;
- compute the cyclic Burnside orbit count for the antipodal subfamily;
- subtract to get the non-antipodal orbit target;
- state explicitly whether rotation canonicalization makes a direct global
  enumeration feasible.

Failure criterion:

- use arbitrary exponent-unit maps, including reflection, without a separate
  algebraic invariance proof;
- confuse anchored supports with rotation orbits;
- present rotation compression as enough to close h=8.

## Rotation invariance

Let

```text
L_R(X) = product_{r in R} (X-r)
```

and suppose the x83 full-zero condition holds:

```text
L_R(X) = S_R(X)^2 - lambda,
```

where `S_R` is monic of degree 8 and `lambda` is a nonzero square.  For
`c in mu_64`,

```text
L_{cR}(X) = c^16 L_R(X/c)
          = (c^8 S_R(X/c))^2 - c^16 lambda.
```

The polynomial `c^8 S_R(X/c)` is again monic of degree 8, and `c^16 lambda` is
a square.  Hence x83 full-zero supports, and their recovered trade splits, are
stable under root scaling.

## Burnside counts

The rotation group has size 64.  Burnside's lemma over the cyclic translations
of exponents gives:

```text
all 16-supports                  = binom(64,16) = 488,526,937,079,580
all 16-support rotation orbits   = 7,633,233,556,276
```

The antipodal 16-supports are the same as 8-subsets of the 32 antipodal pairs.
The induced rotation group on those pairs is cyclic of size 32, so

```text
antipodal 16-supports                = binom(32,8) = 10,518,300
antipodal support rotation orbits    = 328,756
```

Therefore the non-antipodal support-orbit target under the safe rotation
symmetry is

```text
7,633,233,227,520.
```

For comparison, the anchored non-antipodal support target has
`122,131,731,640,320` supports, so rotation canonicalization improves the
anchored workload by an average factor of about `16`.  It does not make a
direct global support enumeration feasible.

## Residual target

The h=8 residual still needs a stronger idea:

```text
either an x83 obstruction-key certificate that avoids one-record-per-support
enumeration, a separately proved larger symmetry/canonicalization group, or an
external/sharded signature join.
```

Rotation canonicalization is worth using in any future certifier, but by itself
it leaves about `7.6e12` non-antipodal support orbits.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_rotation_orbit_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_support_universe_compiler.py
```

Expected digests:

```text
H8_ROTATION_ORBIT_COMPILER_PASS
H8_SUPPORT_UNIVERSE_COMPILER_PASS
```
