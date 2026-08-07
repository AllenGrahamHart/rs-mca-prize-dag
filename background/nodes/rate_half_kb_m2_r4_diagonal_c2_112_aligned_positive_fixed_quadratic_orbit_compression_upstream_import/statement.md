# KoalaBear aligned-positive fixed quadratic orbit compression

- **status:** PROVED
- **scope:** the twelve literal
  `{F04,F05,F06,F07} x {R02,R11,R20}` aligned-positive cells
- **provenance:** Przemek repository PR #1149, exact commit
  `55ac3e07477bd7a768190a3e755f22b0d44354b0`
- **consumer:** source-line literal-assignment coverage

For the first two q-slice rows, write

```text
P=A w^2+B w+C,       Q=D w^2+E w+F,
U=AF-CD,             V=AE-BD,             Z=BF-CE.
```

Then exact polynomial identities give

```text
Res_w(P,Q)=U^2-VZ,                                  (KBFQ-1)
D P-A Q=-(Vw+U).                                   (KBFQ-2)
```

On `V!=0`, the unique common root is `w=-U/V`; after this substitution the
remaining two q-slice rows are cleared by exactly `V^4`. On `V=0`, every
common root also forces `U=0`. This rank-drop component is retained, not
discarded.

Direct literal compilation gives six exact fingerprint orbits:

```text
F04-R02 = F07-R02       F05-R02 = F06-R02
F04-R11 = F07-R11       F05-R11 = F06-R11
F04-R20 = F07-R20       F05-R20 = F06-R20.         (KBFQ-3)
```

Equality in `(KBFQ-3)` means equality of the resultant fingerprint and the
three terminal `U,V,Z` core fingerprints. It is established by rebuilding
all twelve literal cells, not by generic endpoint covariance.

This theorem is a route decomposition, not an emptiness result. Each of the
six orbits still has a generic `V!=0` branch and a rank-drop `U=V=0` branch.

## Falsifier

Failure of `(KBFQ-1)` or `(KBFQ-2)`, a literal cell absent from the census,
unequal partner fingerprints, a generic common root not reconstructed by
`w=-U/V`, or any argument that silently drops `V=0`.
