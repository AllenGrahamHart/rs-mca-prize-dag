# F3 shallow-instance ladder (2026-07-07): exact censuses, the complete
# structural story, and the h=2 closure

Scripts: f3_exponent_ladder_modal.py, f3_h4_window_modal.py (scratch),
f3_h4_tail_modal.py. All exact bucket censuses; T = sum_sig C(k,2)
(intersecting equal-signature pairs impossible — proved in
F3_IDENTIFICATION.md).

## 1. The ladder (42 rows, h = 2..5, q ~ n^2 and n^3, n <= 512)

- MAX FIBER = n/h EXACTLY at every populated row: the moving-root/
  sunflower cap is TIGHT, achieved only by the zero-signature coset
  fiber (h | n) or antipodal fiber (h = 2).
- TORAL column exact: C(n/h, 2) mu_h-coset pairs when h | n (all
  signatures identically zero), both regimes, every row.
- NONTORAL: alpha(2) = 2.03-2.11 measured (n^2-scale, far below both
  the HBK n^{5/2} ceiling and the n^3 floor); h=3 Poisson-consistent
  accidents at the q ~ n^2 boundary (384 measured vs ~363 mean at
  (128, 17921); 3 dilation orbits, unstructured — verified no
  rotation/reflection relations); ZERO at q ~ n^3 everywhere.

## 2. The h=4 "suppression anomaly" RESOLVED (window scan + tail decode)

At n = 64 across q = 193..15361: nontoral-per-crude-classifier tracks
Poisson at small q (2240 vs mean 2230 at q=449), then a STRUCTURED tail
(counts 192, 160, 128, 96 — all orbits stab-2) exceeds the mean 6-15x
before dying between q = 3137 and 4289; ZERO at 5441..15361.

DECODE: every tail orbit is {a, a+n/2} ∪ {b, b+n/2} — two antipodal
pairs; the locator is a polynomial in X^2, so the family is the PULLBACK
under X -> X^2 of h=2 trades on the quotient mu_{n/2}. These are
quotient-pullback shift pairs (upstream's prop:sp-pullback, coefficient
scale s = 2) — PAID by F3's quotient strip; the probe's crude toral test
(mu_h-cosets only) cannot see them, so the probe's "nontoral" column
OVERCOUNTS F3's true residue (conservative direction). After
quotient-pullback accounting: NO genuinely-primitive structured family
at h = 4; accidents die by mean arithmetic; measured primitive residue
ZERO at every q >= n^2(1+eps) row.

## 3. The picture at F3's regime q >= n^2 (all h <= 5 measured)

    primitive residue = Poisson accidents with mean C(n,h)^2/2q^{h-1}
                        <= n^2/(2 h!^2)   at q >= n^2,
    + nothing else observed (structured families are toral or pullback,
      both paid columns).

F3's floor (<= n^3) holds in all data with an n-factor margin, and the
data-driven target theorem is: primitive residue <= C n^2 at q >= n^2.

## 4. h=2 stratum CLOSED (external import + replay)

T_2 total = #{disjoint pairs {x1,x2},{y1,y2} in mu_n, x1+x2 = y1+y2} =
the additive-energy collision count of mu_n. Heath-Brown--Konyagin
(Stepanov method; n <= q^{2/3}, implied by q >= n^{3/2} and a fortiori
by F3's q >= n^2): E(mu_n) <= C n^{5/2}, and 8*T_2 <= E - diagonal, so

    T_2 <= C' n^{5/2}  <  n^3  (margin n^{1/2} absorbs any effective C').

Replay: measured T_2 = C(n/2,2) + nontoral(window) ~ n^2-scale through
n = 512 — the truth sits at n^2, an extra half-power below the imported
ceiling. FIRST KERNEL INSTANCE CLOSED BY AN EXTERNAL THEOREM: the
shallow collision censuses are Stepanov-visible, which neither program's
internal machinery had exploited.

## 5. Next (the Stepanov swing, now data-informed)

