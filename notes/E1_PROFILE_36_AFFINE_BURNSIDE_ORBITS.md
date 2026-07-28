# E1 profile-36 affine Burnside orbits

## Status

Exact draft lemma and independent atlas audit, not a DAG node. The arithmetic
was derived independently, and the deterministic replay is committed. Modal
is over its spend limit, so no verifier execution or status promotion is
claimed.

## Method

Let the affine group

```text
G_n = {x -> ux+b : u odd, b in Z/n}
```

act on six-element supports in `Z/n`. Its order is `n phi(n)`. For each of
its affine permutations, a fixed support is exactly a union of permutation
cycles. A finite DP chooses cycle unions of total size six and records the
Hasse parity mask

```text
(D_0(1),...,D_mu(1)).
```

Lucas's theorem computes a selected cycle's mask by XORing the indicators
`r & ~e == 0` over its exponents. Exact multiplicity `mu` means lower mask
`00...010...0`, with the only required one in position `mu`. Burnside's
lemma then gives the orbit count. Restricting selected cycles to all-even or
all-odd cycles counts the imprimitive branch independently.

## Exact counts

| cofactor role | ambient | multiplicity | affine orbits |
|---|---:|---:|---:|
| `m=2`, primitive | 128 | 1 | 331359 |
| `m=4`, primitive | 128 | 2 | 159216 |
| `m=4`, once-divided quotient | 64 | 1 | 18383 |
| `m=8`, primitive | 128 | 3 | 79360 |
| `m=16`, primitive | 128 | 4 | 39936 |
| `m=16`, once-divided quotient | 64 | 2 | 9080 |
| `m=16`, twice-divided quotient | 32 | 1 | 903 |

The recursive checks are exact:

```text
imprimitive mu2 orbits in Z/128 = 18383 = mu1 orbits in Z/64,
imprimitive mu4 orbits in Z/128 =  9983 = mu2 orbits in Z/64,
imprimitive mu2 orbits in Z/64  =   903 = mu1 orbits in Z/32.
```

For multiplicity three, the identity fixed count is `650,117,120`, while

```text
79360 * |G_128| = 79360 * 8192 = 650117120.
```

All nonidentity fixed counts are therefore zero: the affine action on the
`m=8` singleton supports is free.

## Consequences

1. The independent counts reproduce the committed `m=16` atlas split
   `39,936 + 9,080 + 903 = 49,919` without enumerating ten million normalized
   inputs. A final node verifier can establish completeness by checking every
   committed representative is canonical, primitive, exact-multiplicity four,
   and distinct, then comparing its count with `39,936` from this ledger.
2. The remaining exact-census route grows sharply: `m=8` has 79,360 orbits,
   `m=4` has 177,599 across its branches, and `m=2` has 331,359. Their energy
   windows are also wider than `m=16`. No broad radius census should be
   launched before a strong product, modular, or aggregate contraction.
3. Future generated atlases have an independent exact completion target and
   recursive branch audit before any expensive vector search begins.

## Replay

```bash
./tools/ramguard modal -- modal run \
  experiments/prize_resolution/e1_profile_36_affine_burnside_orbits_modal.py
```
