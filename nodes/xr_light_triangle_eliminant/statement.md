# xr_light_triangle_eliminant

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement

Light configurations (sum r - triple <= 2k, budget >= k+1 still met): syzygy existence is a NON-GENERIC determinantal condition — an explicit eliminant locus in the support coordinates (the kernel of the sum map Lambda_0 + Lambda_1 + Lambda_2 jumps rank). The remaining claim: for every pair, stagnating light triangles are rationed — the eliminant locus's intersection with the pair's aligned-support variety is poly-bounded or paid. This is the SMALLEST closed form of face 4's residual core: one determinantal condition, three supports, exhaustively toy-testable (E32), and M5's chart machinery is its laboratory at deficiency-triple level.

## Attack surface

write the eliminant explicitly at toy scale (the sum-map matrix in MDS coordinates); E32 hunts stagnating light triples; the u5-style dichotomy (eliminant nonzero => rationed; identically zero => the configuration family is structured/paid) at triple level

## Falsifier

a toy pair with super-poly stagnating light triangles outside paid strata (E32 directly)

## Ledger (migrated notes)

E32-MERGED: no profile-forced vanishing anywhere checked; the dichotomy's structured branch is empty at profile level. Remaining: coordinate-special vanishing + the rationing leg (deep-link staircase, E33 pending).
