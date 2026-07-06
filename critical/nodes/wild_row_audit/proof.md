# wild_row_audit proof packet

- **status:** audit complete; no `dag.json` edit in this packet
- **verifier:** `python3 tools/verify_wild_row_audit.py`
- **certificate:** `nodes/wild_row_audit/wild_row_audit.json`

## Claim

The QA.23 audit deliverable is complete:

1. the admissible Mersenne wild rows below `2^256` are exactly enumerated;
2. every coset of `mu_n` inherits wildness by dilation conjugacy;
3. the fully computable `F_49/mu_8` toy has no support/window stratum outside
   the Dickson subgroup-orbit taxonomy;
4. the toy also shows that wild rows have extra Dickson orbit-window
   partitions not visible in the tame dihedral/Sylow-2 ledger.

The packet does not claim a prize-scale Dickson budget theorem for every wild
row.  Its verdict is the narrower one recorded in the node ledger: wild rows
are finite, classical, separately auditable cases, and the campaign's named
clean-rate rows remain tame.

## Arithmetic

For a 2-power row to be wild, the domain must be projectively the subfield
circle `P^1(F_p)` with

```text
n = p + 1,       p = 2^r - 1,
q = p^(2s) < 2^256.
```

The verifier checks the requested exponents:

| `r` | `n` | admissible `s` | count |
| ---: | ---: | --- | ---: |
| 13 | 8192 | `1..9` | 9 |
| 17 | 131072 | `1..7` | 7 |
| 19 | 524288 | `1..6` | 6 |
| 31 | 2147483648 | `1..4` | 4 |

Thus there are exactly 26 admissible `(n,q)` wild rows in the requested
family.  The exact `q` values are pinned in
`nodes/wild_row_audit/wild_row_audit.json`.

For any scalar `alpha`, the domain `alpha*mu_n` is a dilation of `mu_n`.
Conjugating by that dilation carries the stabilizer and every subgroup stratum
from `mu_n` to the coset.  Hence wildness is coset-independent.

## F49/mu8 Toy

The verifier identifies the wild toy with the action of `PGL_2(F_7)` on
`P^1(F_7)`.  It recomputes:

```text
|PGL_2(F_7)| = 336,
the action is sharply 3-transitive,
the subgroup lattice has 413 subgroups,
the selected tame dihedral/Sylow-2 sublattice has 19 subgroups.
```

For every subgroup, the verifier enumerates all invariant subsets and checks
that they are exactly the unions of subgroup orbits.  This proves the toy has
no support/window escape outside the Dickson-derived strata.

The full Dickson lattice has five orbit-window partitions absent from the tame
dihedral sublattice:

```text
(1,1,3,3), (1,1,6), (1,7), (2,3,3), (2,6).
```

So a dihedral-only ledger is incomplete at wild rows, but the incompleteness is
classified: the extra windows are Dickson-lattice windows.

## Nonclaims

This packet does not price every prize-scale Dickson window family.  It gives
the exact wild-row list, coset inheritance, the exhaustive toy taxonomy, and
the boundary condition needed by downstream dossier bookkeeping.
