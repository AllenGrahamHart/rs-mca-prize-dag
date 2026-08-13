# Mersenne fixed-cutoff residue-two anchor repair

- **status:** PROVED
- **scope:** Mersenne-31 full-lift support `e=101156`

Use fixed cutoff `h0=65258`.  The prefix plus all exact boundary-class
charges is

```text
F=16895280.
```

Let `T` be the synchronized top union, and let `D1,D2` be the exact layers
of deficits `H,H-1`.  Their coarse direction-class charges are

```text
D1<=284224,       D2<=258385.
```

At this support

```text
(s,q,H)=(33716,2,67439),
Q_H=94742,       floor(e/(s+1))=3.
```

The complete family satisfies the five-case bound

```text
|Z| <= max{
  3813497,
  16705799,
  16611058,
  16705798,
  16611059
} = 16705799 < 16777215.                           (Q2R)
```

The cases are respectively: at least two top anchors; exactly one top
anchor with a boundary line; exactly one top anchor with at most one
boundary member; no top anchor with a boundary line; and no top anchor with
pairwise-disjoint boundary missed sets.

Thus `e=101156` is safe and the Mersenne full-lift residual starts at
`e=101157`.  At the adjacent support the residue resets to zero, so this
repair is inapplicable.
