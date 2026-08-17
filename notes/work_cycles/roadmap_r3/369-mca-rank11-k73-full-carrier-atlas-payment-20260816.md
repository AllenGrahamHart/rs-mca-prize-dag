# Cycle 369: MCA K'=73 full carrier atlas payment (2026-08-16)

The generic pairwise carrier atlas and fixed-union support-4/5 coupling from
Cycle 368 close the adjacent `K'=73` row without a new structural theorem.
The only additional work is a larger exact conservative frontier and its
finite coupled reroute.

## Cycle pins

```text
our start:       9adad693f
our end:         cycle commit containing this record
canonical prize: 28a62b400
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170..#1173; tips unchanged at inspection
```

## Exact frontier

At `K'=73`, `q=63`, `m=67545`, and `n=1048649`. The streamed conservative
atlas evaluates 8,551,382 leaves. Exactly 218 distinct defect tuples exceed
the safe premium ceiling. The largest conservative leaf already below the
ceiling is

```text
s2=41/s3=33/s4=33/s5=31/c6F/c7F/c8F/c9F/carrier32_plain,
```

with

```text
P_73 = 41123952182016259764480350052978913220338995240,
ceiling-P_73 = 424186681733896065660200756292351785430362.
```

The 218 exceptional tuples expand to 71,806 exact pairwise-carrier charges.
Every charge is safe. Their maximum is

```text
32133901221158725309935103349312670983455197672,
```

leaving margin
`8990475147539268350610906904422534588669227930`.

## Geometry lanes and payment

Seven disjoint pre-routed geometry lanes evaluate another 118,892,669 exact
leaves. Their maximum is the one-step value

```text
35688968442860327556985962346044983398767741600,
```

which is strictly below `P_73`. Thus `P_73` is the global premium. Exact
integral capacity arithmetic gives

```text
demand-capacity
=2120784774514292837614781442321448802184060878375874298355>0.
```

The new PROVED packet pins all replay sources and the 218-cell frontier.
Its primary verifier rejects seven hostile mutations; its independent audit
recomputes all 71,806 exceptional routes. Both pass under the 256 MB local
RAM guard, while full frontier and lane enumerations ran on Modal at 58--62
MB peak RSS.

The manifest replay compiles 2,552 nodes and 7,593 edges and passes reference,
acyclicity, reachability, status-propagation, protocol, crosswalk, orbit, and
harness checks. Generated DAG SHA-256:
`d8d0b7a0bbff80d67fb47984dd5fe4dc8f9655e551c1baf13ec402d7f8b6a71d`.

```text
result:                CLOSED K'=73
newly closed rows:     73
closed prefix:         10..73
remaining rank nine:  74..15528
new nodes:             1 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         none; K'=72..73 extension is a candidate for #1170
delta-star movement:   none
compute:               exact bounded Modal lanes, 58--62 MB peak RSS
next route action:     replay the same atlas at K'=74 and isolate either a
                       closed row or the first genuine structural survivor
```
