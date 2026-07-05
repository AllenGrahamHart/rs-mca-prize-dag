# Conditional proof: fresh-codimension dichotomy

Status: CONDITIONAL on `xr_popular_core_triangles`.

The far-spread stagnation analysis has already been decomposed into three
branches.

1. `xr_syzygy_support_lemma` proves the support-budget reduction: rank
   stagnation gives a twisted syzygy of constrained-support dual codewords, and
   the MDS dual weight forces the `k+1` overlap budget.
2. `xr_scattered_syzygy_flattice` proves that the diffuse branch transports to
   the face-2 F-lattice objects.
3. The remaining budget-meeting branch is the concentrated branch: popular
   cores and the `m = 3` triangle dichotomy.

Therefore the fresh-codimension-or-structure dichotomy follows from the proved
alpha/gamma branches once `xr_popular_core_triangles` closes the concentrated
beta branch.  The proved `xr_ledger_qpower` supplies the q-power accounting for
the residual constraints; it is not an additional open hypothesis.
