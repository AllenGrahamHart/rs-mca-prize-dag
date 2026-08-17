# Replay

The load-bearing enumerations are split into bounded Modal jobs using
`tools/modal_run_script.py` and the source scripts listed in `node.json`.

```text
plain frontier:       8,551,382 evaluations, peak 60 MB
218-cell reroute:        71,806 evaluations, peak 58 MB
carrier geometry:        40,754 evaluations, peak 60 MB
one-step geometry:   15,928,017 evaluations, peak 60 MB
two-step geometry:   12,991,279 evaluations, peak 60 MB
three-step geometry: 16,485,210 evaluations, peak 59 MB
four-step geometry:  20,292,986 evaluations, peak 60 MB
five-step geometry:  24,391,346 evaluations, peak 62 MB
six-step geometry:   28,763,077 evaluations, peak 60 MB
```

Invoke the lane wrapper with `73` and one of
`carrier32_geom,one_geom,...,six_geom`. Invoke the frontier wrapper with
`73 --compact` for the exact failing set and `73 --reroute` for its complete
coupled replay. The final-payment wrapper receives `73` and `(P73)`.
