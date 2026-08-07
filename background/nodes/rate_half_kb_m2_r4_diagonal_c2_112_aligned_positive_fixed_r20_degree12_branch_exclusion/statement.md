# KoalaBear fixed R20 degree-12 branch exclusion

- **status:** PROVED
- **cells:** `F04-R20`, `F05-R20`, `F06-R20`, `F07-R20`
- **closure:** exhaustive `s`, `L6`, and `K10` partition

In each listed cell, the complete selected degree-12 resultant branch is
empty over `F_(2130706433^6)`. The exhaustive leaves are

```text
s=0,
s!=0 and L6=0,
s*L6!=0 and K10!=0,
s*L6!=0 and K10=0.
```

Each leaf is PROVED empty by a required node. No cubic, rank-drop, or
whole-cell claim is made here.
