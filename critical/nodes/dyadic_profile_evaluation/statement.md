# dyadic_profile_evaluation

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

[lifted verbatim 2026-07-27 from this node's own proof.md Statement section] Compute the quotient profile `Q_H(eta)` exactly for **2-power (dyadic) domains**
`n = 2^m` at the four rates `rho in {1/2, 1/4, 1/8, 1/16}`. Here the quotient
mass on a dyadic scale `M = 2^i | n` (with `M > t`, `t = A - k`) is the fixed-tail
quotient-coset count (banked `thm:qcore` / `prop:qfloor`, and the QA.22 column
convention)

```
Q_M = C(n/M - 1, floor(A/M)),          M | n,  M > t,                      (Q)
```

and the profile is `Q_H = sum_{M|n, M>t} Q_M` (with the dihedral/Chebyshev
companion `D_M`, below). "`eta`" is the reserve `eta = t/n`, which sets the
smallest admissible `M`. The deliverable is the *exact* value of `(Q)` at each
rate for both a small dyadic row (RowC, `n = 2^10`) and the prize dyadic row
(`n = 2^41`), together with the structural facts that make the profile
well-defined and computable: **first-scale dominance** and **n-uniformity**.
