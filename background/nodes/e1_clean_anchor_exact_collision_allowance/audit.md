# Audit

## Provenance

The exact count is independently reconstructed from upstream
`przchojecki/rs-mca` at commit
`b13de8113a03f06b6fc22bbd2f289a8abcdf7e95`, file
`tex/slackMCA_v4.tex`, SHA-256
`810ac469b8a8a8ba4638d882ec8426be95ffddf0f8888b83315afb4d60e990b4`,
label `thm:exactcount`. The quotient-locator realization is in the same file,
label `prop:qfloor`. The exact budget-window convention is also printed in
`tex/cs25_cap_v13_2.tex`, SHA-256
`356f1ad4b972746b664260191387b25a89a2e10fcc61962a49dc8282412f93ce`,
label `thm:capf-windows`.

No open upstream PR at the cycle pin advertises a competing direct-E1 or
clean-anchor value-set result. The imported statements are already on main.

## Corrections exposed

1. The preliminary global-sign quotient would have divided the class counts
   by two. This is false: sign negates the slope. The paper's `3280` test at
   `(N,ell)=(16,9)` catches the error.
2. Existing E1 notes use `N' in {128,256}` ambiguously. For the live clean
   anchors those are folded dimensions. The actual quotient orders are
   `N in {256,512}`. This packet uses separate symbols `N` and `h=N/2`.
3. The phrases `o(1)-sparse` and `negligible relative to the signed core` are
   not finite prize certificates. The exact route target is the printed
   integer collision-pair allowance, or a direct proof that the image exceeds
   `B*`.
4. Route assignment cannot depend on the desired collision conclusion. The
   checkable first split is generated-field size. `|F_p(Q)|<=B*` kills E1;
   above it, the exact balanced-fiber floor determines whether the pair-loss
   currency is even feasible.
5. The initial candidate class `|F_p(Q)|>B*` was still too broad. When
   `K` greatly exceeds the generated field, unavoidable pair collisions can
   exceed `K-B*-1` even though the image might exceed `B*`. The corrected
   pointwise pair target begins at the printed `b_pair_min`.

## Independent checks

`verify.py` replays the source pins, exact class formula, small complete subset
quotients, endpoint arithmetic, loss inequality, and DAG wiring.
`audit_verify.py` uses ternary signed-core enumeration and integer partitions
rather than the primary implementation. Neither verifier claims a collision
bound for the official fields.