Target: h = 3 primitive residue <= C n^2 (or any poly below n^3) at
q >= n^2 — the h=2 proof template (shifted-subgroup intersections /
energy), the derivative reformulation (pairs share A'), and the ladder
say the truth is n^2-scale Poisson with no structured interior families.

## 6. h=3 program session (2026-07-07 late; f3_h3_program_modal.py,
##    f3_h3_linedecode_modal.py)

DATA (15 rows, n = 96..256, q ~ c*n^2 for c = 1,2,4):
- THE CONTROL PARAMETER IS 3 | q-1: at (128, 17921) (3 does not divide
  q-1) only Poisson accidents (384, mean ~363, fibmax 2, unstructured);
  at (128, 33409) (3 | q-1) T JUMPS to 1088 with rot=64 structured pairs
  — interior families switch on with the cube root omega's rationality.
- Interior families die with q regardless: (192): 1536 -> 1152 -> 0
  across c = 1, 2, 4; (256, c >= 2): identically zero; fibmax = n/3
  only at the (0,0) toral fiber, = 2 elsewhere.
- Conic counts: max N_2(F) = O(1) (4-8) at 3-nondividing rows — conics
  over subgroups are uniformly thin there (the per-F Weil loss is NOT
  real in data); N_2 up to n at 3 | q-1 rows with 3 | n (the (0,0)
  toral conic).
- Global moment M machine-computed (FFT triple convolution, exact) at
  q <= 66000; bookkeeping M = trivial(multiset perms: 36/9/1 classes)
  + 72*T + repeat-entry residue; residues nonzero at some rows
  (4608 at (128,2), 5760 at (160,1)) = degenerate-trade (double-root)
  collisions — a term the M-form of the h=3 conjecture must carry.

CATCH (hypothesis refuted, banked): the degenerate-conic AFFINE-LINE
decode (Q = omega*P + s or self-stabilized) is FALSE — 0/1632, 0/1024,
0/96 matches at all three 3 | q-1 rows. The interior families are NOT
affine images. Leaked structure in the "other" class: exponent-AP /
geometric-progression motifs ({0,6,12}; recurring gap-6 supports at
(192, 37057)) — the next decode candidate is GP-anchored families
(supports containing geometric triples r, rd, rd^2).

STATE OF THE h=3 TARGET: primitive residue <= C n^2 at q >= n^2 holds in
all data with margin; the M-moment form needs the repeat-entry term; the
proof program's next steps: (1) decode the GP-anchored candidate, (2)
classify the 3 | q-1 interior families as a paid column (the h=3
analogue of quotient pullbacks), (3) then the Stepanov swing on the
residual, with the 3-nondividing case (pure Poisson, conics thin) as
the first target since no interior families exist there at all.

## 7. THE HYPERBOLA NORMAL FORM (2026-07-07, PROVED — the 3 | q-1
##    mechanism and the decode coordinates)

Let F = X^3 + aX^2 + bX + const and G_F(u,v) = (F(u)-F(v))/(u-v) =
u^2 + uv + v^2 + a(u+v) + b (same-fiber pairs of F = zeros of G_F).
Suppose omega (primitive cube root) is in F_q, i.e. 3 | q-1. Then
u^2 + uv + v^2 = (u - omega v)(u - omega^2 v), and with the linear
asymptote coordinates

    X(u,v) = u - omega v + a*beta,   Y(u,v) = u - omega^2 v + a*alpha
    (alpha, beta the explicit constants with u + v = alpha*(u - omega v)
     + beta*(u - omega^2 v); alpha = (1+omega^2)/(omega^2-omega) etc.)

one computes G_F = X*Y - Delta with Delta = a^2*alpha*beta - b. Hence:

    same-fiber pairs of F  <=>  X(u,v) * Y(u,v) = Delta(F),

a MULTIPLICATIVE equation in two linear forms. Consequences (all
elementary given the identity):
- 3 | q-1 SWITCH EXPLAINED: rational asymptotes make the conic a
  hyperbola in torus-friendly coordinates; for q = 2 mod 3 the
  asymptote directions are conjugate (no rational multiplicative
  structure) and only Poisson accidents survive — exactly as measured.
- The interior h=3 families are solution sets of X*Y = Delta with
  u, v ranging over mu_n — SHIFTED-SUBGROUP PRODUCT EQUATIONS, the
  precise object class of Vyugin--Shkredov-type theorems. Both the
  classification path (paid column) and the Stepanov path factor
  through this normal form.
- The toral check: a = b = 0 (mu_3-cosets) gives X*Y = 0 degenerate
  (the two lines u = omega v, u = omega^2 v) — consistent.

Machine verification + invariant extraction: f3_h3_hyperbola_modal.py.

## 8. Hyperbola form VERIFIED; interior families are RIGID ORBIT SHAPES
##    (2026-07-07, f3_h3_hyperbola_modal.py after the alpha-sign catch)

- XY = Delta machine-verified on ALL 2816 interior trades at the three
  3 | q-1 rows (96/96, 1088/1088, 1632/1632) after fixing the alpha
  sign (catch: alpha = +(1+omega^2)/(omega^2-omega); the wrong sign
  "verified" 160 accidental cases — flagged by the identity failing at
  scale, exactly what machine checks are for).
- RIGIDITY DATUM: interior supports are QUANTIZED into a handful of
  rigid gap-patterns per row, each a full dilation orbit ([15,24,39] x96
  and [17,24,41] x96 pairing at n=96; six patterns x128 at n=128;
  [6,90,96] x384, [6,6,12] x192 etc. at n=192). Interior count =
  (#shapes(q)) * n with #shapes = O(1) measured, q-selected
  (knife-edge-style activation).
- Delta invariants: never in mu_n; multiplicative order generic — no
  cheap degeneracy; the structure lives in the SHAPES, not in Delta.

CLASSIFICATION CONJECTURE (posed, next cycle's pose-and-prove): the
interior h=3 trades at 3 | q-1 rows form at most C(h) dilation orbits
per row — because a trade pair (P, Q) up to dilation satisfies the
hyperbola system for BOTH fibers (12 multiplicative conditions on a
bounded parameter count), a torus intersection of bounded degree
(Bezout-type finiteness). With it: T_3 <= C*n (interior) + Poisson
(~n^2/12 at the q ~ n^2 boundary) <= C' n^2 at q >= n^2 — the h=3
target — with the 3-nondividing case needing only the Poisson term.

## 9. THE DICHOTOMY CONFIRMED: interior h=3 families are NORM-GATE
##    ACCIDENTS (2026-07-08, f3_h3_dichotomy_modal.py)

(a) PERSISTENCE TEST (n = 96, seven primes q = 1 mod 96 in [n^2, 5n^2]
    completed): interior shape sets are PAIRWISE DISJOINT across q —
    [0,15,39 | 7,31,48] at 9601 only; [0,10,48 | 38,81,91] at 13249
    only; [0,3,82 | 35,54,79] at 18433 only; EMPTY interiors at 26113,
    36097, 42337, 46273. Each activated row carries exactly ONE orbit.
    No char-0-persistent interior family exists in the data.

(b) CERTIFICATE (machine-verified in Z[zeta_96] + F_p): for the
    9601-shape, the obstruction elements E1 = sum zeta^{a_i} - sum
    zeta^{b_j} and E2 (the e_2 difference) are NONZERO in char 0 (not a
    Mann/Conway-Jones vanishing configuration) while BOTH vanish mod
    p = 9601: activation <=> p | N(E1) and p | N(E2) — a NORM GATE.

CLASSIFICATION (mechanism PROVED + verified; count bound honest):
interior h=3 trades = rigid shapes sigma with char-0-nonzero
obstructions (E1(sigma), E2(sigma)) activating exactly at primes
dividing both norms. T_3(interior) = n * #activated(q), measured
#activated <= 1 per row. The rigorous per-q bound on #activated is the
PAIR-COPRIMALITY statement — generically (N(E1), N(E2)) share no prime
= 1 mod n — which is EXACTLY the coprime-ideal lemma shape of F2-A2
(the engineered-accident obstruction, empirically validated there with
positive control). THE ACCIDENT-LEVEL CONVERGENCE: F2's engineered
sub-balance accidents and F3's h=3 interior families are the same
arithmetic phenomenon (norm-gate selection), now exhibited on both
floors with certificates.

STATE OF h=3 AFTER THIS CYCLE: at the 4/7 empty rows the target
T_3 <= C n^2 holds OUTRIGHT (toral + tiny Poisson). In general:
T_3 = C(n/3,2)[3|n] + n * #activated(q) + Poisson(mean ~ n^2/12 at the
boundary, dying with q). ONE open lemma (pair-coprimality / norm-gate
sparsity) stands between the data and the theorem — shared verbatim
with F2's accident story.
