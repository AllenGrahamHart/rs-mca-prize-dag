# M31 depth-32 uniform-intercept counterexample

- **status:** see `dag.json` (single source of truth)
- **upstream source:** draft PR #1102, independently reconstructed here
- **consumer:** `l1_mixed_petal_amplification`

On the pinned auxiliary Mersenne-31 list profile

```text
p=2^31-1,   c=2048,   (u,v)=(0,1),
|Q'|=1022,  support size=479,  prefix depth=32,
```

there is a canonical support `A` and `1237` distinct supports `B` with

```text
pref_32(V_B)=pref_32(V_A),       479-|A intersect B|=192.
```

The family consists of

```text
C(7,3)^2=1225
```

whole-`T_64` triple exchanges and twelve explicitly reconstructed mixed
`T_16` exchanges. Since `33<=192<=213`, this refutes the proposed uniform
in-band cap `d_e(A)<=1233`.

The counterexample forces any uniform coefficient-four scalar intercept on
that band to be at least `1237`. It does not prove an upper bound of `1237`,
realize a received word, survive first match, pay `U_Q`, move the M31 list
endpoint, or apply to the `2^-128` Prize rows.

## Provenance upgrade (2026-07-29)

The upstream source graduated from draft to integrated: PR #1102's refutation
d_192(A) >= 1237 is banked in the July ledger at upstream 0f7476f0, verbatim
("PR #1102 supplies one pinned target and anchor with d_192(A) >= 1225+12 =
1237"). Our independent reconstruction here is thereby confirmed against the
integrated record.
