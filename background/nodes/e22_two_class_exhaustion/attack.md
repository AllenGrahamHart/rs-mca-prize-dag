# ATTACK - e22_two_class_exhaustion

Use light local computation only.

## Route A: direct proof

Work from the interpolation equations in
`nodes/worst_word_challenger_pricing/notes/e22_core.py`. Prove that a
non-planted crossing codeword touching at most one petal cannot reach
agreement `s = k + sigma`. The desired contradiction should use the core
locator form and the fact that the received word is zero on the core and
background but scalar multiples of `L_core` on petals.

## Route B: remote certificate

Complete the E22 census remotely and require a single `E22_RESULTS` JSON line
with `total_unclassified_on_exhaustive_cells == 0`. Structured-only cells are
evidence, not proof of no third class, because they generate petal-structured
candidates by construction.

## Current gate

`python3 nodes/worst_word_challenger_pricing/notes/e22_gate_local.py` is safe
to run locally and already passes. Do not run broad exhaustive cells locally
on the WSL laptop.
