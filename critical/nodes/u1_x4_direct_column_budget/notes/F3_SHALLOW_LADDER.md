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
