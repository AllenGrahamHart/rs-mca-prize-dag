# Replay certificate

The verifier was shipped by content to Modal and replayed in app
`ap-CDc2LqGGSWglna94IggFnk`. It returned

```text
XR_POSTSTRIP_AFFINE_PENCIL_CHARGE_PASS
cap_cases=13982804 cap_mutations=158218 families=624 selectors=2424
rowc-r1_4:sigma<=4,caps=153/128
rowc-r1_8:sigma<=4,caps=179/149
rowc-r1_16:sigma<=4,caps=320/240
prize-r1_4:sigma<=15,caps=191/191
prize-r1_8:sigma<=15,caps=223/223
prize-r1_16:sigma<=14,caps=479/479
```

The replay exhausts the core-cap arithmetic at 13,982,804 small parameter
instances, all 2,424 eligible selectors in 624 length-four ternary fixtures,
and both the high-core and low-core caps at all six XR rows. The 158,218
hypothesis-removal mutations admit one excess persistent coordinate and
exceed the printed cap. A separate endpoint mutation confirms that RowC rank
five remains unpaid. Peak worker RSS was `56 MB`.

The refreshed full fleet passed `147/147` in Modal app
`ap-4OjdeOhtq9jESBsVkjaadY`. All five integration gates passed in
`ap-mGtgyhBfQYe2GdRCfhUIZX`, retaining the same eight open critical truth
leaves.
