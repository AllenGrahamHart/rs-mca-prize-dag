# Source evidence

- Primary helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_tau_xi_square_direct.py`,
  SHA-256 `8239d7f2aa3f3077ac9b36a3428e4e74bf2dec2fcc02704f64489f093414ca73`.
- Independent helper:
  `critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_tau_xi_square_audit.py`,
  SHA-256 `644dfa4b9c9ba8f601d8cffa00f18a481cbfbcb3c6482c17667c0a92639e657c`.
- Eight primary and eight audit wrappers each replay one endpoint pair and
  allocation below sixty seconds under `ramguard tiny`.
- Primary and audit use independent source solves and opposite exceptional
  eliminations. Both replay exact support modulo `p=2130706433`.
