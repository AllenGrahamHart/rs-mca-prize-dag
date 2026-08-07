# lattice_cone_certificate

- **status:** CONDITIONAL
- **closure:** proved implication
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For a knife-edge row's specific p: a printed lattice certificate (dual/transference bound restricted to the sparse ternary cone, or exhaustion over reduced bases) proving K_p contains no ternary vector of support <= 2l' beyond the cyclotomic relations — certifying FULL injectivity in one per-row computation. Replaces the generator-design existence question as certified_valueset_lower's primary route; fits the repo's certificate grammar (the knife-edge certificate becomes a lattice certificate).

## Attack surface

DECOMPOSED: multiplier lemma (elementary) -> weight-graded MITM (provable radius extension 7 -> ~12 swaps per row) -> k-multiplier reduction (GV-favorable at k ~ 10) -> integer_code_distance_cert (the residue: one small explicit matrix per row). E24's BKZ hunt is the search-side complement throughout.

## Falsifier

BKZ finding a sparse ternary kernel vector = an actual collision = the collided branch is REAL at that cell (a zone-(b) verdict, not a route failure)

## Ledger (migrated notes)

The proof-logging certifier now aligns with the prize's own formal-verification-encouraged criterion — not just convenient, textually favored. | C-4 (#217): the toy pipeline VALIDATED — direct mod-p MITM and the exact B&B totality anchor agree exactly (288 antipodal cyclotomic relations, zero non-cyclotomic at N'=16, p=12289, w<=6); corrected N'=128 MITM costs: w=12 at 2^38.3, w=14 at 2^43.5, w=16 at 2^48.4. The Reading-B anchor works end to end at toy scale.

## Round-22 addendum (2026-08-07, coordinator-applied on replay): the C-4 anchor generalized to a congruence class; a full-radius scope catch; the per-row pricing corrected by ~20 orders

- **C-4 REPLAYED AND GENERALIZED.** The banked anchor (288 antipodal
  cyclotomic relations, zero non-cyclotomic at N' = 16, p = 12289,
  w <= 6) reproduced exactly (576 = 288 up to sign, 0
  non-cyclotomic). Because the fold reduction makes the bad-prime
  set EXACT (p bad iff p | Norm(w) for a box vector w within the l1
  radius), the verdict holds for EVERY p = 1 mod 16 above
  TIGHTEMPTY(16, 6) = 4049 — a congruence-class theorem, not a
  pinned-prime exemplar. At full radius the universal threshold is
  TIGHTEMPTY(16, 16) = 463249, attained (witness printed;
  PROVED-exhaustive).
