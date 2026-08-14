# Rank-eleven order-32 common-support cancellation

- **status:** PROVED
- **closure:** exact support-wise shortening adapter
- **scope:** the 32-record output of the heavy-pair seed compiler

## Statement

Let `32` distinct actual KoalaBear rank-eleven records have exact selected
supports `S_i` of size `m`, and let

```text
C=intersection_i S_i,       c=|C|<K-4922.
```

There is an exact transformed received line on

```text
D'=D\C,       C'=RS[F,D',K-c],       m'=m-c
```

with the same `32` slopes and support-wise MCA-bad records on supports
`S_i'=S_i\C`. The transformed supports have empty common intersection.
The transformation preserves the record labels and chronology and satisfies

```text
n'-K'=n-K=1048576,
m'-K'=m-K=67472,
K'=K-c>=4923.
```

Consequently the rank-two critical order is unchanged:

```text
floor(2(n'-K')/(m'-K'))+1
 =floor(2097152/67472)+1
 =31+1=32.
```

## Nonclaim

The output domain `D\C` is an arbitrary puncturing of the deployed dyadic
domain. The deployed-domain partial-relative theorem is not automatically a
theorem on every such punctured domain. In particular, its common-support-free
slope-degree floor becomes

```text
ceil(32(K'+67472)/(K'+1048576)).
```

It is only `3` at `K'=4923` and returns to `18` only at
`K'>=1044446`, equivalently `c<=4130`. This adapter does not classify or pay
the output packet.

## Falsifier

Failure of divisibility by the common-support locator, loss of a slope or
support, a residual simultaneous pair explanation that does not lift to the
original support, nonempty residual common support, or movement of either
`n-K`, `m-K`, or the critical order.
