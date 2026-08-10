# Upstream crosswalk

- **upstream target:** the base-field-normalized interior census after
  `prob:capfr1-split-pencil` in CAP25 v13.2;
- **local export:** `przchojecki/rs-mca` PR #1151, `LIST: add FPC5 LS6 and
  general t-petal reductions`;
- **pinned head:** `ca93321887b47b0f3323c24ecd4427df2c8dad47`;
- **upstream status at pin:** open draft, mergeable;
- **relation:** exact FPC5 ambient support enumerator and route fence,
  exported as Section 7 of
  `experimental/notes/l1/list_tpetal_joint_anchor_owner_v1.md`.

The theorem is elementary but useful for scope: an owner census that omits
the split predicate is exactly the MDS weight census and is binomial at the
top stratum. It does not prove or instantiate upstream quotient flatness or
the base-field-normalized split-pencil census. It instead proves that a
successful census must use simultaneous splitting and guards rather than
owner coordinates alone.
