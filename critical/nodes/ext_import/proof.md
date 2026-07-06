# ext_import proof

The proved node `ext_pole_floor` supplies the extension-pole witness count
`N(L)` and its gate-crossing formula. In that formula the extension parameter
`L` is exactly the base list-window parameter used on the S7 list side.

Therefore the extension column does not require a new threshold calculation:
the inequality

```text
B_ext >= gate
```

holds exactly at the same base-row list window where the S7 list threshold is
met, after applying the floor convention already included in
`ext_pole_floor`.

This proves the import rule recorded in the node statement: extension poles
are priced by reading the S7 list window at the corresponding base row.
