# F3 h=8 exponent-unit symmetry falsifier

Status: PROVED COUNTEREXAMPLE / CERTIFIER-DESIGN GUARD.

This packet refutes a tempting h=8 n=64 support-certifier shortcut.  Root
scaling

```text
R -> cR, c in mu_64
```

is a valid symmetry of the x83 support condition.  It is natural to ask whether
the larger exponent-unit maps

```text
R -> R^u = {r^u : r in R},  u in (Z/64Z)^*
```

can also be used for canonicalization.  They cannot be used without separately
running the x83 classifier: the x83 full-zero condition is not invariant under
them.

## Pre-registration

Question:

```text
Can the h=8 support certifier quotient supports by exponent-unit maps
e -> u e mod 64, in addition to root-scaling rotations?
```

Success criterion:

- find a banked x83 full-zero support;
- apply an exponent-unit map;
- verify that the image support is not x83 full-zero.

Failure criterion:

- only show that a nonzero obstruction profile changes on a non-full-zero
  support;
- use a support not checked by the same x83 classifier as the h=8 residual;
- weaken the already proved root-scaling symmetry.

## Counterexample

At `p=193`, the support

```text
R = {0,1,2,9,10,16,24,25,32,33,34,41,42,48,56,57}
```

is x83 full-zero.  Its locator and forced square root are

```text
L_R = [14, 0, 189, 0, 138, 0, 90, 0, 167, 0, 78, 0, 66, 0, 29, 0, 1]
S_R = [47, 0, 156, 0, 145, 0, 111, 0, 1]
```

with obstruction vector

```text
[0, 0, 0, 0, 0, 0, 0]
```

and square `lambda = 72`.

First apply the exponent-unit map `e -> 3e mod 64`.  The image support is

```text
R^3 = {0,3,6,8,11,16,27,30,32,35,38,40,43,48,59,62}.
```

The same x83 classifier gives obstruction vector

```text
[0, 180, 0, 60, 0, 20, 0]
```

and `lambda = 30`, which is not a square.  Therefore `R^3` is not x83
full-zero.

The same banked support also refutes the tempting dihedral reflection shortcut
`e -> -e mod 64`.  The reflected support is

```text
R^{-1} = {0,7,8,16,22,23,30,31,32,39,40,48,54,55,62,63}.
```

The x83 classifier gives obstruction vector

```text
[0, 64, 0, 82, 0, 87, 0]
```

and nonsquare `lambda = 125`.  Therefore even reflection is not a safe
canonicalization symmetry for the x83 support condition.

## Consequence

The safe h=8 orbit compiler must remain rotation-only unless a different
symmetry is proved for the exact x83 obstruction system.  Quotienting by the
full affine exponent group, or by the usual dihedral rotation/reflection group
on exponents, would identify supports with different x83 status and would be
unsound for the residual certifier.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_exponent_unit_falsifier.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_rotation_orbit_compiler.py
```

Expected digests:

```text
H8_EXPONENT_UNIT_FALSIFIER_PASS
H8_ROTATION_ORBIT_COMPILER_PASS
```
