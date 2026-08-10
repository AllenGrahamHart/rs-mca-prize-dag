# Repeated-BC cells 3 and 6 BC- complete outside exclusion

- **status:** PROVED
- **scope:** all repeated-`BC` `BC-` outside systems in owner cells 3 and 6

The cell-3 packets are

```text
missing BE:       120 empty
missing CF:       120 empty
missing DE+/DE-:  240 empty
missing DF+/DF-:  240 empty
missing EF:       120 empty
total:            840 empty
```

The exact full-system involution sends the complete cell-3 workload to all
840 cell-6 systems while preserving `BC-`.  Hence cell 6 is also empty.

## Falsifier

An omitted missing-record packet, an arithmetic census mismatch, or a
failure of the certified transport on any sign/role/matching label.
