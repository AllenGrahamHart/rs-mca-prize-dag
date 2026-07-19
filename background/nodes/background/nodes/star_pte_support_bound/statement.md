# star_pte_support_bound

- **status:** PROVED
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/star_pte_support_bound.md']

## Statement

With agreement sets S_f, S_g (|.| = A = k+t), overlap r: the canonical trade is P = S_f \ S_g, Q = S_g \ S_f, so h = A - r; distinct degree-<k codewords agree in <= k-1 points => r <= k-1 => t < h <= A. The trade SUPPORT 2h = 2(A-r) splits across TWO agreement sets and runs up to 2A. Verified via explicit F_101 constructions realizing both extremes (r = 0: h = A; r = k-1: h = t+1). CONSEQUENCE: H_max = A = 67/133/261 confirmed; the beyond-grammar range (100, A] is nonempty at rates 1/4 AND 1/8 (261, 133), empty at 1/16 (67 < 100).
