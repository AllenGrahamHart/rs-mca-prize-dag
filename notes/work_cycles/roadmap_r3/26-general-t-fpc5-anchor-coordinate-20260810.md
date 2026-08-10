### 2026-08-10 general-t FPC5 anchor coordinate

The general-`t` slice theorem has a stronger monic-chart consequence, now
banked as `l1_fpc5_tpetal_anchor_coordinate`. Relative to one squarefree
exact anchor `(F,W)`,

```text
H=(FB-GW)/Lambda,       deg H<=e-1,
```

is an affine bijection from the complete monic pair chart to
`K[X]_(<=e-1)`. At every anchor defect root, `H` vanishes exactly when the
candidate locator `G` vanishes, so

```text
gcd(H,F)=gcd(G,F).
```

This closes pair-coefficient multiplicity, candidate reconstruction, and
fixed common-defect owner ambiguity at arbitrary `t`. Every surviving
large-source fixed cell is now one explicit low-degree coordinate body whose
split-and-exact points must be counted. No critical status changes: aggregate
split-point and chronology-valid owner/profile control remain open.

The identical theorem is exported in upstream PR #1151 at pinned head
`4c8b84f05521bd432b6984e1dd7ca28e3194ab80`; the PR remains an open
mergeable draft.
