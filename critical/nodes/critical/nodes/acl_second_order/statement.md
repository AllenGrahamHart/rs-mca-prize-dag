# acl_second_order

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['wp_detail/wp3_2_symbolic_scaling.md#3']

## Statement

Compute the second-order term of the antipodal class count Acl(N', l') beyond leading order, with explicit error control, so the corridor's quotient end becomes a NUMBER per rate instead of an interval. With it, per-rate bracket widths are exact and the adjacency question (adjacency_closing) is decidable rate-by-rate. Route shape: generating-function / saddle-point expansion of the class count.

## Attack surface

computation-shaped: expand the counting generating function one order past S2's leading term; verify against exact small-N' counts (already tabulated in the E1 packet: log2 A = 49.72/100.44/201.88)

## Falsifier

exact small-N' counts disagreeing with the expansion (arithmetic check, not a conjecture risk)

## Ledger (migrated notes)

Codex red-node pass (2026-07-04): banked as PROVED negative computation. The
second-order term is evaluated and the corridor input is numeric; it does not
close any clean rate by itself. CONCRETE TARGET (corridor computation): deliver
>= 0.367 / 0.023 / 0.304 grid steps at rates 1/4 / 1/8 / 1/16 (log2 Acl
anchors 49.72/100.44/201.88 cited; the E1 packet file needs pinning). The
corridor's one remaining mathematical item.

EVALUATED (agent, verifier replayed): E1 anchors pinned (Acl_tot =
(3^(N'/2)+1)/2 -- the rho=1/2 reference); the size-restricted corridor input
via the certified thm:exactcount formula. X_acl = +0.0497 / +0.0164 / -0.0056
grid steps at rates 1/4 / 1/8 / 1/16. VERDICT: NO RATE CLOSES -- 1/8 short by
0.00707 steps (~0.9 bits, entire interval below required); 1/16 FALSIFIER FIRES
(marginal widening at N'~383, the finite-N' exponent exceeds asymptotic beta).
The second-order term is now a NUMBER, not a hope.
