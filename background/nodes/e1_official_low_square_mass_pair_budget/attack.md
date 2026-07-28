# Attack

Start with prize rate `1/8`, where `N=256`, `ell=33`, and `S<=66`.

1. Use `e1_low_square_mass_weighted_kernel_dictionary` to import every proved
   profile exclusion as a zero contribution and every surviving relation
   orbit with its exact orientation, stabilizer, and `M_33(a,b)` weight.
2. Prove the exact weighted sum is at most the edge budget. After the complete
   `(4,2,S=18)` exclusion, the coarse fallback is
   `|D_p(33)|<=93962` oriented vectors on the binding row.
3. Spend the prize-field-floor exclusion first: all `S=16` profiles are zero.
   The former leading profile `(4,2,S=18)` first has seven prize cofactors; the
   sharpened local-norm theorem
   first leaves seven prize cofactor values after the residue-degree sieve.
   The proved variance/cofactor theorem then removes `1538`, forces
   `V=2 mod 8`, and leaves only `V in {10,18}` for `m=1028`. The complete
   dual census removes `1028` as well, leaving five prize cofactors (RowC still
   has 419 and receives no such prize-interval reduction). Dual censuses and
   exact FLINT/PARI norms then remove `514`, leaving four prize cofactors.
   A nine-chamber dual census and committed FLINT/PARI norm ledger remove
   `256`; analytic/census splits and streamed dual norm ledgers then remove
   `16`, `4`, and `2`. The whole profile is zero on prize-envelope rows. RowC
   still has 419 classes and receives no prize-interval reduction.
4. Prove maximum low-mass collision degree at most three if an incidence
   argument is cheaper. This gives `E_low<=3K/2`, below `1.714K`.
5. If degree four occurs, count the degree distribution rather than abandoning
   the route; the target is an aggregate edge budget, not a max-degree claim.
6. Attack the new maximum-weight profile `(3,6,S=18)` with common-prime
   ideal/resultant constraints or structural emptiness before any broad
   census. Its proved cofactor-window child leaves twelve cofactors; begin
   with `m=1538`, where only `V in {4,6,8,10,12}` remains, then the
   `m=1024,1028` windows through 34. Never count a normalized vector as one
   edge, and do not rerun any `(4,2,S=18)` prize cofactor.
7. Falsify with a pinned row and enough exact weighted edges to exceed the
   table, not a single collision vector.

No broad local or Modal census is authorized. Large exact relation searches
must be recorded as external compute requests with partial-result output.
