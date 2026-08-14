# Rank-eleven component nine-subset target router

- **status:** PROVED
- **scope:** the fixed nine-subset population from the lane concentrator
- **population floor:** 2578110 distinct records

At least one of the following concrete targets exists.

1. **Fixed kernel chart.** One nine-subset `B` carries at least 2578110
   records, each with a rank-deficient component eleven-subset `T` extending
   `B`. Here `rank(ev_B)<=9`, so all component kernels lie inside the same
   nonzero `ker(ev_B)`.
2. **Large shared-core rank-nine plane.** One rank-nine `B` carries at least
   2578110 affine-owner records in one owner plane. After the reversible
   common-core lift to the original row, since
   `2578110>1434405`, the plane has a common received-pair core of size at
   least 134944.
3. **Rank-eight owner flat.** One rank-eight `B` carries at least 2578110
   affine-owner records. Their owners lie in one affine `U^2` flat with
   `dim U=2`, and the selected residual record errors have affine error rank
   at most three; the reversible lift preserves that rank.

This replaces a recordwise owner/pencil/kernel target by one fixed chart of
more than 2.5 million records. It does not pay that chart or the complete
rank-eleven line.

## Falsifier

A dominant-lane fixed `B` outside all three routes; an affine-owner
component of rank ten whose nine-coordinate restriction has rank below
eight or above nine; a rank-nine plane above 1434405 records with shared
core below 134944; or rank-eight owner-flat errors spanning dimension at
least four.
