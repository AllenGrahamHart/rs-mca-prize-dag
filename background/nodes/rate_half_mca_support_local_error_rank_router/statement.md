# Support-local error-rank router

- **status:** PROVED
- **source:** upstream PR #1166 at `af0e7c63b`
- **scope:** direct post-near KoalaBear MCA slope family

For selected errors

```text
e_gamma=r_0+gamma r_1-h_gamma,
a=rank span{e_gamma-e_gamma0},
```

same-support pair noncontainment makes the map
`(delta,c)->delta r_1-c` injective on the selected pair space. Choosing a
pair `(1,b)` and applying the reversible codeword gauge

```text
r'_1=r_1-b,       h'_gamma=h_gamma-gamma b
```

preserves slopes, errors, exact supports, and pair noncontainment while
reducing explanation affine rank from `a` to exactly `a-1`.

After the proved disjoint near-rational charge `2w=134944`, the KoalaBear
consequences are:

```text
a<=9       -> total slopes <=110390969172308040 < B_*;
a=10       -> over budget forces an actual support with <=12 exceptions;
a=11       -> over budget forces an actual support with <=387 exceptions;
a=12       -> over budget forces an actual support with <=12049 exceptions;
a>=13      -> unpaid by this router.
```

The corresponding margins are recomputed after the gauge. This is a direct
maximum-over-lines route cut, not a v4 S/A/E owner assignment.
