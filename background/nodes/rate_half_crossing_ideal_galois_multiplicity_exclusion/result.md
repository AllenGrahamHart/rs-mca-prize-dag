# Result

The exact ideal/Galois multiplicity theorem and periodic reduction are now a
self-contained PROVED supplier.  At the near-256-bit characteristic
benchmark, it excludes the integer window

```text
170,752,922,588 <= w <= 2^39,
```

which is 71.1641% of `[2^34,2^39]`.  At 128 bits the last unexcluded value is
`339,028,612,821`; at 64 bits the theorem excludes none of the bracket.

The successful independent artifact is
`notes/pilots_20260806/cs_transport/cs_independent_audit_rerun_result.json`,
Modal app `ap-JNBoN1s1INvr1ovkHvbf8h`, checker SHA-256
`efc707ece973addc639c3e1463e7c0605e08158836dd28054ed9cb2ac2562c60`.
The final two-verifier artifact is `cs_node_verify_final_result.json`, Modal
app `ap-MCOrXFtNvxPe9tbqfvGCl6`, SHA-256
`ae71d6737c1b98809640d70bbdc58fb37560d45f43d9316b6cb7be2144cb687c`.

No critical node changes status.  The surviving work is rowwise: pairs
`(p,w)` for which `(IG4)` does not bite, plus the exact structural-count or
exceptional-floor obligation required by each consumer.
