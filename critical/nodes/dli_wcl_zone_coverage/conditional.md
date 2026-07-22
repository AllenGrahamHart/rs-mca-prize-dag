# conditional close: dli_wcl_zone_coverage (the WCL amber)

- **status:** CONDITIONAL on the four slot reds (req, gate=all) — flipped
  2026-07-19 at the maintainer-directed ceremony

## Assembly

The ratified equivalence (maintainer rulings 4a/4c + the audited
exclusion ladder, all components PROVED): WCL-ZONE holds iff the four
slots (1,5), (1,6), (2,7), (4,9) are empty at every official row. The
Newton short-window theorem closes every window at ell >= 8 and the
listed low-ell windows; the terminal and ell-2 censuses close (1,3),
(1,4), (2,3), (2,4), (2,5), (2,6); the schedule-r2 + raw-ledger rulings
fix the object. Hence: slot_1_5 AND slot_1_6 AND slot_2_7 AND slot_4_9
==> WCL-ZONE. F-round record 2/2 stands as analogue-scale evidence.

## Re-surgery criteria (pre-registered)

A slot falsifier (one official-admissible prime with the vanisher)
refutes that slot AND WCL-ZONE outright — the amber goes vacuous and
the dli decomposition's baseline arm re-opens. A schedule or ledger
re-ratification re-opens the equivalence.

## TEN-SLOT EQUIVALENCE RE-ISSUE (2026-07-22 forced correction, wcl seam audit)

The four-slot equivalence above predates the C1'-r3 window extension and is
SUPERSEDED as the operative assembly. Statement of record: at every official
row, W_ext(R,L) <= 1/32 at all 34 levels IFF the ten cells
(1,5)(1,6)(1,7)(1,8)(2,7)(2,8)(2,9)(4,9)(4,10)(4,11) are event-free.
Proof components, all PROVED: the Newton short-window theorem (w <= 2*ell;
empties every window at ell >= 8 and floors ell=2 at 5, ell=4 at 9); the
weight-3/4 ambient exclusions (both ell=1 levels); the (2,5) norm-gcd and
(2,6) recursive-norm certificates; and the exact mass arithmetic (one orbit
in any surviving cell charges >= 1 > 1/32, so surviving cells are zero-event;
minimum breach factor 32x at (4,11)). The enumeration is machine-checked by
`verify_slot_decomposition.py`. A census program closing only the four
pre-extension slots does NOT discharge this assembly — all ten cells are
req-wired and load-bearing.
