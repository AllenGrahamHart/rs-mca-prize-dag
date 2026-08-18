# Audit

1. Full owner planes are counted after global common-core shortening.
2. For a 218-point plane, the recurrence count is exactly `|J_A\J|`; the
   plane cap rules out extra owners on those coordinates.
3. The local endpoint lower bound `K_A>=2044` is used in the correct
   direction, giving recurrence at most `K'-2044`.
4. A subset of exactly the required number of distinct planes is chosen
   before the balanced point-plane moment is applied.
5. Plane intersections are selected-point intersections on an affine line,
   so the cap is 15 even when the ambient geometric line has more field
   points.
6. A nonsaturated plane pair loses at least one unit of intersection
   capacity; no equality of the remaining pairs is assumed.
7. Planes through one saturated line have disjoint 203-point off-line parts.
8. The saturated-line common core is an actual received-pair core, not merely
   the zero set of its direction polynomial.
