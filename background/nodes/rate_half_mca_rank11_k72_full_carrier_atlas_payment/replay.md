# Replay

The load-bearing enumerations are split into bounded Modal jobs using
`tools/modal_run_script.py` and the source scripts listed in `node.json`.

```text
plain frontier: 7,991,221 evaluations, peak 59 MB
36-cell reroute: 8,057 evaluations, peak 59 MB
carrier geometry: 40,754 evaluations, peak 61 MB
one-step geometry: 15,170,953 evaluations, peak 60 MB
two-step geometry: 12,368,727 evaluations, peak 59 MB
three-step geometry: 15,690,948 evaluations, peak 59 MB
four-step geometry: 19,308,205 evaluations, peak 59 MB
five-step geometry: 23,198,952 evaluations, peak 59 MB
six-step geometry: 27,345,696 evaluations, peak 62 MB
```

Each geometry job invokes the two-step probe with one of
`carrier32_geom,one_geom,...,six_geom`.  The plain probe emits the complete
strictly-above-ceiling tuple list.  The active-cell probe receives that list
as one semicolon-separated argument and asserts all 36 exact routes safe.
