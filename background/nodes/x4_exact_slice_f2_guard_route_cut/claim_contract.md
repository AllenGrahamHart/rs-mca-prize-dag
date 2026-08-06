# Claim contract

- **Claim:** every official exact-list corridor depth fails the generated-field
  F2 guard.
- **Inputs:** the exact corridor definition `(XR)`, `N=2^41`, the four prize
  rates, and `128<=log2(q)<256`.
- **Output:** a route cut, not an extras count.
- **Nonclaims:** no counterexample to the `n^3` exact-slice budget; no F2 mass
  upper bound; no assertion that `f1/ext` covers generating rows; no change to
  the prize statement.
- **Falsifier:** an official row satisfying `(XR)` with
  `t_XR log2|B0|>=N`.
