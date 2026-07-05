# frontier: midlarge_h7_20

No usable scan result is currently available.

## Existing setup

The Modal script implements a banked MITM-style active-core scan:

- complete census when `W = n`;
- exhaustive window slice over `[0,W)` when `W < n`;
- incomplete/aborted cells are explicitly flagged and must not be treated as
  zero cells.

The script was syntax-checked in this working copy:

```text
python3 -m py_compile nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py
```

## Modal status

The recorded app `ap-vQcKCgn6xEDBu2mAipdR7u` has only stop messages in the
retrieved logs. It emitted no gate or scan JSON, so it supplies no evidence
for or against the zero-active-core claim.

## Remaining proof obligations

- `m720_complete_calibration_certificates`: obtain complete zero certificates for h=7..20 at feasible
  calibration rows, and treat n=1024 slices only as slices.
- `m720_official_exclusion`: prove the bounded-band exclusion lemma for official-shape rows:
  any active core at h=7..20 is empty or charged by the paid ledger.

The scan can de-risk `M720-EXCL`, but the proof cannot be scan-only because
the scan is calibration/slice evidence.

## Falsifier

Any non-toral anchored active core at h=7..20 in a complete calibration cell.
An n=1024 window-slice witness is a serious warning but must be interpreted as
slice-local unless the cell is complete.
