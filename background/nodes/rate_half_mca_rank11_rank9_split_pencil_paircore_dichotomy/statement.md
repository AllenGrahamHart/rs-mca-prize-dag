# Rank-eleven rank-nine split-pencil pair-core dichotomy

- **status:** PROVED
- **scope:** records routed to one fixed rank-nine affine owner plane, lifted
  back to the original KoalaBear row
- **units:** distinct finite bad slopes on the fixed received line

Let `J` be the coordinate set on which every owner point in the plane agrees
with the original received pair, and put `j=|J|`. The lifted ten-coordinate
cell gives `j>=10`. If the plane contains `g` records, and `t_p` record lines
pass through owner point `p`, then the split-pencil ledger gives

```text
sum_p C(t_p,2)=C(g,2)
```

and pairwise disjoint owner petals `P_p=C_p minus J`.

Exactly one of the following holds.

1. **Low common core.** If `j<2m-n=134944`, then

   ```text
   g(g-1) <= 981105*(2097152-j)
          <= 981105*(2097152-10)
           = 2057516501910,
   g <= 1434405.
   ```

2. **Large shared pair core.** The entire affine owner plane has a common
   pair core of size

   ```text
   j>=134944.
   ```

Thus any one rank-nine owner plane carrying more than 1434405 records forces
one `134944`-coordinate pair core shared by every owner and record in that
plane. This is a plane-local dichotomy. It does not count planes or pay the
large shared-core branch.

## Falsifier

Two size-`m` record supports through one owner whose intersection is not in
that owner's pair core; overlapping petals for distinct owner points; a
fixed owner violating exception disjointness; a low-common-core plane with
`g>=1434406`; or a plane above the cap whose lifted common pair core has size
below 134944.
