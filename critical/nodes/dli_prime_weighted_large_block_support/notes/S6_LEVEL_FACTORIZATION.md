# S6: the level-independence hypothesis audited — a real assumption, mis-justified in the pinned file
# (round S6, self-tennis, 2026-07-07)

## The finding

The pinned file justifies the level-product step as: "the central tower
measure is a product across levels (levels use disjoint coordinate sets),
so E[prod] = prod E". The parenthetical is NOT supported by the packet
docs: per the verified skew-tower packet (archive/compressed_dli_lane/
b2b_primitive_core/notes/pro_skew_tower_packet.md, points 2 and 4), the
levels partition the MOMENT indices (each m ≤ t uniquely 2^j·odd,
Σ_j L_j = t) while the skew variables live on the SHARED codeword cells.
Disjoint moment-rows over shared coordinates do NOT give measure
factorization.

Analytically the gap is visible in D3: E_U[Π_j ρ_j] is the Fourier sum of
Π_y cos²(π·Σ_j a_y(λ^{(j)})/q) — cos² of the SUM of level phases at each
shared cell — while Π_j E_U[ρ_j] is the sum of Π_j cos²(π a_y(λ^{(j)})/q)
— the PRODUCT of cos²'s. These differ termwise; equality of the sums is a
genuine cancellation statement, not bookkeeping.

## The two honest routes

1. **Packet-side factorization lemma.** The tower measure's precise
   definition lives with the consumer (x4_exactlist_staircase_split's
   packet), not in this node. If the packet's U-measure is genuinely
   product-form over levels (e.g. because the central-profile weights
   factor over the dyadic decomposition), the lemma is provable THERE.
   This node cannot prove it from its own objects; it must import it.
2. **Unconditional Hölder route (stays inside the core).**
   E_U[Π_j ρ_j] ≤ Π_j (E_U[ρ_j^{t_j}])^{1/t_j} for any Σ 1/t_j = 1 —
   unconditional. By the S2 moment-transfer lemma, E[ρ_j^{s}] is a
   (2s+1)-ary kernel count: the Hölder route replaces level-independence
   by higher-alphabet instances of the SAME singular core (with the S1
   sieve's per-alphabet coverage computable by the same code). No new
   assumption type is created.

## Disposition

- Pinned parenthetical corrected in place (marker added).
- The hypothesis is banked as the named conjecture/import
  **LEVEL-FACTORIZATION**: either the packet-side product lemma (route 1)
  or the Hölder/moment version of DYADIC-K at the required alphabets
  (route 2). Both discharge it; neither is free.
- With this, the node's complete condition list is exactly
  {DYADIC-K, LEVEL-FACTORIZATION} — see the S7 structure report.
