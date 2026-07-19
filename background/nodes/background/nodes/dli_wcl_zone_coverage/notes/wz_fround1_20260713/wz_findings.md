# wz_findings.md — F-round 1 catches and structural findings

- **wz-C1 (predicate quantization / emptiness equivalence).** At the
  official aspect N_L=256L the minimum nonzero W_cl contribution is one
  orbit at w=L+5: `2*256L*2^-(L+5) = 16L/2^L`, and `16L/2^L <= 1/32` iff
  `2^L >= 512L` iff `L >= 13`. So WCL-ZONE at official levels L=1..12 is
  EQUIVALENT to "the primitive window ledger is EMPTY", i.e. exactly the
  per-row low-weight-vanisher absence that `A1_PROD_NORM_SIEVE.md` says
  cannot be certified by exhaustive search at production scale. The 1/32
  threshold only begins to price actual ledger mass at L >= 13 (at L=34 it
  tolerates ~10^6 w=39 orbits). Any proof strategy therefore splits into an
  emptiness certificate (L <= 12) and a counting certificate (L >= 13);
  the node statement conceals this dichotomy. Analogue rows at our aspects
  are quantized the same way (min mass 1/2), so the emptiness event is the
  scale-invariant observable — pre-registered and used as such.
- **wz-C2 (no reference implementation for the pose's de-duplication).**
  No repo script computes W_cl "after ... first-owner de-duplication of
  multiplier shadows and level lifts": the banked M2 ledger counts shadow
  orbits whenever they are primitive (M2 script has only signed-shift +
  primitivity), the round-7 solver exists only as a 4-orbit one-off, and
  the lift identity exists only as a census check. This round froze an
  operationalization (wz_falsifiers.md section 0.7-0.8, round-7 solver +
  census lift identity + (weight, key-lex) first-owner order). The
  convention is MATERIAL: shadow-dedup changed W_cl by up to 4x in band
  cells (4 -> 1 at q=2107073) and 221 links fired in band A/b17 alone.
  Before any WCL certificate work, the node needs a canonical dedup spec,
  or censuses will not be comparable (house catch #137 class).
- **wz-C3 (2-power analogue towers cannot see the forced-family
  channel).** For n' in {64,128}, z^N+1 = Phi_2N(z) is irreducible, so no
  fixed integer relation vanishes at more than finitely many primes:
  strictly q-independent forced orbit families are algebraically
  impossible in every cell of this round. The official tower has n'_L =
  512L with odd part odd(L), where the channel is a priori live. Pre-hoc
  mini-result recorded in the pre-registration: PURE odd-cyclotomic
  subgroup-sum relations (folded d-term progressions, d odd, d | n'_L) are
  excluded at every official level, because window membership forces
  d <= L+5, survival of levels l=1..L forces d > 2L-1 (the relation dies
  at 2l-1 = d), and d | 512L with d odd forces d | L, contradiction.
  COMPOSITE forced constructions remain unprobed; round 2 should add
  odd-n' analogue cells (n'=96, 192) where forced families can exist.
- **wz-C4 (L=2 excess over the independence null, monotone but below
  trip).** Family B rho = 1.62 -> 2.40 -> 4.65 and rho_W = 1.69 -> 3.10 ->
  3.97 across b10/b12/b14, monotone increasing, top/bottom 2.88 (< 4) with
  1 nonempty top-band prime (< 3 required): no kill, but this is the only
  family running persistently ABOVE the q^-2 volume null with an upward
  trend. Candidate mechanisms: genuine level-1/level-2 correlation (cf.
  the banked f2/f2b level-correlation studies in the same notes folder) or
  small-sample noise. Round 2's primary quantitative question: does rho(B)
  stabilize (correlation constant => harmless O(1) factor, official
  prediction still ~2^-500) or grow with q (would extrapolate against
  WCL-ZONE at L=2..12 emptiness levels)?
- **wz-C5 (vacuous validation cell caught and replaced).** The
  pre-registered N=64 engine cross-check at b=25 returned direct == mitm
  on EMPTY sets — orbit clustering makes P(zero hits) ~ exp(-lambda_orb)
  ~ 0.94 despite lambda_vanisher ~ 3.8, so the cell had no validation
  power. Re-sited at b=21 (q=2100097) where it matched on a nonempty
  census (64 signed hits, 1 orbit). Corollary to #137: nonemptiness
  guards must cover VALIDATION cells, not only target censuses; Poisson
  design of controls must be done on orbits, not on signed vectors.
- **wz-C6 (accident primes recur across levels, not across primes).** The
  M2 accident row q=7937 reappeared in the L=2 band sample (b12) as its
  band's largest cell (W_cl = 2 -> 1 after 4 shadow links) — accident
  structure at a prime spans levels via multiplier webs, supporting the
  first-owner design. Across primes: 673 distinct orbit keys, zero
  recurring at even 2 primes — consistent with wz-C3's impossibility and
  the Poisson picture.
- **wz-C7 (volume law confirmed; quantization confirmed empirically).**
  At L=1 the exceptional-fraction null is matched within NK-v wobble at
  both tower widths (A: rho 1.03-1.36 with top band at 1.06; C: 1.00,
  0.99, 1.12, 2.19 with the top Poisson-consistent), spanning q from 2^17
  to 2^27. In all 264 band cells, W_cl > 1/32 iff the ledger is nonempty
  — the quantization equivalence of wz-C1 observed with zero exceptions.
- **wz-C8 (dedup composition order unpinned).** For C cells this round
  reports shadow-dedup and lift-dedup W_cl separately (kill lines use
  nonemptiness, invariant under shadow-dedup; lift-dedup applied for
  emptiness). The pose does not specify the composition/priority of the
  two dedup passes when both apply to one orbit; at official scale this
  changes W_cl values (not emptiness). Should be fixed in the canonical
  spec of wz-C2.
