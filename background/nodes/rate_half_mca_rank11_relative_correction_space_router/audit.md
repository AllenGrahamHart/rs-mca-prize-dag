# Audit

1. The proper-intersection argument is performed on the shortened row and
   uses its actual `n',m'`.
2. The worst shortened proper cap is at the smallest admissible `K'`, not at
   the deployed endpoint. All dimensions `1..12` are replayed.
3. The first method failure at dimension 12 is not called a counterexample.
4. Generalized-weight restriction subtracts exactly the invariant outside
   budget `n'-m'=R-d`.
5. Clone size uses `K'-a`, not the original `K-a`.
6. The clone-tolerant bound is monotone in both shortening and support excess;
   the deployed `a=1` endpoint is therefore a valid uniform worst case.
7. The output is a route cut. Positive-dimensional and dimension-at-least-12
   branches remain unpaid.

No Modal computation is used; all scans contain twelve constant-size exact
integer evaluations.
