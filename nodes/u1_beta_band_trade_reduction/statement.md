# u1_beta_band_trade_reduction

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/h1_u1_toy_harness.md']

## Statement

For h in (t+1, (log2 n)^2]: every family of > n^2 non-v1 canonical band trades (deg(L_P - L_Q) <= h-t-1) satisfies one of: (1) contains > n^2 minimal subtrades after bounded-tail deletion; (2) the moving pencil L_Q + f lies in a v1-chargeable pullback linear series; (3) already moment/PTE-charged. The correspondence route fails as-is (moving curves: psi_P, psi_Q vary per trade — curve-point theorems need fixed curves or a clustering statement).

## Attack surface

the linear-series view (bounded-degree pencils of divisors of X^n - delta with many totally-split members); or a difference/derivative step down in h; toy census of band trades at n = 64 calibrates which exit dominates

## Falsifier

a toy band-trade family avoiding all three exits (searchable with H1 machinery extended to h > t+1)

## Ledger

P-B CENSUS (#29, 93/93): PASS — no toy family avoids the three exits; every canonical dihedral-orbit representative routed. B's three-exit structure is confirmed observed structure; the proof should follow the census's routing table. | B-WRITEUP (#37): exits 1 and 2 REDUCE FORMALLY (proved reductions); exit 3 is EXACTLY the X-10 residue (anchored_nontoral_pte_bound + the defect/tails wrapper). B collapses into the final estimate — status CONDITIONAL on it. THE CONVERGENCE COMPLETES: A, B, both active-shadow bounds, and the tails wrapper are now all faces of A_h^nt.
