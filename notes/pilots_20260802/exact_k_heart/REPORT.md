# Pilot report: the exact-k (d=0) heart of P-A1 (Opus 5, 2026-08-02)

Coordinator note: condensed persistence of the subagent's report (full
detail in the stage JSONs); audit in FABLE_AUDIT.md. 2140 machine
checks, 0 failures; stage10 (1662) coordinator-replayed.

## VERDICT: the per-ray framework TRANSFERS — a LINEAR ceiling at d=0.

**THEOREM (d=0 ceiling).** Peel a post-strip live family F = P u K
(Theorem D0-2); then rank(F) = h.|P| + rank(K) and (Theorem D0-3)
rank <= 2(|U|-k)-1 <= 2R-1, hence |P| <= (2R-1)/h = 307/358/639
(RowC) / **383/447/959 (prize)** and P-A1(d=0) <= (2R-1)/h + |K|.
Margins vs 8n^3: 23.7-24.7 bits (RowC), 116-117 bits (prize).
The three prize integers COINCIDE with the band sunflower law — the
extremum is exactly two maximal sunflowers (factor 2 of the banked
d-adaptive cap, which is achieved exactly, T1-calibrated).

**The two new unconditional lemmas** (the d=0 replacements for the
band's core rows, which VANISH at d=0 — dim C_Z = 0):
- **D0-2 PEELING**: a ray with >= h points of family-coverage <= 2
  contributes 0 to every relation (Vandermonde on <= 2 slopes; r_a
  has >= h roots) — rank = h + rank(rest); confluent; terminates on
  the un-peelable core (every ray: >= k+1 points covered >= 3x).
  Verified 964/964.
- **D0-3 LOCALITY + DEATH**: rank <= 2(|U|-k), and EQUALITY kills the
  family (u,v become codewords on U — P2 strips every ray). Proved
  one direction; the converse empirical 42/42 vs 0/23. Verified
  349/349.

**Structure at d=0 vs the band**: core rows empty; no arithmetic
filter on cores (every k-set interpolates); exclusivity fails (one
support serves C(A,k) cores); pairwise transversality FREE
(C_{S^S'} = 0 — the contrapositive of Theorem G: zero pairwise rank
sharing; every deficit is >= 4-wise). The relation module = the
F5-OS live-syzygy object in locator normal form: support 2 dies
SHARPLY (lcm degree exactly R), support 3 in one line.

**The co-sunflower (the d=0 K_V): built, priced, KILLED EXACTLY.**
m disjoint h-subsets of a (k+2h)-union: a clique of C(m,2) exact-k
cores, rank = min(mh, 4h) — at m >= 4 rank hits the full redundancy
and D0-3 fires: 0/96 admissible (m <= 3: fine). Clustering confers
NO advantage (scale-invariance: a cluster is a d=0 problem on the
shortened row, same formula). Coset/orbit supports BARRED by BP(2)'s
parity (h odd at all six rows; BP(1) vacuous at d=0 — it is the
PARITY that works here).

**Growth law**: max Gamma_0 = 0.5000n - 1.000 EXACTLY = the ceiling,
at 15 points across two regimes incl. the structural regime
(q to 7.5e8, noise 2^-6); ceiling+1 dead 78/78.

**The moment route is strictly the wrong currency (quantified)**: the
T1 identity specialises exactly (349/349), but the extremum has
M_0 ~ Gamma^2/4 — the moment is quadratically larger than the target;
the ray route bounds Gamma directly. The banked non-claim is now a
theorem-grade statement with the loss = Gamma/2.

**The structural invariant**: dim W(F) = R - g, g = n - |union S| —
THE UNION SIZE. dim W >= 2h always (the sharp support-2 kill);
minimal dim W = 2h characterises the co-sunflower = the fatal
configuration; clustering is scale-invariant.

**F3 — the exact blindness threshold**: faithful <=> (h-1) log2 q >
log2 C(n,A). Official rows: noise stratum EMPTY (2^-147 to 2^-9e11) —
every official live ray is structural. Toys at n = 18-20 sat at
2^+5-6 and produced the one observed ceiling violation (4.2x —
coincidence rays, provably absent officially). Faithful noise +
exhaustive scanning are MUTUALLY EXCLUSIVE beyond n ~ 24 — the wall
is structural, not compute.

**RESIDUAL (sharper than the band's)**: |K| — un-peelable live
families, an explicit covering-design condition (>= k+1 points
covered >= 3x per ray) replacing the algebraic support-4 condition.
No bound proved on |K|; official-shaped random hunts found 0 rank
deficits in 600 trials and every un-peelable design was full-rank.

**Caveats**: ceiling conditional on peelability (noise-regime
violations observed at toy scale, provably empty officially); death
law an iff only empirically; gate limit above n ~ 24 as in all band
pilots; Deza cited not verified; the ray-condition rank is NOT the
frontier's affine error rank sigma (dual-side; no bridge proved —
do not compare numbers); the collapsed-face catch re-confirmed from
the d=0 side (|Z^Z'| >= 2k-A = k-h).
