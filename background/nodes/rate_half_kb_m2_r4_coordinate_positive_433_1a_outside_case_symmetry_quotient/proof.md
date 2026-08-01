# Proof

Write a target vertex-sign gauge as
`(g_A,g_B,g_C,g_D,g_E,g_F)`.  Preserving the multiplicity-two-positive,
multiplicity-one-negative `AB` records forces `g_Ag_B=1`.  The singleton
`AC`, colored `BE,CF`, and cycle `EF` records force

```text
g_Ag_C=g_Bg_E=g_Cg_F=g_Eg_F=1.                    (1)
```

Consequently `g_A=g_B=g_C=g_E=g_F`, while `g_D` is free because both signs
of each of `DE` and `DF` occur.  There are four vertex-sign stabilizers.
Simultaneously negating all six representatives acts trivially on every
product, leaving a faithful quotient of order two.  Its nontrivial element
changes `d` relative to the other representatives and acts exactly as
`tau` in `(KBOSQ-2)`.

The aligned and near-aligned labeled counts follow directly from the
source-facet distinction: in the aligned branch the `eta` and `xi` names
refer to the same internal record; in the near branch they refer to
different source records.  The remaining six labeled products are
partitioned into three unordered deck pairs in `(6-1)!!=15` ways.

For a case to be fixed by `tau`, its `eta` record must be fixed.  The only
fixed internal record is `EF`.

In the aligned branch this also forces `xi=EF`.  The six residual records
consist of the two transposed pairs `{DE+,DE-}`, `{DF+,DF-}` and the two
fixed records `BE,CF`.  An invariant perfect matching must pair `BE` with
`CF`; the four transposed records then have exactly three invariant
matchings:

```text
(DE+,DE-)(DF+,DF-),
(DE+,DF+)(DE-,DF-),
(DE+,DF-)(DE-,DF+).                                (2)
```

Thus there are three aligned fixed cases.

In the near branch, fixedness forces `eta=EF` and fixed `xi` distinct from
`eta`, hence `xi=BE` or `xi=CF`.  For either choice the residual records
again consist of two transposed pairs and two fixed records, giving the
same three matchings `(2)`.  Hence there are six near fixed cases.
Burnside's lemma now gives `(KBOSQ-3)--(KBOSQ-5)`.

If `xi=EF`, the aligned ledger has `15` cases and three fixed cases, hence
nine orbits.  In the near branch `eta` can be any of the other four
internal records, giving `4*15=60` cases.  None is fixed because `tau` fixes
no such `eta`, so there are thirty orbits.

Template A has matching

```text
(DE+,DF-), (DE-,CF), (DF+,BE),                     (3)
```

and template B has

```text
(DE+,CF), (DE-,DF+), (DF-,BE).                     (4)
```

Applying `tau` to `(3)` and swapping the first two deck-pair names gives
`(4)`.  In the aligned branch these two labeled cases therefore form one
orbit.  In the near branch the four allowed `eta` records together with
the two matchings give eight labeled cases and four order-two orbits.  The
templates cover five of the 39 `EF` orbits.  The exact enumerator replays
all counts and emits one canonical representative for every orbit. QED.
