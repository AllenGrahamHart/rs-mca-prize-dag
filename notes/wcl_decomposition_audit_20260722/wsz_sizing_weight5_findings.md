# wsz_findings.md — WCL slot-hardening items 4-5 (Burnside sizing + weight-5 subfamily algebra)

Repo: /home/u2470931/smooth-read-solomin/prize @ master 570f0067 (read-only).
Conventions: pinned by notes/wcl_decomposition_audit_20260722/wcl_audit_findings.md
(cell (ell,w) = antipodal-free w-subsets of Z_{512*ell}; dedup group = full affine
group x -> a*x+b, a odd, which contains the global sign b = 256*ell).
Scripts: wsz_sizing.py, wsz_weight5.py (this directory). Exact-integer Burnside;
all runs under tools/ramguard tiny unless noted.

## ITEM 4 — calibration (all three banked anchors reproduced EXACTLY)

Machinery selfcheck: exhaustive orbit enumeration vs Burnside at m=8,16,32
(9 cases) PASS; raw-count identities PASS; coset-descent orbit bijection
(all-even orbits at m == all orbits at m/2) verified exhaustively at
(16,3),(32,3),(32,5) PASS.

- (a) ell=1 anchors: raw 11,054,080 (w=3) and 1,398,341,120 (w=4) reproduced
  exactly from C(256,w)*2^(w-1). Burnside orbit counts: (1,3) = 254,
  (1,4) = 24,979 — both EQUAL the banked class counts. NOTE (reconciliation):
  the task note said "254 is norm-classes after further merging; your orbit
  count will sit between" — in fact the banked 254 IS the exact affine-Galois
  ORBIT count (weight5_orbit_route_fence.md + the weight-3 node's "exact orbit
  partition has 254 classes" both confirm; my machinery returns 254 exactly,
  no residual merging). Fence w=5: 2,296,920 and w=6: 185,569,028 also
  reproduced exactly.
