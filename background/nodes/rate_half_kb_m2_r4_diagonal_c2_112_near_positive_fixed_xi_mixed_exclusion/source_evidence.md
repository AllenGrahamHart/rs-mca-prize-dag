# Source evidence

- Primary helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_mixed_direct.py`,
  SHA-256 `47603de070ff34b59c2e6000c18add44b8d0a40fb281b998264ca38265e4915f`.
- Independent helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_fixed_xi_mixed_direct_audit.py`,
  SHA-256 `694ecea074769c5fd5fc62645c490768ca9f620e15b2739d779bb145313690f7`.
- The primary direct solve and the audit fraction-free solve share no code.
  They project in opposite variables and both reduce their final support gcd
  modulo `p=2130706433`.
- Both complete wrappers replay below sixty seconds under `ramguard tiny`.
  No floating point, Modal, or unpriced remote computation is used.
