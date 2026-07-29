# Audit

- The proof uses only (FEQ1) and the fixed values in (FEQ8). It does not
  import a resultant, factorization, root census, or unrun Modal verdict.
- The equation `E_G=C_b b+C_0` is obtained only after imposing `b^2=z`; no
  polynomial reduction is silently used outside the leading chart.
- Division by `C_b`, by `247`, and by the denominator of the forced value of
  `b` is justified separately for every official characteristic.
- The contradiction is already present in `E_G=0`; dropping `X_*=0` enlarges
  the candidate set, so its exclusion is sufficient for all of (FEQ8).
- The decimal obstruction and all four nonzero residues are printed in the
  proof. `verify.py` reconstructs them over the rationals. The independent
  `verify_audit.py` instead evaluates (FEQ8) and (FEQ1) directly in each
  prime field and uses decimal-chunk modular reduction.
- Under the user-specified Modal-only computation policy, neither arithmetic
  checker was executed locally. Only syntax, manifest, DAG, and textual
  structural checks may be run in this cycle. The theorem status rests on
  the displayed exact derivation, not on an unreported computation.