- (a') weight-4 normalized-section anchor: 1,014,080 keys reproduced EXACTLY
  two independent ways (inclusion-exclusion and brute force) as: antipodal-free
  4-subsets of Z_512 containing 0 and at least one 2^v, 0 <= v <= 7
  (= C(255,3)*8 - sum_k C(8,k) C(247,3-k) 2^(3-k) = 21,849,080 - 20,835,000).
- (b) ell=2 pair space: legal pairs 521,220 and pair orbits under odd dilation
  1,514 reproduced exactly (independent Burnside over the 512 units; fixed
  pairs = pairs-of-fixed-points + clean 2-cycles with antipodal guards).
- (c) (2,7) Pilot B census 94,652,815: reproduced EXACTLY from the wclp
  router-candidate model, re-derived from scratch: W = {(Q,c)}, Q a legal
  4-subset of Z_1024, c in Z_1024 (complement-triple product exponent),
  H = (t,r) dilationsxscalings acting (Q,c)->(tQ+r, tc+3r); Burnside
  collapses to (1/512)*sum_{t odd} N_inv_4(t) (collapse re-proved: g|3r <=>
  g|r since 3 odd, and multiples of g = one translation-conjugacy class of r).
  Control (2,6): 404,740 reproduced. DELTA EXPLAINED: 94,652,815 is NOT the
  ambient (2,7) orbit count — it is the constraint-first router presentation
  space (selected 4-set + complement product; the 3 remaining roots are
  solved from the cubic, not enumerated). The ambient affine-Galois orbit
  count of (2,7) is 435,372,690,550 — 4,600x larger. Both are exact; they
  count different (both legitimate) census spaces.

## ITEM 4 — the sizing table (exact)

raw = reduced signed supports C(256*ell,w)*2^(w-1); orbits = affine-Galois
orbit count (Burnside, exact); rates: A = 0.698 s/row ((1,5)-style: one
Phi-norm + complete factorization per row; applies at ell=1 where the row
pipeline is a single resultant), B = 1.25 s/orbit ((2,7)-style gcd-heavy:
two recursive norms + gcd + saturation per orbit; applies at ell>=2).

| cell | raw signed supports | affine-Galois orbits | rate | CPU-h | CPU-y |
|---|---:|---:|---|---:|---:|
| (1,5) | 140,952,784,896 | 2,296,920 | A | 445 | 0.05 |
| (1,6) | 11,793,049,669,632 | 185,569,028 | A | 35,980 | 4.1 |
| (1,7) | 842,360,690,688,000 | 13,043,008,668 | A (floor) | 2,528,894 | 289 |
| (1,8) | 52,436,952,995,328,000 | 805,780,021,078 | A (floor) | 156,231,793 | 17,823 |
| (2,7) | 112,395,893,866,201,088 | 435,372,690,550 (ambient) / 94,652,815 (router) | B | 32,866 (router) | 3.7 |
| (2,8) | 14,189,981,600,607,887,360 | 54,536,209,281,493 (ambient) / 18,555,400,106 (router) | B | 6,442,847 (router) | 735 |
| (2,9) | 1,589,277,939,268,083,384,320 | 6,084,811,884,730,416 (ambient) / 3,084,343,642,846 (router) | B | 1,070,952,654 (router) | 122,171 |
| (4,9) | 843,074,503,247,756,347,572,224 | 807,072,005,426,817,050 | n/a | census infeasible | — |
| (4,10) | 171,144,124,159,294,538,557,161,472 | 163,521,797,841,818,171,390 | n/a | census infeasible | — |
| (4,11) | 31,552,753,072,277,211,290,356,678,656 | 30,118,932,580,535,131,797,260 | n/a | census infeasible | — |

Rate-class notes: (1,5) projection 445 CPU-h total is consistent with the
banked remaining-work quote (46.44% done, 1,230,232 rows x 0.698 s = 238
CPU-h remaining). (1,6)-(1,8) use rate A as a FLOOR: the norm bound grows
w^256 (2^594 at w=5 -> 2^768 at w=8), so complete-factorization cost per row
grows; treat 36k / 2.5M / 156M CPU-h as lower bounds. (2,7) router x 1.25 s
= 32,866 CPU-h reproduces the banked 33,000-39,000 quote. (2,8)/(2,9)
router spaces grow ~x196 and ~x166 per weight step: even constraint-first,
(2,8) is ~735 CPU-years — out of reach without new algebra.

Constraint-first assessment: see final report section (router = 4,600x
reduction at (2,7); (4,w) cells have banked fixed-divisor descents that
collapse the census to <=5-variable ideal certificates — the ONLY viable
route at 8.1e17-3.0e22 ambient orbits).

## ITEM 5 — weight-5 subfamily exclusion algebra at ell=1

Machinery selfcheck (wsz_weight5.py selfcheck, all PASS): recursive 2-power
norm vs sympy resultants (m = 4..64); coset descent identity
Norm_512(P) = Norm_256(Q)^2 on random even-support words; AP-orbit unit
norm; symmetric norms perfect squares; symmetric orbit model vs brute force
at m=32 (12 = 12); factor-screen reassembly.

Event equivalence used throughout (standard, as in the banked censuses):
official event on P <=> q | Norm_n(P) = Res(X^{n/2}+1, P).  (=>) evaluation;
(<=) at official rows v_2(q-1) >= 41 => mu_n in F_q => Phi_n splits into
distinct linear factors mod q => the common factor has a root in F_q of
exact order n.  Norm != 0 over C by Lam-Leung parity (a vanishing sum of an
ODD number of roots of unity of 2-power order is impossible — signs are
themselves in mu_n).  Norm is ODD: Res mod 2 = Res((X+1)^{n/2}, P) =
P(1)^{n/2} = (sum of signs)^{n/2} == 5^{n/2} == 1 mod 2.
CORRECTION CAUGHT BY AN ASSERT: prime factors of Norm need NOT be
== 1 mod n (q | Res only forces a common root in an extension of F_q; e.g.
31 | an order-64 norm).  This does not affect the event equivalence at
official rows, but any future "factors live on the progression 1 mod n"
shortcut would be UNSOUND — flagged for the census designers.

### (a) Coset / arithmetic-progression supports

THEOREM A1 (AP, odd difference — PROVED, unit norm). Every 5-term AP with
odd common difference is affine-equivalent to {0,1,2,3,4}, i.e. ONE orbit;
its word is 1+X+X^2+X^3+X^4 = Phi_5 and |Norm_512| = Res(Phi_512, Phi_5) = 1
(verified exactly). No prime divides: the orbit hosts NO event in ANY
characteristic.  APs with difference 2^v*odd dilate into the coset family.

THEOREM A2 (coset descent — PROVED). Support in a coset of 2Z_512 <=>
P = X^c Q(X^2) with Q a reduced signed weight-5 word at exact order 256, and
Norm_512(P) = Norm_256(Q)^2 exactly (verified numerically; the affine-orbit
correspondence coset-orbits(512) <-> all-orbits(256) verified exhaustively
at small moduli).  Events descend/lift 1:1; recursion continues while the
support stays parity-uniform.  The coset subfamily = the order-<=256 tower:
275,145 of 2,296,920 orbits = 11.979% of the (1,5) orbit space.

THEOREM A3 (orders <= 32 — PROVED, size argument). A weight-5 relation at
exact order n <= 32 has 0 < |Norm_n| <= 5^{phi(n)} <= 5^16 = 152,587,890,625
< 6,597,069,766,657 = 3*2^41+1 = the SMALLEST official-admissible prime
(banked as the first MITM row).  So no official prime can divide: the
order-<=32 tower (292 orbits' worth of (1,5) cosets) hosts no official
event.  (n = 8: vacuous — max antipodal-free subset of Z_8 is 4 < 5.)

THEOREM A4 (order-64 layer — PROVED by census, this work). All 3,031
mixed-parity orbits at order 64 (count = Burnside 3,323 - 292, exact
cross-check) swept: 7 unit-norm rows; all other norms COMPLETELY factored
(probable-prime certification); max v_2(q-1) over all prime factors = 16
<< 41; zero unresolved; zero official-admissible factors.

THEOREM A5 (order-128 layer — PROVED by census, this work). All 28,255
mixed-parity orbits at order 128 (= 31,578 - 3,323, exact cross-check)
swept in 8 tiny shards: 4 unit-norm rows; zero unresolved; max
v_2(q-1) = 22 < 41; zero official-admissible factors.

=> Combining A2-A5: the sub-subfamily "support in a coset of 4Z_512"
(= primitive order <= 128; 31,578 orbits = 1.375% of (1,5)) hosts NO
official event.  REMAINING coset core: the order-256 mixed-parity layer,
243,567 orbits (of which 93 are closed below via the symmetric census) —
NOT closed here; it is a ~7-20 CPU-h Modal job (297-bit norms, i.e. HALF
the bit size of the (1,5) production rows) — the cheapest full-subfamily
closure available (see recommendations).

### (b) Antipodal sub-pair (e, e+256)

THEOREM B (PROVED, two readings — removes 0 orbits). (i) Reduced reading:
the audited candidate space is antipodal-free BY DEFINITION (supports =
w-subsets of [0,256) with signs; root sets antipodal-free); a sub-pair
{r, r+256} cannot occur in any census row — the subfamily is EMPTY as a
subset of the swept space.  (ii) Raw-window reading (weight-5 words with
exponents in [0,512) before reduction): a pair {e, e+256} evaluates to
s*(omega^e + omega^{e+256}) = s*(omega^e - omega^e) = 0 at ANY order-512
root, so the residual weight-3 word must vanish — excluded at official rows
by the banked (1,3) ambient census (max v_2 = 18 < 41).  Either way no
official event; but no orbit of the reduced space is removed (the family is
disjoint from it).  The nearest NONEMPTY analogue — quarter-pairs
{r, r+128} (rho' = +-i*rho) — admits no valuation argument we could find:
the pair contributes omega^e(1 +- i), which is a SUMMAND, not a factor, of
P; Norm stays odd and does not factor through (1+-i).  Honest failure.

### (c) Symmetric / palindromic supports

Structure (PROVED): R symmetric means R = c - R setwise in Z_512 (this
covers palindromic AND antipalindromic words; the sign epsilon is absorbed
by c -> c+256).  c must be even (an involution on a 5-set has a fixed
point; 2r = c needs c even), and the center is UNIQUE (two centers would
force translation invariance, impossible for |R| = 5 since 5 does not
divide 512).  Normal form R = -R with exactly one fixed element
f in {0,256}; 64,008 normalized sets; affine orbits of symmetric sets <->
orbits of normalized sets under N = {x -> ax+b : a odd, b in {0,256}}
(|N| = 512; model validated by brute force at m=32).  Exactly 360
symmetric orbits = 0.0157% of the (1,5) space.  Galois conjugates of
symmetric words are REAL, so Norm = M^2 with M an integer (asserted on
every row) — the effective factoring size HALVES (theoretical bound 297
bits; max M actually seen: 131 bits).

THEOREM C (PROVED by census, this work). All 360 symmetric orbits swept:
25 unit-norm rows; 360/360 M-values COMPLETELY factored (probable-prime
certification; one 102-bit semiprime needed ECM: 1,286,886,042,525,697 x
2,434,449,620,088,833); max v_2(q-1) = 17 << 41; zero official-admissible
factors.  The symmetric subfamily hosts NO official event.
Overlaps (exact): 171 of the 360 are coset-of-2Z-supported; 78 are
coset-of-4Z-supported (these 78 are the double-counted rows vs A4/A5); the
93 symmetric rows with primitive order 256 are the only closed part of the
order-256 coset core.

### (d) Factorization / cyclotomic-multiple subfamilies

THEOREM D1 (PROVED, field-uniform, parity). No weight-5 signed word is
divisible by ANY weight-2 signed word (equivalently by any X^d - gamma,
gamma = +-1, in particular by any 2-power cyclotomic Phi_{2^j}): folding
X^e -> gamma^{floor(e/d)} X^{e mod d} sends P to bucket sums of +-1's;
divisibility forces every bucket to vanish, needing an even count per
bucket — total 5 is odd.  Valid over Z and over F_q for char 0 or > 5
(bucket sums lie in [-5,5]).  So the "weight-2 x weight-3" and
"2-power-cyclotomic multiple" subfamilies are STRUCTURALLY EMPTY (stronger
than an exclusion, but removes 0 orbits from the census space).
(20,000-word x 18-divisor numerical spot check: 0 divisible.)

THEOREM D3 (PROVED, one direction only). Any weight-5 word that is a
monomial times a product of cyclotomics has |Norm_512| = 1 and hosts no
event in any characteristic: within degree < 256 the only Phi_m with
Res(Phi_512, Phi_m) != +-1 are the 2-power ones (prime-power-ratio law),
and those cannot divide by D1.  (Phi_5 = the AP-orbit word is the model
case.)  CONVERSE FALSE (measured): the 25 unit-norm symmetric canonical
reps all have roots OFF the unit circle (max | |root|-1 | = 0.318), so
unit norm does NOT imply cyclotomic shape — those rows are event-free
directly by |Norm| = 1, not via D3.  (Norms are affine-orbit invariants;
polynomial factorizations are not.)

THEOREM D2' (transfer closure — PROVED). If P = A*B over Z[X] where B
reduces to a signed word of weight <= 4 and Res(Phi_512, A) = +-1, then
Norm_512(P) = +-Norm_512(B) and the banked weight-<=4 exclusions close P
at official rows.  Verified exhibit: P = 1+X+X^2+X^5-X^8 =
Phi_3 * (1+X^5-X^6); the cofactor IS a reduced weight-3 word; transfer
checked exactly (Norm_512(P) = Norm_512(1+X^5-X^6) =
119,737,368,942,402,443,441,359,072,683,214,849).

HONEST FAILURE D2 (exact reason the general exclusion stops). For
P = A*B with a NON-word cofactor B (integer coefficients not in
{0,+-1}), no banked census or Newton floor applies to B: the event
transfers to Norm(B) with no weight control.  There is no 2-adic forcing
anywhere in family (d): Norm is odd for every odd-weight word, and
v_2(q-1) of a factor of Norm(B) is unconstrained by the factorization
shape.  Also "P reducible over F_q" is vacuous as a subfamily (P(omega)=0
always forces SOME irreducible factor mod q to vanish).  Detecting the
D2' family orbit-by-orbit requires per-orbit factorization — usable as a
cheap pre-filter inside a census row, not as an a-priori subfamily count.

### Removed-fraction table ((1,5) orbit space, T = 2,296,920)

| subfamily | orbits | % of T | status |
|---|---:|---:|---|
| coset of 2Z (= order<=256 tower) | 275,145 | 11.979% | partially closed |
|   - order<=32 tower | 292 | 0.013% | PROVED (size, A3) |
|   - order-64 mixed layer | 3,031 | 0.132% | PROVED (census, A4) |
|   - order-128 mixed layer | 28,255 | 1.230% | PROVED (census, A5) |
|   - order-256 mixed layer | 243,567 | 10.604% | OPEN (93 closed via C) |
| symmetric (R = c-R) | 360 | 0.0157% | PROVED (census, C) |
| AP odd-difference | 1 | 0.00004% | PROVED (unit norm, A1; also in C) |
| antipodal sub-pair | 0 | 0% | empty by convention (B) |
| weight-2-factor / 2-power-cyclotomic | 0 | 0% | structurally empty (D1) |
| PROVED-REMOVED (exact union) | 31,860 | 1.387% | = 31,578 + 360 - 78 |

Union accounting: coset<=128 (31,578) + symmetric (360) - overlap
(symmetric & coset-of-4Z = 78; AP orbit is inside symmetric) = **31,860
orbits = 1.387% of T PROVED event-free** (probable-prime certification
level; Pocklington promotion needed for node-grade banking).
IRREDUCIBLE CORE left for the census: **2,265,060 orbits**; the single
cheapest structured bite remaining is the order-256 mixed layer (243,474
orbits net of the 93 symmetric) at ~297-bit norms.

Complementary banked partial results (orthogonal axes, not orbit
removals): the first-64-official-rows MITM exclusion (row axis), and the
46.44% of (1,5) production rows already banked on the Modal volume (sweep
progress, not subfamily theorems).

## Constraint-first assessment (item 4 tail)

- (2,7): the audited router model IS constraint-first (selected 4-set +
  complement product; the 3 remaining roots come from the cubic resolvent,
  never enumerated): 94,652,815 rows vs 435,372,690,550 ambient orbits —
  a 4,600x reduction, already banked.  Extending the same router to
  (2,8)/(2,9) gives 18,555,400,106 / 3,084,343,642,846 rows (exact, this
  work): even constraint-first, (2,8) is ~735 CPU-years at the banked
  rate — the router alone does not rescue ell=2 beyond w=7.
- (4,w): ambient orbit spaces are 8.1e17 / 1.6e20 / 3.0e22 — no census of
  any kind can run.  But the FOUR conjugate vanishings collapse the cells
  structurally: the banked quartic-divisor descent (4,9) and the
  fixed-divisor straight-line lift reduce (4,9) to a 4-variable divisor
  ideal (114 vars / 119 eqs / degree <= 3 in SL form) with a Delta-integer
  certificate; the OND pattern w = 2*ell+3 extends verbatim to (4,11)
  (deg A = 5, Y*A^2 - (bY+1)^2 | Y^1024 - 1), and the (1,6) END even-weight
  pattern extends to (4,10) (E(Y)^2 - Y*B(Y)^2 shape).  Constraint-first
  is not merely better at (4,w) — it is the only viable route, and 2 of
  the 3 descents are already proved nodes; the missing pieces are the
  (4,10)/(4,11) descent statements and the Delta certificates themselves
  (the SL node warns Groebner cost is unproven).
- (1,7)/(1,8): no banked descent; the OND family covers only w = 2ell+3.
  At 13.0e9 / 8.06e11 orbits a blind census is 289 / 17,800 CPU-years —
  these two cells NEED new constraint-first algebra (e.g. an even/odd
  analogue of END/OND at w = L+6, L+7) before any census talk.

## Ranked recommendation for item-6 sampling screens (controller)

Screens = orbit samples + the peel screen (small-prime strip, p-1 stage 1
with exponent boosted by 2^44 — a DIRECT detector of official-admissible
primes with B1-smooth odd part — then budgeted Brent rho, ECM fallback).
Samples give survival evidence, not exclusions.  All timings from this
work's measured rates on this host (pure Python): norm ~2-6 ms (297-bit) /
~10-20 ms (594-bit+); peel ~0.1-1 s/row depending on cofactor hardness.

1. **(1,5) order-256 coset core — recommend FULL closure, not a sample.**
   243,474 orbits at 297-bit norms (HALF the production bit size).  As a
   Modal job at (1,5)-pipeline rates scaled by norm size: ~7-25 CPU-h,
   $2-5.  Closes subfamily (a) entirely and lifts the proved-removed
   fraction of (1,5) from 1.387% to 11.99%.  5-min local screen version:
   400-orbit sample ~2-3 min.
2. **(2,7) router-orbit sample** via the audited (2,6)-style pipeline:
   200 orbits x 1.25 s ~ 4.2 min.  Doubles as the GMP-gcd optimization
   pilot the wclp report demands before any (2,7) budget decision.
3. **(1,6) uniform orbit sample**: 256 rows, norms ~661 bits, peel-only
   ~0.5-0.9 s/row ~ 3-4 min.  Calibrates the 36k CPU-h projection's
   factor-stage growth.
4. **(1,7) sample**: 128 rows (~718-bit norms) ~ 3 min.  Purpose:
   v_2-statistics + measuring how far 0.698 s/row degrades — feeds the
   go/no-go on ever attacking (1,7) by census vs waiting for algebra.
5. **(1,8)/(2,8)/(2,9) expectation-setting samples**: 64 rows each,
   ~2-4 min.  Low value beyond confirming infeasibility; run last.
6. **(4,w): DO NOT sample the ambient space** (3e17+ orbits; a sample is
   information-free for emptiness).  Instead: (i) mint the (4,10)/(4,11)
   descent statements (pure proof work, no compute); (ii) pilot the
   (1,5) OND straight-line system (52 vars) under msolve/Groebner mod a
   few split primes on Modal as the cheapest feasibility probe of the
   whole Delta-certificate program — if THAT is tractable, (4,9)'s 114-var
   system becomes a plausible target.

Screen-order rationale: 1 converts compute directly into a subfamily
THEOREM at trivial cost; 2 unblocks the only currently-planned production
census ((2,7)) via its required optimization pilot; 3-4 buy rate truth for
the two cells whose projections span the fund/no-fund boundary; 5 is
bookkeeping; 6 redirects (4,w) effort from censuses (impossible) to the
descent/certificate lane (the banked, viable one).
