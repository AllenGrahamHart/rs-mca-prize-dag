# Replay certificate

The standalone verifier was shipped by content to Modal and replayed in app
`ap-0mqk9ulwaktpocJUty4WUK`. It returned

```text
XR_AFFINE_CORE_ALL_ZERO_CHARGE_PASS
cap_cases=123409 cap_mutations=10660 families=624 subfamilies=3720
rowc-r1_4:sigma<=4 rowc-r1_8:sigma<=4 rowc-r1_16:sigma<=4
prize-r1_4:sigma<=11 prize-r1_8:sigma<=11 prize-r1_16:sigma<=10
```

The replay exhausts the persistent-zero allocation for all parameter triples
of length at most 40, all 3,720 transverse subfamilies in 624 nontrivial
length-four ternary repetition-code fixtures, and the six exact XR rows. The
10,660 endpoint cases reject the false `r` cap. It also checks that the former
`N-a` charge fails RowC `1/16` rank four, the new `r+1` charge passes it, and
rank five remains outside the budget by a factor greater than `145`. Peak
worker RSS was `56 MB`.

The refreshed full fleet passed `146/146` in Modal app
`ap-6Kj4y2fc3bzHsi6hwin5LZ`. All five integration gates passed in
`ap-rUidLCCRaFnrJX4CPjKOrN`, retaining the same eight open critical truth
leaves.
