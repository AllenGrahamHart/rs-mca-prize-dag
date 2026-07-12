# W1 specification recovery audit

Date: 2026-07-12.

The banked F7 artifacts were searched for a definition of `K_cell`, a
coincidence system, or a symbolic rank certificate.

Findings:

1. `f7a2_envelope_stress_modal.py` defines the observed proxy
   `challenger_count*q^sigma` and calls its approximate scale `K_cell`. This is
   computed after exact challenger enumeration; it is not an independent upper
   bound or certificate.
2. `f7_beta_check_modal.py` likewise infers approximate values such as
   `148*17`. It proves the base-field normalization seam, but constructs no
   matrix or rank bound.
3. The complete and sharded F7 censuses enumerate toy cells and classify their
   outputs. They contain no Jacobian, symbolic minors, rank routine, or
   official-row descriptor.
4. `QUALITY_ww_kcell_upper_lemma.md` says the symbolic machinery exists and
   queues a pilot, but supplies no source path or definition. Repository-wide
   searches find only this prose assertion.
5. The consumer allowance is still #493-branched in the old statement, so even
   a numerical proxy has no single printed acceptance threshold there.

Therefore a `K_hat>=K_cell` replay cannot currently be constructed or
falsified without inventing the object it is meant to certify. Treating the
empirical proxy as the definition would be circular: it uses the exact count
that the certificate is supposed to upper-bound.

Disposition: remove W1 from the logical critical path and retain it as a
background wall/possible proof method. Re-pose W3 directly on the actual
challenger count and the conservative exact residual budget. This does not
prove W3; it makes the remaining red statement mathematically testable.

