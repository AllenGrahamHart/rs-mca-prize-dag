# Status ruling: route-uniform E1 control remains open

Date: 2026-07-26.

The former `CONDITIONAL` proof used a valid named-exhibit certificate
implication at an invalid row-family scope. A complete no-vector certificate
over one named field excludes collisions only in that field. The official
challenge instead quantifies over every admissible `F,L,k`. No premise in the
former packet transported finitely many exhibits to every row on which the
direct E1 route might be invoked.

This audit does not claim that the corrected route-uniform statement is false. It
rules that the old implication did not prove it. The node is therefore a live
`TARGET`. The named-exhibit machinery remains truth-apt background work and
may still supply algorithms, calibration, or exhibit-specific results.

Promotion requires either a route-uniform proof at the exact `e1_fullness`
budget, or a complete per-input theorem/certifier covering every row assigned
to direct E1. Finite successful experiments or exhibit certificates are
insufficient. Universal row coverage is a separate target.
