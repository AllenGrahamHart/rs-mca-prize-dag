# DRAFT node statement — `tern_master_threshold` (NOT MINTED)

**DRAFT ONLY.** Written by the round-19 Opus pilot in
`notes/pilots_20260806/tern_master_statement/`. The coordinator mints; this
file proposes text and nothing else. No `dag.json` or node shard was touched.

- **proposed id:** `tern_master_threshold`
- **proposed status:** PROVED (the master object, the spine, and the
  threshold; every open question named below is a stated residual, NOT a
  claim)
- **proposed closure:** proof
- **provenance:** `notes/pilots_20260806/tern_master_statement/`
  (92,263 checks, 0 FAIL, fail-closed proven), subtraction-swept against all
  five surfaces with the sibling `tern_unification_adversary/` unread.

---

## Statement

THE TERNARY RELATION MODULE `T(P, Lambda)` AS THE COMMON OBJECT OF THE THREE
ROUND-18 INSTANCES, AND THEOREM MT: THEIR THREE THRESHOLDS ARE ONE
INEQUALITY.

**THE OBJECT.** `T(P, Lambda) := {eps in {0,±1}^M : sum_j eps_j theta_j^l = 0
for all l in Lambda}`, `P = (theta_j) in (F_{p^d}^*)^M`. The target is a
PARAMETER `omega` (existence / count / weighted mass), never a conflation —
round-18 CATCH-Z1 proves the forms come apart.

**PROPOSITION HS.** For `P` the half-system `(xi^j)_{j<h}` of `mu_n`,
`n = 2h`, and `Lambda ⊆ (Z/n)^*`: `T(P,Lambda) = T(P,Lambda^*)` with
`Lambda^* = <p>Lambda`, and `T` is exactly the set of ternary words of the
negacyclic `F_p`-code of length `h` with defining set `Lambda^*`, of
codimension `g = |Lambda^*|`.

**THE DICTIONARIES (exact).** I1 `f2_z1_mass_knife_edge` = `(h = S =
2^{e_p-1}, Lambda = {1,3,..,2R-1}, g = R, omega = 2^{-U})`; I2
`crossing_dsa_refutation` deep stratum = `(h = L = n/w, Lambda = {1},
g = delta_a, omega = C(L-U,(r'_a-U)/2))`; I3
`es_ternary_suppression_instruments` = `(h = n/2, Lambda = odd s in [1,w-1],
g = |Z_w^odd|, omega = 2^{h-U})`. **Two honest qualifications:** I2's
EXISTENCE reading does NOT specialize (its parity/support side conditions are
not conditions on `T`; only the mass reading does), and I3 specializes only
onto its ODD-condition sub-object — the even conditions are a different
instance at half length over the alphabet `{0,1,2}` (LEMMA OE), which is
CATCH E-2's self-similarity with the recursion named.

**THEOREM MT (the master threshold).** For `P` a half-system,
`Lambda ⊆ (Z/n)^*`, `g = |Lambda^*|`, `h = n/2`, the single quantity
`g·log2 p` versus `h` governs `T`:
(a) `g·log2 p < h` `=>` `T != {0}` and `|T| >= 2^h/p^g` (Z-FLOOR-M);
(b) `g = h` `=>` `T = {0}` (SP-COVER-M);
(c) `T != {0}` `=>` every nonzero `eps` has `wt >= p^{2g/h}` (CS4-M).
**COROLLARY MX:** in regime (a), (c) yields only `wt < 4` — the norm
mechanism and the pigeonhole mechanism are NEVER simultaneously informative.

