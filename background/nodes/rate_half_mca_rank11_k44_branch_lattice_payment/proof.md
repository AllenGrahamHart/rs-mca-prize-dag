# Proof

Put `q=34`, `n=1048620`, `m=67516`, and retain the exact record floor
`274980728111260126`.  Begin with the 27 leaves of the descending source
order `5,4,3,2`.  Replace each of the leaves `c5_defect_2` and
`c5_defect_3` by the support-six alternatives

```text
M_6=q-s for s=0,1,2,3,       or       M_6<=q-4.
```

The branch-lattice theorem makes each replacement disjoint and exhaustive,
and preserves every cap inherited from its support-five parent.  The leaf
count is therefore `27-2+2*5=35`.

On each leaf, intersect inherited, source, and valid cross-support caps and
weight support `d` by `C(11-d,2)`.  The largest premium occurs at

```text
c5_defect_2__c6_defect_2
```

and equals

```text
40318474413130846902399237147930487840413149400.    (1)
```

The all-core chart is maximized at core `43` with value
`9276017644877905`.  Retaining every nonzero kernel corank gives

```text
K_cap=19365553760266721707534909128794870835638127507520795923192.
```

The exact rank-nine marks and full-rank capacity are

```text
39187436374399025413366978554448342106160515916819218919383612300,
914077087724671945403235996597792003150819968653996672976080667.
```

Thus complete capacity is

```text
914096453278432212124943531506920798021655606781504193772003859.
```

Sharp isolated incidence gives demand

```text
R C(67516,11)-C(1048620,11).
```

Its exact value is

```text
914632087688377144021446114681200227193194740473705158570542108.
```

Their exact difference is

```text
535634409944931896502583174279429171539133692200964798538249>0.
```

The cleared record coefficient and floor-record cross are

```text
142629210022785653381290835627715566932078928340>0,
29459892546971254307642074585368604434652353071053063919603680>0.
```

Thus the gap persists above the floor.  Repeating all 35 leaves at `K'=45`
gives capacity excess

```text
5651502053446174523626296867091469400380654135040887972894842,
```

so `K'=45` is retained as the first wall.  QED.
