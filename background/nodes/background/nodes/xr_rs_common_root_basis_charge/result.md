# Replay certificate

The verifier was shipped by content to Modal and replayed in app
`ap-BHD3bLqvOtZLzyODyF43JJ`. It returned

```text
XR_RS_COMMON_ROOT_BASIS_CHARGE_PASS
matroids=5722 strict=5577 root_cases=559716 endpoint_cases=628320
rowc-r1_4:sigma<=4,caps=153/128
rowc-r1_8:sigma<=4,caps=179/149
rowc-r1_16:sigma<=4,caps=320/240
prize-r1_4:sigma<=16,caps=191/191
prize-r1_8:sigma<=16,caps=223/223
prize-r1_16:sigma<=14,caps=479/479
```

The replay exhausts 5,722 small loopless represented matroids, 559,716
one-slope common-root allocations, 628,320 two-variable corner-envelope
cases, and both post-strip caps at all six XR rows. The 5,577 strict cases
confirm that the loopless weighting genuinely strengthens the unweighted
cogirth bound. Peak worker RSS was `55 MB`.

The refreshed full fleet passed `148/148` in Modal app
`ap-agJiaI7nKh1ZPowgx9mmJm`. All five integration gates passed in
`ap-8VdzGh7F2OdwU8FmobKZ4P`, retaining the same eight open critical truth
leaves.
