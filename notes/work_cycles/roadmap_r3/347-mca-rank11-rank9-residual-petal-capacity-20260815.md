# Cycle 347: MCA rank-11 residual petal capacity (2026-08-15)

The repaired rank-nine frontier was `10<=K'<=20617`. This cycle keeps every
quantity in the residual row and closes its upper 4,983 rows.

## Residual owner geometry

Fix a rank-nine nine-set `B`, its one-dimensional evaluation kernel `u`, and
the affine owner plane. If `J` is the common pair core of the plane, then

```text
B subset J subset Z(u),        9<=j:=|J|<=K'-1.
```

Every owner core is `J disjoint_union P_p`; the petals `P_p` are pairwise
disjoint. With `s_p=|P_p|`, support-wise pair noncontainment gives
`s_p<=m'-j-1`. A marked extension `B union {x,y}` must use at least one
coordinate outside `Z(u)`, so one owner has at most

```text
q_p=s_p(j-9)+C(s_p,2)
```

available extension pairs. Charging at most `981105` selected records to
each owner and summing the disjoint petals yields

```text
W_B <= floor(981105*(n'-j)*(m'+j-20)/2).
```

## Exact crossing

The envelope `F(j)=(n'-j)(m'+j-20)` has forward difference
`981104-2j+19`, positive throughout the claimed interval. Its maximum is
therefore at `j=K'-1`. Exact adjacent arithmetic gives

```text
K'=15634:
  demand=50777401704768572,
  cap   =50779283449126807;

K'=15635:
  demand=50783693985583057,
  cap   =50780312213264392.
```

The rational demand/cap ratio is a product of nine increasing
Reed--Solomon factors and

```text
(K'+67463)(K'+67462)/(2K'+67451).
```

After cancelling its positive common factor, the latter has forward
cross-difference `2(K'-11)`. The ratio is strictly increasing above the
crossing. Hence rank nine is absent on `15635<=K'<=20617`; combining this
with the repaired high-row theorem makes the full surviving interval
exactly `10<=K'<=15634`.

The primary verifier replays every row `10..20617`, both raw adjacent
cross-products, and eight hostile mutations. The independent audit checks
206,060 factor identities, 52,846 core-envelope steps, and the proof pins
under the `tiny` RAMguard profile.

```text
result:                PROVED rank-nine closure on K'>=15635
newly closed rows:     15635..20617 (4,983 rows)
remaining rank nine:  10..15634
original-row floor:   not used
delta-star movement:  none
compute:               constant-memory exact integers under RAMguard
next route action:     couple owner-line incidence with the residual petal
                       budget on K'<=15634 without chartwise duplication
```
