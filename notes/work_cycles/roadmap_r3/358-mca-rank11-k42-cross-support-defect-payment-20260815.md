# Cycle 358: MCA rank-11 K'=42 cross-support defect payment (2026-08-15)

Cycle 357 left exact capacity excess at `K'=42`.  The isolated-incidence
allowance was already sharp, so this cycle attacked the weighted completion
premium and the fact that its support strata had been maximized independently.

## Cycle pins

```text
our start:       ad44a0555d5f085cc90e7c96b28248d9e244f647
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 16ee6cfb2fe6f33630f5b4adf50a25eedea69d99
```

## Cross-support carrier

Suppose one independent support-`c` deletion has `q-s` completions.  Their
private coordinates span `q-s` dimensions of the common `q`-dimensional
annihilator.  At most `s` support-`d` labels complete that span, producing a
carrier of size

```text
q+c-1+s(d-1).
```

Comparing a target circuit's carrier representation with its minimal
representation is Vandermonde-safe whenever

```text
c+(s+1)d-s-1<=10.
```

Thus every support-`d` circuit lies in that carrier.  For source support five
and defects zero through four, the controlled target sets are

```text
{2,3,4,5,6}, {2,3}, {2}, {2}, {2}.
```

The proof compares only abstract sparse-label representations.  It does not
pair a quotient label with support-dependent received values.

## K'=42 payment

Partition by the maximum support-five deletion count.  If it is `q-s` for
`s=0..4`, apply the direct deletion cap and all valid cross-support carriers.
Otherwise every deletion has at most `q-5` completions.  The six weighted
premiums are

```text
defect 0:  3982795567806168516229316108688140450163630384
defect 1: 32010916243694499800320717073630461749362242674
defect 2: 38248686795246707324552098975684990817633239548
defect 3: 37909212899522784820182461169606692027883637848
defect 4: 37569681406601825198675563099275312923276993433
fallback: 39561073029598078809344868550502487135515187669.
```

The fallback is worst.  Keeping every chart, kernel, and shadow term, exact
sharp-isolated demand exceeds capacity by

```text
4081031051590194485758587836050845115467905186032497191061176.
```

Both the record coefficient and floor-record cross are positive.  Replaying
the same six branches at `K'=43` fails by

```text
2590504432899371163130658487199612335023802688487478696166262.
```

```text
result:                PROVED K'=42 component-row closure
newly closed row:      42
closed prefix:         10..42
remaining rank nine:  43..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         not yet exported; #1170 is the natural packet
delta-star movement:   none
compute:               exact local arithmetic and a tiny finite-field audit
next route action:     attack the exact K'=43 wall through a deeper
                       cross-support hierarchy or another shared resource
```
