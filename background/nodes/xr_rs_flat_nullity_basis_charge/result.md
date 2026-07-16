# Replay certificate

The verifier was shipped by content to Modal and replayed in app
`ap-eyZ8qPcmHb1nwaFdiBqbwT`. It returned

```text
XR_RS_FLAT_NULLITY_BASIS_CHARGE_PASS
matroids=5722 strict=5312 packing_cases=66115 packing_mutations=210
rowc-r1_4:all=32131,A=14,B=8,umax=10/7,vmax=1/1
rowc-r1_8:all=7875,A=70,B=49,umax=38/29,vmax=3/2
rowc-r1_16:all=1891,A=323,B=274,umax=60/60,vmax=7/6
```

The replay exhausts 5,722 small represented matroids, 66,115 small packing
families, and every admissible rank-five `(u,v)` pair on the three RowC rows.
The 5,312 strict matroid cases witness genuine improvement over the bare
ordered-basis floor, while 210 hypothesis-removal packing families exceed the
disjoint-subset ledger. Peak worker RSS was `56 MB`.

The refreshed full fleet passed `149/149` in Modal app
`ap-W4nB7J5CQsklOl37mNKRPO`. All five integration gates passed in
`ap-xFLOVNHfqNLsXZIZZIoeZt`, retaining the same eight open critical truth
leaves.
