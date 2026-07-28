# Audit

- The proof uses the exact Euclidean variance identity, not a heuristic sphere
  packing estimate.
- Even square mass is load-bearing: absence of edges at `S<=2ell` gives the
  strict separation `S>=2ell+2`.
- The class vectors may have varying singleton counts; `||x||^2<=ell` is the
  only weight input.
- `c_max` is rounded with `(K-1)//(B*(ell+1))`, preserving the strict image
  inequality.
- The prize rate-`1/8` value `c_max=3` is binding for this route: the verifier
  confirms that four colors are not certified by the same argument.
- No graph coloring, row payload, or prize endpoint is claimed here.
