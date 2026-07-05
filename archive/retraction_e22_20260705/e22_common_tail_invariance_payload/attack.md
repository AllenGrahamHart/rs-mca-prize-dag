# ATTACK - e22_common_tail_invariance_payload

This is now an assembly node. The live E22 cofactor-structure leaf is
`e22_tail_removed_factor_manifest_payload`.

Needed output at the payload:

- identify a common tail `B` for all touched-petal divisors;
- prove `|B| < min_i M_i`;
- choose dyadic local moduli `M_i>t`;
- prove exact squarefree identities
  `L_{T_i\B}(X)=prod_z (X^{M_i}-z)` from the actual cofactor divisibility
  constraints.

Once this payload is available, `e22_common_tail_invariance_certificate_soundness`
promotes it to the old kernel-invariance node, and
`e22_kernel_invariance_full_fiber_criterion` converts kernel invariance to
full local quotient fibers.
