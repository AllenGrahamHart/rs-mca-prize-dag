# Cycle 370: MCA K'=74 full carrier atlas payment (2026-08-16)

The generic pairwise carrier atlas and fixed-union support-4/5 coupling also
close `K'=74`. This cycle first vendors the proved `K'=72,73` extension to
upstream PR #1170, then advances the local exact frontier by one row.

## Cycle pins

```text
our start:       fdef16d4b
our end:         cycle commit containing this record
canonical prize: 28a62b400
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PR:     #1170 head 5d3cda9475b03777c488e35ab152231bd338da71
```

## Exact frontier

At `K'=74`, `q=64`, `m=67546`, and `n=1048650`. The conservative atlas
evaluates 8,869,588 leaves. Exactly 729 distinct defect tuples exceed the
safe premium ceiling. To avoid another long payload, the node stores their
canonical lexicographic SHA-256 rather than copying the list:

```text
e036791483f8f10702731c02172071ce6106a1587f1996439640f08122162cf4.
```

The largest conservative leaf already below the ceiling is

```text
s2=32/s3=31/s4=32/s5=30/c6F/c7F/c8F/c9F/offset1_plain,
```

with

```text
P_74 = 41148280931947468743645570894078252803553423792,
ceiling-P_74 = 151207872362754098743792508682842947287405.
```

The 729 exceptional tuples expand to 338,149 exact pairwise-carrier charges.
Every charge is safe. Their maximum is

```text
32837046420997427924790365894433685328482435320,
```

leaving margin
`8311385718822403572953948792153250318018275877`. Two tuples tie at this
maximum, and the contract explicitly makes no unique-maximizer claim.

## Geometry lanes and payment

Seven disjoint geometry lanes evaluate another 124,851,888 exact leaves.
Their maximum is the one-step value

```text
36187398164184684606907419896584782044225756904,
```

strictly below `P_74`. Exact integral capacity arithmetic then gives

```text
demand-capacity
=755986378881174710705888877305550381612101047062792678211>0.
```

The primary verifier pins the compact contract and rejects eight hostile
mutations. The remote audit reconstructs the full conservative frontier,
digest, reroute, and payment at 61 MB peak RSS. The seven geometry lanes ran
as independent Modal tasks at 59--62 MB peak RSS.

The manifest replay compiles 2,553 nodes and 7,597 edges and passes reference,
acyclicity, reachability, status-propagation, sectioned-document, protocol,
crosswalk, orbit, and critical-harness checks. Generated DAG SHA-256:
`8b359112c4fa4de5c532d2125f8099c56241dbde91108dce1fa866439b2c7872`.

```text
result:                CLOSED K'=74
newly closed rows:     74
closed prefix:         10..74
remaining rank nine:  75..15528
new nodes:             1 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         PR #1170 advanced through K'=73
delta-star movement:   none
compute:               exact sharded Modal lanes, 59--62 MB peak RSS
next route action:     replay the same compact atlas at K'=75 and stop only
                       at a genuine structural survivor or a closed row
```
