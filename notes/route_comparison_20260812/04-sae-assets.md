# Direct S/A/E route — instrument and constraint inventory

All units: distinct finite affine bad slopes on one actual received line, KoalaBear row (n,k,m,d,R,t) = (2097152, 1048576, 1116048, 67472, 1048576, 981104), B_* = 274980728111395087.

## 1. Proved local charges available to a regenerated ledger

**(a) Near-rational stratum: 2w = 134944** [SOURCE-STATED]. If w >= 1 and 3w <= n-K, any set L of distinct slopes that are simultaneously (i) within distance w of a codeword and (ii) actually support-wise MCA-bad on a genuine size-m witness satisfies |L| <= 2w (`v13_2_near_rational_supportwise_two_anchor_payment/statement.md:10-32`; proof via two-anchor error-line reconstruction and coordinate-ratio injection, `proof.md:3-60`). KoalaBear: 2w = 2(1116048-1048576) = 134944; Mersenne-31: 134896 (#1160 note §3 table; `audit.md:22-24` pins both). Crucially it is "a standalone upper bound for the full near-rational bad-slope stratum, hence also for any first-match subset of it" — so it drops into any chronology unchanged — but "integrating the charge into a summed ledger still requires the declared owner order" (#1160 §3, pr1163:`kb_mca_supportwise_near_rational_two_anchor_repair_v1.md`). It does not define a first-owner predicate or bound the far-from-code complement (`statement.md:34-36`).

**(b) Tangent atom: U_paid = t = 981104**, the only banked global atom [SOURCE-STATED context]. Repair 4 of #1160 fixes its scope: a fixed identically split kernel is tangent-paid **only** at thresholds satisfying the existing guard **n-a' <= t** (including deficiency one); at arbitrary deficiency it is a structural rank-one/spread route, *not a payment*, and common-support deletion is never used (#1160 §3, repair 4). The staircase-import audit confirms t = n-m = 981104 equals U_paid (`rate_half_kb_common_core_shortening_adapter_staircase_import/audit.md:33-36`).

**(c) Fixed-core family payments via the shortening adapter** [SOURCE-STATED]. The same-record common-core cancellation is a typed reversible adapter (n,k,m) -> (n-c,k-c,m-c) = (R+s, s, d+s), s = k-c, preserving slopes, field, (d,R,t), maximal supports, and same-support noncontainment in both directions, with a noncontained witness through the core guaranteed by the exchange-graph argument (`statement.md:30-56`; `proof.md:3-41`). A **fixed-family** common-core terminal is paid iff:
- it is **globally affine**, or
- **s <= 2**: B_cell(s) = min{C(R+s,d+s), C(R+s,s+1)}, with B_cell(1) = 549756338176 and B_cell(2) = 192154133857304576 < B_*, or
- under **direction separation**, **3 <= s <= 13**: J_s = floor(prod_{i=0..s}(R+i)/(d+i)), J_13 = 47876303026096432 < B_*
(#1163 §3, lines 170-226; `statement.md:69-86`).

## 2. Exact walls constraining any staircase compiler

All four PROVED and independently replayed (`proof.md:43-59`, `audit.md:20-28`):

1. **Degree-18 interface wall**: 32m - 17n = 61952, so the deployed order-32 degree-18 interface survives iff 61952 > 15c — last core c = 4130 (slack 2), floor drops to 17 at c = 4131 (overshoot 13), floor 3 at c = k-1. The `thm:partial-relative` constants cannot be reused uniformly after cancellation (#1163 §3; `statement.md:63-67`).
2. **Fixed-core cell wall**: B_cell first fails at s = 3, B_cell(3) = 50372197381489643749376, exceeding B_* by 50371922400761532354289 (#1163 §3 table).
3. **Direction-separated boundary**: B_* sits exactly between J_13 and J_14 = 743896698428332665 (#1163 §3).
4. **Jo transfer wall**: C(n,4131) > B_*·C(m,4131); the double-counting multiplier ceil(C(n,4131)/C(m,4131)) has 3765 bits (1134 decimal digits), and staged shortening telescopes to the identical factor by exact binomial identity — the published slope-preserving transfer cannot pay the first uncovered core (#1163 §4, lines 227-250; `proof.md:55-59`). This is a budget obstruction to *that theorem*, "not a proof that every possible common-core compiler must fail" (#1163 §4).

**Residual labels** (residuals, not owners): `DIRECTION_LIST_SHORTENED_s` for 3 <= s <= 13 when separation fails; `COMMON_CORE_SHORTENED_s_GE_14` for s >= 14 (#1163 §3; `statement.md:84-86`). The missing bridge is a total chronology-correct selector sending every actual first-match non-affine common-core 32-record's slope exactly once to a named earlier owner, a disjoint paid fixed-core family, or one of these two labels, with projection fibers and add-back multiplicities derived in distinct-slope units (#1163 §5, lines 251-284). Summing B_cell(s) or J_s over core choices is invalid — it converts the maximum-type endgame into an additive support census (#1163 §5).

## 3. Controls any selector must survive

1. **The #1160 67,472-slope line**: u,v supported on a w-set E with v(e_i)=1, u(e_i)=-γ_i; every slope near-rational (distance <= w from zero), each γ_i support-wise bad on S_i = R ∪ {e_i} (#1160 §1). It is **globally affine and separately near-rational-owned — a control, not a casualty** of the adapter (#1163 §6, first bullet; `statement.md:100-102`). Any selector deleting it via a common support elsewhere is refuted.
2. **The inverse-lifted GF(17) atom**: the degree-two atom cancels from (8,4,6) by core {1,15} to (6,2,4) preserving all five slopes and identical-support noncontainment; puncturing without lowering k destroys it (#1163 §6, second bullet). §7 names this and the #1160 line as the hostile controls of the required forest compiler; the smallest actual selector collision is the preferred falsifier.
3. **The converse embedding**: every compatible shortened RS-MCA record lifts (c fresh points, arbitrary degree-<c a_0,a_1) into a common-core record with the same slopes and badness — "divide the core and declare it paid" is false; zero-cost core deletion is ruled out (`statement.md:57-59`; `proof.md:38-41`; #1163 §5).
4. [Additional, SOURCE-STATED] The exact GF(7) census attains 2d, and cancellation preserves (d,R,t) — so no selector can sharpen the 2w charge by shortening (#1163 §6, third bullet).

## 4. Which of the seven #1160 repairs matter for chronology regeneration

The seven repairs are SOURCE-STATED (#1160 §3, lines 166-201); the triage is YOUR-INFERENCE:

- **Load-bearing for the regenerated ledger**: **Repair 1** (both corollaries charge 2w, not 1 — the ledger's near-rational line item); **Repair 4** (the tangent guard n-a' <= t delimits exactly what U_paid = 981104 already covers, so the selector knows where tangent ownership ends); **Repair 5** (global code-line and owner-localization proofs now use the *identical* bad witness support — the chronology's first-match adjudication must be same-witness, never inferring global column-farness from support-wise badness). #1160 §3 states directly that "the reserve and the S/A/E interfaces must be updated rather than pretending this stratum costs one slope."
- **Instruments the whole-line selector will reuse**: **Repair 3** (rank-one injection from one noncommon witness per bad slope, valid even when another common support exists — makes S-outcomes chronology-safe); **Repair 6** (triple-collapse same-support outside-coordinate injection uniform over small and large cores — the varying-core case is precisely the selector's hard case).
- **Scoping constraints, not instruments**: **Repair 2** (common support = translation to a sparse pair with the identical bad-slope set — the only legitimate use of common supports); **Repair 7** (correction-ray theorem restricted to MCA-rich records with a noncontained exact support — the selector may not invoke it for unrestricted rich pairs).

**Bottom line** [YOUR-INFERENCE, consistent with `statement.md:88-98`]: the direct route now has a complete paid perimeter (2w stratum, guarded tangent atom, globally-affine terminals, s<=2 cells, direction-separated 3<=s<=13) and two honest residual bins; everything reduces to the one missing chronology-correct whole-line selector, which must reproduce the #1160 line and the inverse-lifted GF(17) atom as fixed points and pay nothing through the four walls. U_S = U_A = U_E = 0 until then.