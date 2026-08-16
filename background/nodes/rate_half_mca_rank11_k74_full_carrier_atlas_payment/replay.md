# Replay

The focused audit reconstructs the conservative frontier, canonical digest,
729-cell reroute, and final payment in one bounded Modal job:

```text
plain frontier: 8,869,588 evaluations
reroute:          338,149 evaluations
observed peak:         60 MB
```

Run the lane wrapper at `74` with each of
`carrier32_geom,one_geom,...,six_geom`. The seven lanes contain 124,851,888
evaluations and observed peak RSS at most 62 MB. Default local verification
does not repeat these enumerations.
