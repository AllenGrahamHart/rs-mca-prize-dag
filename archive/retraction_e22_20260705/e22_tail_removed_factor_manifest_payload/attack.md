# ATTACK - e22_tail_removed_factor_manifest_payload

This is now the live E22 cofactor-structure leaf.

Needed output:

- identify one common tail `B` for all touched-petal divisors;
- prove `|B| < min_i M_i`;
- choose dyadic local moduli `M_i>t`;
- for each touched petal, identify quotient values `Z_i`;
- prove the exact squarefree identity
  `L_{T_i\B}(X)=prod_{z in Z_i}(X^{M_i}-z)` from the actual divisor
  constraints `L_{T_i}|H_i`.

Once this manifest is available,
`e22_tail_removed_factor_manifest_soundness` turns it into the old
common-tail invariance payload.
