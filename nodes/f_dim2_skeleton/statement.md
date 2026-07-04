# f_dim2_skeleton

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_iii_3_fibers_and_noanchor.md#1']

## Statement

On a gcd-trivial plane P: (i) domain traces H_x cap P are genuine lines; (ii) DISTINCT-trace pairs meet in one point, so sum of C(mult,2) <= C(n,2), giving #(P cap D_j) <= C(n,2)/C(j,2) for twin-free planes — elementary double counting; (iii) TWINS (coincident traces x,y) force every member through x to pass through y: the sub-pencil shares divisor (X-x)(X-y) and f_gcd_reduction pays it as tangent. F-dim-2 = pair bound + twin reduction, with the twin count T entering as (C(n,2) + (q+1)T)/C(j,2).

## Attack surface

write-up + verifier; TESTABLE PREDICTION against E7's own artifact: the j=5 kernel-sample top planes (primitive max 13 > 12 = C(16,2)/C(5,2)) must contain >= 1 twin pair — count twins in the recorded top planes

## Falsifier

a twin-free plane exceeding C(n,2)/C(j,2) (would break the double count — arithmetic, not conjecture, so a hit means an error in the skeleton)

## Ledger (migrated notes)

explains the E7 numbers: 38 <= 40 at j=3 (bound TIGHTER than the packet's floor 60); the kernel excess 13 > 12 is the twin signature | CROSS-POLLINATION: #183's 'Align E7 evidence with fixed-dimension theorem' commit followed this node's publication on the #178 branch — the census packet is being aligned to the pair-bound frame. | E10 PREDICTION CONFIRMED (#183): 5/5 sampled j=5 top kernel planes contain twins; ZERO twin-free planes above the simple bound 12. Full j=4 Grassmannian census (25,734,890 planes): primitive max 28 vs simple floor 20 vs pair floor 40, all 9 top primitive planes twin-rich (2^8 profile).
