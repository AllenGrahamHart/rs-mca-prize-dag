# Uniform corank-two projective cap

- **status:** TARGET
- **proposition:** every official corank-two canonical-basis chart has at
  most `84416263` records.

The value is proved for the complete chart `t=0`.  Current support-local
transversality controls `t>=1` only through

```text
floor(max(F_2(1),F_2(K'-10))).
```

At `K'=377674` this is `253238254`, so a proof of the target must exploit
additional Reed-Solomon structure or improve the near-complete `t=1`
chart.  Closing this target reactivates the conditional capacity cut
through `568338`.
