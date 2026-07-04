# acl_second_order

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['wp_detail/wp3_2_symbolic_scaling.md#3']

## Statement

Compute the second-order term of the antipodal class count Acl(N', l') beyond leading order, with explicit error control, so the corridor's quotient end becomes a NUMBER per rate instead of an interval. With it, per-rate bracket widths are exact and the adjacency question (adjacency_closing) is decidable rate-by-rate. Route shape: generating-function / saddle-point expansion of the class count.

## Attack surface

computation-shaped: expand the counting generating function one order past S2's leading term; verify against exact small-N' counts (already tabulated in the E1 packet: log2 A = 49.72/100.44/201.88)

## Falsifier

exact small-N' counts disagreeing with the expansion (arithmetic check, not a conjecture risk)

## Ledger (migrated notes)

CONCRETE TARGET (corridor computation): deliver >= 0.367 / 0.023 / 0.304 grid steps at rates 1/4 / 1/8 / 1/16 (log2 Acl anchors 49.72/100.44/201.88 cited; the E1 packet file needs pinning). The corridor's one remaining mathematical item.
