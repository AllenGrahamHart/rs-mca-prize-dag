# Lineage

- Starting local pin: `17833b451`
- Canonical prize pin: `23df01a65`
- Upstream main pin: `93fba1be`
- Open upstream PR reconciliation: eight PRs; none supplies WCL arithmetic
- Source notes:
  `notes/kernel_basis/wclp_sizing_20260719/wclp_b_count.py`,
  `notes/kernel_basis/wclp_sizing_20260719/wclp_b_sample_modal.py`, and
  `notes/wcl_decomposition_audit_20260722/wscr_findings.md`
- Mathematical correction: replaces blind rational `Norm(u)` saturation by
  the exact split-embedding filter `(QCR6)`

The source notes supplied the recurrence and sizing evidence. This node
freezes their exact theorem, corrects the unresolved soundness point, and
adds independent replay.
