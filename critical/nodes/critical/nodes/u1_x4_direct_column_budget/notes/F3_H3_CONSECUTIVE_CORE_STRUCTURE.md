# F3 h=3 consecutive-core exception structure

Status: MACHINE-CHECKED STRUCTURAL CLASSIFICATION OF A BANKED SUBFAMILY CENSUS.
This classifies the 44 activation exceptions found in the complete
`A=[0,1,2]` slice.  It does not classify the full `n=96` shape space.

## Statement

In the complete consecutive-core census

```text
A = [0,1,2],  B any 3-subset of {3,...,95},
```

all 44 actual common-root activation exceptions satisfy at least one of:

```text
Fixed-pair family:      {17,81} subset B
Antipodal-pair family:  {a,a+48} subset B for some a mod 96.
```

Counts:

```text
total activation exceptions = 44
fixed-pair family           = 18
antipodal-pair family       = 28
overlap                     = 2
union                       = 44
```

The stabilizer of `A=[0,1,2]` inside the affine/Galois group is

```text
id,  x -> 2-x.
```

It pairs the 44 exceptions into 22 two-element orbits, and the activation prime
is constant on every orbit.

## Replay

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_structure.py
```

Expected digest:

```text
H3_CONSECUTIVE_CORE_STRUCTURE_PASS
```

