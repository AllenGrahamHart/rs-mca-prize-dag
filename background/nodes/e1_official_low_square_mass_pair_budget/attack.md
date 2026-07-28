# Attack

Start with prize rate `1/8`, where `N=256`, `ell=33`, and `S<=66`.

1. Use `e1_low_square_mass_weighted_kernel_dictionary` to import every proved
   profile exclusion as a zero contribution and every surviving relation
   orbit with its exact orientation, stabilizer, and `M_33(a,b)` weight.
2. Prove the exact weighted sum is at most the edge budget. The coarse fallback
   is `|D_p(33)|<=27520` oriented vectors on the binding row.
3. Prove maximum low-mass collision degree at most three if an incidence
   argument is cheaper. This gives `E_low<=3K/2`, below `1.648K`.
4. If degree four occurs, count the degree distribution rather than abandoning
   the route; the target is an aggregate edge budget, not a max-degree claim.
5. Use common-prime ideal/resultant constraints to bound low-mass vectors at
   one row prime. Never count a normalized vector as one edge.
6. Falsify with a pinned row and enough exact weighted edges to exceed the
   table, not a single collision vector.

No broad local or Modal census is authorized. Large exact relation searches
must be recorded as external compute requests with partial-result output.
