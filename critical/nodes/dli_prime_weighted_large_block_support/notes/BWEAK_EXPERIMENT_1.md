# B-WEAK falsification program — experiment 1: the joint scaling study
# (2026-07-07; bweak_joint_scaling_modal.py + hot-prime classification; VERDICT: NO REFUTATION SIGNAL)

Pre-registered target: sustained super-polylog per-junction growth of the
JOINT loss (exact nested-tower t-null counts, all conditions jointly)
across >= 3 q-scales at >= 2 depths, with structure routed through the
packet's exact accounting.

## Raw sweep (n = 32; ~35 exact Modal tower jobs)

- t=2: band ratios vs naive mean-field (coset column only subtracted):
  1.008, 1.087, 1.233, 4.39, 43.9 — an apparent strong growth trend.
- t=3: 1.29, 1.72, 0, 0. t=4: 0, 0, 0 (all deep sub-volume bands EMPTY —
  cleaner than mean-field).

## The apparent t=2 signal dissolves under exact structural routing

Per-prime decomposition: the large-q mass is carried by a MINORITY of hot
primes in orbit-quantized quanta (256-448), the rest sit at ZERO.
Classification at q = 60289 (exhaustive local MITM): the 256 noncoset
objects = ONE primitive size-10 accident orbit (32 shifts) dressed by
symmetric differences with its 3 disjoint mu_4-cosets — predicted
histogram {10:1,14:3,18:3,22:1} x 32 = {32,96,96,32}, EXACTLY observed.
Not antipodal-closed, not dihedral (0/256 each): a generic primitive
accident with deterministic coset dressing.

The dressing is precisely the packet's QuotientStaircase column
(L_B(X)·G(X^M) locators = primitive part x coset factor): ONE q^-t
coincidence is counted 2^d x (shift orbit) times in the raw census. The
naive mean-field baseline treats each subset independently and therefore
UNDERCOUNTS clustering by the dressing multiplier — the same
amplification phenomenon as the round-7 additive lattice clusters.
After routing the dressing: primitive-accident rate 0.2/prime observed vs
~0.4 Poisson-expected (sub-Poisson) at the deepest band; every t=3/t=4
sub-volume band literally empty.

## Verdict and what was learned

1. NO refutation signal under the pre-registered standard: the joint loss
   at every depth/scale is at or below the correctly-routed mean-field;
   the trend was an artifact of subtracting only 1 of the packet's
   structural columns.
2. The experiment independently VALIDATES the x4 four-column design from
   the joint side: the exact objects that inflate raw counts are exactly
   the column structures the split charges (quotient-staircase dressing
   observed in the wild; dihedral column empty here — 0/256).
3. Methodological: the pre-registration's exact-routing clause did its
   job — a naive baseline manufactures a 43.9x false signal at the first
   band where dressing quanta dominate mean-field. Any future claimed
   trend must classify its hot population first.
4. Depth note: t >= 5 towers at n = 32 are born sub-volume at the
   smallest admissible prime (no informative range) — deeper joint tests
   need n = 64 machinery (2^32 masks: needs a sharded MITM redesign;
   queued as experiment 2 if wanted).

B-WEAK survival ledger: +1 (first direct joint attack, designed to hit
the F-round's most threatening trend, absorbed with the mechanism
identified and priced).
