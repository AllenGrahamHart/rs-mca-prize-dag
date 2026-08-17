# Cycle 375: MCA K'=74..78 compact upstream export (2026-08-16)

The five proved carrier-atlas rows were exported as one reviewable extension
of draft upstream PR #1170:

```text
https://github.com/przchojecki/rs-mca/pull/1170
review range:
b4bad860750f91955dbaead8f2b5a0fdef1f1343
  ..0b6cb72c025ddaafbddd92e3daf398e5993ef320
```

The export uses Przemek's base-field-normalized split-pencil terminology and
retains the existing full-completion pairwise carrier atlas and flat-coupled
support-four/support-five census. It adds a separate compact certificate for
`K'=74..78`: canonical SHA-256 digests replace an expanded 25,733-tuple
payload, while an optional one-row verifier reconstructs the conservative
frontier and complete reroute.

All five fresh upstream full replays pass:

```text
rows:                     74,75,76,77,78
exceptional cells:        729,1995,3800,7657,11552
total reroute leaves:     20995128
peak RSS per Modal job:   57--58 MB
closed rank-nine prefix:  10..78
first open rank-nine row: 79
```

The primary verifier recomputes every row payment and rejects eight hostile
mutations. An independent implementation recomputes the exact capacity
arithmetic. Grande Finale builds in three passes at 175 pages.

```text
upstream commit:          0b6cb72c025ddaafbddd92e3daf398e5993ef320
compact manifest:         20dff5ce1c9634f9cd99e2cbacd4809fc860894f4549265a6f8b69176c0843c4
primary verifier:         b3be282aa7ecc1696c53bc46a1a96702a03f7892db672ff1292090981480157a
independent verifier:     55717ab77ccae0fdb7b774867ab95d1bb7b02b55a2979ad016114f01a36196a1
full-frontier verifier:   4da8cfa98aa22cfde6cf14ebfda687371cff28a35c7e8c04ffca10c8bebcdbe5
paper PDF:                ff4837ec8438f469f7d8d9b872e341c216fb61e6029062e36afc508191e1ec2d
```

The live open queue still contains complementary rank-eleven router PRs
#1171--#1173. No overlap was imported and no claim was made that this packet
pays rank eight, chronology, aggregate error rank eleven, KoalaBear, or
either prize problem. The canonical `prize` worktree remained clean at its
earlier `K'=71` integration point throughout this export.

```text
start:                   9526b45dc
DAG delta:               none; integration-only cycle
critical status delta:   none; 167 green / 37 amber / 27 red math orbit
upstream delta:          PR #1170 extended through K'=78 at 0b6cb72
delta-star movement:     none
compute:                 five bounded exact Modal replays, 57--58 MB RSS
next route action:       probe K'=79 with the same complete atlas before
                         deciding whether a new geometric charge is needed
```
