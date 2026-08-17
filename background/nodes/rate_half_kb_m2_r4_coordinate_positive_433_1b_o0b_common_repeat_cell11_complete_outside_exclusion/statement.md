# Complete repeated-BC cell-11 outside exclusion

- **status:** PROVED
- **field:** `F_2130706433`
- **scope:** all 16 formal cell-11 rows and all 105 raw labels per row

Every outside system on a guarded repeated-BC cell-11 common source is empty.
The exact label census is

```text
missing BE, CF:             2*15 = 30
missing DE+, DF+, EF:       3*15 = 45
transported DE-, DF-:       2*15 = 30
total per formal row:              105
formal rows:                         16
raw labels excluded:              1,680
```

## Falsifier

An uncovered source boundary, missing-record class, residual matching,
outside-cycle sign, or a nonempty one of the 1,680 raw systems.
