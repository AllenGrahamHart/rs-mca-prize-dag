### 2026-08-10 K3 bridge and allocation refactor

Round-30 canonical audits and the current upstream PR snapshot changed the
K3 priority. Upstream `main` remains `93fba1be`; the relevant open frontier is
PR `#1152` (living K3 export), `#1153`--`#1155` (independent cell packets and
route cuts), `#1150` (corrected F2 branch), and `#1151` (LIST LS6 reductions).
No new upstream merge closes an active critical leaf.

The former K3 orientation leaf conflated three different domains: active
first-match bad slopes, endpoint components, and raw workboard systems. The
component-level theorem is now isolated and proved:

```text
(m,r,delta)=(2,4,2), stabilizer order two
  coordinate <tau x 1> or <1 x tau> (one transpose orbit)
  diagonal <tau x tau>
       source-line lift | biquadratic source cover
```

This theorem has no slope-domain conclusion. The active ledger also retains
the separate trivial-stabilizer type `(2,8,1)`. The corrected critical K3
sub-DAG is therefore:

```text
active Z_BC slope-to-component bridge [TARGET]
             |
             +-- positive coordinate: 11 remaining routes [TARGET]
             +-- negative coordinate [PROVED empty]
             +-- source-line remaining rows [TARGET]
             +-- biquadratic source-cover workboard/payment [TARGET]
             +-- trivial-stabilizer (2,8,1) payment [TARGET]
                              |
                    geometry assembly [CONDITIONAL]
                              |
positive + geometry + certified U_BC allocation [CONDITIONAL]
                              |
                    exact K3 ledger [CONDITIONAL]
```

The source-line target explicitly retains `(1,0,4)`, `(0,1,4)`, the
near-aligned `(0,0,6)` row, and exceptional unsaturated `(1,1,2)` orbit
`KBDM-10`; the saturated c112 packet is only one proved zero subcase. The
source-cover target is a new explicit workboard over both proved V4 passports.

The allocation audit also corrected a false placeholder. The integer

```text
274980728110413983 = B* - 981104
```

is jointly owned by `U_Q`, `U_BC`, and `U_new`; it is not
`U_K3_allocation`. A new red leaf must prove the sibling values or an
equivalent certified three-way allocation before the K3 comparison can run.
The derived lower floor `U_Q+U_BC+U_new >= 57197049262` remains conditional
on the recorded owner ruling and does not isolate `U_BC`.

This refactor adds one PROVED node and five explicit mathematical/payment
leaves plus the allocation-definition leaf. It closes no active K3 slope
cell, but removes two unsound shortcuts: component classification is no
longer treated as a slope bridge, and the joint reserve is no longer treated
as a K3-only budget.

```text
DAG after refactor: 2159 nodes / 6371 edges
statuses:          1919 PROVED / 70 CONDITIONAL / 92 TARGET
critical K3 reds:  bridge; 11 positive routes; source line; source cover;
                   trivial stabilizer; allocation definition; review
next theorem:      active Z_BC bad-slope-to-component bridge
```
