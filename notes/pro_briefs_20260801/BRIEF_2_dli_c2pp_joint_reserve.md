# Brief 2 — the joint reserve (C2'')

**Node:** `critical/nodes/dli_c2pp_joint_reserve/` · **status TARGET** ·
successor of the REFUTED `dli_level_factorization` ·
**upstream:** no counterpart (OURS_ONLY).

## The mystery in one paragraph

Across an official prize row's nested evaluation tower, the *joint* loss of
the exact staircase account stays within a fixed **21-bit** reserve of the
iid product of per-level expectations — even though no per-level or
per-junction version of this statement is true (the factorized form was
refuted). Something makes accidents across levels *globally* small without
being *locally* small, and we do not know what.

## Formal pose (C2'', posed 2026-07-10; survived its first adversarial round)

For every official prize row `R`, with the generated evaluation field and
the packet's state-dependent nested tower:

```text
A(R) = product_j E_U[rho_j]          (iid product of level expectations)
X(R) = q^(-t+H) W_cen(R)             (exact joint staircase account)

CLAIM (C2''):   X(R) <= 2^21 A(R).
```

Accounting discipline (normative): route every quotient/coset class through
the exact staircase; charge every non-coset accident at its **absolute**
weight with **unique first ownership**; never absorb accident mass into an
iid-relative constant. The aggregate 21-bit form is primary — **no uniform
per-junction bound and no factorization identity are asserted** (both are
dead; see below).

Records: `critical/nodes/dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md`
(three-part pose), `.../notes/M1_RESULT_AUDIT.md` (first survived round).

## Death ledger — do not resurrect

- **C2 = `dli_level_factorization`:** REFUTED. The per-level factorization
  identity is false; cross-level accidents are real and were exhibited.
- The refutation is why C2'' is stated as an aggregate with an explicit
  reserve: the 21 bits are the measured headroom for everything the
  factorization misses. Any proposal that reintroduces a per-junction
  uniform constant must exhibit why the C2 refuting instance is evaded.

## Why it resists — and the conversion ask

The difficulty is a quantifier inversion: accidents are unbounded *per
junction* but appear bounded *in aggregate*. That is exactly the shape of
two conversions that worked elsewhere in this project, which suggests the
same moves:

1. **Accident typology (the m2 move).** Classify non-coset accidents into
   finitely many types (by which tower junction they straddle, by coset
   geometry, by valuation). If the type list is provably complete and each
   type's total mass is bounded by an exact computation per official row,
   C2'' becomes a case program: `sum of per-type budgets <= 2^21`. The
   unique-first-ownership discipline already makes accident mass additive —
   the missing piece is the completeness of a type enumeration.
2. **Budget ladder (the E1 move).** Order accident types by weight and
   compute the sharp per-type cap that keeps the aggregate under `2^21`
   (analogous to `floor(2E/M)` in the E1 ladder). Then the heavy types need
   proofs; light types need only the census bound. This prices which part
   of the mystery actually needs an idea.
3. **Row-family finiteness (shared with brief 1):** the claim quantifies
   over official prize rows only. A completeness/enumeration theorem for
   that family plus a bounded per-row decision procedure converts C2'' to
   a certified census. The staircase account `X(R)` is already computed
   exactly by the packet machinery for audited rows.

**The sharpest question for a fresh mind:** is there a martingale /
telescoping decomposition of `X(R)/A(R)` along the tower in which the
non-coset accidents appear as finitely many boundary terms with signs —
i.e., is `2^21` secretly `sum of a short explicit series` rather than an
empirical headroom? The measured margins (first-round audit) are far from
tight, which is consistent with a short-series explanation.

> **[CORRECTION 2026-08-01 — three updates from the Pro dossier's stress
> test, audited and accepted on our side.]** (1) Route 3 (row-family
> finiteness) is DEAD — the official row family is universal
> (`official_row_primes_pinning`); finiteness lives in witness types,
> never in primes. (2) Route 1 is SHARPENED: the type enumeration cannot
> be the observed theta=2 k-classes (accident status flips under harmless
> regrouping — exact 51/50 fixture — and the classifier branch runs in
> binary64, confirmed at `m1_dli_m1_tower_census_modal.py:571`); it must
> be a canonical owner grammar on concrete paths, stable under arbitrary
> prefix tilt. (3) The sharpest question above is REFINED to its sound
> form: exact tilted increments `g_m = Z_(m+1)/Z_m` + a Bellman
> supersolution — no cancellation entitlement without an exact sign
> identity, and NO pairwise/adjacent/one-junction inference: 33 pairwise-
> exactly-independent mean-one factors can have 33-fold product 2^22
> (the F_2^11 trap, verified exhaustively). Also: C2'' has survived TWO
> recorded rounds (M1 + C2R2 2026-07-13), not one. See
> `responses/BRIEF2_PRO_DOSSIER.md` and
> `responses/BRIEF2_DOSSIER_AUDIT.md`.

## Guards

- The absolute-weight, unique-first-ownership accounting is normative;
  proposals in iid-relative accounting are not comparable and will be
  rejected by the interface guardrail.
- `2^21` is a frozen constant of the pose, not tunable; a proof of any
  finite constant would be accepted as closing a weaker sibling, but the
  node as posed asks for 21 bits.
- Exact rational verdicts only.
