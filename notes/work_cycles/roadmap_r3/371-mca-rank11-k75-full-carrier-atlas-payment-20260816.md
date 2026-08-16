# Cycle 371: MCA K'=75 full carrier atlas payment (2026-08-16)

The same proved carrier atlas closes the next row. This cycle also
parameterizes the compact frontier audit and extracts one shared contract
validator, so later rows need only small row-specific contracts and wrappers.

## Exact frontier

At `K'=75`, `q=65`, `m=67547`, and `n=1048651`, the conservative stream has
9,479,358 leaves and 1,995 above-ceiling defect tuples. Their canonical
lexicographic digest is

```text
49a191e500624b4f98761863cbce004d3dc2911055c7e24b8b966a2b99e2d440.
```

The largest already-safe leaf is

```text
s2=43/s3=36/U23/s4=37/s5=32/c6F/c7F/c8F/c9F/ordinary,
```

with premium and margin

```text
P_75 = 41172442942616752083301734067206968949181736144,
ceiling-P_75 = 42309306941100164131542711491454099991233.
```

The exact reroute has 1,228,878 evaluations and is entirely safe. Its maximum
is `33540409167198343349228340842477255779539196790`, leaving margin
`7632076084725349834237524767441204623742530587`. The seven geometry lanes
contain 131,010,586 leaves and have maximum
`36818718942605286540367916391174777496642019789`, below `P_75`.

Exact integral capacity arithmetic gives

```text
demand-capacity
=211531709609936637728192389252911579074455707755248457894>0.
```

## Replay refactor

The compact audit now accepts the requested row as an argument, with `74` as
the backward-compatible default. A shared compact-contract API validates
source hashes, active conservative caps, thresholds, lane partitions, floor
placement, and exact payment arithmetic. K'=74 and K'=75 each retain a thin
row-specific primary and remote-audit wrapper. Both full audits pass on Modal
at 58 MB peak RSS; both primary wrappers reject eight hostile mutations.

The manifest compiles 2,554 nodes and 7,601 edges. Generated DAG SHA-256:
`aae742a3cb5374366320c5664541c35657464518db1401fc4383dce37168ac48`.

```text
result:                CLOSED K'=75
newly closed rows:     75
closed prefix:         10..75
remaining rank nine:  76..15528
new nodes:             1 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         none; batch K'=74..75 for the next #1170 extension
delta-star movement:   none
compute:               exact sharded Modal lanes, 58--62 MB peak RSS
next route action:     probe K'=76 with the parameterized compact audit
```
