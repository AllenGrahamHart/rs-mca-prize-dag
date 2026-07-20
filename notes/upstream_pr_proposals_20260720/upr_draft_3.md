# PR DRAFT 3 (RANK 3) — §0.5 falsifiability objects: explicit prefix-fiber family + split-pencil census (LEAD)

> Title: **Toward §0.5: an explicit super-polynomial primitive prefix-fiber family and a budget-3 split-pencil census (rank-deficient branch empty)**

Base: `origin/main@9908454995f3f195cfe748f35a1135211609d066`.
Cross-repo reference (SHA-pinned): `github.com/AllenGrahamHart/rs-mca-prize-dag@b8a169acb020f4a8cf990a552daf12b29127337b`,
nodes `critical/nodes/rate_half_cyclic_rotated_prefix_floor` (PROVED, wave-9),
`background/nodes/rate_half_list_budget_three_quadratic_scroll_full_rank` (PROVED),
`critical/nodes/rate_half_list_adjacent_crossing` (TARGET, budget-3 census).

## Scope (a lead, not a closure)

Your §0.5 asks a counterexample to be one of two explicit, machine-checkable objects: a
"super-polynomial primitive prefix fiber" or a "super-polynomial primitive split-pencil family." This
PR contributes two audited objects in exactly that vocabulary, and is honest that they CALIBRATE the
falsifiability boundary rather than resolve it.

### 1. Explicit prefix-fiber family (prefix-fiber object)

For `C = RS[F,D,n/2]`, `c | n/2`, `N = n/c`, `0 < s < c`, `1 ≤ d ≤ N/2 − 1`, `m = N/2 + d`, cyclic
rotation modulo `Y^N − delta` plus a fixed `s`-point tail produces at least

```text
ceil( C(N-1, m) / (N * q^(d-1)) )
```

distinct codewords at agreement `n/2 + dc + s`. The count is `s`-independent (the `s = c−1` lemma), so
the entire residual band is list-unsafe: at the official cap row `N * q^d < 2^128 * C(N−1,m)` even at
`q = 2^256`, with a 75.08-bit margin. This is an EXPLICIT primitive prefix fiber that is
super-polynomial — the shape your §0.5 names — realized on the UNSAFE side (it confirms, and does not
contradict, the envelope).

### 2. Budget-3 split-pencil census (split-pencil object)

Any hypothetical 4-codeword list witness at the Johnson predecessor `3n/4 − 1` reduces, via the
split-pencil normal form `A_k b_ij + A_i b_jk = A_j b_ik` (entries degree ≤ 2) and the Plücker gate
`b01 b23 − b02 b13 + b03 b12 = 0` (edge polynomials degree ≤ 4), to EXACTLY 13 chambers. The
rank-deficient quadratic-scroll branch is proved **EMPTY**:

```text
det C = b01^2 (L12 L03 − L02 L13) != 0   in all four quadratic chambers.
```

So no super-polynomial primitive split-pencil family arises in the rank-deficient scroll branch.
**The other chambers are open (0/13 closed).**

## Verification

- Prefix floor: Modal verifier + independent backward audit `ap-YVuPe20N3lQuwNgedf0h5c`; full manifest
  178/178 in `ap-CRn9AwYF0xIGWOsvrDntDM`; toy fixtures `(5005,313,315)`, `(3003,2,6)`; cap margin
  75.079624489 bits, `q_boundary` 256.036659972895 bits. Wave-9 audited.
- Split-pencil census: both censuses machine-enumerated AND independently re-enumerated at audit
  (wave-11); Plücker/normal-form degrees pinned in the verifier contract.

## Non-claims (fence)

This PR does **not**:

- exhibit a counterexample to your envelope — the prefix-fiber family is a CONFIRMING unsafe
  construction, not a super-polynomial primitive prefix fiber that beats the envelope,
- prove that no super-polynomial primitive split-pencil family exists — only the rank-deficient
  scroll branch is empty; **13 chambers remain open** and are not closed here,
- move any threshold — the proved budget-3 bracket `[k+2^34, 3n/4]` is unchanged by the
  classification (the single-fiber split-unit exclusion closes ZERO chambers; the wave-12 note),
- claim any Grand List / MCA / Proximity Prize result; official score unchanged,
- transport to your `n=2^21` §0.4 rows (different row family).

## What this gives your §0.5

A concrete, machine-checkable instance of each named falsifiability object, with the prefix-fiber
family pinned on the unsafe side (envelope-consistent) and the split-pencil search narrowed to 13
chambers with one branch provably empty — i.e. a sharpened, honest map of where a §0.5 counterexample
could still hide (the 13 open budget-3 chambers on the official subgroup) and where it cannot (the
rank-deficient scroll branch).
