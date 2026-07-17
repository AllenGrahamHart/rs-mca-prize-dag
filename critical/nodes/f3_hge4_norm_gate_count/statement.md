# F3 h>=4 norm-gate aggregate count

- **status:** TARGET
- **consumer:** `f3_hge4_aggregate_budget`
- **binding claim:** NG-COUNT

## Row and width scope

At every official corridor row,

```text
n=2^s,                    13<=s<=41,
p prime,                  p==1 mod n,
p>=n^2,
H_max=min(k+t,floor(n/2)).
```

For each `4<=h<=H_max`, let `N_h^strip` count records in the direct-column
convention with all of the following properties:

1. the record is F-4-minimal in the x81 square-shift convention;
2. it is not a characteristic-zero full-fiber trade;
3. all `h-1` cleared x83 low obstructions vanish modulo the row prime and the
   recovered `lambda` is a nonzero square;
4. it survives the ordered quotient, dihedral, moment-trade, U2-boundary, and
   DLI/skew deletion columns.

The binding target is

```text
sum_(h=4)^H_max N_h^strip <=14n^3.                  (NG-COUNT)
```

An empty sum is zero. The count is on records in the x81/x83 anchoring and
deduplication convention, not on raw support pairs, moments, or unanchored
presentations.

## Strip-free sufficient target

Let `N_h^raw` count the same F-4-minimal, non-full-fiber x83 norm-gate records
before the five deletion columns. Deletion is monotone, so

```text
N_h^strip<=N_h^raw
```

at every width. Therefore

```text
sum_(h=4)^H_max N_h^raw<=14n^3                    (RAW-NG)
```

is a stronger sufficient theorem. RAW-NG is the preferred proof interface
because it does not require operational implementations of the U2-boundary
and DLI/skew deletions.

## Posedness and falsifiers

The consumer names all five deletion predicates, but the current repository
has operational analogues for only three. This does not obstruct a RAW-NG
proof. It does mean that a purported counterexample to NG-COUNT must first
give positive definitions and an exact implementation of the U2-boundary and
DLI/skew deletions. An unstripped aggregate above `14n^3` is not by itself a
falsifier.

A valid falsifier is a complete official row or a proved transported slice
whose correctly stripped F-4-minimal norm-gate aggregate is greater than
`14n^3`. NG-ZERO is not claimed.

## Nonclaims

- Empirical zero on the banked cells is not a uniform theorem.
- No fixed width cap is assumed.
- The first-moment vacancy curve is evidence only.
- Reopening F-4 minimality changes the counted object and requires DAG
  surgery.
