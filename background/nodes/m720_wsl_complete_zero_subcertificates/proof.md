# proof: m720_wsl_complete_zero_subcertificates

The verifier in this folder reproduces the anchored MITM complete-cell scan
from `nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py` for only the cells
whose complete-window combination count is at most the Modal scan ceiling
`6,000,000`.

It uses `W=n`, so every listed row has `complete=true`. The replay checks the
anchored trade condition exactly: matching lower elementary signatures,
disjoint halves, and unequal top coefficient. It then separates toral pairs
from unpaid non-toral pairs using the same `is_coset` test as the Modal helper.

The exact local replay returns:

```text
n=16, h=7, p=257:   anchored_nontoral=0, anchored_toral=0
n=16, h=7, p=4129:  anchored_nontoral=0, anchored_toral=0
n=32, h=7, p=1153:  anchored_nontoral=0, anchored_toral=0
n=32, h=7, p=32801: anchored_nontoral=0, anchored_toral=0
n=16, h=8, p=257:   anchored_nontoral=0, anchored_toral=1
n=16, h=8, p=4129:  anchored_nontoral=0, anchored_toral=1
```

Thus every WSL-safe complete calibration cell has zero unpaid non-toral
anchored active cores. This proves the local subcertificate packet.
