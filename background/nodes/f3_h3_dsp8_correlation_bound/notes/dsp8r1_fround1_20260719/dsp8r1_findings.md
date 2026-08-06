# DSP8 F-round 1 — findings (catches dsp8r1-C1...)

- **dsp8r1-C1 (operational, self-caught)**: shard n2048_b was launched
  without an explicit `pmax` and the script's default fence (10^7)
  silently excluded its whole window (rows=0 printed — the summary line
  made the mistake visible immediately). Re-run clean as n2048_b2 with
  pmax=15000000. No data loss; lesson: the per-shard summary MUST print
  rows/last_m so empty shards cannot pass as coverage.

- **dsp8r1-C2 (structure, new exact datum — the TWIN LAW of near-rich
  rows)**: every maxP >= 19 row found anywhere in the round — official
  (8192, 67657729) and analogue (2048, 4360193), (2048, 4513793),
  (4096, 16801793) — has EXACTLY two rich targets, both antipodal-free,
  both P = 20, each fiber with 10 generic members and N_6^disj = 45 =
  C(10,2) (one fiber has 44): all or all-but-one generic pairs are
  support-disjoint. Two consequences: (i) the DSO1 overlap payment
  (O_6 <= 6) is inactive exactly where fibers are rich — the disjoint
  moment IS the whole distance-six moment there; (ii) rich targets
  arrive in pairs (plausibly a t <-> t' involution — worth a lemma
  hunt). Round-2 relevance: the disjointness filter cannot be relied on
  to thin rich fibers, and any P >= 25 accident should be expected to
  arrive as a twin.

- **dsp8r1-C3 (large-field thinning, expected but now measured)**: all
  fifteen high-p sample rows (n = 64/128/256, p ~ 1e11) have max_t P(t)
  = 2 — total collapse of fiber richness, consistent with the proved
  Parseval branch (P(t) >= 19 => p <= 6^{n/4}). Named NOT-kill (h) in the
  pre-registration; carries no extra evidence weight.

- **dsp8r1-C4 (row bookkeeping)**: 67657729 is the FIFTH official prime
  at n = 8192; the first four are 67239937, 67280897, 67411969, 67452929
  (maxP = 18, 18, 18, 16; all J_25 = 0). Consistent with the banked
  "first twelve rows X_35 = 0" claim; useful pin for future official-row
  fleets.

- **dsp8r1-C5 (exhaustive analogue corridor closure at n=32)**: the
  ENTIRE analogue corridor at n = 32 (all 7,937 primes p = 1 mod 32,
  1024 <= p <= 6^8 = 1679616) has max_{t!=1} P(t) = 10 < 25. DSP8 holds
  identically-vacuously at every n=32 analogue row — an exhaustive
  enumeration fact for the full corridor at that scale (evidence for the
  official predicate, not a promotion).

- **dsp8r1-C7 (maxP saturation at 20)**: the per-scale richness maximum
  is 10, 14, 14, 14, 18, 18, 20, 20, 20 for n = 32..8192 — monotone
  nondecreasing but apparently SATURATING at 20 = the banked wave-5
  maximum, across three consecutive scales including the official one.
  Combined with the paired-sweep bound P + 2R <= 37 (R >= 1 forced for
  contribution), the empirical frontier sits 5 units below the DSP8
  cutoff. A proved "P <= 24 at official aspect" satellite would close
  DSP8 outright (vacuously); its falsifier (any row, any t != 1 with
  P >= 21) is crisp and cheap to monitor in every future sweep.

- **dsp8r1-C8 (antipodal starvation)**: no antipodal-class target came
  anywhere near richness in 48,544 rows (class A was only ever seen at
  P <= ~6 in spot data; every P = 20 fiber is antipodal-free). The
  17-weighted J^A term of DSP8 has never once been nonzero at any
  cutoff >= 19 in measured data. The antipodal side of the inequality is
  completely untested — and possibly empty at official aspect (another
  candidate satellite lemma: antipodal targets cannot be cutoff-19
  rich).

- **dsp8r1-C6 (vacuity margin profile)**: across every scanned scale the
  best observed maxP stays in single/low-double digits (32: 10; 64: 14;
  128: 14; 256: 14; see results for 512..4096) while the retention
  cutoff is 25 and the pigeonhole cap is n-1. The gap between observed
  richness and the cutoff is what makes DSP8 vacuous at analogue scales;
  the only known non-vacuous pressure anywhere is sub-cutoff (P = 20)
  at n = 8192. Round-2 design should therefore either (i) hunt engineered
  rich primes via the collision-norm ideal machinery (the wave-12/13
  fixed-order lane) to build a non-vacuous test at cutoff 25, or
  (ii) pre-register a sharper sub-cutoff instrument (e.g. the exact
  distribution of J_19 across official rows) as the trend carrier, since
  J_25 currently cannot trend from zero.
