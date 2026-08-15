# Carrier trichotomy closes `K'=71`

- **status:** PROVED
- **closed row:** `K'=71`
- **first method wall:** `K'=72`

Refine every exact support-two/support-three defect pair by the
carrier-position theorem whenever `M_3<=M_2`.  Exclude its impossible
defect pairs, retain both transverse and anchor cases, and preserve every
existing same-support, cross-support, support-four/support-five joint, and
support-six through support-nine terminal/fallback cap.

When `M_3=M_4=M_2+1`, retain all six carrier-position alternatives before
Pareto compression.  Exact integral replay then closes `K'=71`.  The
maximal branch is

```text
s2=33/s3=31/s4=31/s5=31/c6F/c7F/c8F/c9F,
```

with completion premium

```text
41052480732722315950912559282994987357541498029
```

and demand-capacity gap

```text
118872281099445772155993127155914865045379156488810154591370.   (P71)
```

The same complete replay first fails at `K'=72`, where capacity exceeds
demand by

```text
4821537739796415753639473905341364357966460110033651367468100.  (W72)
```

## Falsifier

An omitted exact defect tuple or carrier-position case; a Pareto deletion
without componentwise domination; a nonpositive `K'=71` exact gap; or a
nonpositive `K'=72` capacity excess.