**THE THREE INSTANCES ARE ONE INEQUALITY (the unification's payoff).**
I1: `h - g log2 p = -46.0249` bits at `R = 4,294,967,340` and `+17.9751` at
`R = 4,294,967,339` — the banked knife edge reproduced to four decimals from
the master threshold alone, and I1's saturation `R/S = 1/log2 p` says exactly
that the F2 object sits ON the threshold. I2: `h/g = n/w = L` at the deep
stratum, against DSA's `p^{delta_a} < 2^{L-2}` — the same inequality to
within 2, at all six `w`. I3: stratum 0 has `h/g = n/w = L`, the SAME number
as the deep stratum. The banked four-face seam (`f2_o1_status_split`) is
F2-internal; MT adds two further lanes.

**THEOREM CS-M.** CS reads VERBATIM over `T(P,Lambda)` for every
Frobenius-stable `Lambda ⊆ (Z/n)^*`, with `|Z_w^odd| -> |Lambda^*|` and
`(r' - a_{n/2}(S)) -> wt(eps)`: `p^{|Lambda^*|} | |N(X)|`,
`|N(X)|^2 <= wt(eps)^h`, `|Lambda^*| log2 p <= (h/2) log2 wt(eps)`. NO window
or consecutivity hypothesis is needed; the three real hypotheses are that `P`
is a half-system (used twice), that `Lambda` consists of units (even `l` have
no `sigma_l` — they are the next stratum), and that `n` is a 2-power. The
archimedean half is the BANKED `dli_c1_ternary_relation_norm_sandwich` Claim
2, cited not claimed. **LEMMA BR** (the hinge): `r' - a_{n/2}(S) = wt(A-B)`
exactly — CS2's archimedean quantity IS the ternary support size.

**THEOREM CZ-M.** In char 0, on the half-system of `mu_n` with one unit in
`Lambda`, `T` = the ternary vectors of the lattice `Phi_n·Z[X]_{<N-phi(n)}`;
`T = {0}` iff `N = phi(n)` iff `n` is a 2-power, for ALL integer coefficients.
This is the exact master form of CATCH-Z6's grid rule, with a closed count:
`3^{N-phi(n)} - 1` in the three banked cases (8 / 8 / 80, reproduced exactly).

**THEOREM Z-FLOOR-M and its exact scope.** The collision floor holds for ANY
finite `X ⊆ Z^M` and ANY map: `sum_s |fibre|^2 >= |X|^2/|image|`. With
`X = {0,..,k-1}^M` it floors the mass whose weight is the DIFFERENCE
MULTIPLICITY `prod_j(k-|eps_j|)`; the ternary case is `k = 2`. It is
alphabet-agnostic in exactly that sense and NOT weight-agnostic: it says
nothing about I2's constant-weight crossing weight.

**THEOREM I3-FORCE (the transfer that pays).** If `|Z_w^odd| log2 p < n/2`
then `C_odd(n,p,w)` contains a nonzero ternary vector, hence a `strat = 0`
set satisfying every odd window condition; consequently SP-COVER and
SP-TERNARY — the whole odd-condition exclusion mechanism — **provably cannot
exclude** at that row. This is the first existence/forcing instrument on the
(ES) object, which had only exclusion instruments and a banked-dead Ax–Katz
route. At `n = 2^41, w = 2^34` it fires on every `delta = 1` admissible row
with `log2 p < 128` — the tower rows, never the `e = 1` rows (the banked
dichotomy). It STRENGTHENS CATCH E-3 from "SP-COVER is vacuous" to "SP-COVER
provably fails, on a named row set". **It is a no-go on a METHOD, not a
refutation:** it produces no bad set and does not touch `p | N(I_S)`.

**Verified:** 92,263 checks, 0 FAIL, exact integer/finite-field arithmetic,
fail-closed proven (injected-false stage exits 1). The banked exact ternary
censuses of `efloor_sparsity` (6560 / 16640 / 288 / 148224 and every 0) are
reproduced independently; CATCH-Z6's 8/8/80 are reproduced; the I1 knife-edge
constants are reproduced to four decimals.

## Falsifier

A cell with `g·log2 p < h` and an exact ternary count of 0 (kills MT(a) and
I3-FORCE); a nonzero ternary `eps` with `p^{|Lambda^*|}` not dividing `N(X)`
or with `N(X)^2 > wt(eps)^h` (kills CS-M); a nonzero ternary char-0 relation
on a 2-power half-system (kills CZ-M); a banked instance threshold that
disagrees with `g log2 p` vs `h`.

## NOT claimed

The one-framework object and the mass/census functional identity (BLIND-
CONVERGENT with the live sibling `tern_small_scale_laws`, whose PREREG
registers both — credited, not claimed); the AM-GM ternary ceiling (banked in
the DLI lane); Z-FLOOR, CS, LEMMA AB, LEMMA Z, the collision identity (all
banked). No open master question is closed: the I1 mass bound
`Z_1 <= 2^{o(m)}` at `k = e`, the I2/I3 mid-range primes, and CC-sparsity are
ALL untouched. I3's specialization is partial (odd conditions only). The
`delta > 1` rows at I3 and the `delta_a > 1` orbit refinement are not
covered. The transfers at §4.4 (SP-COVER at I1) and §4.5 (CS at I1) pay
NOTHING and are reported as zeros.

## Catches carried

**CATCH-T3 (a wrong constant of record).** `f2_sl1_powersums/PROOFS.md:271`
uses `|N(alpha)| <= w^{n/2}`; the banked sharp ceiling
(`dli_c1_ternary_relation_norm_sandwich/statement.md:27-28`) is
`w^{N/2}` with `N = n/2`, i.e. `w^{n/4}` — the SQUARE ROOT. The recorded
dead-route constant `w >= p^{2R/n} = 2.0000` should read `p^{4R/n} = 4.0000`,
which propagates into the minted `f2_z1_mass_knife_edge/statement.md:59-61`.
No verdict changes (the route is dead either way); the constant is wrong.
**CATCH-T4 (citation drift).** `z1_ternary_mass/PROOFS.md:56-59` and `:383`
cite the norm route as `f2_sl1_powersums/PROOFS.md:262-266`; it is at
`:271-274` (lines 262-266 are the Z-basis paragraph).
