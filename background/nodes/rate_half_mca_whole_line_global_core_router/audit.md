# Audit

The primary checker reconstructs the global `GF(11)` core, performs the
common division for all seven slopes, verifies exact shortened supports and
same-support noncontainment, and computes the failed direction-separation
gate.

The independent checker enumerates every degree-`<4` shortened codeword for
all seven slope words. It confirms one explanation and an actual bad witness
per slope, then separately checks the official `s=2/3` and `J_13/J_14`
payment boundaries.

Both checkers reject mutations of the global core, shortened parameters,
outcome, and official boundary constants.
