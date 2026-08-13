# Cycle 215: profile-(4,4) energy-five exclusion

## Compression before compute

The naive abstract energy-five census has roughly `224M` spectra. Parity
reduces it sharply. The only integer energy partitions are

```text
5=1+1+1+1+1=4+1.
```

Therefore the odd autocorrelation mask has weight five or one. A complete
four-singleton support census gives only

```text
1785 weight-five masks,       31 weight-one masks,
100 and 5 odd-unit mask orbits, respectively.
```

Enumerating all signs directly, without relying on the orbit quotient,
requires exactly

```text
1785*32 + 31*62*4=64808
```

spectra.

## Exact result

The primary eight-shard FLINT census computes the exact cyclotomic norm of
all `64808` spectra and finds no official hit. A separately written
eight-shard replay changes the support loops, mask representation, spectrum
order, and interval test. It finds the stronger result that no spectrum has
even one integer cofactor in the exact official prime interval.

Both runs used `512 MiB` workers and approximately `33` aggregate worker
seconds. The mask census and both norm runs are pinned by source hash and
Modal run identifier.

Thus energy five is empty. With cycle 213,

```text
E>=6,       V>=12,       m<=853574
```

for every official profile-`(4,4)` collision. The exact cofactor frontier
contracts from `645` to `608` values.

## Banked node

`e1_profile44_official_energy5_exclusion` is PROVED with a complete proof
packet, primary verifier, independent audit, and evidentiary edges into the
E1 pair-budget and unsafe-crossing nodes.

## Stop rule

No energy-six census is selected. Even hypothetical exclusions through
energy twenty leave more than three hundred locally admissible cofactors,
while the target is seven total collision orbits. The next route must control
multiplicity collectively through collision coloring, ideal occupancy and
associate coupling, or direct weighted payment.
