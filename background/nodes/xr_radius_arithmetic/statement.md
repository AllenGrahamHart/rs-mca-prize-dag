# xr_radius_arithmetic

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_2_displacement_spectral.md#2']

## Statement

FULL VERDICT (wave 1, 215/215 checks — CORRECTING the premature 's*=1' reading): s* = 1 NEVER closes a corridor row. Under the pinned-ledger two-regime model every corridor edge needs full reach s* = t*-1 (~8.6e9 exchange steps at rate-1/2 prize scale, ~n*2^-8); Chebyshev-strict reads identically; even the generous three-regime scenario needs s* ~ t*/15 at prize scale. THE RESIDUAL-LEDGER CONVERSION PATH IS HARD, localized to the mid band s in (t/15, t-1]. Structural facts that survive: the distinct-slope plateau = E[X]^2 exactly (Vandermonde); s=1 dominates the head; a second bulk peak (~j(n-j)/n) rides the plateau at a q^-1 discount. MITIGATIONS: the A=265 stripped exemplar needs only s* = 4 (small-t partial XR = what P2 needs); at rates 1/4, 1/8, 1/16 the corridor edges have E[X] < 1 (moment-level Markov-trivial) — THE CONTENTFUL ROWS ARE RATE 1/2 ONLY; the n^3-budget and plateau-absorption mechanisms hand off with ~3 bits of margin at the rate-1/2 edge (the arithmetic shadow of E[X] ~ B*).

## Ledger (migrated notes)

UNBLOCKED: c(s,t) = min(s,t-1) pinned — QX.14 is RUNNABLE NOW. Ledger reach resolved in principle: s_L = t-1 (full linear reach to the independence plateau); QX.14 determines the much smaller s* the coverage actually needs. | Ball profile N_s = C(j,s)C(n-j,s) proved + exhaustively verified; bulk peak formula verified exactly.

## Addendum (2026-08-06, mint-4, round-17 t_naming)

1. t* (= A - k at the corridor edge) is the SAME OBJECT as
   rate_half_cyclic_simple_pole_mca_floor's sigma* + 1 (sigma = A-k
   by (SP2); sigma* = t* - 1 exactly), and the superseding
   rotated-prefix contract proves the unsafe band 1 <= sigma <=
   2^34 - 1 — t* sits at 0.50017 of the proved-unsafe reach.
   Conflict of USE flagged to the maintainer; formal
   predicate-compatibility unchecked.
2. THE SLIVER IS RETIRED (forced): {L : t*(L)·L >= n} is EMPTY for
   every L < 256 (dt*/dL = -3.36e7/bit); the L = 255.9 convention
   is re-labelled a representative evaluation point of an L-indexed
   family. NEVER cross-audit this node's (T*) balance against the
   F2 counting balance — they are different instantiations of one
   schema (UFMB) and comparisons manufacture phantom
   inconsistencies of size Delta = n - log2 C(n,n-k-t) - 128.
