# xr_eliminant_vanishing_class

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement

The triple-level u5 dichotomy's structured branch: classify support/slope configurations where the light-triangle eliminant vanishes IDENTICALLY (for structural reasons) — conjecturally exactly the paid patterns (near-heavy boundary, dihedral-symmetric, pullback-patterned). Per the program's strategy this node is NOT decomposed further until the census runs: E32-extended enumerates ALL eliminant-vanishing light configurations at n = 16 exhaustively; the classification will be written along the observed cases (the E9/E13 pattern). SHARPENED POST-E32: since the eliminant is nonzero on every light profile, coordinate-special stagnation means lying on a PROPER hypersurface inside the profile cell — the remaining obligation is 'per pair, aligned light triples on an explicit proper hypersurface are rationed', a Bezout/SPI-shaped counting statement, no longer a classification. Its proof route likely shares the deep-link staircase's budget machinery (E33 pending).

## Attack surface

E32-extended census first; then the M5 chart machinery per observed class

## Falsifier

an unpaid identically-vanishing configuration class at toys (the census reports it directly)

## Conditional decomposition

This node is conditional on:

- `xr_profile_eliminant_nonvanishing`;
- `xr_coordinate_hypersurface_reduction`.

The latter is a proved algebraic reduction. The open content is profile
nonvanishing.

## Ledger (migrated notes)

E32-MERGED VERDICT (17/17, replayed green): NO identically-vanishing light profile exists at any checked row — the canonical normal-form matrix has full rank on every budget-meeting light profile (34/91/163 light profiles across three F_17 rows, representing ~4e11 triples by profile class). The profile-forced S9 scenario is REMOVED. Remaining sliver: coordinate-special vanishing (vanishing at special point choices within a full-rank profile) — a much smaller target, E32-coordinate refinement queued. BONUS CRITERION: sigma >= 3A - n always, so rows with 3A > n + 2k have EMPTY light regime (E27's toy corridor row is one — its triples are all heavy/boundary); prize rows do have light regimes (3A < n + 2k there). | E32-COORD (#18, 7/7 replayed): ZERO coordinate-special eliminant vanishings across 382,200 exact toy placements — the sliver is EMPTY in practice; the hypersurface-rationing statement is safe-side slack at toys. Combined with the profile-level emptiness (E32-MERGED), beta-3b's structured branch is empty at every level censused.
