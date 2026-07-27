# fm1

- **status:** see dag.json (single source of truth; dag status PROVED)
- **closure:** proof
- **statement provenance:** written 2026-07-27 during the empty-statement remediation; see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md

## Statement

FM1 — THE FIRST-MOMENT ALIGNMENT COUNT (exact). Fix a support R of size j and write S = H \ R; the RS restriction to S has dimension k with |S| = k + t, so the quotient syndrome space has dimension t. For a received pair (u,v) with syndromes U,V in F^t of u|_S, v|_S, the support R is aligned at a finite slope z exactly when U + z V = 0 with V != 0 (the excluded V = 0 case is the standard all-slope/paid-fiber degeneracy and is not counted in this column). Counting q^t - 1 nonzero V and q choices U = -z V gives alignment probability q(q^t - 1)/q^(2t) = (1 - q^(-t)) q^(1-t), so by linearity of expectation over the binom(n,j) supports: E[#aligned] = binom(n,j) (1 - q^(-t)) q^(1-t). [statement written 2026-07-27 from this node's own proof.md]
