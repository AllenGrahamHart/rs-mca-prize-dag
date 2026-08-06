# f2_admissible_object

- **status:** REFUTED (composite statement; corrected 2026-08-06)
- **minted:** 2026-08-06 (mint-4, rounds 17-18), coordinator-audited.
- **provenance:** notes/pilots_20260806/f2_adm/ (373/373),
  notes/pilots_20260806/o1_generating_adversary/ (187/187),
  notes/pilots_20260806/f2_tq_pin/ (64/64) — all
  coordinator-replayed; FABLE_AUDIT.md in each dir is the audit of
  record.

## Scope correction

The composite all-admissible proposition below is false. It uses the
`p=1 mod 4` order formula on every row and therefore omits the minus branch.
At the official generating row

```text
p=2^61-1, q=p^2, ord_(2^41)(p)=2,
```

the antipodal half-system has `2^40` singleton `F_p`-proportionality
classes, not at most four. The exact replacement is the five-type signed
classification plus the coupled minus-branch negacyclic reduction. The field
cap, trace-rank, and coset-invariance components survive in their corrected
scopes. The historical Round-18 packet is retained below for provenance.

## Statement

THE PRIZE-ADMISSIBLE F2 OBJECT (replacing the 16-rung KoalaBear
tower, which is NOT prize-admissible — the field cap |F| < 2^256 is
broken from rung 4; f2_tq_pin CATCH-1). The admissible region at the
maximal rate-1/2 row (n = 2^41) is v_2(e) <= 2, e <= 6,
log2 p >= 39, tower depth <= 2 moving rungs. On it:

**LEMMA ADM-1.** With e_p := v_2(p-1) and D := 41 - e_p <= 2, window
representatives fall into F_p-proportionality classes indexed mod
2^D.

**LEMMA ADM-2 (replaces the 16-rung descent).** For D <= 2 the class
representatives are F_p-independent and L^perp = DIRECT SUM of C
class kernels (C = max(1, 2^{D-1}) new-part / 2^D nested), each a
prime-field GRS/MDS code [S, S-R, R+1]_p with S = m/C. Hence
dim_{F_p} L = C·min(S, R) EXACTLY, and Z(L) = Z_1^C. (Proved for
D <= 2 — exactly the admissible regime; checked computationally at
D = 3.)

**LEMMA ADM-3 (trace-tower collapse).** dim L <= min(m, k·|Lambda|)
with k = ord_n(p) — NOT [F_q:F_p] — unconditionally, even for
coefficients over F_q. (This corrects the constant in LEMMA
SL-1b-DIM's upper bound; the two coincide on the tower only.)

**Depth-budget trade-off.** D moving rungs force
t <= n/(2^D(41-D)): 5.36e10 / 2.75e10 / 1.41e10 at D = 0/1/2; D = 3
inadmissible.

**THEOREM G1 (generating classes).** ord_{2^41}(p) is always a
2-power ((Z/2^41)^* = Z/2 x Z/2^39), so k = e forces e in {1,2,4}:
the generating admissible classes are EXACTLY (e_p, e, k) in
{(>=41,1,1), (40,2,2), (39,4,4)}; e in {3,5,6} can never generate.

**THEOREM G2 (non-vacuity).** All three classes are non-empty, with
primality established twice (deterministic MR + Lucas p-1
certificates): 3·2^41+1, 27·2^40+1, 5·2^39+1, and the prize-max
witness 18446735827372343297 (e_p = 39, q = p^4,
L = 255.999997420).

**THEOREM C1 (coset invariance).** For any g in F_q^*, phi_g is an
F_q-linear bijection of K1(Lambda) with L(gW) = L(W) as subspaces
and E_{c in K1}[T_{gW}] = E[T_W] EXACTLY — the rules-level coset
domain costs the F2 first moment a factor of 1. (The coset gap of
f2_adm CATCH-6 is thereby confined to the parity/descent machinery;
the antipodal law still fails off-subgroup and remains a named
obligation there.)

**Ladder at the prize-max witness** (k = e = 4): fixed sector
n_0 = 2^39 (25% of the domain), rung 1 (n_1 = 2^40, p^2), rung 2
(n_2 = 2^41, p^4, 50%). THEOREM A discharges only order layers
a <= 42 - log2 L (0.78% of the domain at prize-max; every moving
rung misses by >= 39x). (M3) is VACUOUS on admissible rows (needs
R/m > 0.61; admissible max 0.0488).

## Falsifier

Any admissible (p, e) violating the class census; any D <= 2 row
where the class kernels fail F_p-independence; a coset g with
E[T_{gW}] != E[T_W].

## NOT claimed

Any bound on Z_1 (see f2_z1_mass_knife_edge); the status of (O1)
itself (see f2_o1_status_split); the antipodal law on cosets (open);
the n = 2^40 alternative tabulation.