- **SCOPE CATCH on the anchor**: at the SAME prime p = 12289 but
  FULL radius (2l' = 16) there are 6 non-cyclotomic kernel
  witnesses (e.g. w = (-1,-1,-2,-1,2,2,1,-1), Norm = 12289). No
  contradiction — C-4 declared w <= 6 — but the anchor does NOT
  extend to full radius; any consumer treating it as a full-radius
  exemplar is wrong.
- **PER-ROW PRICING CORRECTED (~20 orders).** The certification
  lattice is the FOLDED kernel lattice: dimension h = N'/2 (not
  N'), determinant p, target radius 2*sqrt(h). At N' = 128
  (dim 64, log2 p ~ 250): R/lambda1(GH) = 0.551 — the box sits
  strictly inside the shortest vector, and a complete Fincke-Pohst
  enumeration certifying emptiness costs 2^27.4 nodes with LLL
  alone (2^10.4 with BKZ-90), NOT the banked 2^188.2/memory-bound/
  Modal-scale figure (that model's weight-split is correct only
  below w = 28; the folded coordinate-split MITM alone is 2^74.3).
  Cost model validated against exhaustive brute force at h = 4, 8,
  where the enumerator decides BOTH directions at 10^3-10^4x
  speedup and every witness has Norm(w) = p exactly. Production
  spec (external tool, not installed here): fplll, basis
  (p,0,...,0) + (-zeta^j,...,1,...), BKZ-30, enumerate radius 16
  with per-coordinate box pruning |w_j| <= 2; certificate = empty
  enumeration transcript + reduced basis. The lambda1 > 16
  observation itself is banked prior art
  (e1_folded_no_vector_certificate_256_payload/PRO_W3, which also
  correctly forbids the N' = 256/dim-128 attempt: there
  R/lambda1 = 2.135 and witnesses are expected). What is new is
  the PRICE, and the resulting reclassification: per-row GE-WEAK
  certification at N' = 128 is laptop-scale, not Modal-scale.
- The genuine residue is UNIVERSALITY: bad primes exist right up
  to the threshold with no gap (536 bad primes at N' = 16, largest
  = the threshold), and there is no hidden finite registry of
  official rows. Cheap per row; unbounded in rows.
Source: notes/pilots_20260807/ge_floor_falsifier/ (d3_kernel.py,
d4_cone.py, d4_price.py — all coordinator-replayed).

## Round-23 corrections + results (2026-08-07, coordinator-applied on replay: ge_lattice_cert CATCH-23A)

**CATCH-23A — the round-22 enumerator was not fail-closed.** The
round-22 d4_cone.py per-level half-width used an integer floor of a
rational window, truncating valid points. VERDICTS SURVIVE (all
EMPTY cells confirmed empty by exhaustive brute force AND complete
corrected enumeration), but three banked witness COUNTS are
superseded: (h=4, p=137): 2 -> **8**; (h=8, p=12289, full radius):
6 -> **16**; (h=8, p=463249): 2 -> **16**. Structural confirmation
independent of recomputation: Lambda_p is an ideal, so witness sets
are single full <sigma, -1>-orbits of size exactly 2h — round-22's
partial sets were not sigma-closed, hence detectably incomplete.
The "6 witnesses at full radius" figure in the round-22 addendum
above is superseded accordingly (the SCOPE of that catch — the
anchor does not extend to full radius — stands, more strongly).

**E1-128 CERTIFIED EMPTY (the first complete transcript).** At the
literal pinned Pocklington field and displayed 128th root
(e1_folded_no_vector_certificate_128_payload, now PROVED):
complete Fincke-Pohst enumeration, 2,061,127,954 nodes, 12/12
shards byte-identical basis, deterministic standalone checker +
seed-reproducible planted fail-closed control at the same
dimension/determinant. Certificate banked on that node.

**PRICE-CLIFF — the round-22 reclassification scoped.** "Laptop-
scale per row at N' = 128" holds only above ~242 bits with LLL
(FPPRICE crosses 2^30 at log2 p = 241.8): TRUE at the 249-bit
exhibit prime (measured 2^30.94), FALSE at the four DEPLOYED Proth
prize rows (167-171 bits), where the same cell costs 2^60-2^63
with LLL and 2^38-2^40 with BKZ-90. Those four rows are instead
certified to support <= 24 (radius-graded complete enumerations,
2^25-2^30 nodes each — 12 swaps, the radius named in this node's
own MITM line; the archimedean-free radius there is only L = 6);
full radius UNRESOLVED and priced.

**GS-FLOOR OBSTRUCTION (proved).** The cheapest conceivable
certificate lambda_1 >= min ||b*_i|| requires p > (2 sqrt h)^h =
(4h)^{h/2} — EXACTLY the AM-GM norm ceiling, which at h = 64
equals 2^256 = the spec's own field cap. Hence NO admissible
N' = 128 prize row admits a Gram-Schmidt/lambda_1-floor
certificate for ANY basis; reduction can cheapen the enumeration
but can never replace it. (The PROVED 253^32 branch beats the
ceiling by 0.544 bits — that sliver is the entire free region.)
Source: notes/pilots_20260807/ge_lattice_cert/ (catch adjudicated
by exhaustive brute force; all gates coordinator-replayed).
