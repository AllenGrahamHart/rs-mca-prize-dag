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
   census. Its `m=1538` child is now closed by a dual exact low-energy
   classifier. The sharp product envelope contracts `m=1024,1028` to
   `V in {4,6,8,10,12}`, and the dual `mu=10` census closes `m=1024`, leaving
   ten cofactors. The `mu=2` census plus factor-257 test then closes `m=1028`,
   leaving nine. The capped sharp product envelope contracts their upper
   endpoints to `284,266,254,216,170,130,60,34,34` in increasing cofactor
   order. A multiplicity-nine radius census plus exact norm ledger closes
   `m=512`, leaving eight cofactors. Attack `m=514` through `V=34` using its
   multiplicity-one structure and required factor 257. The energy-adaptive
   product theorem has already reduced this to the nine live `(E,q)` chambers
   `(7,3),(7,7),(8,4),(8,8),(9,5),(9,9),(10,6),(10,10),(11,11)` and has
   separately contracted `m=256` to `V<=46`. The dual nine-chamber census and
   exact norm ledger close `m=514`, leaving seven cofactors. An exact
   parity-product ledger, complete 5920-orbit multiplicity-eight census, and
   dual norm packet then close `m=256`, leaving the six pure cofactors
   `2,4,8,16,32,64`. Attack `m=64` through `E=65` next, spending
   multiplicity six before any norm work. Never count a normalized vector as
   one edge, and do not rerun any closed cofactor.
7. Falsify with a pinned row and enough exact weighted edges to exceed the
   table, not a single collision vector.
8. On the residual `(3,6,S=18)` profile, consume
   `e1_pure_cofactor_common_prime_associate_router` and then
   `e1_conductor256_character_diagonal_exponent_router` before any further
   norm classification. Fix one row root and one normalized prime generator `g`;
   every residual vector is `pi^mu u g`, with `mu in {1,2,3,4}` and `u` an
   algebraic unit of `Z[zeta_256]`. In each fixed-cofactor branch, consume the exact
   coefficient boxes for both `u` and `u^(-1)` and retain the negacyclic
   inverse equation. Seek a height, coefficient, or packing bound on these
   bounded associates. Do not replace arbitrary units by roots of unity or
   by the cyclotomic-unit subgroup, enumerate the raw box, or merge different
   quotient roots without the Galois transport. The alternative exact count
   is in the full rank-63 unit log lattice inside the router's AM-GM body;
   any regulator or packing argument must apply to that full lattice. The
   character router, certified preflight, and inverse-kernel contraction give
   `|xi_t|<=3`, `sum|xi_t|<=60`, and `sum xi_t^2<=101`. The earlier coarse
   zero-sum envelope has more than `2^143` points, and even the weighted
   ellipsoid already contains over
   `3.8*10^13` explicit sparse points. Generic exponent enumeration is
   rejected. Make the exact sparse product and inverse equations the first
   generator, or prove a support-propagation classification before proposing
   computation. The exact profile target is at most 367 points modulo
   `mu_256`; retain all lower-profile charges after paying it.
9. Consume `e1_high_cofactor_schinzel_height_collapse` before any associate
   search. It pays the `m=4,8,16` multiplicities analytically at most one
   torsion orbit each. Restrict every subsequent unit search to `m=2`; its
   necessary maximum-profile fallback is at most 364 orbits after charging
   the possible three high-cofactor orbits. Do not confuse this with the
   complete weighted budget, which still includes lower profiles.

No broad local or Modal census is authorized. Large exact relation searches
must be recorded as external compute requests with partial-result output.
