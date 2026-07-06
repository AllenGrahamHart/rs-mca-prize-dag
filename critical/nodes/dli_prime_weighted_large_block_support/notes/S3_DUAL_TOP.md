# S3: the dual-top attack executed and killed — toward the dual-top emptiness lemma
# (round S3, self-tennis, 2026-07-07; Modal run s3_dual_geometric_modal.py,
#  exact local kill-mechanism check inline below)

## 1. REFUTE CHAIR: the dual-geometric attack (designed, executed, FAILED)

Attack design: DYADIC-K's second hypothesis (dual-top emptiness: no λ with
T(λ) ≥ 2^−j₁) should fail at rows whose embedding has a geometrically small
orbit — ω = 2 with q | Φ_{n′}(2) makes u_y = λ·2^y mod q small for 2-adic λ,
so T(λ) should be macroscopic where the iid model predicts none. Toy
instance: q = 6700417 (large factor of F5 = 2^32+1), n′ = 64, ord(2) = 64
exactly.

Modal measurement (full λ-scans, three rows):
| row | E | max_λ T | near-peak spectrum |
|---|---|---|---|
| GEO ω=2 (q=6700417) | 1.000000 | 2^−64.0 | EMPTY to j = 32 |
| GEO pinned (same q) | 1.000000 | 2^−64.0 | EMPTY to j = 32 |
| CTRL pinned (q=6700609) | 1.001332 | 2^−17.0 | iid-consistent, orbit-quantized |

The attack row is FLATTER than a random control. The attack fails, for two
exact reasons that generalize into a proof:

**(K1) The order condition assassinates base 2.** ord(ω) = n′ = 2N means
ω^N ≡ −1, so for ω = 2: 2^{N−1} ≡ −2^{−1} ≡ (q−1)/2 (mod q) — the EXACT
cosine dead-zone. Verified exactly: at y = 31 the signed residue is
−3350208 = −(q−1)/2, fraction 0.5000, contributing −44.05 of T(1)'s
log2 = −64.0. Every 2-adic λ = ±2^k has some coordinate with exponent
N−1, hence hits the same dead-zone: the entire geometric family is killed
identically, not probabilistically.

**(K2) Coverage kills every other base.** A base-b orbit is small only for
y ≤ log_b(q); the remaining N − log_b(q) coordinates wrap pseudo-randomly
at ~2 bits each. At balanced rows (q ≈ 2^N): base 2 covers all N (then K1
kills it); base b ≥ 3 covers N/log2(b) ≤ 63% (≥ 0.74N bits lost — dead);
rational ratios b/c ∈ (1,2) need λ ≥ c^{N−1} ≥ q (dead). At UNBALANCED rows
(q ≪ 2^N) the wrap region is even larger — the toy measurement is this.

## 2. PROVER CHAIR: the transference/classification route (proof program)

**Lemma A (proved sketch — determinant transference).** If λ has ALL
‖λω^y/q‖ ≤ ε with ε < (2q)^{−1/2}, then the 2×2 determinants
u_y u_{y+2} − u_{y+1}² ≡ 0 (mod q) and |·| ≤ 2ε²q² < q force EXACT
vanishing: u_{y+1}/u_y is a constant rational b/c with |b|,|c| ≤ 2εq,
i.e. ω ≡ b·c^{−1} (mod q) — the peak is GEOMETRIC.

**Lemma B (the kill, from §1).** Geometric peaks die at balanced rows:
b = 2 by the forced −1/2 dead-zone (K1: cos² ≤ sin²(π/2q) ≈ q^{−2}, i.e.
~2·log2 q ≈ 510 bits at production); b ≥ 3 and rational ratios by coverage
(K2). Hence NO uniform-small dual peak exists at balanced admissible rows.

**Remaining case (the honest gap): mixed peaks.** A peak T ≥ 2^−j₁ with
some large coordinates: ≥ N − j₁/2 coordinates must still be ε-small, so by
pigeonhole there are runs of ≥ (N − j₁/2)/(j₁/2 + 1) consecutive small
coordinates; Lemma A applies WITHIN a run (local geometricity), and the
order condition + coverage must then be run-localized. This is a real but
bounded piece of work — constants and the run-gluing argument. STATUS:
dual-top emptiness at balanced rows is now a PROOF PROGRAM (Lemmas A + B
done at sketch level with the exact kill verified; mixed-case gluing open),
no longer a bare hypothesis.

## 3. Production check: the Fermat escape is factually closed

Even ignoring K1: a balanced base-2 row at production n′ = 512 would need a
prime q ∈ (2^255, 2^256] dividing Φ_512(2) = 2^256 + 1 = F8. F8's complete
factorization is known (1238926361552897 × p62, p62 ≈ 2^206): NO factor is
in the band. The base-2 geometric row does not exist at production scale
even before the dead-zone kills it.

## 4. What S3 changes

- DYADIC-K's structure after S3: bulk (j ≥ j₁) = kernel counting via
  moment transfer (S2), with the S1 norm-sieve covering its sieve zone;
  top (j < j₁) = Lemmas A/B + mixed-case gluing — a PROVABLE lemma target,
  not a new assumption. The node's irreducible core continues to shrink
  toward: bounded-alphabet kernel counting in the sieve-uncovered zone.
- Attack ledger for the self-adversary: the dual side now has the same
  shape as the primal (round 5): the only mechanism is exact algebraic
  structure (geometric/rational), and it is classified and killed. Next
  attack surface: mixed-run peaks (engineer λ with a long small-run at a
  non-geometric ω?) — Lemma A says a long run IS locally geometric, so the
  attack needs SHORT runs + many of them ⟹ j₁ large ⟹ back in the bulk.
  The dual surface looks closed modulo the gluing constants.

Verifier artifacts: s3_dual_geometric_modal.py (Modal, 21 shards, all
< 10 s); exact kill-mechanism check (T(1) = 2^−64.0 with the y=31
coordinate at fraction 0.5000 contributing −44.05) reproduced inline in
the round log.
