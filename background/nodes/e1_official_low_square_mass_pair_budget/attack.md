# Attack

Start with prize rate `1/8`, where `N=256`, `ell=33`, and `S<=66`.

1. Use `e1_low_square_mass_weighted_kernel_dictionary` to import every proved
   profile exclusion as a zero contribution and every surviving relation
   orbit with its exact orientation, stabilizer, and `M_33(a,b)` weight.
2. Prove the exact weighted sum is at most the edge budget. The coarse fallback
   is `|D_p(33)|<=69541` oriented vectors on the binding row.
3. Spend the prize-field-floor exclusion first: all `S=16` profiles are zero.
   The live leading profile is `(4,2,S=18)`; the sharpened local-norm theorem
   first leaves seven prize cofactor values after the residue-degree sieve.
   The proved variance/cofactor theorem then removes `1538`, forces
   `V=2 mod 8`, and leaves only `V in {10,18}` for `m=1028` (RowC still has
   419 cofactors and receives no such prize-interval reduction).
4. Prove maximum low-mass collision degree at most three if an incidence
   argument is cheaper. This gives `E_low<=3K/2`, below `1.714K`.
5. If degree four occurs, count the degree distribution rather than abandoning
   the route; the target is an aggregate edge budget, not a max-degree claim.
6. Use common-prime ideal/resultant constraints to bound low-mass vectors at
   one row prime. For the leading profile, start with the two `m=1028`
   chambers before the broader five-cofactor windows. Never count a normalized
   vector as one edge.
7. Falsify with a pinned row and enough exact weighted edges to exceed the
   table, not a single collision vector.

No broad local or Modal census is authorized. Large exact relation searches
must be recorded as external compute requests with partial-result output.
